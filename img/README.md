# Images

Pictures for Water Lab, generated from the prompts in [`../image-prompts/`](../image-prompts/). Every one is optional: `water-lab.html` still works on its own, offline, with this folder missing. Each figure removes itself if its image fails to load.

## Where each kind appears

| File pattern | Where on the site |
|---|---|
| `<sim>-field.webp` | Slim banner under the simulator's title, and the thumbnail on its "Popular right now" card |
| `<sim>-concept.webp` | "How it works" card under the simulator, with a key of what the picture shows |
| `<sim>-trap.webp` | "Common trap" card beside it, with the two halves labelled |
| `mNN-cover.webp` | Topic page banner (`#/m/NN`) and the topic tile thumbnail on the home page |
| `site-hero-backdrop.webp` | Faint background behind the home page hero |
| `site-apps-header.webp` | Banner on the all-simulators page |
| `site-about-banner.webp`, `site-how-to-use.webp` | About page |
| `site-not-found.webp` | The page shown for an unknown link |
| `site-study-aid.webp` | Very faint background of the study-aid strip at the bottom |
| `site-social-card.jpg` | Link preview on WhatsApp, Facebook and LinkedIn (`og:image`) |

## Adding or replacing an image

1. Save it here under the exact name its prompt file gives, as WebP, 1200 px wide.
2. Run `python3 image-prompts/_build/inject_manifest.py`.

The script lists only the images that exist here, with their alt text, captions and labels, inside `water-lab.html`. Add an image and it appears; delete one and it disappears cleanly.

## Held back for regeneration (`_review/`)

These two were generated but are not used, because the physics in them is wrong and a wrong diagram teaches the wrong thing:

- **`egl-concept.webp`**: the grade lines end well above the downstream reservoir. The hydraulic grade line has to finish at that reservoir's water surface.
- **`profiles-concept.webp`**: the water is at the same level on both sides of the dam, and the M1 backwater curve is missing.

Both prompts have been corrected. Regenerate them from `image-prompts/01-foundations/egl-concept.md` and `image-prompts/07-profiles/profiles-concept.md`, save the new images here (not in `_review/`), and run the script above.
