**Created:** 2026-05-18
**Modified:** 2026-05-18
**Version:** 1.0

# Jerry Higgsfield Casting Log

Date started: 2026-05-18

## Goal

Use Higgsfield to explore Jerry's visual identity before committing to ComfyUI workflows, LoRA/reference-conditioning, or production shot tests.

## Casting Criteria

- Reads as Jerry: small, brave, expressive flame.
- Clearly made of fire.
- Appealing and emotionally readable through silhouette and body language.
- Clean silhouette.
- No embedded eyes, mouth, brows, or facial features; facial animation will be a separate layer.
- No baked scene or plate background.
- No monster/demon traits.
- Not just a generic flame.

## Base Prompt Seed

Small sentient flame character named Jerry, expressive body language through flame shape only, bright warm inner core, orange and yellow flame body with subtle ember-red edges, clean silhouette, charming and brave, vulnerable but energetic, soft feature-animation appeal, physically made of flame, isolated character design, neutral background, full body visible, no scene background, no facial features.

## Negative / Avoid Language

Avoid monster-like fire demon, avoid humanoid costume, avoid random limbs, avoid scary horror design, avoid baked grass or dirt background, avoid eyes, mouth, brows, nose, smile, face, text, or logos.

## Run Log

### Run 001

- Date: 2026-05-18
- Interface: CLI
- Model: `nano_banana_2` / Nano Banana Pro
- Prompt: Create a single clean character-bible casting still for Jerry, a small sentient flame character. Use the storyboard references for Jerry's charm, simple expressive face, and vulnerable brave personality. Use the fire reference for flame material, warm inner glow, orange/yellow body, and compact teardrop flame silhouette. Full body visible, one character only, readable large eyes and simple mouth, soft animated-film appeal, physically made of real fire, clean isolated character design on black background. Avoid monster, demon, skull, horror, humanoid arms or legs, costume, campfire logs, grass, dirt, forest, plate background, heavy smoke hiding the face, text, logo.
- Input media:
  - `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/priority_06_21_clean-cute.jpg`
  - `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/priority_03_132a_close-worried.jpg`
  - `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/jerry_exr-black_shot12u_jerry5_f0120.png`
- Aspect ratio: `1:1`
- Resolution: `1k`
- Cost: not captured
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260518_235226_be5a40fb-b25b-4e79-9761-5493babf7c66.png`
- Local copy: `assets/characters/jerry/higgsfield-candidates/run001/jerry_higgsfield_nano-banana-pro_casting_run001.png`
- Notes: Good first casting signal for cute, simple, emotionally readable Jerry, but it incorrectly generated embedded eyes and a mouth. The output is appealing and non-monster-like, but it missed the requested black background and reads more like a soft icon/mascot than physically real flame material. Useful only as an appeal/body-language reference, not as a production material target.
- Decision: candidate for appeal direction; not approved

### Run 002

- Date: 2026-05-18
- Interface: CLI
- Model: `nano_banana_2` / Nano Banana Pro
- Prompt: Create a clean base-body casting still for Jerry, a small living flame body for an animated short film. This is ONLY the flame body asset: no eyes, no mouth, no brows, no nose, no face, no facial features, no smile. Make the flame feel cute, vulnerable, brave, and alive only through its compact teardrop silhouette, slight forward lean, soft rounded base, warm glow, squash-and-stretch shape language, and gentle flickering posture. Physically made of real fire with a warm yellow-white inner core, orange and amber body, subtle ember-red edges, soft transparent flame wisps, high quality flame material. Single isolated flame body on pure black background, full body visible, no scene, no logs, no grass, no dirt, no text, no logo, no other characters. Do not draw or imply any face.
- Input media:
  - `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/jerry_exr-black_shot12u_jerry5_f0120.png`
  - `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/jerry_exr-black_shot4_small-fire-extracted_f0089.png`
- Aspect ratio: `1:1`
- Resolution: `1k`
- Cost: not captured
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_000546_8787e485-efc8-4649-b0b2-bf353b80feff.png`
- Local copy: `assets/characters/jerry/higgsfield-candidates/run002/jerry_higgsfield_nano-banana-pro_no-face-body_run002.png`
- Notes: Corrected no-face attempt. Uses only EXR fire-body references because storyboard references contain temp facial animation that may cause baked-in eyes/mouth. Output correctly has no embedded eyes, mouth, or face and sits on black. It is closer to a usable base flame body, though it is less cute/character-specific than Run 001 and still needs stronger Jerry-specific silhouette/personality.
- Decision: candidate for base-body/material direction; not approved

### Run 003

- Date: 2026-05-19
- Interface: CLI
- Model: `nano_banana_2` / Nano Banana Pro
- Prompt: Create Jerry base body design v003 for an animated short film. Jerry is a small living flame body with NO embedded facial features: no eyes, no mouth, no brows, no nose, no smile, no face, no facial marks. This is only the elemental flame body; facial animation will be added later as a separate layer. Use the no-face flame reference for material, black background, warm glow, and real fire texture. Use the storyboard reference only for compact cute body language and vulnerable/brave personality; ignore and do not copy any drawn face from that reference. The body should feel cute and alive through silhouette only: compact rounded teardrop base, slight curious forward lean, soft squash-and-stretch shape, gentle flickering posture, warm yellow-white inner core, orange and amber flame body, subtle ember-red edges, soft transparent flame wisps. Single isolated full-body flame on pure black background. No scene, no logs, no grass, no dirt, no other characters, no text, no logo. Absolutely do not draw or imply eyes or a mouth.
- Input media:
  - `assets/characters/jerry/higgsfield-candidates/run002/jerry_higgsfield_nano-banana-pro_no-face-body_run002.png`
  - `outputs/review/jerry_asset-triage_v001/single-images/storyboard-priority/priority_06_21_clean-cute.jpg`
  - `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/jerry_exr-black_shot4_small-fire-extracted_f0089.png`
- Aspect ratio: `1:1`
- Resolution: `1k`
- Cost: not captured
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_195051_cd17b2b0-829b-45b1-a051-a09fd7dc3cdc.png`
- Local copy: `assets/characters/jerry/higgsfield-candidates/run003/jerry_higgsfield_nano-banana-pro_no-face-body_run003.png`
- Notes: Bridge attempt to combine Run 002 no-face material with storyboard-driven cute body language without copying the temp facial marks. Output kept the no-face rule and black background, but stayed very close to Run 002. It did not gain enough cute/Jerry-specific silhouette.
- Decision: candidate for no-face base-body continuity; not approved

### Run 004

- Date: 2026-05-19
- Interface: CLI
- Model: `nano_banana_2` / Nano Banana Pro
- Prompt: Create Jerry base body design v004, a production-ready no-face living flame body for an animated short film. Keep the strict rule: no eyes, no mouth, no brows, no nose, no smile, no face, no facial marks. The character should feel like a small cute young flame through body shape only: compact rounded lower body, soft teardrop silhouette, slight shy forward lean, gentle asymmetry, small vulnerable scale, brighter warm inner core, lively but contained flickering tip. Make it crisper and more detailed than the reference, with high-resolution real fire material, defined flame layers, glowing yellow-white core, orange amber edges, subtle ember-red rim, soft transparent wisps. Single isolated full-body flame on pure black background, centered, no scene, no logs, no grass, no dirt, no other characters, no text, no logo. Do not draw or imply any facial features.
- Input media:
  - `assets/characters/jerry/higgsfield-candidates/run003/jerry_higgsfield_nano-banana-pro_no-face-body_run003.png`
  - `outputs/review/jerry_asset-triage_v001/single-images/exr-black-stills/jerry_exr-black_shot12tt_jerry5_f0010.png`
- Aspect ratio: `1:1`
- Resolution: `4k`
- Cost: not captured
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_195413_02119220-ebb9-4d43-a3ed-a15c1582300f.png`
- Local copy: `assets/characters/jerry/higgsfield-candidates/run004/jerry_higgsfield_nano-banana-pro_no-face-body_4k_run004.png`
- Notes: Higher-resolution/sharper pass to test whether Run 002/003 softness can be improved while preserving the no-face rule. Output is sharper and still no-face, but it pushed into a close-up/tall fire element and lost the full-body small-character read.
- Decision: useful material/detail reference; not approved as Jerry body anchor

### Run 005

- Date: 2026-05-19
- Interface: CLI
- Model: `nano_banana_2` / Nano Banana Pro
- Prompt: Create a production-ready no-face Jerry base-body reference for an animated short film. Jerry is a small living flame character with no embedded facial features: no eyes, no mouth, no brows, no nose, no smile, no face, no facial marks. Use the external Jerry references for the target body language: compact rounded lower body, cute small teardrop silhouette, warm contained glow, poseable living flame shape. Use the material reference only for sharper real-fire layers and glow detail. Express personality only through body shape, posture, glow, and flame motion: cute, vulnerable, brave, alive. Full body visible with generous negative space around the flame, centered on pure black background, high-resolution real fire material, warm yellow-white inner core, amber/orange body, subtle ember-red rim, transparent wispy flame edges, contained lively flicker. No logs, no grass, no dirt, no scene, no text, no logo, no other characters. Absolutely do not draw or imply facial features.
- Input media:
  - `assets/characters/jerry/look-references/external-v001/jerry_external-look_v001_01_upright-compact-idle.png`
  - `assets/characters/jerry/look-references/external-v001/jerry_external-look_v001_10_round-idle-glow.png`
  - `assets/characters/jerry/higgsfield-candidates/run004/jerry_higgsfield_nano-banana-pro_no-face-body_4k_run004.png`
- Aspect ratio: `1:1`
- Resolution: `2k`
- Cost: not captured
- Output URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3Crp6ySH4DZAPmxwygCFUAodsOa/hf_20260519_201304_4213359e-cd7c-4351-bde9-64f181299635.png`
- Local copy: `assets/characters/jerry/higgsfield-candidates/run005/jerry_higgsfield_nano-banana-pro_final-look-candidate_run005.png`
- Notes: First final-look candidate using the external look-reference set as the primary shape/body target and Run 004 only as material/detail support. Output preserved the no-face rule and has usable high-resolution flame material, but Run 004 dominated the result. It is still too tall/close-up and does not preserve the compact external-v001 body shape.
- Decision: useful material/detail reference; not approved as Jerry body anchor

## Approved Design Notes

Add approved Jerry visual decisions here after review.

-
