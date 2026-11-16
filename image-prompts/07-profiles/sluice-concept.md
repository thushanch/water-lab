# sluice-concept · Sluice Gate and Discharge, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `sluice` · Sluice Gate and Discharge (deep link `#/sluice`) |
| **Save as** | `img/sluice-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A two-row side-section comparison of flow under a vertical sluice gate. Top row (free flow): deep water upstream, a jet under the gate that contracts to its smallest depth a short distance downstream (vena contracta), then a hydraulic jump further downstream. Bottom row (drowned flow): the same gate with high tailwater, the jump has moved upstream and submerged the jet right against the gate, with turbulent water over it.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Upstream depth, gate opening, vena contracta, free jump, drowned outlet, tailwater level. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Upstream depth
- Gate opening
- Vena contracta
- Free jump
- Drowned outlet
- Tailwater level

## Alt text

Two side sections of flow under a sluice gate: a free jet with a jump downstream, and a drowned jet under high tailwater.

## Caption for the page

Free or drowned changes the discharge. The tailwater decides which one you have.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
