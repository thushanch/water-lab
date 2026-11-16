# Water Lab image prompts

All 122 ChatGPT image prompts in one document. Copy the text in each grey box into ChatGPT as one message, then save the image under the name given.

## Before you start

- **Images carry no text.** Every prompt forbids letters and numbers, because image models still misspell them. Diagram labels go on top in HTML; each diagram lists them.
- **One ChatGPT chat per family** (A, B, C, D, E). After the first good image in a family, attach it to later requests with: *"Match the exact style, palette and line weight of this image."*
- **Order:** site and covers first, then concept cutaways (B) for the popular sims, then traps (C), then field scenes (A).
- **Check the physics** before publishing: still water is level, grade lines fall in the flow direction, a jump goes shallow to deep, water dips over a hump in slow flow. The full list is in STYLE_GUIDE.md.
- **Export:** WebP, 1200 px wide, quality about 78, into an `img/` folder next to `water-lab.html`.

## Quick fixes

| Problem | Reply to ChatGPT |
|---|---|
| Text or numbers crept in | *Same image, but remove every letter, number and label.* |
| Water turned teal | *Make all water a clear blue to blue-grey, no green or teal tint.* |
| Soil turned brown | *Make all soil and earth a muted olive-grey.* |
| Style drifted | Attach your best earlier image: *Match the exact style, palette and line weight of this image.* |

## Families

| Family | What it is | Count |
|---|---|---:|
| A · In the field | Realistic scene of where the topic shows up | 41 |
| B · Concept cutaway | Textbook cutaway of the mechanism | 41 |
| C · Common trap | Assumption vs reality, two panels | 23 |
| D · Module cover | Banner per topic | 10 |
| E · Site | Home, social card, About, 404, onboarding | 7 |


---

## Site images

### site-hero-backdrop · Home hero backdrop

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-hero-backdrop.webp` |
| **Where it goes** | Home page hero, as a soft background layer behind the existing animated SVG water-cycle scene (low opacity, around 12 to 18 percent), or as a fallback when CSS animation is unavailable. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, used as a wide crop |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A soft, airy watercolour and gouache landscape painting on textured off-white paper, gentle washes, very calm, lots of white space, with faint pencil topographic contour lines visible underneath the paint. Palette strictly limited to deep ocean blue #14416B, water blue #1E78B0, pale blue #9FC4E6, forest green #2E6B4F and off-white paper #F6F7F4, with olive-grey #6E6A5E for earth.
SCENE: The whole water cycle across a Sri Lankan landscape, read from left to right: a rain cloud over misty hill-country ridges, forest and tea on the slopes, a river winding down through paddy terraces and a village, into a reservoir, and out to a calm coastline on the far right with a gentle sea. Very subtle, no hard edges, painted lightly enough to sit behind other content.
COMPOSITION: Keep the left third and the top band especially pale and quiet so a headline and buttons can sit over them. Horizon in the lower half.
DO NOT include: any text, letters, numbers, logos or watermarks; teal or turquoise water; brown soil; people; strong saturated colours; heavy dark areas.
```

#### Alt text

A soft watercolour of the water cycle across hills, a river, a reservoir and the coast.

#### Caption for the page

(decorative, no caption)

### site-social-card · Social share card (Open Graph)

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-social-card.webp (also export a 1200x630 .png)` |
| **Where it goes** | The og:image and twitter:image meta tags, so links shared on WhatsApp, Facebook and LinkedIn show a proper preview. Crop to 1200x630 and add the title "Water Lab" in Poppins 600 yourself in Canva or Figma, on the empty left side. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 1200x630 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Premium editorial illustration, clean flat vector shapes with soft gradients and subtle paper grain, like a high-end engineering textbook cover. Palette: deep ocean blue #14416B background gradient into #0F2C44, water blue #1E78B0, pale blue #9FC4E6, forest green #3E9A6E, a single small accent of orange #E8913C, off-white #F6F7F4 highlights.
SCENE: On the right half, a striking cutaway composition: a hillslope with forest on top, soil and groundwater layers inside, water flowing down into a river channel, a pipe emerging from the hillside with a glowing orange energy line above it, and a small hydraulic jump of white foam in the channel. Faint topographic contour lines drift across the dark background.
COMPOSITION: The entire left 45 percent is calm, dark, empty deep blue so a title can be added later. Important content stays inside the central horizontal band so a 1200x630 crop keeps it.
DO NOT include: any text, letters, numbers, logos, watermarks; teal or turquoise; brown; people.
```

#### Alt text

Water Lab: a cutaway illustration of a hillslope, pipe and river on a deep blue background.

#### Caption for the page

(used in link previews, no caption)

### site-about-banner · About page banner

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-about-banner.webp` |
| **Where it goes** | Top of the About page (#/about), above the person card. Do not generate a likeness of a real person; this is a desk scene, not a portrait. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to a wide strip |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Warm, calm editorial photograph style with soft natural window light, shallow depth of field, gently desaturated colours that lean toward blue and green. Palette leaning on deep blue #14416B, water blue #1E78B0, pale blue #9FC4E6, forest green #2E6B4F and off-white.
SCENE: An engineering lecturer's desk by a window looking out on green trees and a rainy afternoon: an open notebook with hand-drawn sketches of a channel cross-section and a hydrograph (no readable text or numbers), a scale ruler, a mechanical pencil, a scientific calculator, a small glass of water catching the light, and a laptop at the edge showing a blue water simulation. Rain droplets on the window glass.
COMPOSITION: Objects grouped in the right two thirds, the left side softer and quieter so it can be cropped into a wide strip.
DO NOT include: any person or face; any readable text, numbers, logos or brand names; teal; brown wood dominating the frame (use pale grey or white desk).
```

#### Alt text

A study desk by a rainy window with a notebook of channel sketches, a ruler, a calculator and a laptop.

#### Caption for the page

(decorative, no caption)

### site-not-found · Lost route (404 / unknown hash)

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-not-found.webp` |
| **Where it goes** | Shown by route() when a hash does not match any sim or alias, beside a line such as "That simulator has moved or never existed" and a button back to all simulators. |
| **Size in ChatGPT** | 1:1 square, 1024x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a square image (1024x1024).
STYLE: Clean flat vector illustration with soft gradients and thin dark-ink outlines #1C2A33, on an off-white #F6F7F4 background with faint topographic contour lines. Palette: water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, olive-grey #6E6A5E, one small orange #E8913C accent.
SCENE: A friendly, slightly humorous scene: a small paper boat floating on a stream that splits into several channels, with a little wooden signpost at the fork whose arrow boards are blank, the boat drifting toward a calm pool. Gentle and reassuring, not sad.
COMPOSITION: Centred subject with generous empty space around it.
DO NOT include: any text, letters, numbers or symbols on the signpost; logos; teal; brown wood (make the signpost pale grey or white); people.
```

#### Alt text

A paper boat at a fork in a stream beside a blank signpost.

#### Caption for the page

(no caption; the page text carries the message)

### site-apps-header · All simulators page header

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-apps-header.webp` |
| **Where it goes** | Top of the full listing at #/apps, as a slim banner behind the page heading. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to roughly 4:1 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean flat vector illustration with soft gradients and fine contour-line texture, off-white #F6F7F4 background, palette of water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, olive-grey #6E6A5E, and one small orange #E8913C accent.
SCENE: A single continuous horizontal journey of water from left to right through ten small connected vignettes, each a tiny scene: a pipe from a reservoir; a pipe network; a pump; a rain cloud with gauges; rain running off a hill; a lined canal; a hydraulic jump; pebbles on a riverbed; a bell curve over a river; and a whole catchment with a reservoir. The vignettes flow into each other with no borders.
COMPOSITION: Everything sits in the middle horizontal band (about 40 percent of the height) so the image can be cropped into a slim 4:1 strip; above and below are plain off-white.
DO NOT include: any text, numbers, labels or logos; teal; brown; people.
```

#### Alt text

A continuous strip of ten small water scenes from a pipe and a pump to a whole catchment.

#### Caption for the page

(decorative, no caption)

### site-how-to-use · How to read a simulator (onboarding)

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-how-to-use.webp` |
| **Where it goes** | A small "How to use this" card on the home page, or the first time someone opens any sim. Add numbered callouts (1 controls, 2 scene, 3 charts, 4 equations, live, 5 theory) in HTML over the empty margins. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean flat vector UI illustration, isometric-lite, soft shadows, off-white #F6F7F4 background with faint contour lines, thin dark-ink outlines #1C2A33, palette of water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, one small orange #E8913C accent.
SCENE: A stylised laptop screen floating slightly tilted, showing a simplified simulator layout: a column of slider controls on the left, a large scene panel in the middle showing water flowing in a channel, a small line chart below it, and a strip of equation-like blank bars at the bottom. A hand cursor drags one slider and small motion lines show the water in the scene reacting.
COMPOSITION: Leave clear empty margin around each of the five areas (controls, scene, chart, equation strip, a folded theory panel at the bottom) for numbered callouts to be added later.
DO NOT include: any readable text, numbers, letters, logos; teal; brown; real brand UI.
```

#### Alt text

A stylised laptop showing a simulator with sliders, a water scene, a chart and an equation strip.

#### Caption for the page

Move a control, watch the water, read the numbers. The equations update as you go.

### site-study-aid · Study-aid strip / Curious LK footer art

| | |
|---|---|
| **Family** | E · Site |
| **Save as** | `img/site-study-aid.webp` |
| **Where it goes** | The study-aid strip under the footer, as a wide low-contrast background. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to roughly 5:1 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Minimal paper-cut layered illustration in tones of deep ocean blue #14416B, water blue #1E78B0 and pale blue #9FC4E6, with a single thin line of forest green #3E9A6E, soft shadows between layers, very low contrast, calm.
SCENE: Layered gentle waves and contour lines in a horizontal band, with a few small floating icons cut from paper: an open book, a pencil, a water drop, a tiny paper boat, a small lightbulb, scattered with lots of breathing room.
COMPOSITION: All content within the middle horizontal band so it can be cropped very wide and short.
DO NOT include: any text, numbers, logos; teal; brown; people.
```

#### Alt text

Layered paper-cut waves with small floating icons of a book, a pencil, a water drop and a boat.

#### Caption for the page

(decorative, no caption)


---

## 01 · Foundations: Energy and Momentum

### m01-cover · Module 01 cover: Foundations: Energy and Momentum

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m01-cover.webp` |
| **Where it goes** | Module page `#/m/01` header banner, and a cropped thumbnail as the background of the "Foundations: Energy and Momentum" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A single large pipe emerging from a hillside reservoir, with a glowing orange energy line and a blue grade line floating above it like light trails, a Pelton jet spray on one side and a siphon arch on the other, all arranged along one horizontal band.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a pipeline from a reservoir with glowing energy and grade lines above it.

#### Caption for the page

(decorative, no caption)


---

## 02 · Pressure Pipe Systems and Networks

### m02-cover · Module 02 cover: Pressure Pipe Systems and Networks

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m02-cover.webp` |
| **Where it goes** | Module page `#/m/02` header banner, and a cropped thumbnail as the background of the "Pressure Pipe Systems and Networks" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A glowing blue network of pipes and junction nodes spreading beneath a stylised town, with a single pressure wave pulse travelling along one long pipe as a ring of light.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a glowing pipe network beneath a town with a pressure pulse travelling along one pipe.

#### Caption for the page

(decorative, no caption)


---

## 03 · Pumps and Pump Systems

### m03-cover · Module 03 cover: Pumps and Pump Systems

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m03-cover.webp` |
| **Where it goes** | Module page `#/m/03` header banner, and a cropped thumbnail as the background of the "Pumps and Pump Systems" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A spinning centrifugal impeller in the centre with motion blur, water spiralling outward in blue ribbons, two more pumps fading into the background on either side.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a spinning pump impeller with water spiralling outward.

#### Caption for the page

(decorative, no caption)


---

## 04 · Precipitation and Design Rainfall

### m04-cover · Module 04 cover: Precipitation and Design Rainfall

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m04-cover.webp` |
| **Where it goes** | Module page `#/m/04` header banner, and a cropped thumbnail as the background of the "Precipitation and Design Rainfall" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: Monsoon clouds over a stylised island landscape with curtains of rain of different densities falling from them, a few rain gauge silhouettes on the ground, and faint isohyet contour lines drawn over the land.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of monsoon clouds and rain curtains over a landscape with faint rainfall contours.

#### Caption for the page

(decorative, no caption)


---

## 05 · Rainfall-Runoff and Design Flows

### m05-cover · Module 05 cover: Rainfall-Runoff and Design Flows

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m05-cover.webp` |
| **Where it goes** | Module page `#/m/05` header banner, and a cropped thumbnail as the background of the "Rainfall-Runoff and Design Flows" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: Rain falling on a stylised landscape that changes from forest to paddy to town, with blue runoff threads gathering across the surface and converging to one river outlet that rises into a smooth hydrograph shape at the right.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of rain on forest, paddy and town gathering into a river that becomes a hydrograph shape.

#### Caption for the page

(decorative, no caption)


---

## 06 · Open Channel: Uniform and Critical Flow

### m06-cover · Module 06 cover: Open Channel: Uniform and Critical Flow

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m06-cover.webp` |
| **Where it goes** | Module page `#/m/06` header banner, and a cropped thumbnail as the background of the "Open Channel: Uniform and Critical Flow" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A long straight lined canal running to a vanishing point, with a sharp-crested weir and a ripple V-wake in the foreground and smooth uniform water reflecting the sky.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a straight canal with a weir and a V-shaped ripple wake.

#### Caption for the page

(decorative, no caption)


---

## 07 · Profiles and Rapidly Varied Flow

### m07-cover · Module 07 cover: Profiles and Rapidly Varied Flow

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m07-cover.webp` |
| **Where it goes** | Module page `#/m/07` header banner, and a cropped thumbnail as the background of the "Profiles and Rapidly Varied Flow" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A side-section ribbon of water flowing left to right over a spillway into a white hydraulic jump roller, then curving gently into a calm backwater, drawn like a long elegant wave.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of water flowing over a spillway into a hydraulic jump and a calm backwater.

#### Caption for the page

(decorative, no caption)


---

## 08 · Sediment and Scour

### m08-cover · Module 08 cover: Sediment and Scour

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m08-cover.webp` |
| **Where it goes** | Module page `#/m/08` header banner, and a cropped thumbnail as the background of the "Sediment and Scour" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A close-up of riverbed grains and pebbles with a few lifting into the current, transitioning across the banner into a bridge pier with a swirling vortex at its base, then a reservoir silt delta at the far right.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of riverbed grains lifting, a bridge pier vortex, and a reservoir silt delta.

#### Caption for the page

(decorative, no caption)


---

## 09 · Probability and Risk for Design

### m09-cover · Module 09 cover: Probability and Risk for Design

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m09-cover.webp` |
| **Where it goes** | Module page `#/m/09` header banner, and a cropped thumbnail as the background of the "Probability and Risk for Design" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A river valley overlaid with many faint translucent possible flood levels like ghosted futures, a bell curve shape rising from the water, and a scatter of glowing dots trailing into an uncertainty fan.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a river valley with ghosted possible flood levels and an uncertainty fan of dots.

#### Caption for the page

(decorative, no caption)


---

## 10 · Catchment Modelling Studio

### m10-cover · Module 10 cover: Catchment Modelling Studio

| | |
|---|---|
| **Family** | D · Module cover |
| **Save as** | `img/m10-cover.webp` |
| **Where it goes** | Module page `#/m/10` header banner, and a cropped thumbnail as the background of the "Catchment Modelling Studio" tile in Browse by topic on the home page (keep it faint behind the text). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024, cropped to 3:1 and 4:3 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green #3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered.
SUBJECT: A whole catchment in a single cutaway band: a cloud and rain on the left, forested hillslope with soil and groundwater layers in the middle, and a river with a reservoir on the right, faint arrows tracing water through every part.
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; people.
```

#### Alt text

Abstract banner of a whole catchment cutaway from rain through hillslope and groundwater to a river and reservoir.

#### Caption for the page

(decorative, no caption)


---

## 01 · Foundations: Energy and Momentum

### egl-field · EGL / HGL Pipeline Explorer, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `egl` · EGL / HGL Pipeline Explorer (deep link `#/egl`) |
| **Save as** | `img/egl-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A gravity water supply main running down a terraced tea-estate hillside in the central highlands of Sri Lanka. A large-diameter blue-painted steel pipe on concrete saddles follows the slope from a small concrete service reservoir at the top, past a dark green air-release valve chamber on a hump in the line, down to a village water tower far below in the valley. Morning mist in the lower valley, neat rows of tea bushes, silver oak shade trees. Two small engineers in hard hats inspect the valve chamber, seen from behind.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A blue steel water main running down a terraced tea-estate hillside from a reservoir at the top to a village in the valley.

#### Caption for the page

Every gravity main is a story told in head: it starts with height and spends it on friction all the way down.

### egl-concept · EGL / HGL Pipeline Explorer, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `egl` · EGL / HGL Pipeline Explorer (deep link `#/egl`) |
| **Save as** | `img/egl-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean side-section diagram of a pipeline connecting a high reservoir on the left to a lower reservoir on the right. The pipe changes diameter twice along its length (wide, narrow, medium) and climbs over one gentle hump in the middle. Seven slim vertical glass piezometer tubes rise from the pipe crown at even spacing, each filled with blue water to a different height: the water levels step down smoothly from left to right, dropping fastest along the narrow section. The blue line runs exactly through the water level in every tube: it STARTS at the upper reservoir water surface on the left and ENDS exactly at the lower reservoir water surface on the right, so the lower reservoir surface sits level with the end of the blue line, not below it. An orange line runs parallel above the blue line, a small gap above it, the gap widest along the narrow section; it also starts at the upper reservoir surface. Both lines slope down from left to right. Faint flow arrows inside the pipe point from the high reservoir to the low one.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Energy grade line (orange), hydraulic grade line (blue), velocity head gap, friction loss over each segment, the hump where pressure is lowest. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Energy grade line (orange)
- Hydraulic grade line (blue)
- Velocity head gap
- Friction loss over each segment
- The hump where pressure is lowest

#### Alt text

Side section of a pipeline between two reservoirs with glass tubes showing the water pressure falling along the pipe, and two sloping lines above it.

#### Caption for the page

The piezometer tubes draw the hydraulic grade line for you. The energy line sits one velocity head above it.

### egl-trap · EGL / HGL Pipeline Explorer, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `egl` · EGL / HGL Pipeline Explorer (deep link `#/egl`) |
| **Save as** | `img/egl-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): The pipe climbs over a hill that pokes above the blue hydraulic grade line, and the water inside the pipe is drawn as stopped, still and empty past the hump, as if flow simply cannot pass.
RIGHT PANEL (what really happens): The same pipe and hill, but water keeps flowing through the hump. The section above the grade line is tinted pale red to show suction (sub-atmospheric pressure), tiny air bubbles gather at the crown, and a small air-release valve sits on top of the hump.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: what students assume, flow stops
- Right: flow continues under suction, air comes out of solution, the valve matters

#### Alt text

Two panels: a pipe over a hill drawn empty on the left, and flowing under suction with bubbles at the crown on the right.

#### Caption for the page

A pipe above the HGL still flows. It just runs under suction, which invites air, cavitation and dirty groundwater in.

### venturi-field · Venturi and Pitot Virtual Bench, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `venturi` · Venturi and Pitot Virtual Bench (deep link `#/venturi`) |
| **Save as** | `img/venturi-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: Inside the pipe gallery of a modern water treatment plant in Sri Lanka. A large flanged steel pipeline painted in deep blue runs along the floor and narrows smoothly into a venturi section, with small instrument tubing connecting the throat and the inlet to a grey differential pressure transmitter on a wall panel. Clean concrete floor, yellow safety railings in soft focus, soft daylight from high clerestory windows, a hint of filter beds through a glass window in the background.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A blue steel pipeline in a treatment plant gallery narrowing into a venturi meter with instrument tubing to a pressure transmitter.

#### Caption for the page

A venturi meter has no moving parts. It measures flow by reading how much pressure the water spends to speed up.

### venturi-concept · Venturi and Pitot Virtual Bench, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `venturi` · Venturi and Pitot Virtual Bench (deep link `#/venturi`) |
| **Save as** | `img/venturi-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A precise cutaway of a horizontal venturi tube: a straight inlet, a smooth converging cone, a short narrow throat, then a long gentle diverging cone back to full size. Blue water inside with streamlines squeezing together through the throat and spreading again. Two vertical glass piezometer tubes rise from the inlet and from the throat, the throat tube visibly lower. In a separate smaller inset on the right, a Pitot-static tube points upstream into a flow, with a stagnation point at its nose and a U-tube manometer below showing a height difference in darker blue fluid.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Inlet, throat, diverging cone, head difference between the tubes, stagnation point on the Pitot nose, manometer deflection. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Inlet
- Throat
- Diverging cone
- Head difference between the tubes
- Stagnation point on the Pitot nose
- Manometer deflection

#### Alt text

Cutaway of a venturi meter with two pressure tubes, and an inset of a Pitot tube with a manometer.

#### Caption for the page

Faster at the throat means lower pressure there. That pressure drop is the flow measurement.

### thrust-field · Thrust Block Designer, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `thrust` · Thrust Block Designer (deep link `#/thrust`) |
| **Save as** | `img/thrust-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: An open trench in a suburban street near Colombo during pipe laying. At the bottom of the trench, a large ductile iron pipe makes a 45 degree horizontal bend. Behind the outside of the bend, a freshly cast grey concrete thrust block is wedged against the undisturbed trench wall, its timber formwork partly stripped. Trench shoring on the sides, a small excavator arm at the edge of the frame, coconut palms and low houses in the background, overcast sky.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A ductile iron pipe bend at the bottom of a trench with a freshly cast concrete thrust block behind it.

#### Caption for the page

Water changing direction pushes on the bend. The block hands that push to the soil.

### thrust-concept · Thrust Block Designer, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `thrust` · Thrust Block Designer (deep link `#/thrust`) |
| **Save as** | `img/thrust-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A plan-view (seen from above) engineering illustration of a horizontal pipe bend buried in soil. Blue flow arrows enter from the left and leave at an angle. Two pressure force arrows along each pipe leg combine into one thick orange resultant force arrow pointing outward from the bend. Behind the bend, a grey concrete thrust block bears against undisturbed olive-grey soil, with soft fan-shaped pressure contour bands spreading into the soil behind the block. Soil drawn with fine stipple texture.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Pressure force on each leg, resultant thrust, bearing area of the block, passive soil resistance zone. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Pressure force on each leg
- Resultant thrust
- Bearing area of the block
- Passive soil resistance zone

#### Alt text

Plan view of a buried pipe bend with force arrows combining into a resultant that pushes into a concrete block and the soil behind it.

#### Caption for the page

The block area is the thrust divided by what the soil can safely bear.

### jet-field · Jet and Vane Momentum Lab, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `jet` · Jet and Vane Momentum Lab (deep link `#/jet`) |
| **Save as** | `img/jet-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A small run-of-river mini-hydro power house in a forested valley in the Sri Lankan hill country, its side wall cut away to reveal a polished steel Pelton wheel with rows of double cup buckets. A high-speed water jet from a nozzle strikes the buckets and splits into two white curling sprays. Wet stone walls, a green generator housing beside the wheel, rainforest and a stream visible through a doorway.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A Pelton wheel inside a small hydro power house being struck by a water jet that splits into two sprays.

#### Caption for the page

A Pelton bucket turns the jet almost all the way back. Reversing momentum is how it takes nearly all the force.

### jet-concept · Jet and Vane Momentum Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `jet` · Jet and Vane Momentum Lab (deep link `#/jet`) |
| **Save as** | `img/jet-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean side-view diagram of a horizontal water jet leaving a nozzle on the left and striking a curved vane mounted on a small cart with wheels on a rail. The jet follows the vane surface and leaves at a deflection angle. Blue velocity arrows show the incoming and outgoing jet, an orange arrow shows the force on the vane, and a faint dashed outline of a control volume box surrounds the vane.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Incoming jet velocity, outgoing jet velocity, deflection angle, force on the vane, control volume, cart velocity. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Incoming jet velocity
- Outgoing jet velocity
- Deflection angle
- Force on the vane
- Control volume
- Cart velocity

#### Alt text

A water jet striking a curved vane on a wheeled cart, with velocity and force arrows and a control volume around the vane.

#### Caption for the page

Force equals the rate of momentum change. Draw the box, count what crosses it.

### siphon-field · Siphon and Cavitation Sim, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `siphon` · Siphon and Cavitation Sim (deep link `#/siphon`) |
| **Save as** | `img/siphon-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A traditional village irrigation tank (wewa) in the dry zone of Sri Lanka at golden hour. A farmer, seen from behind and small in the frame, has laid a long black flexible siphon pipe over the grassy earth bund, one end in the calm tank water and the other end pouring a steady stream into a channel feeding green paddy fields below. Palmyrah palms, a white egret in the shallows, water lilies on the tank.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A farmer using a flexible pipe to siphon water over an earth tank bund into paddy fields.

#### Caption for the page

A siphon lifts water over the bund with no pump, but only so high before the column breaks.

### siphon-concept · Siphon and Cavitation Sim, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `siphon` · Siphon and Cavitation Sim (deep link `#/siphon`) |
| **Save as** | `img/siphon-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section cutaway of a siphon pipe rising out of an upper tank, arching over a hill crest, and dropping into a lower tank. Water fills the pipe. A smooth colour gradient inside the pipe shows pressure: normal blue near the tanks, fading to pale near the crown. At the very top of the arch a small cluster of vapour bubbles forms. A thin dashed vertical dimension line from the upper tank surface to the crown shows the lift height.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Upper tank level, crown (lowest pressure), lift height, outlet level, total head driving the flow, vapour forms here. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Upper tank level
- Crown (lowest pressure)
- Lift height
- Outlet level
- Total head driving the flow
- Vapour forms here

#### Alt text

Cutaway of a siphon arching over a hill between two tanks, with the lowest pressure and a few vapour bubbles at the crown.

#### Caption for the page

The crown is where the siphon is most at risk. Pressure there falls with every metre of lift and every bit of speed.

### siphon-trap · Siphon and Cavitation Sim, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `siphon` · Siphon and Cavitation Sim (deep link `#/siphon`) |
| **Save as** | `img/siphon-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A siphon over a very tall hill, the arch rising far above the upper tank (clearly more than the height of a three storey building), drawn flowing happily from tank to tank.
RIGHT PANEL (what really happens): The same tall siphon, but at the crown the water column has torn apart: a large pale vapour gap fills the top of the arch and both legs have drained partly back toward their tanks, the flow stopped.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: what people assume, any height works
- Right: above roughly 7 to 8 m of lift, the column breaks

#### Alt text

Two panels: a very tall siphon drawn flowing, and the same siphon with its water column broken by a vapour gap at the top.

#### Caption for the page

Air pressure can only push water up about 10 m, and less in practice. Ask a siphon to lift more and it simply quits.


---

## 02 · Pressure Pipe Systems and Networks

### pipeflow-field · Pipe Network Solver, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `pipeflow` · Pipe Network Solver (deep link `#/pipeflow`) |
| **Save as** | `img/pipeflow-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: An elevated view over a small hillside town in Sri Lanka at dusk, with a cylindrical concrete service reservoir on the hilltop. The image is a semi-cutaway: the streets are partly transparent like an x-ray, revealing a glowing blue network of water pipes beneath them forming connected loops between blocks of houses, with small junction nodes at street corners. Warm house lights, rooftops with clay tiles, palms.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A hillside town at dusk with its streets shown semi-transparent, revealing a looped blue water network fed from a hilltop reservoir.

#### Caption for the page

Under every town is a network where each loop must balance and each junction must add up.

### pipeflow-concept · Pipe Network Solver, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `pipeflow` · Pipe Network Solver (deep link `#/pipeflow`) |
| **Save as** | `img/pipeflow-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean isometric diagram of a looped pipe network on a pale grid: one elevated reservoir on the left feeding a network of eight round junction nodes connected by pipes into two closed loops plus one dead-end branch. Pipes are drawn with thickness proportional to flow, darker blue for bigger flows, with small arrowheads showing direction. Two curved circular arrows inside the loops indicate loop direction. Each junction has a small downward drop icon showing water being drawn off.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Reservoir head, junction demands, pipe flows, loop 1 and loop 2, head loss around each loop sums to zero. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Reservoir head
- Junction demands
- Pipe flows
- Loop 1 and loop 2
- Head loss around each loop sums to zero

#### Alt text

Isometric diagram of a looped pipe network fed by a reservoir, with arrows showing flow direction and junction demands.

#### Caption for the page

Two rules solve any network: flow in equals flow out at every node, and head loss around every loop adds to zero.

### serpar-field · Series and Parallel Pipes, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `serpar` · Series and Parallel Pipes (deep link `#/serpar`) |
| **Save as** | `img/serpar-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A rural road in Sri Lanka where a second large blue water pipeline is being laid in a trench right beside an existing older pipeline, both running parallel into the distance toward low green hills. Pipe sections stacked on the verge, a small crew far away, red earth muted to an olive grey tone, overcast monsoon sky.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A new water pipeline being laid in a trench parallel to an existing one along a rural road.

#### Caption for the page

Duplicating a main is a parallel pipe problem. The gain is real, and smaller than most people guess.

### serpar-concept · Series and Parallel Pipes, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `serpar` · Series and Parallel Pipes (deep link `#/serpar`) |
| **Save as** | `img/serpar-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A two-row comparison diagram. Top row: three pipes of different diameters joined end to end in series between two tanks, each pipe drawn to scale, with a stepped water level in small standpipes showing head falling fastest along the thinnest pipe. Bottom row: two pipes of different diameters running side by side between a common inlet manifold and a common outlet manifold, standpipes at each manifold showing the same head drop across both branches, more flow arrows in the larger pipe.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Series: same flow, losses add. Parallel: same head loss, flows add. The thin pipe dominates. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Series: same flow, losses add
- Parallel: same head loss, flows add
- The thin pipe dominates

#### Alt text

Top: three pipes in series with head stepping down. Bottom: two pipes in parallel sharing one head drop.

#### Caption for the page

In series the flow is shared and losses add. In parallel the head loss is shared and flows add.

### serpar-trap · Series and Parallel Pipes, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `serpar` · Series and Parallel Pipes (deep link `#/serpar`) |
| **Save as** | `img/serpar-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): One pump feeding a single pipe, and beside it the same pump feeding two identical pipes in parallel, with the parallel case drawn delivering twice as many fat flow arrows as the single pipe.
RIGHT PANEL (what really happens): The same comparison, but the parallel case delivers only modestly more flow (a few extra arrows), because the shared pump and the fixed lift still set the limit. A small pump curve icon sits beside each.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: two pipes, double the flow
- Right: more flow, but well short of double

#### Alt text

Two panels comparing one pipe and two parallel pipes: drawn as double the flow on the left, only a modest increase on the right.

#### Caption for the page

Add a second pipe and friction falls, but the pump and the static lift do not care. Flow rises, it does not double.

### moody-field · Moody Chart Navigator, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `moody` · Moody Chart Navigator (deep link `#/moody`) |
| **Save as** | `img/moody-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A university hydraulics laboratory in Sri Lanka. A long pipe friction test rig runs along a wall: transparent and steel pipes of different diameters mounted on a frame, connected by small tubes to a board of manometer columns with coloured fluid at different heights. A sump tank and a small blue pump underneath. Soft afternoon light through tall windows, a notebook and calculator on a workbench in the foreground (pages blank).
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A pipe friction test rig in a hydraulics lab with pipes of different sizes and a manometer board.

#### Caption for the page

Every curve on the Moody chart was once a rig like this, run for hours and read by hand.

### moody-concept · Moody Chart Navigator, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `moody` · Moody Chart Navigator (deep link `#/moody`) |
| **Save as** | `img/moody-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A split illustration of the inside of a pipe cut lengthwise. Left half: laminar flow, smooth parallel streamlines in neat layers with a parabolic velocity profile drawn as arrow lengths. Right half: turbulent flow, swirling eddies of many sizes with a flatter velocity profile. Below the right half, a circular magnified inset of the pipe wall shows small roughness bumps poking through a very thin calm layer of fluid next to the wall.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Laminar: friction set by viscosity. Turbulent: eddies and wall roughness. Viscous sublayer, roughness height. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Laminar: friction set by viscosity
- Turbulent: eddies and wall roughness
- Viscous sublayer
- Roughness height

#### Alt text

Pipe interior split into laminar flow with smooth layers and turbulent flow with eddies, plus a close-up of wall roughness.

#### Caption for the page

Whether roughness matters depends on whether the bumps poke through the thin calm layer at the wall.

### hammer-field · Water Hammer Simulator, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `hammer` · Water Hammer Simulator (deep link `#/hammer`) |
| **Save as** | `img/hammer-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A steep steel penstock pipe descending a forested mountainside to a hydropower station in the Sri Lankan hill country, with a tall cylindrical concrete surge tower standing on the ridge where the pipe begins its descent. Mist drifting through the forest, a reservoir glimpsed at the top, the power house with its tailrace at the bottom. Wide documentary view.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A steel penstock running down a forested mountainside to a power station, with a surge tower on the ridge above.

#### Caption for the page

The surge tower exists for one moment: when the turbine valve shuts and the water in the penstock has nowhere to go.

### hammer-concept · Water Hammer Simulator, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `hammer` · Water Hammer Simulator (deep link `#/hammer`) |
| **Save as** | `img/hammer-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A four-step horizontal storyboard, one step above the next, of the same straight pipe running from a reservoir on the left to a valve on the right. Step 1: valve just closed, a high-pressure zone shown as a slightly bulging, darker section of pipe begins at the valve. Step 2: the bulging high-pressure zone has travelled halfway back toward the reservoir. Step 3: the pressure wave reaches the reservoir and reflects. Step 4: a pale low-pressure zone travels back toward the valve, the pipe wall slightly contracted. Small arrows show the wave direction in each step.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Valve closes, wave travels at speed a, reflection at the reservoir, low pressure returns, one cycle takes 4L/a. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Valve closes
- Wave travels at speed a
- Reflection at the reservoir
- Low pressure returns
- One cycle takes 4L/a

#### Alt text

Four-step storyboard of a pressure wave running from a closed valve back to a reservoir and returning as low pressure.

#### Caption for the page

Close a valve suddenly and a pressure wave runs the length of the pipe, reflects, and comes back inverted.

### hammer-trap · Water Hammer Simulator, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `hammer` · Water Hammer Simulator (deep link `#/hammer`) |
| **Save as** | `img/hammer-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A hand slamming a large valve wheel shut in an instant, with a violent pressure spike drawn as a tall jagged red shape rising from the pipe and the pipe wall visibly bulging.
RIGHT PANEL (what really happens): The same valve being turned slowly over a long time (suggested by a small clock with a long arc), with only a gentle low hump of pressure above the pipe.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: closed faster than 2L/a, full Joukowsky rise
- Right: closed over many wave periods, small rise

#### Alt text

Two panels: a valve slammed shut causing a tall pressure spike, and a valve closed slowly causing only a gentle rise.

#### Caption for the page

Close faster than one wave round trip and you get the full pressure rise, whatever the valve looks like.


---

## 03 · Pumps and Pump Systems

### pump-field · Pump-System Operating Point, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `pump` · Pump-System Operating Point (deep link `#/pump`) |
| **Save as** | `img/pump-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: The interior of a clean municipal water pumping station: three large horizontal centrifugal pumps painted deep blue sit in a row on concrete plinths, each coupled to a grey electric motor, with large flanged suction and delivery pipes and gate valves. Overhead crane rail, a pressure gauge on each delivery pipe, soft industrial daylight, polished floor reflections.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

Three blue centrifugal pumps with motors in a row inside a pumping station.

#### Caption for the page

A pump does not choose its flow. It runs wherever its curve meets the pipeline's.

### pump-concept · Pump-System Operating Point, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `pump` · Pump-System Operating Point (deep link `#/pump`) |
| **Save as** | `img/pump-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A two-part illustration. Left: a cutaway centrifugal pump showing the curved-vane impeller inside a spiral volute casing, water entering at the eye and spiralling out to the delivery. Right: a minimal text-free chart with a falling blue curve (pump head) and a rising orange curve (system head) crossing at one highlighted glowing point, with faint dashed lines from that point down to the horizontal axis and across to the vertical axis.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Impeller eye, volute, delivery. Pump curve, system curve, operating point, static lift. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Impeller eye
- Volute
- Delivery
- Pump curve
- System curve
- Operating point
- Static lift

#### Alt text

Cutaway of a centrifugal pump beside a chart where a falling pump curve crosses a rising system curve.

#### Caption for the page

Where the two curves cross is the only place the pump and the pipes agree.

### pump-trap · Pump-System Operating Point, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `pump` · Pump-System Operating Point (deep link `#/pump`) |
| **Save as** | `img/pump-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A huge oversized pump connected to a modest pipeline, drawn delivering an enormous gush of water out of the pipe end.
RIGHT PANEL (what really happens): The same oversized pump, but a valve on its delivery is almost closed to hold it back, the pump glowing faintly warm, and only a normal stream leaves the pipe. A small chart icon shows the operating point far to the left of the pump's best efficiency zone.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: bigger pump, more water
- Right: the system curve decides; an oversized pump gets throttled and wastes energy

#### Alt text

Two panels: an oversized pump imagined delivering a huge flow, and in reality throttled by a nearly closed valve.

#### Caption for the page

Buying a bigger pump buys a bigger electricity bill. The pipeline still sets the flow.

### pumpbuild-field · Pump Station Builder, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `pumpbuild` · Pump Station Builder (deep link `#/pumpbuild`) |
| **Save as** | `img/pumpbuild-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A stormwater pumping station beside a canal in a low-lying area of Colombo during monsoon rain. A compact concrete building with louvres, large discharge pipes arching over the canal embankment and releasing water, an electrical control kiosk, and the canal running high with greyish water. Wet road, a few umbrellas far away, dense urban buildings behind.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A stormwater pumping station beside a high canal in Colombo during monsoon rain, discharging over the embankment.

#### Caption for the page

When the canal is high, gravity drainage stops and the duty pumps take over.

### pumpbuild-concept · Pump Station Builder, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `pumpbuild` · Pump Station Builder (deep link `#/pumpbuild`) |
| **Save as** | `img/pumpbuild-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section cutaway of a wet-well pumping station. Incoming sewer or drain pipe enters a deep concrete wet well holding blue water. Three submersible pumps stand on the floor, two running (small motion lines) and one idle as standby. Four float switches hang on cables at different heights marking stop, duty start, assist start and high-level alarm. Discharge pipes rise from each pump into a common header with non-return valves, leaving the station to the right.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Inlet, duty pump, assist pump, standby pump, float levels: stop, start, assist, alarm, common discharge header. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Inlet, duty pump, assist pump, standby pump, float levels: stop, start, assist, alarm, common discharge header

#### Alt text

Cutaway of a wet-well pump station with three pumps, float switches at different levels and a common discharge header.

#### Caption for the page

Float levels decide which pumps run. The standby only wakes when something fails.

### npsh-field · NPSH and Cavitation Check, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `npsh` · NPSH and Cavitation Check (deep link `#/npsh`) |
| **Save as** | `img/npsh-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A dramatic close-up of a bronze centrifugal pump impeller removed for inspection, resting on a workshop bench under a work lamp. The leading edges of the vanes near the eye are badly pitted and eroded into a spongy, cratered texture by cavitation, while the rest of the metal is smooth. A gloved hand points at the damage (only the glove visible). Shallow depth of field.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A bronze pump impeller with its vane edges pitted and cratered by cavitation damage.

#### Caption for the page

Cavitation damage looks like the metal was eaten. In a sense, it was: by millions of collapsing bubbles.

### npsh-concept · NPSH and Cavitation Check, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `npsh` · NPSH and Cavitation Check (deep link `#/npsh`) |
| **Save as** | `img/npsh-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section cutaway of a pump drawing water from an open sump below it. The water surface in the sump, the suction pipe rising to the pump, and the impeller eye are clearly drawn. Inside the suction pipe a colour gradient shows pressure falling as the water rises and accelerates. At the impeller eye, small white vapour bubbles form, are carried along the vane, and then collapse near the vane surface, drawn as tiny star bursts with micro-jets hitting the metal.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Sump level, suction lift, friction in the suction pipe, lowest pressure at the eye, bubbles form, bubbles collapse. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Sump level
- Suction lift
- Friction in the suction pipe
- Lowest pressure at the eye
- Bubbles form
- Bubbles collapse

#### Alt text

Cutaway of a pump lifting water from a sump, with vapour bubbles forming at the impeller eye and collapsing on the vane.

#### Caption for the page

NPSH available is what the suction side offers. NPSH required is what the impeller demands. Keep a margin.

### npsh-trap · NPSH and Cavitation Check, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `npsh` · NPSH and Cavitation Check (deep link `#/npsh`) |
| **Save as** | `img/npsh-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): The outside of a running pump installed high above its sump, looking perfectly calm and normal, painted blue, with a green check-shaped indicator light glowing.
RIGHT PANEL (what really happens): The same pump with its casing cut away, revealing the impeller inside churning with vapour bubbles and visible pitting on the vanes, a small red warning glow.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: it runs, so it is fine
- Right: inside, cavitation is eating the impeller

#### Alt text

Two panels: a pump that looks fine from outside, and its cutaway showing cavitation bubbles and pitting inside.

#### Caption for the page

A cavitating pump often keeps running for months. The damage is quiet until it is expensive.

### impeller-field · Impeller and Specific Speed, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `impeller` · Impeller and Specific Speed (deep link `#/impeller`) |
| **Save as** | `img/impeller-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: Three pump impellers displayed on a dark grey workshop bench in a row under soft studio light: a narrow radial-flow centrifugal impeller with long curved vanes, a mixed-flow impeller with angled vanes, and an axial-flow propeller impeller with three broad blades. Machined bronze and stainless steel, crisp reflections, product-photography feel.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

Three impellers on a workbench: a radial centrifugal impeller, a mixed-flow impeller and an axial propeller.

#### Caption for the page

High head and low flow wants a radial impeller. Low head and huge flow wants a propeller. Specific speed tells you which.

### impeller-concept · Impeller and Specific Speed, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `impeller` · Impeller and Specific Speed (deep link `#/impeller`) |
| **Save as** | `img/impeller-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A horizontal morphing sequence of five impeller cross sections (meridional view, half section) from left to right: a wide flat radial impeller where flow turns 90 degrees outward, gradually changing through mixed-flow shapes where the outlet tilts, to an axial impeller where flow passes straight through. A curved arrow under the sequence suggests increasing specific speed. Small blue flow-path arrows in each section.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Radial, mixed flow, axial. Low specific speed to high specific speed. Flow path through each. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Radial
- Mixed flow
- Axial
- Low specific speed to high specific speed
- Flow path through each

#### Alt text

Five impeller cross sections morphing from radial to mixed flow to axial.

#### Caption for the page

Specific speed is one number that predicts the shape of the impeller before anyone draws it.


---

## 04 · Precipitation and Design Rainfall

### idf-field · IDF Curve Lab, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `idf` · IDF Curve Lab (deep link `#/idf`) |
| **Save as** | `img/idf-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: An intense afternoon monsoon downpour over a busy Colombo street, rain falling in heavy grey sheets, roadside drains overflowing at the kerb, tuk-tuks with headlights on in soft focus. In the sharp foreground stands a standard cylindrical copper-and-steel rain gauge on a short concrete post in a small fenced plot, raindrops splashing on its funnel rim.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A heavy monsoon downpour over a Colombo street with a rain gauge standing in the foreground.

#### Caption for the page

Short storms are fierce, long storms are gentle. An IDF curve puts a number on how fierce, for how long, and how rare.

### idf-concept · IDF Curve Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `idf` · IDF Curve Lab (deep link `#/idf`) |
| **Save as** | `img/idf-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: An illustrated row of five rain clouds over identical small squares of ground, arranged from left to right: a small, very dark, compact cloud releasing extremely dense rain for a short time, then progressively larger and lighter clouds releasing gentler rain for longer, ending with a broad pale cloud with light drizzle. Under each, a vertical bar shows intensity (tallest on the left), and a horizontal bar shows duration (longest on the right). A faint smooth curve connects the tops of the intensity bars, falling from left to right.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Intensity, duration, the falling IDF curve, shorter means fiercer, rarer storms sit on higher curves. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Intensity
- Duration
- The falling IDF curve
- Shorter means fiercer
- Rarer storms sit on higher curves

#### Alt text

Five rain clouds from short and intense to long and gentle, with bars showing intensity falling as duration grows.

#### Caption for the page

The same rare storm is fierce over ten minutes and gentle over a day. The curve is that trade-off.

### thiessen-field · Areal Rainfall Studio, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `thiessen` · Areal Rainfall Studio (deep link `#/thiessen`) |
| **Save as** | `img/thiessen-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A wide elevated view over a green river basin in Sri Lanka from a hilltop: paddy fields, villages, patches of forest and a winding river. Scattered across the landscape, small but clearly visible, are rain gauges: a few standard cylinder gauges in fenced plots and one automatic tipping-bucket weather station with a small solar panel. Faint dotted lines drawn over the landscape suggest the boundaries between gauge zones. A grey rain shower falls over one part of the basin while the rest is in sunshine.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An elevated view over a river basin with rain gauges scattered across it and a shower falling over one part.

#### Caption for the page

Each gauge sees one point. The question is how much rain fell on everything in between.

### thiessen-concept · Areal Rainfall Studio, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `thiessen` · Areal Rainfall Studio (deep link `#/thiessen`) |
| **Save as** | `img/thiessen-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A top-down map illustration of an irregular river basin outline on off-white paper. Seven gauge points are marked as small dark circles. The basin is split down the middle: the left half is divided into flat-tinted polygon cells around each gauge in different shades of blue (Thiessen polygons, cell edges as thin lines), the right half shows smooth curved contour bands of rainfall in graded blues (isohyets), darkest where rain was heaviest. The river network drawn as thin pale lines.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Gauges, Thiessen polygons (left), isohyets (right), basin boundary, heavier rain darker. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Gauges
- Thiessen polygons (left)
- Isohyets (right)
- Basin boundary
- Heavier rain darker

#### Alt text

Map of a river basin with seven gauges, divided into polygon cells on the left and smooth rainfall contours on the right.

#### Caption for the page

Polygons give each gauge the area nearest to it. Isohyets let the rainfall field bend between gauges.

### thiessen-trap · Areal Rainfall Studio, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `thiessen` · Areal Rainfall Studio (deep link `#/thiessen`) |
| **Save as** | `img/thiessen-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A hilly basin cross-section where all the rain gauges sit in the lowland valley near the town and river, under light rain, with a small bar chart icon showing modest rainfall.
RIGHT PANEL (what really happens): The same basin with the full storm visible: very heavy rain on the windward ridges and mountain slopes where no gauge stands, and only light rain over the valley gauges.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: what the gauges report
- Right: the orographic rain they never saw

#### Alt text

Two panels: rain gauges all in a valley reporting light rain, while heavy rain falls on the ungauged ridges.

#### Caption for the page

Gauges are put where people live, not where rain falls hardest. Every averaging method inherits that bias.

### designstorm-field · Design Storm Builder, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `designstorm` · Design Storm Builder (deep link `#/designstorm`) |
| **Save as** | `img/designstorm-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A dramatic monsoon storm front approaching across wide green paddy fields in Sri Lanka: a towering dark blue-grey cloud wall with a sharp leading edge and a curtain of rain under it on the left half of the sky, while the right half still has soft late sunlight on the fields. A lone farmhouse and a line of coconut palms on a field bund, wind bending the rice.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A dark monsoon storm front with a rain curtain advancing across paddy fields.

#### Caption for the page

Two storms can drop the same depth. When the heaviest part arrives decides the flood.

### designstorm-concept · Design Storm Builder, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `designstorm` · Design Storm Builder (deep link `#/designstorm`) |
| **Save as** | `img/designstorm-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A grid of four small identical catchments, each with a rain hyetograph drawn as blue vertical bars hanging above it and a flood hydrograph drawn as a filled blue shape beside it. The four rain patterns have the same total but different timing: heaviest at the start, heaviest in the middle, heaviest at the end, and evenly spread. The hydrographs differ: the end-loaded storm gives the tallest sharpest peak, the even storm the lowest broadest one.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Front loaded, centre loaded, back loaded, uniform. Same depth, different peaks. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Front loaded
- Centre loaded
- Back loaded
- Uniform
- Same depth
- Different peaks

#### Alt text

Four catchments with rain bar charts of equal total but different timing, each producing a differently shaped flood.

#### Caption for the page

Rain that arrives late falls on wet ground. That is why back-loaded storms make bigger floods.

### infil-field · Infiltration and Runoff Split, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `infil` · Infiltration and Runoff Split (deep link `#/infil`) |
| **Save as** | `img/infil-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: Close-up, low angle, of heavy rain falling on a grassy field edge next to a dirt track. Raindrops splash on the ground, small puddles have formed in a shallow depression and thin sheets of muddy water have started to flow across the track surface. The soil shown in muted olive-grey earth tones. Dark overcast sky, droplets frozen mid-splash.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

Heavy rain on a field edge with puddles forming and thin sheets of runoff starting to flow across a track.

#### Caption for the page

Runoff starts the moment the rain falls faster than the soil can take it in.

### infil-concept · Infiltration and Runoff Split, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `infil` · Infiltration and Runoff Split (deep link `#/infil`) |
| **Save as** | `img/infil-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A tall rectangular soil column cutaway in olive-grey earth tones, like a lab specimen. Rain falls on top. In the upper soil, a darker wet zone extends downward with a sharp wavy wetting front marking its lower edge, above dry lighter soil. On the surface a thin pond of water has formed and a small arrow shows excess water running off to the side. Beside the column, a small inset curve shows infiltration capacity falling quickly at first then levelling off.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Rain, ponding, runoff, wet zone, wetting front, dry soil, infiltration capacity falling with time. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Rain
- Ponding
- Runoff
- Wet zone
- Wetting front
- Dry soil
- Infiltration capacity falling with time

#### Alt text

Cutaway soil column with rain on top, a wet zone and wetting front moving down, and runoff from a surface pond.

#### Caption for the page

Dry soil drinks fast, then slows. Rain that exceeds the current rate becomes runoff.


---

## 05 · Rainfall-Runoff and Design Flows

### rational-field · Rational Method Explorer, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `rational` · Rational Method Explorer (deep link `#/rational`) |
| **Save as** | `img/rational-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A high aerial view over a dense suburb near Colombo during steady rain: clay-tile and metal roofs, narrow roads shining wet, roadside drains carrying water, all converging to a large concrete box culvert under a main road where a stream of runoff gushes out. Patches of garden green and a few trees between buildings. Soft grey light.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An aerial view of a wet suburb with drains converging to a culvert under a main road.

#### Caption for the page

Every drain in a town like this was sized with Q = CiA, whether the designer knew the name or not.

### rational-concept · Rational Method Explorer, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `rational` · Rational Method Explorer (deep link `#/rational`) |
| **Save as** | `img/rational-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A top-down illustration of a small leaf-shaped catchment draining to an outlet at the bottom. The catchment is divided into curved bands (isochrones) shaded from pale blue near the outlet to deeper blue at the far edge, showing equal travel-time zones. A thin highlighted path runs from the most remote point at the top to the outlet, with small footprint-like dots along it. Small rooftops and trees are scattered across the catchment in a mix.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Outlet, isochrones, the longest flow path, time of concentration, runoff coefficient from land cover. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Outlet
- Isochrones
- The longest flow path
- Time of concentration
- Runoff coefficient from land cover

#### Alt text

Top-down catchment with curved travel-time bands and the longest flow path from the farthest point to the outlet.

#### Caption for the page

The peak comes when water from the farthest point finally reaches the outlet: the time of concentration.

### rational-trap · Rational Method Explorer, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `rational` · Rational Method Explorer (deep link `#/rational`) |
| **Save as** | `img/rational-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A catchment where the entire area is lit up as contributing to the outlet from the very first minute of rain, with arrows from everywhere at once.
RIGHT PANEL (what really happens): The same catchment a few minutes into the storm: only the band nearest the outlet is lit and contributing, the rest still grey, and a clock icon shows that full contribution has not arrived yet.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: the whole catchment from minute one
- Right: only the area within the travel time contributes until t_c

#### Alt text

Two panels: a whole catchment drawn contributing at once, and only the band near the outlet contributing early in the storm.

#### Caption for the page

Choose a storm shorter than t_c and part of the catchment never gets to join in.

### uh-field · Unit Hydrograph Convolution, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `uh` · Unit Hydrograph Convolution (deep link `#/uh`) |
| **Save as** | `img/uh-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A river gauging station on a medium-sized Sri Lankan river during a rising flood: a tall white staff gauge with graduated bands (no readable numbers) stands in brown-grey swirling water that has already covered its lower half, next to a small concrete gauge house with a cableway above the river. Debris floating, overcast sky, green riverbank trees.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A staff gauge standing in a rising flood beside a small gauge house and a cableway over the river.

#### Caption for the page

The unit hydrograph is read from records like this: the river's signature response to one unit of rain.

### uh-concept · Unit Hydrograph Convolution, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `uh` · Unit Hydrograph Convolution (deep link `#/uh`) |
| **Save as** | `img/uh-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A layered illustration showing convolution. At the top, four blue rain bars of different heights in sequence. Below, four identical-shaped translucent hydrograph humps, each scaled to its rain bar's height and shifted right by one time step, in four different blues. At the bottom, the four humps stacked and summed into one larger smooth flood hydrograph outline drawn in dark ink.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Rainfall excess blocks, one scaled and delayed unit hydrograph per block, the sum is the flood. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Rainfall excess blocks
- One scaled and delayed unit hydrograph per block
- The sum is the flood

#### Alt text

Four rain bars each producing a scaled, delayed copy of the same hydrograph shape, stacked into one flood hydrograph.

#### Caption for the page

Each block of rain launches its own copy of the unit hydrograph. The flood is all the copies added up.

### uh-trap · Unit Hydrograph Convolution, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `uh` · Unit Hydrograph Convolution (deep link `#/uh`) |
| **Save as** | `img/uh-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A small flood hydrograph and a huge flood hydrograph drawn as exact scaled-up copies of each other, same timing, same shape, just taller, over a simple river channel.
RIGHT PANEL (what really happens): The huge flood arriving earlier and peaking more sharply than the scaled copy, with the river spilling onto its floodplain in a small inset, a faint ghost outline of the scaled copy behind it for comparison.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: linearity assumed
- Right: extreme floods run faster than the UH predicts

#### Alt text

Two panels: a big flood drawn as a scaled copy of a small one, and in reality arriving earlier and peaking sharper.

#### Caption for the page

A unit hydrograph built from ordinary floods tends to be too slow for extreme ones. The bias has a known direction.

### scs-field · SCS Curve Number Explorer, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `scs` · SCS Curve Number Explorer (deep link `#/scs`) |
| **Save as** | `img/scs-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A panoramic view across a Sri Lankan landscape during light rain showing three land covers side by side from left to right: dense natural forest on a hillside, terraced green paddy fields in the middle, and a growing town of concrete roofs and tarmac roads on the right. Rainwater visibly runs off the roads and roofs into a drain, while the forest floor looks absorbent and calm.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A landscape in rain with forest on the left, paddy fields in the middle and a town on the right.

#### Caption for the page

Same rain, three surfaces, three very different amounts of runoff. The curve number is that difference in one index.

### scs-concept · SCS Curve Number Explorer, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `scs` · SCS Curve Number Explorer (deep link `#/scs`) |
| **Save as** | `img/scs-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section illustration of rain falling on a strip of ground that changes from forest on the left to grassland in the middle to paved town on the right. The rain is split into three visible paths shown with arrows in different blues: water caught by leaves and small surface hollows (initial abstraction), water soaking down into olive-grey soil, and water running off over the surface. The runoff arrow grows dramatically from left to right while the infiltration arrow shrinks.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Initial abstraction, infiltration, runoff. Low CN forest, medium CN grass, high CN town. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Initial abstraction
- Infiltration
- Runoff
- Low CN forest
- Medium CN grass
- High CN town

#### Alt text

Rain falling on forest, grass and town, splitting into abstraction, infiltration and runoff, with runoff growing toward the town.

#### Caption for the page

Nothing runs off until the initial abstraction is filled. After that, the soil and the surface share what is left.

### scs-trap · SCS Curve Number Explorer, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `scs` · SCS Curve Number Explorer (deep link `#/scs`) |
| **Save as** | `img/scs-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): Two identical catchments each receiving the same daily rain total, one storm compressed into a single intense hour and one spread across a whole day, both drawn producing an identical tall flood peak at the outlet.
RIGHT PANEL (what really happens): The same two storms: the one-hour storm producing a sharp tall flood peak, the all-day storm producing a low broad hydrograph, while a small bucket icon beside each shows that their runoff volumes are similar.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: CN gives the peak
- Right: CN gives volume only; timing sets the peak

#### Alt text

Two panels: two storms with the same daily total drawn giving the same flood, and in reality very different peaks with similar volumes.

#### Caption for the page

The curve number method knows nothing about intensity. Use it for runoff volume, not for the peak.

### scsuh-field · SCS Synthetic Unit Hydrograph, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `scsuh` · SCS Synthetic Unit Hydrograph (deep link `#/scsuh`) |
| **Save as** | `img/scsuh-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A remote, ungauged small catchment in the dry zone of Sri Lanka seen from a low hill: scrub jungle, rocky outcrops, a few seasonal streams converging into a small village tank in the middle distance, no gauge or station in sight. A lone engineer with a field tablet and a measuring wheel stands small on a dirt track, seen from behind. Hazy afternoon heat.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An ungauged dry-zone catchment of scrub and rock draining into a small tank, with an engineer on a track.

#### Caption for the page

Most catchments were never gauged. A synthetic unit hydrograph builds their response from the map.

### scsuh-concept · SCS Synthetic Unit Hydrograph, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `scsuh` · SCS Synthetic Unit Hydrograph (deep link `#/scsuh`) |
| **Save as** | `img/scsuh-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A two-part illustration. Left: a top-down catchment sketch with the divide drawn as a dashed line, contour lines inside it, the longest flow path highlighted with arrows to the outlet, and a small wedge symbol showing average slope. Right: a smooth bell-like hydrograph curve with a simple triangle of the same area overlaid on it, the triangle's peak aligned with the curve's peak.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Area, longest flow path, slope, curve number, lag time, time to peak, base time of the triangle. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Area
- Longest flow path
- Slope
- Curve number
- Lag time
- Time to peak
- Base time of the triangle

#### Alt text

A catchment map with its longest flow path and slope beside a smooth hydrograph overlaid with an equivalent triangle.

#### Caption for the page

Area, length, slope and land cover. Four numbers off a map give you a hydrograph.


---

## 06 · Open Channel: Uniform and Critical Flow

### manning-field · Manning Normal Depth, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `manning` · Manning Normal Depth (deep link `#/manning`) |
| **Save as** | `img/manning-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A long, straight concrete-lined trapezoidal irrigation canal of a Mahaweli-style scheme in Sri Lanka, running toward the horizon between green paddy fields and a service road. The water flows smooth and steady at uniform depth, reflecting the sky. A small foot bridge crosses in the middle distance, palmyrah palms, a clear morning sky.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A long straight lined irrigation canal flowing at uniform depth between paddy fields.

#### Caption for the page

Down a long straight canal, gravity and friction strike a balance. That depth is normal depth.

### manning-concept · Manning Normal Depth, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `manning` · Manning Normal Depth (deep link `#/manning`) |
| **Save as** | `img/manning-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean cross-section of a trapezoidal channel filled with water, with concentric curved velocity contour bands inside the water: deepest blue fastest band just below the surface in the middle, fading to pale near the bed and sloping sides. The wetted perimeter (bed plus wetted sides) is traced with a bold orange line. Small hatch marks on the concrete lining. A faint side-view wedge in a corner shows the bed slope.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Flow area, wetted perimeter, hydraulic radius, bed slope, roughness n, fastest flow near the surface centre. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Flow area
- Wetted perimeter
- Hydraulic radius
- Bed slope
- Roughness n
- Fastest flow near the surface centre

#### Alt text

Trapezoidal channel cross-section with velocity contours fastest near the surface centre and the wetted perimeter highlighted.

#### Caption for the page

Area over wetted perimeter is the hydraulic radius. Friction lives on the perimeter.

### manning-trap · Manning Normal Depth, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `manning` · Manning Normal Depth (deep link `#/manning`) |
| **Save as** | `img/manning-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A clean concrete-lined canal with a material swatch icon of smooth concrete beside it, drawn with a single low roughness indicator.
RIGHT PANEL (what really happens): The same concrete canal after years of service: weeds and grass growing on the side slopes, silt deposits on the bed, floating debris, and a bend in the alignment, with a much higher roughness indicator.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: n is set by the lining
- Right: weeds, silt, debris and bends raise n far above the textbook value

#### Alt text

Two panels: a clean new concrete canal, and the same canal with weeds, silt and debris that raise its roughness.

#### Caption for the page

Manning's n describes the channel you will actually have, not the one in the drawings.

### specific-energy-field · Specific Energy Playground, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `specific-energy` · Specific Energy Playground (deep link `#/specific-energy`) |
| **Save as** | `img/specific-energy-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A long glass-walled laboratory flume in a university hydraulics lab with blue-tinted water flowing over a smooth raised hump fixed to the flume floor. The water surface visibly dips as it passes over the hump. A pointer gauge on a carriage above the flume, a technician's hand adjusting a valve at the far end (hand only). Clean lab lighting, glass reflections.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A glass laboratory flume with water flowing over a raised hump, the surface dipping above it.

#### Caption for the page

Raise the floor and slow, deep water drops over it. That surprises almost everyone the first time.

### specific-energy-concept · Specific Energy Playground, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `specific-energy` · Specific Energy Playground (deep link `#/specific-energy`) |
| **Save as** | `img/specific-energy-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A longitudinal side-section of a rectangular flume with a smooth raised hump on the floor. Upstream the water is deep and calm, over the hump the water surface dips noticeably, and downstream it returns to its original depth. A perfectly horizontal dashed line runs above the water along the whole length showing constant energy. Small vertical dimension markers show depth upstream, over the hump and the hump height.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Upstream depth, hump height, depth over the hump, energy line stays level, subcritical flow. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Upstream depth
- Hump height
- Depth over the hump
- Energy line stays level
- Subcritical flow

#### Alt text

Side section of a flume where water dips over a floor hump while a level energy line runs above.

#### Caption for the page

With no losses, energy stays level. Raising the floor takes energy out of the depth.

### specific-energy-trap · Specific Energy Playground, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `specific-energy` · Specific Energy Playground (deep link `#/specific-energy`) |
| **Save as** | `img/specific-energy-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A channel with a raised floor hump where the water surface simply dips over the hump, drawn the same way for a very high hump that nearly fills the channel.
RIGHT PANEL (what really happens): The same very high hump, but the flow has choked: water backs up into a much deeper pool upstream, then pours over the hump at critical depth and races away shallow and fast downstream.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: a bigger hump just means a bigger dip
- Right: past the critical height, the flow chokes and backs up upstream

#### Alt text

Two panels: water dipping over a very tall hump, and in reality the flow choking and backing up upstream.

#### Caption for the page

Every channel has a limit. Raise the hump past it and the upstream water must rise to get over.

### froude-field · Froude Wave Tank, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `froude` · Froude Wave Tank (deep link `#/froude`) |
| **Save as** | `img/froude-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: Two streams side by side in a split composition. Left: a slow, calm lowland stream where a dropped pebble creates concentric ripples that spread in all directions, including upstream. Right: a fast, shallow mountain stream rushing over smooth rocks, where a single protruding stone leaves a sharp V-shaped wake trailing only downstream. Clear water, natural stones, soft daylight, both from a similar elevated angle.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

Left: ripples spreading in all directions on a slow stream. Right: a sharp V wake behind a stone in a fast stream.

#### Caption for the page

If ripples can climb upstream, the flow is subcritical. If they are swept away in a V, it is supercritical.

### froude-concept · Froude Wave Tank, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `froude` · Froude Wave Tank (deep link `#/froude`) |
| **Save as** | `img/froude-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: Three square panels viewed from above, each showing water flowing left to right with a small disturbance point. Panel 1: a set of ripple circles shifted slightly downstream but still enclosing the source on all sides. Panel 2: circles whose upstream edges all line up on one vertical line through the source. Panel 3: circles swept far downstream forming a sharp V-shaped wedge behind the source, nothing upstream of it. Flow arrows at the top of each panel get longer from panel 1 to panel 3.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Fr < 1 subcritical, Fr = 1 critical, Fr > 1 supercritical, wave speed versus flow speed. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Fr < 1 subcritical
- Fr = 1 critical
- Fr > 1 supercritical
- Wave speed versus flow speed

#### Alt text

Three overhead panels of ripple rings from a point source as flow speed rises, ending in a V-shaped wedge.

#### Caption for the page

The Froude number compares how fast the water moves with how fast a wave can travel through it.

### froude-trap · Froude Wave Tank, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `froude` · Froude Wave Tank (deep link `#/froude`) |
| **Save as** | `img/froude-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A fast, shallow channel with a gate partly lowered far downstream, and imagined ripple signals drawn travelling upstream from the gate to warn the water above, which adjusts its level.
RIGHT PANEL (what really happens): The same fast channel, but the ripple signals from the gate are swept downstream and never reach the water above, which stays unaware until a hydraulic jump forms right at the gate.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: downstream changes travel up
- Right: in supercritical flow, no information goes upstream

#### Alt text

Two panels: signals drawn travelling upstream in a fast channel, and in reality swept downstream with a jump forming at the gate.

#### Caption for the page

In supercritical flow the water upstream cannot know what lies ahead. Control comes from upstream.

### weir-field · Weir and Flume Lab, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `weir` · Weir and Flume Lab (deep link `#/weir`) |
| **Save as** | `img/weir-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A sharp-crested rectangular measuring weir across a concrete irrigation channel in Sri Lanka. A thin steel plate crest with a clean transparent sheet of falling water (the nappe) springing clear of the plate and falling into a pool below, air visible beneath the falling sheet. A small staff gauge set upstream on the channel wall, green paddy fields and a farmer's bicycle in the background.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A sharp-crested weir in an irrigation channel with a clear sheet of water springing off its crest.

#### Caption for the page

Measure the head above the crest and the weir tells you the flow. That is what a weir is for.

### weir-concept · Weir and Flume Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `weir` · Weir and Flume Lab (deep link `#/weir`) |
| **Save as** | `img/weir-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section of a sharp-crested weir plate across a channel. Upstream the water approaches calmly; at the crest the water surface draws down and springs off as a curved nappe, with a pocket of air drawn under the nappe against the downstream face of the plate. A small vent pipe connects the air pocket to the atmosphere. Upstream at a distance of about four times the head, a point gauge touches the water surface. The tailwater pool sits low below.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Head over crest H, measure about 4H upstream, crest height p, nappe, aerated pocket, vent, tailwater. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Head over crest H
- Measure about 4H upstream
- Crest height p
- Nappe
- Aerated pocket
- Vent
- Tailwater

#### Alt text

Side section of a sharp-crested weir with a curved nappe, an aerated pocket below it and a head gauge upstream.

#### Caption for the page

Read the head upstream, before the surface starts to draw down, or the rating will lie to you.

### compound-field · Compound Channel Capacity, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `compound` · Compound Channel Capacity (deep link `#/compound`) |
| **Save as** | `img/compound-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A Sri Lankan river in flood during the southwest monsoon: the main channel runs fast and dark with debris, and the water has spilled over its banks onto wide floodplain paddy fields on both sides, where it spreads shallow and slow, with rice tops and fence posts poking through. A road embankment and a line of trees in the distance, heavy grey sky.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A river in flood spilling out of its main channel onto wide floodplain paddy fields.

#### Caption for the page

Once the river leaves its banks, two very different flows share one cross-section.

### compound-concept · Compound Channel Capacity, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `compound` · Compound Channel Capacity (deep link `#/compound`) |
| **Save as** | `img/compound-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A cross-section of a compound channel: a deep main channel in the centre with wide shallow floodplains on both sides, all filled with water. Thin vertical dashed lines divide the section into three zones at the main channel banks. The main channel water is a deeper, faster blue with long flow arrows; the floodplain water is paler with short flow arrows. At the junctions between zones, small swirling vortex shapes indicate shear.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Main channel, left and right floodplain, division lines, fast and slow zones, shear at the interface. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Main channel
- Left and right floodplain
- Division lines
- Fast and slow zones
- Shear at the interface

#### Alt text

Cross-section of a main channel with floodplains on both sides, divided into fast and slow zones with vortices between them.

#### Caption for the page

Treat the floodplain and the main channel separately, then add the flows. Lumping them together underestimates capacity.


---

## 07 · Profiles and Rapidly Varied Flow

### openchannel-field · Open Channel Modeller, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `openchannel` · Open Channel Modeller (deep link `#/openchannel`) |
| **Save as** | `img/openchannel-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A long irrigation canal descending in steps through a gently sloping Sri Lankan landscape, seen from a raised viewpoint: a series of concrete drop structures where the water falls a short height into stilling pools, with calm reaches between them. Paddy fields and coconut groves on both sides, a vehicle track along the bund.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An irrigation canal stepping down through a landscape with a series of small drop structures.

#### Caption for the page

Build a channel of reaches and structures, and each one sets the water surface of its neighbours.

### openchannel-concept · Open Channel Modeller, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `openchannel` · Open Channel Modeller (deep link `#/openchannel`) |
| **Save as** | `img/openchannel-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A long-section illustration of a channel along its length: the bed changes slope twice, with a sluice gate near the left, a mild reach, a steeper reach in the middle and a weir at the right end. The water surface curves smoothly between controls: rising behind the weir, drawing down toward the slope break, and showing a small hydraulic jump below the gate. Two thin dashed reference lines run along each reach for normal and critical depth.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Gate, mild reach, steep reach, weir, normal depth, critical depth, backwater, drawdown, jump. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Gate
- Mild reach
- Steep reach
- Weir
- Normal depth
- Critical depth
- Backwater
- Drawdown
- Jump

#### Alt text

Long section of a channel with a gate, two slopes and a weir, the water surface curving between them.

#### Caption for the page

Controls hold the water surface; the reaches between them bend it toward normal depth.

### profiles-field · Water Surface Profiles, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `profiles` · Water Surface Profiles (deep link `#/profiles`) |
| **Save as** | `img/profiles-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A traditional stone anicut (diversion weir) across a wide, slow river in Sri Lanka in the dry season. Upstream of the weir the river is backed up into a long calm mirror-like reach extending far into the distance, while water spills smoothly over the weir crest. Large trees reflected in the backwater, a few cattle grazing on the bank.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A stone diversion weir across a river with a long calm backwater reach extending far upstream.

#### Caption for the page

A weir raises the river for kilometres upstream. That long gentle curve is a backwater profile.

### profiles-concept · Water Surface Profiles, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `profiles` · Water Surface Profiles (deep link `#/profiles`) |
| **Save as** | `img/profiles-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: Two separate long side-section panels stacked one above the other, water flowing from left to right in both, on the same gently sloping (mild) channel bed. TOP PANEL: the channel ends at a concrete dam at the right edge of the panel. Far upstream on the left the water is at its natural uniform depth; moving right toward the dam the water gets steadily deeper, its surface curving gently upward until it is level with the reservoir behind the dam. Nothing is drawn downstream of the dam. BOTTOM PANEL: the same channel ends in a free overfall at the right edge, a sharp drop where water pours off the end. Far upstream the water is at its natural uniform depth; moving right toward the brink the surface curves gently downward, the water getting shallower, and pours over the edge. In both panels a dashed line parallel to the bed marks the natural uniform (normal) depth, and a second, lower dashed line parallel to the bed marks critical depth.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Normal depth line, critical depth line, M1 backwater behind the dam (top), M2 drawdown at the fall (bottom), mild slope. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Normal depth line
- Critical depth line
- M1 backwater behind the dam (top)
- M2 drawdown at the fall (bottom)
- Mild slope

#### Alt text

Long section of a river with a curved backwater behind a dam and a drawdown curve toward a free overfall.

#### Caption for the page

Every profile is the water surface easing from what a control demands toward what the channel prefers.

### profiles-trap · Water Surface Profiles, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `profiles` · Water Surface Profiles (deep link `#/profiles`) |
| **Save as** | `img/profiles-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A river reach behind a dam with the water surface drawn level with the dam only very close to it, and parallel to the bed (uniform depth) everywhere else, as if the dam's influence ends a few metres upstream.
RIGHT PANEL (what really happens): The same reach with the backwater curve extending far upstream, many kilometres, flooding a village and a bridge far away, with a faint ghost of the uniform-depth surface for comparison.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: the dam only affects its immediate surroundings
- Right: on a mild slope, backwater reaches far upstream

#### Alt text

Two panels: a dam's effect drawn as short, and in reality a backwater curve reaching a distant village and bridge.

#### Caption for the page

On a mild river, a new weir can raise flood levels in a town many kilometres away.

### jump-field · Hydraulic Jump Lab, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `jump` · Hydraulic Jump Lab (deep link `#/jump`) |
| **Save as** | `img/jump-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: The stilling basin at the foot of a concrete dam spillway during a release: fast smooth water shoots down the spillway chute, then abruptly erupts into a churning white roller of foam and spray in the basin, and leaves calmer and deeper downstream. Concrete baffle blocks just visible in the basin, mist hanging in the air, forested hills around.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A hydraulic jump erupting into white foam in the stilling basin at the foot of a dam spillway.

#### Caption for the page

The stilling basin is built to make a jump. Its job is to destroy energy before it reaches the riverbed.

### jump-concept · Hydraulic Jump Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `jump` · Hydraulic Jump Lab (deep link `#/jump`) |
| **Save as** | `img/jump-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section of a horizontal rectangular channel showing a hydraulic jump: on the left a thin, fast supercritical stream with long arrows, then a steep turbulent roller where the depth rises sharply with swirling eddies and entrained air bubbles, then on the right a deep, slow subcritical flow with short arrows. Two vertical dimension markers show the shallow depth before and the deep depth after. A thin energy line above drops sharply across the jump.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Supercritical inflow y1, roller, subcritical outflow y2, sequent depths, energy lost in the jump. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Supercritical inflow y1
- Roller
- Subcritical outflow y2
- Sequent depths
- Energy lost in the jump

#### Alt text

Side section of a hydraulic jump from shallow fast flow through a turbulent roller to deep slow flow.

#### Caption for the page

Momentum is conserved across a jump. Energy is not, and that loss is the point.

### jump-trap · Hydraulic Jump Lab, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `jump` · Hydraulic Jump Lab (deep link `#/jump`) |
| **Save as** | `img/jump-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A stilling basin below a spillway with the jump sitting neatly inside the basin, drawn as a permanent fixed feature.
RIGHT PANEL (what really happens): The same basin with low tailwater: the jump has been swept out of the basin and sits far downstream on the unprotected riverbed, which is badly eroded with scattered riprap.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: the jump stays put
- Right: too little tailwater and the jump sweeps out of the basin

#### Alt text

Two panels: a jump held inside a stilling basin, and the jump swept downstream onto an eroded riverbed when tailwater is low.

#### Caption for the page

Tailwater holds the jump in place. Get it wrong and the jump goes looking for the riverbed.

### sluice-field · Sluice Gate and Discharge, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `sluice` · Sluice Gate and Discharge (deep link `#/sluice`) |
| **Save as** | `img/sluice-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A steel vertical-lift sluice gate in the concrete headworks of an irrigation canal off a large Sri Lankan reservoir: the gate is raised a short way and a powerful jet of water rushes out underneath it into the canal, forming whitewater a short distance downstream. A grey gate hoist mechanism on the deck above, the reservoir water calm behind the gate, a mountain in the distance.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A vertical-lift sluice gate raised slightly with a powerful jet of water rushing out underneath into a canal.

#### Caption for the page

Under a gate, depth is traded for speed. Where that fast water slows down decides the rest.

### sluice-concept · Sluice Gate and Discharge, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `sluice` · Sluice Gate and Discharge (deep link `#/sluice`) |
| **Save as** | `img/sluice-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A two-row side-section comparison of flow under a vertical sluice gate. Top row (free flow): deep water upstream, a jet under the gate that contracts to its smallest depth a short distance downstream (vena contracta), then a hydraulic jump further downstream. Bottom row (drowned flow): the same gate with high tailwater, the jump has moved upstream and submerged the jet right against the gate, with turbulent water over it.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Upstream depth, gate opening, vena contracta, free jump, drowned outlet, tailwater level. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Upstream depth
- Gate opening
- Vena contracta
- Free jump
- Drowned outlet
- Tailwater level

#### Alt text

Two side sections of flow under a sluice gate: a free jet with a jump downstream, and a drowned jet under high tailwater.

#### Caption for the page

Free or drowned changes the discharge. The tailwater decides which one you have.

### stepmethod-field · Standard Step Method, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `stepmethod` · Standard Step Method (deep link `#/stepmethod`) |
| **Save as** | `img/stepmethod-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A survey team, small figures seen from the side, measuring river cross-sections along a gentle Sri Lankan river in the dry season: one person holds a levelling staff in the shallow water, another stands at an automatic level on a tripod on the bank, colourful ranging poles mark a line across the river. Several such section lines continue upstream, marked by poles. Green banks, clear sky.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A survey team measuring a river cross-section with a levelling staff and an automatic level on the bank.

#### Caption for the page

The step method marches from section to section. Every section was first a line of poles like these.

### stepmethod-concept · Standard Step Method, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `stepmethod` · Standard Step Method (deep link `#/stepmethod`) |
| **Save as** | `img/stepmethod-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: An oblique three-dimensional illustration of a river reach sliced into five evenly spaced vertical cross-section planes, like glass panes. Each pane shows the channel shape and the water level at that section. Curved arrows hop from the most downstream pane to the next one upstream, one step at a time. The water surface connecting the panes is drawn as a smooth translucent ribbon that rises gently upstream.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Known section, next section, step length, water surface computed section by section, march direction. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Known section
- Next section
- Step length
- Water surface computed section by section
- March direction

#### Alt text

A river reach sliced into cross-section planes with arrows stepping upstream from one to the next.

#### Caption for the page

Start where you know the depth, then balance energy one step at a time.


---

## 08 · Sediment and Scour

### shields-field · Shields Threshold of Motion, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `shields` · Shields Threshold of Motion (deep link `#/shields`) |
| **Save as** | `img/shields-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: An underwater macro view at bed level in a clear, flowing gravel-bed stream: a carpet of rounded pebbles and coarse sand, with a few of the smaller grains lifting off the bed and rolling or hopping downstream in the current, while the larger pebbles stay put. Sunlight caustic patterns ripple across the stones. Natural grey-olive stone colours.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

Underwater view of a gravel stream bed with a few small grains starting to roll downstream while larger pebbles stay.

#### Caption for the page

At the threshold, only some grains move, and only some of the time. Shields put a number on that moment.

### shields-concept · Shields Threshold of Motion, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `shields` · Shields Threshold of Motion (deep link `#/shields`) |
| **Save as** | `img/shields-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A close-up side-view diagram of one rounded grain resting in a pocket between neighbouring grains on a stream bed. Flow passes over it from left to right with a velocity profile drawn as arrows growing with height. Force arrows act on the grain: a horizontal drag arrow, an upward lift arrow, and a downward weight arrow, with a small pivot point marked where the grain touches the downstream neighbour.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Flow, drag, lift, submerged weight, pivot point, bed shear stress. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Flow
- Drag
- Lift
- Submerged weight
- Pivot point
- Bed shear stress

#### Alt text

A single grain on a stream bed with drag, lift and weight arrows and a pivot point against its neighbour.

#### Caption for the page

The grain moves when drag and lift can roll it over its pivot against its own weight.

### shields-trap · Shields Threshold of Motion, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `shields` · Shields Threshold of Motion (deep link `#/shields`) |
| **Save as** | `img/shields-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A deep, calm river pool with a lot of water above the bed, the gravel bed beneath moving vigorously as if deep water alone sets the grains in motion.
RIGHT PANEL (what really happens): The same deep calm pool with a perfectly still bed, beside a shallow, steep riffle where the water is thin but fast, and gravel is actively rolling.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: deeper water moves more sediment
- Right: shear stress depends on depth times slope; the steep riffle wins

#### Alt text

Two panels: a deep pool drawn moving its bed, and in reality a still pool beside a shallow steep riffle where gravel moves.

#### Caption for the page

It is shear stress, depth times slope, that moves grains, not depth on its own.

### scour-field · Bridge Pier Scour, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `scour` · Bridge Pier Scour (deep link `#/scour`) |
| **Save as** | `img/scour-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A road bridge with round concrete piers over a fast-flowing Sri Lankan river in flood. At the base of the nearest pier, the muddy water swirls in a visible horseshoe-shaped eddy wrapping around the upstream face, with a turbulent wake trailing downstream. Floating debris caught against the pier. Overcast sky, green banks.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A bridge pier in a flooded river with water swirling around its base and a turbulent wake behind it.

#### Caption for the page

The most dangerous thing a river does to a bridge happens underwater, at the foot of its piers.

### scour-concept · Bridge Pier Scour, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `scour` · Bridge Pier Scour (deep link `#/scour`) |
| **Save as** | `img/scour-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A three-dimensional cutaway of a cylindrical bridge pier standing in a riverbed, with the bed and water cut open to reveal what happens below. Flow approaches from the left; at the upstream face a downward flow dives to the bed and rolls into a horseshoe-shaped vortex that wraps around both sides of the pier. A cone-shaped scour hole is excavated around the pier base, deepest at the front. Small wake vortices peel off behind the pier.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Approach flow, down flow, horseshoe vortex, scour hole, wake vortices, foundation depth. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Approach flow
- Down flow
- Horseshoe vortex
- Scour hole
- Wake vortices
- Foundation depth

#### Alt text

Cutaway of a bridge pier with a horseshoe vortex wrapping around its base and a scour hole dug around it.

#### Caption for the page

Flow diving down the front of the pier rolls into a horseshoe vortex and digs the hole.

### scour-trap · Bridge Pier Scour, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `scour` · Bridge Pier Scour (deep link `#/scour`) |
| **Save as** | `img/scour-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A bridge pier after a flood, seen in a cutaway: the riverbed around the pier looks flat and normal, and an inspector's torch beam shows nothing unusual.
RIGHT PANEL (what really happens): The same cutaway with layers revealed: a deep scour hole that formed at the flood peak, now refilled with loose, lighter-coloured sediment, and the pier's foundation exposed and undermined beneath the refill.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: the bed looks fine after the flood
- Right: the hole that formed at the peak has been refilled with loose sediment

#### Alt text

Two panels: a normal looking bed after a flood, and the cutaway revealing a refilled scour hole that undermined the foundation.

#### Caption for the page

Scour holes refill as floods recede. A post-flood inspection can miss the depth that nearly took the bridge.

### traplife-field · Reservoir Trap Efficiency and Life, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `traplife` · Reservoir Trap Efficiency and Life (deep link `#/traplife`) |
| **Save as** | `img/traplife-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A large reservoir in the Sri Lankan hills during a dry spell with low water: at the upstream end, where a river enters, a broad grey-olive sediment delta has built out into the reservoir, cracked silt flats with scattered green weeds, the river meandering across it. The dam is visible far away at the other end of the lake. Hazy hills, low sun.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A reservoir at low water with a large silt delta built out where the river enters.

#### Caption for the page

Every reservoir is slowly filling with soil. Trap efficiency tells you how fast.

### traplife-concept · Reservoir Trap Efficiency and Life, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `traplife` · Reservoir Trap Efficiency and Life (deep link `#/traplife`) |
| **Save as** | `img/traplife-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A long-section illustration of a reservoir from the river inflow on the left to the dam on the right. Coarse sediment (drawn as larger grey-olive particles) settles first as a delta with a steep front near the inflow; finer sediment (small pale particles) travels further and settles as a thin layer along the bed toward the dam. A small plume of the finest particles passes over the dam crest with the outflow. Faint horizontal bands mark the live storage and dead storage zones.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Inflow with sediment, delta (coarse), bottomset (fine), dead storage, live storage, sediment passing the dam. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Inflow with sediment
- Delta (coarse)
- Bottomset (fine)
- Dead storage
- Live storage
- Sediment passing the dam

#### Alt text

Long section of a reservoir with a coarse sediment delta near the inflow and fine silt settling toward the dam.

#### Caption for the page

Coarse grains drop first and build a delta. Fines travel to the dam. Some escape downstream.

### traplife-trap · Reservoir Trap Efficiency and Life, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `traplife` · Reservoir Trap Efficiency and Life (deep link `#/traplife`) |
| **Save as** | `img/traplife-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A brand-new reservoir full of clear blue water behind its dam, with a symbol suggesting it lasts forever.
RIGHT PANEL (what really happens): The same reservoir a few decades later from the same viewpoint: a large sediment delta has crept down the lake, the water area is noticeably smaller, and the intake tower stands close to the encroaching silt.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: storage is permanent
- Right: sediment eats live storage year after year

#### Alt text

Two panels: a new full reservoir, and the same reservoir decades later with a sediment delta shrinking it.

#### Caption for the page

A reservoir's capacity is a stock being drawn down. Design life is part of the design.


---

## 09 · Probability and Risk for Design

### montecarlo-field · Monte Carlo Design Risk, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `montecarlo` · Monte Carlo Design Risk (deep link `#/montecarlo`) |
| **Save as** | `img/montecarlo-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A rural road crossing a seasonal stream in Sri Lanka through a box culvert, seen from the downstream side in the dry season. Painted onto the image as faint translucent blue horizontal lines across the culvert headwall are many possible flood water levels, clustered thickly in the middle and sparse at the top and bottom, like ghosted futures. Scrub vegetation, dry stream bed, warm afternoon light.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A box culvert under a rural road with faint ghosted lines showing many possible flood levels across its headwall.

#### Caption for the page

Every input is uncertain, so the answer is a spread of futures, not a single line.

### montecarlo-concept · Monte Carlo Design Risk, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `montecarlo` · Monte Carlo Design Risk (deep link `#/montecarlo`) |
| **Save as** | `img/montecarlo-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: An abstract illustration of a Monte Carlo simulation: on the left, three small input distribution bell curves stacked vertically, each with dots being drawn out of it like balls from a machine. In the middle, a stream of many small dots flows through a simple funnel-shaped model box. On the right, the dots pile up into a histogram of outcomes, with a thin vertical line marking a design limit and the dots beyond it tinted red.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Uncertain inputs, random samples, model, distribution of outcomes, design limit, probability of failure. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Uncertain inputs
- Random samples
- Model
- Distribution of outcomes
- Design limit
- Probability of failure

#### Alt text

Dots sampled from three input distributions flow through a model box and pile up into a histogram with a failure tail.

#### Caption for the page

Sample the inputs thousands of times and count how often the design fails. That count is the risk.

### risk-field · Risk and Return Period, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `risk` · Risk and Return Period (deep link `#/risk`) |
| **Save as** | `img/risk-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: The weathered whitewashed wall of an old riverside building in a Sri Lankan town, with several historical flood high-water marks painted as horizontal lines at different heights, some with small blank metal plaques beside them (no readable text). A river flows calmly past in the background, a bicycle leaning against the wall, soft morning light, gentle documentary realism.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An old building wall with several historical flood high-water marks painted at different heights.

#### Caption for the page

Some of these marks sit only a few years apart. A 100-year flood is a probability, not a timetable.

### risk-concept · Risk and Return Period, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `risk` · Risk and Return Period (deep link `#/risk`) |
| **Save as** | `img/risk-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A calendar-like grid of 100 small squares in ten rows of ten, each square one year, pale off-white. A handful of squares contain a blue water drop icon marking flood years, scattered randomly: two drops sit in adjacent squares, and a long stretch of rows has no drops at all. Above the grid, a small horizontal bar shows the probability of seeing at least one flood during a project lifetime.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: One square per year, annual exceedance probability 1/T, design life n, risk of at least one exceedance. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- One square per year
- Annual exceedance probability 1/T
- Design life n
- Risk of at least one exceedance

#### Alt text

A grid of 100 year-squares with a few randomly scattered flood drops, two of them in consecutive years.

#### Caption for the page

Over a 100-year life, a 100-year flood has about a two in three chance of turning up at least once.

### risk-trap · Risk and Return Period, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `risk` · Risk and Return Period (deep link `#/risk`) |
| **Save as** | `img/risk-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A timeline of 300 years with 100-year floods drawn as neat evenly spaced markers exactly every 100 years, like a clock.
RIGHT PANEL (what really happens): The same 300-year timeline with flood markers placed randomly: two in back-to-back years, then a gap of over 150 years, then another.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: once every 100 years
- Right: a 1 percent chance each year, in any order

#### Alt text

Two timelines: floods evenly spaced every 100 years, and floods randomly clustered with two in consecutive years.

#### Caption for the page

The river does not keep a diary. Last year's flood does not make this year safer.

### freqfit-field · Frequency Fitting Studio, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `freqfit` · Frequency Fitting Studio (deep link `#/freqfit`) |
| **Save as** | `img/freqfit-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: An archive room at a hydrology office: shelves of old bound streamflow record ledgers and long paper chart rolls from a mechanical water-level recorder, one chart unrolled on a wooden table showing a hand-drawn ink trace of river level rising and falling (no readable text or numbers). A desk lamp, a magnifying glass, dust in the light.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An archive of old river record ledgers with a paper water-level chart unrolled on a table.

#### Caption for the page

A frequency curve is only as good as the record behind it, and records are short.

### freqfit-concept · Frequency Fitting Studio, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `freqfit` · Frequency Fitting Studio (deep link `#/freqfit`) |
| **Save as** | `img/freqfit-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A clean text-free chart illustration: a cloud of dark dots representing annual flood peaks plotted against a horizontal axis of rarity. A smooth fitted curve passes through the dots and continues to the right beyond the last dot. Past the data, a shaded uncertainty fan opens up around the curve, getting very wide toward the far right. Two or three alternative fitted curves in different line styles diverge in the fan region.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Observed annual maxima, fitted distribution, record length, extrapolation region, widening uncertainty. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Observed annual maxima
- Fitted distribution
- Record length
- Extrapolation region
- Widening uncertainty

#### Alt text

Annual flood peaks with a fitted curve that continues past the data into a widening uncertainty fan.

#### Caption for the page

Inside the record, every distribution agrees. Outside it, they argue.

### freqfit-trap · Frequency Fitting Studio, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `freqfit` · Frequency Fitting Studio (deep link `#/freqfit`) |
| **Save as** | `img/freqfit-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A fitted flood frequency curve extended far beyond a short cloud of data points to a very rare event, with one confident thin line and a precise glowing dot at the far end.
RIGHT PANEL (what really happens): The same data and extrapolation, but the far end is surrounded by a huge shaded uncertainty band, with several different fitted curves spreading apart.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: a confident 1000-year flood from 30 years of data
- Right: the honest uncertainty

#### Alt text

Two panels: one confident extrapolated curve to a rare flood, and the same with a wide band of disagreeing curves.

#### Caption for the page

Thirty years of data cannot tell you the 1000-year flood to the nearest cubic metre.

### freqlab-field · Flood Frequency Lab, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `freqlab` · Flood Frequency Lab (deep link `#/freqlab`) |
| **Save as** | `img/freqlab-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A student's study desk at night, viewed over their shoulder (no face visible): a laptop showing a blank spreadsheet grid and a scatter chart with a curve (no readable numbers), a printed table of annual peaks with highlighter marks, a scientific calculator, a cup of tea, and a window showing rain on the glass and city lights beyond.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A student's desk at night with a laptop showing a spreadsheet and a flood frequency chart, rain on the window.

#### Caption for the page

Bring your own record. The real work is defending the fit you choose.

### freqlab-concept · Flood Frequency Lab, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `freqlab` · Flood Frequency Lab (deep link `#/freqlab`) |
| **Save as** | `img/freqlab-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A left-to-right workflow illustration in four stages connected by arrows: a river gauge station icon; a vertical bar chart of annual peak flows by year; the same bars sorted from largest to smallest with rank numbers suggested by dot markers; and finally a scatter of points on probability paper with a fitted straight-ish line through them.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Gauge record, annual maximum series, rank and plotting position, fit on probability paper. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Gauge record
- Annual maximum series
- Rank and plotting position
- Fit on probability paper

#### Alt text

Four stage workflow from a river gauge to annual peaks, sorted ranks, and points with a fitted line.

#### Caption for the page

Pick the annual maxima, rank them, give each a probability, then fit and argue.

### reliability-field · Reliability and Redundancy, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `reliability` · Reliability and Redundancy (deep link `#/reliability`) |
| **Save as** | `img/reliability-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A grassy earthen flood levee protecting a small Sri Lankan village during high river levels: the river on the left runs swollen and close to the levee crest, while houses and paddy fields sit lower on the right, protected. Sandbags stacked along one section of the crest, a few people small in the distance checking the bank. Grey sky with a break of light.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An earth levee holding back a swollen river close to its crest, with a village sitting lower behind it.

#### Caption for the page

A levee is designed for a chosen flood. Reliability asks how often nature exceeds the choice.

### reliability-concept · Reliability and Redundancy, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `reliability` · Reliability and Redundancy (deep link `#/reliability`) |
| **Save as** | `img/reliability-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A side-section of an earth levee with the river on the left. Instead of a single water level, a sideways bell-shaped probability curve rises from the riverbed, showing the spread of possible annual flood levels, its upper tail extending above the levee crest. The part of the tail above the crest is shaded in red. The freeboard between the design level and the crest is marked with a small dimension line.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Distribution of flood levels, design level, freeboard, crest, probability of overtopping. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Distribution of flood levels
- Design level
- Freeboard
- Crest
- Probability of overtopping

#### Alt text

Earth levee section with a sideways bell curve of possible flood levels, its tail above the crest shaded red.

#### Caption for the page

Overtopping probability is the area of the tail that peeks over the crest.

### reliability-trap · Reliability and Redundancy, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `reliability` · Reliability and Redundancy (deep link `#/reliability`) |
| **Save as** | `img/reliability-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A long levee drawn uniformly strong along its whole length, all sections glowing a healthy green.
RIGHT PANEL (what really happens): The same long levee seen from above with one short low spot (a road crossing ramp) and one section weakened by an animal burrow, water breaking through at that one weak point while the rest holds.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: strong almost everywhere means safe
- Right: a series system fails at its weakest link

#### Alt text

Two panels: a uniformly strong levee, and the same levee failing at one low road crossing.

#### Caption for the page

Systems fail where you did not look. One low spot sets the reliability of the whole line.


---

## 10 · Catchment Modelling Studio

### catchment-field · The Living Catchment, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `catchment` · The Living Catchment (deep link `#/catchment`) |
| **Save as** | `img/catchment-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A sweeping aerial panorama of a Sri Lankan hill-country catchment: misty forested ridges at the top, tea estates and home gardens on the middle slopes, a village and paddy terraces in the valley, a river winding down to a reservoir with a dam in the lower right. Patches of rain falling from a cloud over the ridges, sunlight on the valley. Cinematic yet calm.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

An aerial panorama of a hill-country catchment from forested ridges through tea and villages down to a river and reservoir.

#### Caption for the page

One catchment, one storm, every millimetre accounted for.

### catchment-concept · The Living Catchment, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `catchment` · The Living Catchment (deep link `#/catchment`) |
| **Save as** | `img/catchment-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A detailed side-section cutaway of a single hillslope draining to a river channel on the right. Above: a rain cloud. Rain falls on a forest canopy, some caught on leaves, some evaporating upward as faint wisps. On the ground: an olive-grey soil layer with a darker moist zone, arrows showing infiltration down into soil, percolation further down to a groundwater zone with a gently sloping water table, groundwater seeping slowly toward the stream as baseflow, and a thin sheet of overland flow running down the surface to the channel. Each flux shown as a clean arrow in a distinct shade of blue or green.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Rain, interception, evapotranspiration, infiltration, soil store, percolation, groundwater, baseflow, overland flow, channel flow. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Rain
- Interception
- Evapotranspiration
- Infiltration
- Soil store
- Percolation
- Groundwater
- Baseflow
- Overland flow
- Channel flow

#### Alt text

Cutaway hillslope showing rain, interception, evaporation, infiltration, groundwater, baseflow and overland flow to a river.

#### Caption for the page

Every arrow is a flux the model tracks, and the ledger must balance.

### catchment-trap · The Living Catchment, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `catchment` · The Living Catchment (deep link `#/catchment`) |
| **Save as** | `img/catchment-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A forested catchment under an extreme multi-day storm, the river beside it calm and well within its banks, a shield icon over the forest.
RIGHT PANEL (what really happens): The same forested catchment under the same extreme storm with saturated soils: the river is in flood and spilling over its banks, though a faint ghost line shows the flood would have been even higher without the forest.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: forests stop floods
- Right: forests damp moderate floods; extreme storms on wet soil still flood

#### Alt text

Two panels: a forested catchment drawn as flood-proof, and in reality still flooding under an extreme storm, though less than if cleared.

#### Caption for the page

Forest buys storage, and storage fills. In the biggest storms it helps, but it cannot stop the flood.

### calib-field · Calibration Arena, in the field

| | |
|---|---|
| **Family** | A · In the field |
| **Simulator** | `calib` · Calibration Arena (deep link `#/calib`) |
| **Save as** | `img/calib-field.webp` |
| **Where it goes** | Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under "Where you meet it in practice"). |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Editorial digital painting with gentle photographic realism, like a documentary photo lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and trustworthy. Colours lean on deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E. Water reads as clear blue to blue-grey, never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. Any people are small in the frame, in work clothes, seen from behind or the side, with no recognisable faces.
SCENE: A hydrologist, seen from behind and small, standing on the bank at a river gauging station at dusk with a rugged laptop open on a field case, comparing a screen showing two overlapping hydrograph curves (no readable text) with the river flowing in front. A staff gauge in the river, a cableway above, warm last light on the water.
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; readable signage or brand names; close-up faces.
```

#### Alt text

A hydrologist at a river gauging station at dusk comparing two hydrograph curves on a laptop.

#### Caption for the page

A model earns trust by matching the river, and by showing how many other models match it just as well.

### calib-concept · Calibration Arena, how it works

| | |
|---|---|
| **Family** | B · Concept cutaway |
| **Simulator** | `calib` · Calibration Arena (deep link `#/calib`) |
| **Save as** | `img/calib-concept.webp` |
| **Where it goes** | Theory panel, at the top of the first section ("What this is"), with the labels below overlaid in HTML. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: Clean technical illustration in the style of a premium engineering textbook: flat vector shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or isometric cutaway, generous negative space on an off-white #F6F7F4 background with very faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in #2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line or a force arrow, red #D2452F only for danger.
SUBJECT: A three-dimensional landscape illustration representing a model performance surface: a smooth terrain in graded blues with a long, narrow, curving bright ridge running diagonally across it instead of a single peak. Several small glowing dots sit at different positions along the ridge top, each representing a different parameter set with an almost equal score. Faint contour lines on the terrain.
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: Parameter 1, parameter 2, score (NSE or KGE), the ridge of equally good parameter sets. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; photographic textures; 3D render gloss.
```

#### Labels to add in HTML afterwards

- Parameter 1
- Parameter 2
- Score (NSE or KGE)
- The ridge of equally good parameter sets

#### Alt text

A 3D performance surface with a long bright ridge instead of a single peak, and several dots along the ridge.

#### Caption for the page

The best score is not a summit, it is a ridge. Many parameter sets fit almost equally well.

### calib-trap · Calibration Arena, the common trap

| | |
|---|---|
| **Family** | C · Common trap |
| **Simulator** | `calib` · Calibration Arena (deep link `#/calib`) |
| **Save as** | `img/calib-trap.webp` |
| **Where it goes** | Theory panel, in the "Common trap" section, with the two short labels overlaid in HTML above each panel. |
| **Size in ChatGPT** | 3:2 landscape, 1536x1024 |
| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |

#### Prompt

```text
Create a 3:2 landscape image (1536x1024).
STYLE: A two-panel side-by-side comparison in the same clean technical illustration style as a premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines #1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, #1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red #D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check mark icon in its top corner. Both panels share the same viewpoint and scale so the difference is obvious.
LEFT PANEL (the assumption): A single winning parameter set shown as one gold trophy on a podium, with one model diagram above it, presented as the catchment's true values.
RIGHT PANEL (what really happens): Five quite different model diagrams (different store sizes and arrow thicknesses) side by side, each producing a near-identical hydrograph curve that overlaps the observed one.
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster or injury imagery; letters inside the icons (use shapes only).
```

#### Labels to add in HTML afterwards

- Left: calibration finds the true parameters
- Right: equifinality, many different models fit equally well

#### Alt text

Two panels: one trophy-winning parameter set, and five different models all producing the same good hydrograph.

#### Caption for the page

A calibrated parameter set is one plausible explanation, not the catchment's truth.
