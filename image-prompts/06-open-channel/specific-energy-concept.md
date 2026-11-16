# specific-energy-concept · Specific Energy Playground, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `specific-energy` · Specific Energy Playground (deep link `#/specific-energy`) |
| **Save as** | `img/specific-energy-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A longitudinal side-section of a rectangular flume with a smooth raised hump on the floor. Upstream the water is deep and calm, over the hump the water surface dips noticeably, and downstream it returns to its original depth. A perfectly horizontal dashed line runs above the water along the whole length showing constant energy. Small vertical dimension markers show depth upstream, over the hump and the hump height.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Upstream depth, hump height, depth over the hump, energy line stays level, subcritical flow. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Upstream depth
- Hump height
- Depth over the hump
- Energy line stays level
- Subcritical flow

## Alt text

Side section of a flume where water dips over a floor hump while a level energy line runs above.

## Caption for the page

With no losses, energy stays level. Raising the floor takes energy out of the depth.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
