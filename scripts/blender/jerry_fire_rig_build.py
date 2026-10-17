"""Build the Jerry fire rig (r09 look) from an empty Blender scene.

Run headless with Blender 5.2+:

    /Applications/Blender.app/Contents/MacOS/Blender -b --factory-startup \
        --python scripts/blender/jerry_fire_rig_build.py -- \
        --out assets/characters/jerry/source-cgi/jerry_fire-rig_v001.blend \
        --cache outputs/jerry_fire-rig_v001/cache_fluid

The fluid cache is not baked here; run fluid_bake.py next. Design, settings
history and assessment: workflows/blender/jerry/jerry_fire-rig_log_v001.md.
"""

import argparse
import math
import os
import sys

import bmesh
import bpy
from mathutils import Matrix, Vector


# --- look and sim parameters (r09) -------------------------------------------
BODY_RADIUS = 0.25          # base radius of the teardrop body, metres
BODY_BASE_Z = -0.225        # bottom of the body
FLAME_GAMMA = 0.55          # lifts low flame values out of the dim-red band
FIRE_EMISSION = "14.0 * flare"
CORE_EMISSION = "3.5 * flare"
EMBER_EMISSION = "60.0 * flare"
FUEL = "3.0 * flare"
FLOW_TEMPERATURE = "0.4 + 0.6 * flare"
FIRE_RAMP = [
    (0.0, (0.0, 0.0, 0.0)),
    (0.08, (0.5, 0.03, 0.0)),
    (0.25, (1.0, 0.24, 0.0)),
    (0.5, (1.0, 0.5, 0.07)),
    (0.85, (1.0, 0.9, 0.62)),
]
CORE_RAMP = [
    (0.2, (1.0, 0.75, 0.38)),
    (0.7, (1.0, 0.45, 0.05)),
    (1.05, (0.85, 0.12, 0.0)),
]


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(description="Build the Jerry Blender fire rig.")
    p.add_argument("--out", required=True, help=".blend to write")
    p.add_argument("--cache", required=True, help="fluid cache directory")
    return p.parse_args(argv)


def smoothstep(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


def add_flare_driver(target, path, expr, rig):
    fc = target.driver_add(path)
    var = fc.driver.variables.new()
    var.name = "flare"
    var.type = "SINGLE_PROP"
    var.targets[0].id = rig
    var.targets[0].data_path = '["flare"]'
    fc.driver.expression = expr
    return fc


def set_ramp(ramp_node, stops, interpolation="LINEAR"):
    cr = ramp_node.color_ramp
    cr.interpolation = interpolation
    while len(cr.elements) > 1:
        cr.elements.remove(cr.elements[-1])
    cr.elements[0].position = stops[0][0]
    cr.elements[0].color = (*stops[0][1], 1.0)
    for pos, col in stops[1:]:
        cr.elements.new(pos).color = (*col, 1.0)


def new_mesh_object(name, collection, build):
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    build(bm)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    collection.objects.link(ob)
    return ob


# --- scene ---------------------------------------------------------------------
def setup_scene():
    scn = bpy.context.scene
    for name in ("Cube", "Light"):
        ob = bpy.data.objects.get(name)
        if ob:
            bpy.data.objects.remove(ob, do_unlink=True)

    scn.render.engine = "CYCLES"
    scn.cycles.device = "GPU"
    scn.cycles.samples = 96
    scn.cycles.use_denoising = True
    scn.cycles.volume_bounces = 2
    scn.cycles.transparent_max_bounces = 16
    scn.render.fps = 24
    scn.frame_start, scn.frame_end = 1, 120
    scn.render.resolution_x, scn.render.resolution_y = 1920, 1080
    scn.render.resolution_percentage = 50
    scn.render.use_motion_blur = True       # embers only; domain and core opt out
    scn.render.motion_blur_shutter = 0.5
    scn.view_settings.view_transform = "AgX"
    scn.view_settings.look = "AgX - Punchy"
    scn.view_settings.exposure = 1.0

    world = scn.world or bpy.data.worlds.new("World")
    scn.world = world
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0, 0, 0, 1)
    bg.inputs["Strength"].default_value = 0.0

    cam = bpy.data.objects.get("Camera")
    if cam is None:
        cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
        scn.collection.objects.link(cam)
    cam.location = (0.0, -3.9, 0.33)
    cam.rotation_euler = (math.radians(90), 0, 0)
    cam.data.lens = 65
    scn.camera = cam

    col = bpy.data.collections.new("JERRY")
    scn.collection.children.link(col)
    return scn, col


# --- body + rig ----------------------------------------------------------------
def build_body(col):
    def teardrop(bm):
        bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=24, radius=1.0)
        for v in bm.verts:
            x, y, z = v.co
            if z > 0:   # taper to a soft tip and lengthen the top half
                taper = 1.0 - 0.72 * (z ** 1.6)
                v.co = Vector((x * taper, y * taper, z * 1.55)) * BODY_RADIUS
            else:       # slightly flattened, rounded base
                v.co = Vector((x * 1.04, y * 1.04, z * 0.9)) * BODY_RADIUS

    body = new_mesh_object("JERRY_body", col, teardrop)
    for poly in body.data.polygons:
        poly.use_smooth = True
    body.display_type = "WIRE"
    # emitter only: invisible to every render ray, still drives fire and embers
    for attr in ("visible_camera", "visible_diffuse", "visible_glossy",
                 "visible_transmission", "visible_volume_scatter", "visible_shadow"):
        setattr(body, attr, False)

    g_body = body.vertex_groups.new(name="body")
    g_tip = body.vertex_groups.new(name="tip")
    g_emit = body.vertex_groups.new(name="fire_emit")
    for v in body.data.vertices:
        w_tip = smoothstep(0.0, 0.2, v.co.z)
        g_tip.add([v.index], w_tip, "REPLACE")
        g_body.add([v.index], 1.0 - w_tip, "REPLACE")
        # low emission around the base, full on the upper body and tip
        g_emit.add([v.index], 0.3 + 0.7 * smoothstep(-0.12, 0.2, v.co.z), "REPLACE")
    return body


def build_rig(col, body):
    arm = bpy.data.armatures.new("JERRY_rig")
    arm.display_type = "STICK"
    rig = bpy.data.objects.new("JERRY_rig", arm)
    col.objects.link(rig)
    rig.show_in_front = True

    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode="EDIT")
    eb = arm.edit_bones
    root = eb.new("root")
    root.head, root.tail = (0, 0, BODY_BASE_Z - 0.05), (0, 0.18, BODY_BASE_Z - 0.05)
    bone_body = eb.new("body")
    bone_body.head, bone_body.tail = (0, 0, BODY_BASE_Z), (0, 0, 0.08)
    bone_body.parent = root
    tip = eb.new("tip")
    tip.head, tip.tail = (0, 0, 0.08), (0, 0, 0.42)
    tip.parent = bone_body
    tip.use_connect = True
    bpy.ops.object.mode_set(mode="OBJECT")

    rig["flare"] = 1.0
    rig.id_properties_ui("flare").update(
        min=0.0, max=2.5, soft_min=0.2, soft_max=2.0,
        description="Flare (>1) / Dim (<1): fuel, heat, core glow, fire and embers")
    for name in ("root", "body", "tip"):
        rig.pose.bones[name].rotation_mode = "XYZ"
    # squash and stretch: animators scale body Y only, volume is preserved
    mv = rig.pose.bones["body"].constraints.new("MAINTAIN_VOLUME")
    mv.free_axis = "SAMEVOL_Y"
    mv.owner_space = "LOCAL"

    body.parent = rig
    body.modifiers.new("Armature", "ARMATURE").object = rig
    return rig


# --- core glow -----------------------------------------------------------------
def build_core(col, rig):
    core = new_mesh_object(
        "JERRY_core", col,
        lambda bm: bmesh.ops.create_icosphere(bm, subdivisions=4, radius=1.0))
    core.display_type = "WIRE"
    core.cycles.use_motion_blur = False
    core.parent = rig
    core.parent_type = "BONE"
    core.parent_bone = "body"
    # bone-relative transform must be set against the rest pose
    rig.data.pose_position = "REST"
    bpy.context.view_layer.update()
    core.matrix_world = Matrix.LocRotScale(Vector((0, 0, -0.035)), None, Vector((0.23, 0.23, 0.27)))
    rig.data.pose_position = "POSE"
    bpy.context.view_layer.update()

    mat = bpy.data.materials.new("JERRY_core_glow")
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    new, link = nt.nodes.new, nt.links.new

    coords = new("ShaderNodeTexCoord")
    rising = new("ShaderNodeVectorMath")          # object coords drifting upward over time
    rising.operation = "SUBTRACT"
    link(coords.outputs["Object"], rising.inputs[0])
    rising.inputs[1].driver_add("default_value", 2).driver.expression = "frame / 24 * 0.6"

    edge_noise = new("ShaderNodeTexNoise")
    edge_noise.noise_dimensions = "4D"
    edge_noise.inputs["Scale"].default_value = 2.2
    edge_noise.inputs["Detail"].default_value = 6.0
    edge_noise.inputs["Roughness"].default_value = 0.55
    edge_noise.inputs["W"].driver_add("default_value").driver.expression = "frame / 24 * 0.9"
    link(rising.outputs[0], edge_noise.inputs["Vector"])

    radius = new("ShaderNodeVectorMath")
    radius.operation = "LENGTH"
    link(coords.outputs["Object"], radius.inputs[0])
    noisy_radius = new("ShaderNodeMath")
    noisy_radius.operation = "MULTIPLY_ADD"
    noisy_radius.inputs[1].default_value = 0.4
    link(edge_noise.outputs["Fac"], noisy_radius.inputs[0])
    link(radius.outputs["Value"], noisy_radius.inputs[2])

    falloff = new("ShaderNodeValToRGB")           # 1 inside, 0 at the shell
    set_ramp(falloff, [(0.55, (1, 1, 1)), (1.02, (0, 0, 0))], "EASE")
    link(noisy_radius.outputs[0], falloff.inputs["Fac"])
    colour = new("ShaderNodeValToRGB")            # yellow-white core to amber to ember red
    set_ramp(colour, CORE_RAMP)
    link(noisy_radius.outputs[0], colour.inputs["Fac"])

    # vertical flame strands scrolling upward inside the body
    stretch = new("ShaderNodeVectorMath")
    stretch.operation = "MULTIPLY"
    stretch.inputs[1].default_value = (4.5, 4.5, 1.1)
    link(rising.outputs[0], stretch.inputs[0])
    strands = new("ShaderNodeTexNoise")
    strands.noise_dimensions = "4D"
    strands.inputs["Scale"].default_value = 1.6
    strands.inputs["Detail"].default_value = 8.0
    strands.inputs["Roughness"].default_value = 0.6
    strands.inputs["Distortion"].default_value = 0.6
    strands.inputs["W"].driver_add("default_value").driver.expression = "frame / 24 * 1.4"
    link(stretch.outputs[0], strands.inputs["Vector"])
    strand_ramp = new("ShaderNodeValToRGB")
    set_ramp(strand_ramp, [(0.35, (0.2, 0.2, 0.2)), (0.7, (2.0, 2.0, 2.0))])
    link(strands.outputs["Fac"], strand_ramp.inputs["Fac"])
    strand_mask = new("ShaderNodeMath")
    strand_mask.operation = "MULTIPLY"
    link(falloff.outputs["Color"], strand_mask.inputs[0])
    link(strand_ramp.outputs["Color"], strand_mask.inputs[1])

    emission = new("ShaderNodeMath")
    emission.name = "core_emission_strength"
    emission.operation = "MULTIPLY"
    link(strand_mask.outputs[0], emission.inputs[0])
    add_flare_driver(emission.inputs[1], "default_value", CORE_EMISSION, rig)
    density = new("ShaderNodeMath")               # thin: emission-dominant, translucent
    density.operation = "MULTIPLY"
    density.inputs[1].default_value = 0.12
    link(falloff.outputs["Color"], density.inputs[0])

    vol = new("ShaderNodeVolumePrincipled")
    vol.inputs["Color"].default_value = (1.0, 0.5, 0.15, 1)
    vol.inputs["Absorption Color"].default_value = (0, 0, 0, 1)
    link(density.outputs[0], vol.inputs["Density"])
    link(colour.outputs["Color"], vol.inputs["Emission Color"])
    link(emission.outputs[0], vol.inputs["Emission Strength"])
    link(vol.outputs["Volume"], new("ShaderNodeOutputMaterial").inputs["Volume"])
    core.data.materials.append(mat)
    return core


# --- fire ------------------------------------------------------------------------
def build_fire(col, rig, body, cache_dir):
    flow = body.modifiers.new("Fluid", "FLUID")
    flow.fluid_type = "FLOW"
    fs = flow.flow_settings
    fs.flow_type = "FIRE"
    fs.flow_behavior = "INFLOW"
    fs.flow_source = "MESH"
    fs.surface_distance = 0.02
    fs.volume_density = 0.0        # any volume emission makes a white candle column
    fs.density_vertex_group = "fire_emit"
    fs.subframes = 1
    fs.use_initial_velocity = True
    fs.velocity_factor = 1.0
    add_flare_driver(body, 'modifiers["Fluid"].flow_settings.fuel_amount', FUEL, rig)
    add_flare_driver(body, 'modifiers["Fluid"].flow_settings.temperature', FLOW_TEMPERATURE, rig)

    dom = new_mesh_object("JERRY_fire_domain", col, lambda bm: bmesh.ops.create_cube(bm, size=1.0))
    dom.location = (0.0, 0.0, 0.53)
    dom.scale = (1.0, 1.0, 1.7)
    dom.cycles.use_motion_blur = False     # volume motion blur smears the flame
    ds = dom.modifiers.new("Fluid", "FLUID")
    ds.fluid_type = "DOMAIN"
    ds = ds.domain_settings
    ds.domain_type = "GAS"
    ds.resolution_max = 128
    ds.use_adaptive_domain = False
    ds.cache_directory = cache_dir
    ds.cache_type = "ALL"
    ds.cache_data_format = "OPENVDB"
    ds.cache_frame_start, ds.cache_frame_end = 1, 120
    ds.vorticity = 0.05
    ds.alpha = 0.4
    ds.beta = 1.0
    ds.burning_rate = 1.0
    ds.flame_smoke = 0.0
    ds.flame_vorticity = 0.35
    ds.flame_max_temp = 1.8
    ds.flame_ignition = 1.4
    ds.use_dissolve_smoke = True
    ds.dissolve_speed = 6
    ds.use_dissolve_smoke_log = True
    ds.highres_sampling = "FULLSAMPLE"
    ds.clipping = 0.0              # default clipping cuts smokeless flame in hard lines
    ds.use_noise = True
    ds.noise_scale = 2
    ds.noise_strength = 0.5
    ds.noise_pos_scale = 2.0

    mat = bpy.data.materials.new("JERRY_fire")
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    new, link = nt.nodes.new, nt.links.new
    flame = new("ShaderNodeAttribute")
    flame.attribute_name = "flame"
    gamma = new("ShaderNodeMath")
    gamma.name = "flame_gamma"
    gamma.operation = "POWER"
    gamma.inputs[1].default_value = FLAME_GAMMA
    link(flame.outputs["Fac"], gamma.inputs[0])
    ramp = new("ShaderNodeValToRGB")
    set_ramp(ramp, FIRE_RAMP)
    link(gamma.outputs[0], ramp.inputs["Fac"])
    emission = new("ShaderNodeMath")
    emission.name = "fire_emission_strength"
    emission.operation = "MULTIPLY"
    link(gamma.outputs[0], emission.inputs[0])
    add_flare_driver(emission.inputs[1], "default_value", FIRE_EMISSION, rig)
    vol = new("ShaderNodeVolumePrincipled")
    vol.inputs["Density"].default_value = 0.0     # bible: no heavy smoke
    vol.inputs["Color"].default_value = (0.05, 0.04, 0.035, 1)
    link(ramp.outputs["Color"], vol.inputs["Emission Color"])
    link(emission.outputs[0], vol.inputs["Emission Strength"])
    link(vol.outputs["Volume"], new("ShaderNodeOutputMaterial").inputs["Volume"])
    dom.data.materials.append(mat)
    return dom


# --- embers ----------------------------------------------------------------------
def build_embers(col, rig, body):
    src = bpy.data.collections.new("JERRY_ember_src")
    col.children.link(src)
    ember = new_mesh_object(
        "JERRY_ember", src,
        lambda bm: bmesh.ops.create_icosphere(bm, subdivisions=1, radius=1.0))
    layer = bpy.context.view_layer.layer_collection.children[col.name].children[src.name]
    layer.exclude = True

    mat = bpy.data.materials.new("JERRY_ember")
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    new, link = nt.nodes.new, nt.links.new
    info = new("ShaderNodeParticleInfo")
    age = new("ShaderNodeMath")
    age.operation = "DIVIDE"
    link(info.outputs["Age"], age.inputs[0])
    link(info.outputs["Lifetime"], age.inputs[1])
    fade = new("ShaderNodeMapRange")              # bright at birth, out at death
    fade.inputs["To Min"].default_value = 1.0
    fade.inputs["To Max"].default_value = 0.0
    link(age.outputs[0], fade.inputs["Value"])
    strength = new("ShaderNodeMath")
    strength.operation = "MULTIPLY"
    link(fade.outputs["Result"], strength.inputs[0])
    add_flare_driver(strength.inputs[1], "default_value", EMBER_EMISSION, rig)
    emit = new("ShaderNodeEmission")
    emit.inputs["Color"].default_value = (1.0, 0.38, 0.06, 1)
    link(strength.outputs[0], emit.inputs["Strength"])
    link(emit.outputs[0], new("ShaderNodeOutputMaterial").inputs["Surface"])
    ember.data.materials.append(mat)

    mod = body.modifiers.new("Embers", "PARTICLE_SYSTEM")
    mod.particle_system.vertex_group_density = "tip"
    ps = mod.particle_system.settings
    ps.name = "JERRY_embers"
    ps.count = 400
    ps.frame_start, ps.frame_end = -24, 120
    ps.lifetime = 36
    ps.lifetime_random = 0.6
    ps.emit_from = "FACE"
    ps.distribution = "RAND"
    ps.normal_factor = 0.18
    ps.factor_random = 0.12
    ps.physics_type = "NEWTON"
    ps.effector_weights.gravity = -0.18    # embers rise
    ps.brownian_factor = 0.5
    ps.damping = 0.03
    ps.render_type = "OBJECT"
    ps.instance_object = ember
    ps.particle_size = 0.006
    ps.size_random = 0.6
    ps.display_method = "DOT"


# --- idle animation --------------------------------------------------------------
def build_idle(rig):
    deg = math.radians

    def key(bone, path, index, frames_values):
        pb = rig.pose.bones[bone]
        for frame, value in frames_values:
            getattr(pb, path)[index] = value
            pb.keyframe_insert(path, index=index, frame=frame, group=bone)

    key("body", "scale", 1, [(1, 1.0), (13, 1.045), (37, 0.965), (49, 1.0)])                     # breath, 48 f
    key("body", "rotation_euler", 2, [(1, 0.0), (17, deg(4.5)), (49, deg(-4.5)), (65, 0.0)])     # lean, 64 f
    key("tip", "rotation_euler", 2, [(1, deg(-6)), (33, deg(9)), (65, deg(-6))])                # whip, lags body
    key("tip", "rotation_euler", 0, [(1, 0.0), (21, deg(6)), (45, deg(-4)), (65, 0.0)])          # curl, 64 f
    key("tip", "scale", 1, [(1, 1.0), (9, 1.09), (17, 0.96), (25, 1.0)])                         # flicker, 24 f
    for frame, value in [(1, 1.0), (29, 1.12), (53, 0.94), (81, 1.0)]:                           # flare pulse, 80 f
        rig["flare"] = value
        rig.keyframe_insert('["flare"]', frame=frame)
    rig["flare"] = 1.0

    from bpy_extras import anim_utils
    action = rig.animation_data.action
    action.name = "JERRY_idle_v001"
    channels = anim_utils.action_get_channelbag_for_slot(action, rig.animation_data.action_slot)
    for fcu in channels.fcurves:
        for kp in fcu.keyframe_points:
            kp.interpolation = "BEZIER"
            kp.handle_left_type = kp.handle_right_type = "AUTO_CLAMPED"
        fcu.modifiers.new("CYCLES")
        fcu.update()


# --- compositor --------------------------------------------------------------------
def build_compositor(scn):
    ng = bpy.data.node_groups.new("JERRY_comp", "CompositorNodeTree")
    ng.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
    layers = ng.nodes.new("CompositorNodeRLayers")
    glare = ng.nodes.new("CompositorNodeGlare")     # soft orange halo
    glare.inputs["Type"].default_value = "Bloom"
    glare.inputs["Quality"].default_value = "High"
    glare.inputs["Threshold"].default_value = 0.35
    glare.inputs["Strength"].default_value = 0.45
    glare.inputs["Size"].default_value = 0.7
    out = ng.nodes.new("NodeGroupOutput")
    ng.links.new(layers.outputs["Image"], glare.inputs["Image"])
    ng.links.new(glare.outputs["Image"], out.inputs[0])
    scn.compositing_node_group = ng
    scn.render.use_compositing = True


def main():
    args = parse_args()
    out = os.path.abspath(args.out)
    cache = os.path.abspath(args.cache)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    os.makedirs(cache, exist_ok=True)

    scn, col = setup_scene()
    body = build_body(col)
    rig = build_rig(col, body)
    build_core(col, rig)
    dom = build_fire(col, rig, body, cache)
    build_embers(col, rig, body)
    build_idle(rig)
    build_compositor(scn)
    scn.frame_set(1)

    bpy.ops.wm.save_as_mainfile(filepath=out, relative_remap=True)
    dom.modifiers["Fluid"].domain_settings.cache_directory = bpy.path.relpath(cache)
    bpy.ops.wm.save_mainfile()
    print("BUILT", out, "cache", bpy.path.relpath(cache))


main()
