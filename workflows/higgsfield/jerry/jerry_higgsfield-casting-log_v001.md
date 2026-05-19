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

## Approved Design Notes

Add approved Jerry visual decisions here after review.

- 
