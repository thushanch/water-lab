# weir-concept · Weir and Flume Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `weir` · Weir and Flume Lab (deep link `#/weir`) |
| **Save as** | `img/weir-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section of a sharp-crested weir plate across a channel. Upstream the water approaches calmly; at the crest the water surface draws down and springs off as a curved nappe, with a pocket of air drawn under the nappe against the downstream face of the plate. A small vent pipe connects the air pocket to the atmosphere. Upstream at a distance of about four times the head, a point gauge touches the water surface. The tailwater pool sits low below.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Head over crest H, measure about 4H upstream, crest height p, nappe, aerated pocket, vent, tailwater. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Head over crest H
- Measure about 4H upstream
- Crest height p
- Nappe
- Aerated pocket
- Vent
- Tailwater

## Alt text

Side section of a sharp-crested weir with a curved nappe, an aerated pocket below it and a head gauge upstream.

## Caption for the page

Read the head upstream, before the surface starts to draw down, or the rating will lie to you.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
