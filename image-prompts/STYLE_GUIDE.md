# Image style guide

Read this once before generating. It is short on purpose.

## 1. The images carry no text

Every prompt tells ChatGPT to draw **no letters, numbers, labels or equations**. Image models still misspell words and invent symbols, and a single garbled "Hydraulc Grade Lnie" on a teaching site costs more trust than the picture earns. So:

- The picture shows the mechanism.
- The words go on top in HTML. Each family B and C file lists the exact labels to overlay.
- HTML labels can be selected, translated into Sinhala or Tamil later, and read by screen readers. Baked-in text can do none of that.

If text sneaks in anyway, reply: *"Same image, but remove every letter, number and label."*

## 2. Five families

| Family | Look | Used for |
|---|---|---|
| **A · In the field** | Editorial painting with gentle photographic realism, soft light, slightly desaturated. Sri Lankan setting where it fits: tanks, Mahaweli canals, hill-country penstocks, Colombo drains, monsoon rain. | A banner under each sim title: "this is where you meet it". |
| **B · Concept cutaway** | Flat vector textbook cutaway, thin dark-ink outlines, off-white paper with faint contour lines. | Top of each theory panel: "this is how it works". |
| **C · Common trap** | Two panels in the B style. Left is faded with a red frame (the assumption), right is crisp with a green frame (the reality). | The "Common trap" section of the theory panel. |
| **D · Module cover** | Layered paper-cut with topographic contours, deep blue gradients. | Module page header and home topic tiles. |
| **E · Site** | Individually specified. | Hero backdrop, social card, About, 404, onboarding. |

Every prompt file already contains its family's full style paragraph, so each one works on its own when pasted.

## 3. Palette

These are the site's own tokens from `water-lab.html`, so images and UI agree.

| Role | Hex |
|---|---|
| Deep ocean (darkest water, ink on dark) | `#0F2C44`, `#14416B` |
| Water | `#1E78B0` |
| Pale water and sky | `#9FC4E6` |
| Forest | `#2E6B4F`, `#3E9A6E` |
| Paper | `#F6F7F4` |
| Ink | `#1C2A33` |
| Earth (olive grey, never brown) | `#4F4B41`, `#6E6A5E`, `#8A8474` |
| Energy line and force arrows only | `#E8913C` |
| Danger only | `#D2452F` |

House rules carried into the images: **no teal or turquoise water, no brown soil.** These are the two drifts ChatGPT makes most often. Each prompt forbids them, and each file has a one-line fix if they appear.

## 4. Keeping 120 images consistent

1. **One chat per family.** Do all the B images in one ChatGPT conversation, all the C images in another. The model keeps the style better inside one thread.
2. **Start each chat with a reference.** Generate the first image of the family, pick the best, and from then on attach it with: *"Match the exact style, palette and line weight of this image."*
3. **Generate in the order in the README.** Site and covers first fixes the look. Then the popular sims.
4. **Regenerate rather than patch** when composition is wrong. Use ChatGPT's region edit (select an area, describe the change) only for small fixes like removing a stray letter.
5. **Same aspect every time.** Every prompt asks for 1536x1024 (3:2) except the 404 square. Cropping is done later.

## 5. Check the physics before you publish

Image models draw water that looks right and behaves wrong. Before an image goes on the site, check it against this list. A wrong diagram teaches the wrong thing better than no diagram.

- **Still water is level.** Tank and reservoir surfaces are flat and horizontal.
- **Piezometer tubes** fall in height along the flow, never rise (unless a pump sits between them).
- **The energy line** is above the hydraulic grade line, and both slope down in the flow direction.
- **Flow arrows** go downhill in head: reservoir to valve, upstream to downstream.
- **A hydraulic jump** goes from shallow and fast to deep and slow, never the other way round.
- **Over a hump in subcritical flow** the surface dips. It does not rise.
- **A weir nappe** springs clear of the crest with air under it, and head is measured upstream of the drawdown.
- **Velocity is fastest** near the surface in the middle of a channel, slowest at the bed and walls.
- **Ripples in supercritical flow** form a V that points upstream at the source, with nothing ahead of it.
- **Sediment in a reservoir**: coarse delta at the inflow, fines toward the dam.
- **Scour** is deepest at the upstream face of a pier.
- **Groundwater** flows toward the stream, and the water table slopes the same way.

## 6. Being honest about what the pictures are

Family A images are illustrations, even when they look like photographs. The prompts describe *kinds* of places (a hill-country penstock, a dry-zone tank) rather than real named sites, and the captions do not claim a location. Keep it that way: do not caption a generated image as Victoria, Kotmale or any real structure. If you want a real site, use a real photograph with its credit.

Do not generate a likeness of yourself or any real person for the About page; the About banner is a desk scene for that reason.

## 7. Putting them on the site

The images live in an `img/` folder next to `water-lab.html`, **not** embedded in the file. That keeps the single file under the 1.3 MB limit in the house rules.

- **Format:** WebP, 1200 px wide, quality about 78. Each should land between 60 and 150 kB. `cwebp -q 78 -resize 1200 0 in.png -o out.webp` does it, or Squoosh in a browser.
- **Loading:** `loading="lazy"` and `decoding="async"` on every `<img>`, with `width` and `height` set to stop layout shift.
- **Offline:** the README promises the file works offline on its own. If `img/` is missing, the images should simply not appear. An `onerror="this.closest('figure').remove()"` on each image does that.
- **Social card:** the og:image needs a full absolute URL (`https://thushanch.github.io/water-lab/img/site-social-card.png`), PNG or JPG, 1200x630.

**How they are wired in:** `_build/inject_manifest.py` writes an `IMGS` object into `water-lab.html`, listing only the images that exist in `img/`, with their alt text, captions and labels. The page reads that object, so adding an image is: save it in `img/`, run the script. See [`../img/README.md`](../img/README.md) for where each kind of image appears. The diagram labels are shown as a key under each picture rather than pinned onto it, so they never need per-image coordinates.

## 8. Editing the prompts

All 122 files are generated from three data files in [`_build/`](_build/). To change a prompt, a caption or the shared style text, edit `_build/data_sims.py`, `_build/data_site.py` or `_build/build.py`, then run:

```bash
python3 image-prompts/_build/build.py
```

It rewrites every prompt file and the README index. Hand edits to the generated `.md` files are overwritten on the next run.
