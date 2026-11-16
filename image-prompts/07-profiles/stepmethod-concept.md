# stepmethod-concept · Standard Step Method, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `stepmethod` · Standard Step Method (deep link `#/stepmethod`) |
| **Save as** | `img/stepmethod-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: An oblique three-dimensional illustration of a river reach sliced into five evenly spaced vertical cross-section planes, like glass panes. Each pane shows the channel shape and the water level at that section. Curved arrows hop from the most downstream pane to the next one upstream, one step at a time. The water surface connecting the panes is drawn as a smooth translucent ribbon that rises gently upstream.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Known section, next section, step length, water surface computed section by section, march direction. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Known section
- Next section
- Step length
- Water surface computed section by section
- March direction

## Alt text

A river reach sliced into cross-section planes with arrows stepping upstream from one to the next.

## Caption for the page

Start where you know the depth, then balance energy one step at a time.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
