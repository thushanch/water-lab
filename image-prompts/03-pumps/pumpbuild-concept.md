# pumpbuild-concept · Pump Station Builder, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `pumpbuild` · Pump Station Builder (deep link `#/pumpbuild`) |
| **Save as** | `img/pumpbuild-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section cutaway of a wet-well pumping station. Incoming sewer or drain pipe enters a deep concrete wet well holding blue water. Three submersible pumps stand on the floor, two running (small motion lines) and one idle as standby. Four float switches hang on cables at different heights marking stop, duty start, assist start and high-level alarm. Discharge pipes rise from each pump into a common header with non-return valves, leaving the station to the right.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Inlet, duty pump, assist pump, standby pump, float levels: stop, start, assist, alarm, common discharge header. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Inlet, duty pump, assist pump, standby pump, float levels: stop, start, assist, alarm, common discharge header

## Alt text

Cutaway of a wet-well pump station with three pumps, float switches at different levels and a common discharge header.

## Caption for the page

Float levels decide which pumps run. The standby only wakes when something fails.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
