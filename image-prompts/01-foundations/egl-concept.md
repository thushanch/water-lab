# egl-concept · EGL / HGL Pipeline Explorer, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `egl` · EGL / HGL Pipeline Explorer (deep link `#/egl`) |
| **Save as** | `img/egl-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean side-section diagram of a pipeline connecting a high reservoir on the left to a lower reservoir on the right. The pipe changes diameter twice along its length (wide, narrow, medium) and climbs over one gentle hump in the middle. Seven slim vertical glass piezometer tubes rise from the pipe crown at even spacing, each filled with blue water to a different height: the water levels step down smoothly from left to right, dropping fastest along the narrow section. The blue line runs exactly through the water level in every tube: it STARTS at the upper reservoir water surface on the left and ENDS exactly at the lower reservoir water surface on the right, so the lower reservoir surface sits level with the end of the blue line, not below it. An orange line runs parallel above the blue line, a small gap above it, the gap widest along the narrow section; it also starts at the upper reservoir surface. Both lines slope down from left to right. Faint flow arrows inside the pipe point from the high reservoir to the low one.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Energy grade line (orange), hydraulic grade line (blue), velocity head gap, friction loss over each segment, the hump where pressure is lowest. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Energy grade line (orange)
- Hydraulic grade line (blue)
- Velocity head gap
- Friction loss over each segment
- The hump where pressure is lowest

## Alt text

Side section of a pipeline between two reservoirs with glass tubes showing the water pressure falling along the pipe, and two sloping lines above it.

## Caption for the page

The piezometer tubes draw the hydraulic grade line for you. The energy line sits one velocity head above it.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
