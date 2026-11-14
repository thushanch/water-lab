# freqfit-trap · Frequency Fitting Studio, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `freqfit` · Frequency Fitting Studio (deep link `#/freqfit`) |
| **Save as** | `img/freqfit-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A fitted flood frequency curve extended far beyond a short cloud of data points to a very rare event, with one confident thin line and a precise glowing dot at the far end.
RIGHT PANEL (what really happens): The same data and extrapolation, but the far end is surrounded by a huge shaded uncertainty band, with several different fitted curves spreading apart.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Left: a confident 1000-year flood from 30 years of data
- Right: the honest uncertainty

## Alt text

Two panels: one confident extrapolated curve to a rare flood, and the same with a wide band of disagreeing curves.

## Caption for the page

Thirty years of data cannot tell you the 1000-year flood to the nearest cubic metre.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
