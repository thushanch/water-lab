# shields-trap · Shields Threshold of Motion, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `shields` · Shields Threshold of Motion (deep link `#/shields`) |
| **Save as** | `img/shields-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

## Prompt

Paste everything in the box into ChatGPT as one message.

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A deep, calm river pool with a lot of water above the bed, the gravel bed beneath moving vigorously as if deep water alone sets the grains in motion.
RIGHT PANEL (what really happens): The same deep calm pool with a perfectly still bed, beside a shallow, steep riffle where the water is thin but fast, and gravel is actively rolling.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

## Labels to add in HTML afterwards

AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:

- Left: deeper water moves more sediment
- Right: shear stress depends on depth times slope; the steep riffle wins

## Alt text

Two panels: a deep pool drawn moving its bed, and in reality a still pool beside a shallow steep riffle where gravel moves.

## Caption for the page

It is shear stress, depth times slope, that moves grains, not depth on its own.

## If the first result is off

- Text or numbers crept in: reply *"Same image, but remove every letter, number and label."*
- Water turned teal: reply *"Make all water a clear blue to blue-grey, no green or teal tint."*
- Soil turned brown: reply *"Make all soil and earth a muted olive-grey."*
- Style drifted from earlier images: attach your best previous image and say *"Match the exact style, palette and line weight of this image."*
