"""Shot004 comp geometry shared by the Blender and Fusion comp builders (standard library only).

Pixel coordinates are on the 4096x2160 plate, x from the left, row from the top.
"""

import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))  # repo root
SHOT = os.path.join(ROOT, "shots/shot004_fire-jump/")
PLATE = os.path.join(SHOT, "plates/FW_test_scene.mp4")
JERRY = os.path.join(
    SHOT, "pass-a_jerry/runs/shot004_fire-jump_mick13-skyreels_graymask-promptv3-jb010-str125-lenovo_seed1218565630_v001.mp4")

W, H = 4096, 2160
PLATE_FRAMES, JERRY_FRAMES = 84, 81

# A Mick 1.3 512p clip (912x512) maps onto the plate by a uniform scale about the frame
# centre: x2.0192 at 1920 wide (docs/findings.md, 2026-11-01), then up to 4096.
JERRY_SCALE = (1842 / 912) * (4096 / 1920)  # 4.3077

# Ridge top edge, traced from the focus fall-off of the defocused foreground ridge on
# frame 0; the camera is locked.
RIDGE_EDGE = [(-40, 1812), (576, 1805), (960, 1815), (1216, 1798), (1600, 1796), (1984, 1803),
              (2368, 1800), (2624, 1778), (3008, 1781), (3264, 1782), (3648, 1786), (4136, 1790)]
RIDGE_POLYGON = RIDGE_EDGE + [(4136, 2240), (-40, 2240)]

# The ground-glow limit runs from this row down to the ridge (ground and grass).
GROUND_TOP = 500
GROUND_POLYGON = [(-40, GROUND_TOP), (4136, GROUND_TOP)] + RIDGE_EDGE[::-1]
