"""Free and rebake every Mantaflow domain in a .blend, then save it.

    /Applications/Blender.app/Contents/MacOS/Blender -b FILE.blend \
        --python scripts/blender/fluid_bake.py [-- --domain NAME]

Bakes run on the CPU only. Run from a scratch directory: noise-upres bakes write
a 24 MB waveletNoiseTile.bin into the working directory.
"""

import argparse
import sys
import time

import bpy


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    p = argparse.ArgumentParser(description="Bake Mantaflow domains headless.")
    p.add_argument("--domain", help="bake only this domain object")
    args = p.parse_args(argv)

    scn = bpy.context.scene
    domains = [ob for ob in scn.objects
               if any(m.type == "FLUID" and m.fluid_type == "DOMAIN" for m in ob.modifiers)]
    if args.domain:
        domains = [ob for ob in domains if ob.name == args.domain]
    if not domains:
        sys.exit("fluid_bake: no matching fluid domain")

    for dom in domains:
        ds = next(m for m in dom.modifiers if m.type == "FLUID").domain_settings
        start = time.time()
        with bpy.context.temp_override(scene=scn, object=dom, active_object=dom):
            bpy.ops.fluid.free_all()
            result = bpy.ops.fluid.bake_all()
        print("BAKED", dom.name, result, "seconds", round(time.time() - start, 1),
              "has_data", ds.has_cache_baked_data, "cache", ds.cache_directory)
    bpy.ops.wm.save_mainfile()


main()
