# Module cover banners (family D) and site-wide images (family E).

COVERS = {
 '01': dict(subject="A single large pipe emerging from a hillside reservoir, with a glowing orange energy line and a blue grade line floating above it like light trails, a Pelton jet spray on one side and a siphon arch on the other, all arranged along one horizontal band.",
            alt="Abstract banner of a pipeline from a reservoir with glowing energy and grade lines above it."),
 '02': dict(subject="A glowing blue network of pipes and junction nodes spreading beneath a stylised town, with a single pressure wave pulse travelling along one long pipe as a ring of light.",
            alt="Abstract banner of a glowing pipe network beneath a town with a pressure pulse travelling along one pipe."),
 '03': dict(subject="A spinning centrifugal impeller in the centre with motion blur, water spiralling outward in blue ribbons, two more pumps fading into the background on either side.",
            alt="Abstract banner of a spinning pump impeller with water spiralling outward."),
 '04': dict(subject="Monsoon clouds over a stylised island landscape with curtains of rain of different densities falling from them, a few rain gauge silhouettes on the ground, and faint isohyet contour lines drawn over the land.",
            alt="Abstract banner of monsoon clouds and rain curtains over a landscape with faint rainfall contours."),
 '05': dict(subject="Rain falling on a stylised landscape that changes from forest to paddy to town, with blue runoff threads gathering across the surface and converging to one river outlet that rises into a smooth hydrograph shape at the right.",
            alt="Abstract banner of rain on forest, paddy and town gathering into a river that becomes a hydrograph shape."),
 '06': dict(subject="A long straight lined canal running to a vanishing point, with a sharp-crested weir and a ripple V-wake in the foreground and smooth uniform water reflecting the sky.",
            alt="Abstract banner of a straight canal with a weir and a V-shaped ripple wake."),
 '07': dict(subject="A side-section ribbon of water flowing left to right over a spillway into a white hydraulic jump roller, then curving gently into a calm backwater, drawn like a long elegant wave.",
            alt="Abstract banner of water flowing over a spillway into a hydraulic jump and a calm backwater."),
 '08': dict(subject="A close-up of riverbed grains and pebbles with a few lifting into the current, transitioning across the banner into a bridge pier with a swirling vortex at its base, then a reservoir silt delta at the far right.",
            alt="Abstract banner of riverbed grains lifting, a bridge pier vortex, and a reservoir silt delta."),
 '09': dict(subject="A river valley overlaid with many faint translucent possible flood levels like ghosted futures, a bell curve shape rising from the water, and a scatter of glowing dots trailing into an uncertainty fan.",
            alt="Abstract banner of a river valley with ghosted possible flood levels and an uncertainty fan of dots."),
 '10': dict(subject="A whole catchment in a single cutaway band: a cloud and rain on the left, forested hillslope with soil and groundwater layers in the middle, and a river with a reservoir on the right, faint arrows tracing water through every part.",
            alt="Abstract banner of a whole catchment cutaway from rain through hillslope and groundwater to a river and reservoir."),
}

SITE = [
 dict(id='site-hero-backdrop', title='Home hero backdrop', file='img/site-hero-backdrop.webp',
  where='Home page hero, as a soft background layer behind the existing animated SVG water-cycle scene (low opacity, around 12 to 18 percent), or as a fallback when CSS animation is unavailable.',
  aspect='3:2 landscape, 1536x1024, used as a wide crop',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: A soft, airy watercolour and gouache landscape painting on textured off-white paper, gentle washes, very calm, lots of white space, with faint pencil topographic contour lines visible underneath the paint. Palette strictly limited to deep ocean blue #14416B, water blue #1E78B0, pale blue #9FC4E6, forest green #2E6B4F and off-white paper #F6F7F4, with olive-grey #6E6A5E for earth.
SCENE: The whole water cycle across a Sri Lankan landscape, read from left to right: a rain cloud over misty hill-country ridges, forest and tea on the slopes, a river winding down through paddy terraces and a village, into a reservoir, and out to a calm coastline on the far right with a gentle sea. Very subtle, no hard edges, painted lightly enough to sit behind other content.
COMPOSITION: Keep the left third and the top band especially pale and quiet so a headline and buttons can sit over them. Horizon in the lower half.
DO NOT include: any text, letters, numbers, logos or watermarks; teal or turquoise water; brown soil; people; strong saturated colours; heavy dark areas.""",
  alt="A soft watercolour of the water cycle across hills, a river, a reservoir and the coast.",
  cap='(decorative, no caption)'),
 dict(id='site-social-card', title='Social share card (Open Graph)', file='img/site-social-card.webp (also export a 1200x630 .png)',
  where='The og:image and twitter:image meta tags, so links shared on WhatsApp, Facebook and LinkedIn show a proper preview. Crop to 1200x630 and add the title "Water Lab" in Poppins 600 yourself in Canva or Figma, on the empty left side.',
  aspect='3:2 landscape, 1536x1024, cropped to 1200x630',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: Premium editorial illustration, clean flat vector shapes with soft gradients and subtle paper grain, like a high-end engineering textbook cover. Palette: deep ocean blue #14416B background gradient into #0F2C44, water blue #1E78B0, pale blue #9FC4E6, forest green #3E9A6E, a single small accent of orange #E8913C, off-white #F6F7F4 highlights.
SCENE: On the right half, a striking cutaway composition: a hillslope with forest on top, soil and groundwater layers inside, water flowing down into a river channel, a pipe emerging from the hillside with a glowing orange energy line above it, and a small hydraulic jump of white foam in the channel. Faint topographic contour lines drift across the dark background.
COMPOSITION: The entire left 45 percent is calm, dark, empty deep blue so a title can be added later. Important content stays inside the central horizontal band so a 1200x630 crop keeps it.
DO NOT include: any text, letters, numbers, logos, watermarks; teal or turquoise; brown; people.""",
  alt="Water Lab: a cutaway illustration of a hillslope, pipe and river on a deep blue background.",
  cap='(used in link previews, no caption)'),
 dict(id='site-about-banner', title='About page banner', file='img/site-about-banner.webp',
  where='Top of the About page (#/about), above the person card. Do not generate a likeness of a real person; this is a desk scene, not a portrait.',
  aspect='3:2 landscape, 1536x1024, cropped to a wide strip',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: Warm, calm editorial photograph style with soft natural window light, shallow depth of field, gently desaturated colours that lean toward blue and green. Palette leaning on deep blue #14416B, water blue #1E78B0, pale blue #9FC4E6, forest green #2E6B4F and off-white.
SCENE: An engineering lecturer's desk by a window looking out on green trees and a rainy afternoon: an open notebook with hand-drawn sketches of a channel cross-section and a hydrograph (no readable text or numbers), a scale ruler, a mechanical pencil, a scientific calculator, a small glass of water catching the light, and a laptop at the edge showing a blue water simulation. Rain droplets on the window glass.
COMPOSITION: Objects grouped in the right two thirds, the left side softer and quieter so it can be cropped into a wide strip.
DO NOT include: any person or face; any readable text, numbers, logos or brand names; teal; brown wood dominating the frame (use pale grey or white desk).""",
  alt="A study desk by a rainy window with a notebook of channel sketches, a ruler, a calculator and a laptop.",
  cap='(decorative, no caption)'),
 dict(id='site-not-found', title='Lost route (404 / unknown hash)', file='img/site-not-found.webp',
  where='Shown by route() when a hash does not match any sim or alias, beside a line such as "That simulator has moved or never existed" and a button back to all simulators.',
  aspect='1:1 square, 1024x1024',
  prompt="""Create a square image (1024x1024).
STYLE: Clean flat vector illustration with soft gradients and thin dark-ink outlines #1C2A33, on an off-white #F6F7F4 background with faint topographic contour lines. Palette: water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, olive-grey #6E6A5E, one small orange #E8913C accent.
SCENE: A friendly, slightly humorous scene: a small paper boat floating on a stream that splits into several channels, with a little wooden signpost at the fork whose arrow boards are blank, the boat drifting toward a calm pool. Gentle and reassuring, not sad.
COMPOSITION: Centred subject with generous empty space around it.
DO NOT include: any text, letters, numbers or symbols on the signpost; logos; teal; brown wood (make the signpost pale grey or white); people.""",
  alt="A paper boat at a fork in a stream beside a blank signpost.",
  cap='(no caption; the page text carries the message)'),
 dict(id='site-apps-header', title='All simulators page header', file='img/site-apps-header.webp',
  where='Top of the full listing at #/apps, as a slim banner behind the page heading.',
  aspect='3:2 landscape, 1536x1024, cropped to roughly 4:1',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: Clean flat vector illustration with soft gradients and fine contour-line texture, off-white #F6F7F4 background, palette of water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, olive-grey #6E6A5E, and one small orange #E8913C accent.
SCENE: A single continuous horizontal journey of water from left to right through ten small connected vignettes, each a tiny scene: a pipe from a reservoir; a pipe network; a pump; a rain cloud with gauges; rain running off a hill; a lined canal; a hydraulic jump; pebbles on a riverbed; a bell curve over a river; and a whole catchment with a reservoir. The vignettes flow into each other with no borders.
COMPOSITION: Everything sits in the middle horizontal band (about 40 percent of the height) so the image can be cropped into a slim 4:1 strip; above and below are plain off-white.
DO NOT include: any text, numbers, labels or logos; teal; brown; people.""",
  alt="A continuous strip of ten small water scenes from a pipe and a pump to a whole catchment.",
  cap='(decorative, no caption)'),
 dict(id='site-how-to-use', title='How to read a simulator (onboarding)', file='img/site-how-to-use.webp',
  where='A small "How to use this" card on the home page, or the first time someone opens any sim. Add numbered callouts (1 controls, 2 scene, 3 charts, 4 equations, live, 5 theory) in HTML over the empty margins.',
  aspect='3:2 landscape, 1536x1024',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: Clean flat vector UI illustration, isometric-lite, soft shadows, off-white #F6F7F4 background with faint contour lines, thin dark-ink outlines #1C2A33, palette of water blues #0F2C44, #1E78B0, #9FC4E6, forest green #3E9A6E, one small orange #E8913C accent.
SCENE: A stylised laptop screen floating slightly tilted, showing a simplified simulator layout: a column of slider controls on the left, a large scene panel in the middle showing water flowing in a channel, a small line chart below it, and a strip of equation-like blank bars at the bottom. A hand cursor drags one slider and small motion lines show the water in the scene reacting.
COMPOSITION: Leave clear empty margin around each of the five areas (controls, scene, chart, equation strip, a folded theory panel at the bottom) for numbered callouts to be added later.
DO NOT include: any readable text, numbers, letters, logos; teal; brown; real brand UI.""",
  alt="A stylised laptop showing a simulator with sliders, a water scene, a chart and an equation strip.",
  cap='Move a control, watch the water, read the numbers. The equations update as you go.'),
 dict(id='site-study-aid', title='Study-aid strip / Curious LK footer art', file='img/site-study-aid.webp',
  where='The study-aid strip under the footer, as a wide low-contrast background.',
  aspect='3:2 landscape, 1536x1024, cropped to roughly 5:1',
  prompt="""Create a 3:2 landscape image (1536x1024).
STYLE: Minimal paper-cut layered illustration in tones of deep ocean blue #14416B, water blue #1E78B0 and pale blue #9FC4E6, with a single thin line of forest green #3E9A6E, soft shadows between layers, very low contrast, calm.
SCENE: Layered gentle waves and contour lines in a horizontal band, with a few small floating icons cut from paper: an open book, a pencil, a water drop, a tiny paper boat, a small lightbulb, scattered with lots of breathing room.
COMPOSITION: All content within the middle horizontal band so it can be cropped very wide and short.
DO NOT include: any text, numbers, logos; teal; brown; people.""",
  alt="Layered paper-cut waves with small floating icons of a book, a pencil, a water drop and a boat.",
  cap='(decorative, no caption)'),
]
