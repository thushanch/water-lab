#!/usr/bin/env python3
"""Generate the Water Lab image prompt library (one .md per image) plus an index."""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from data_sims import MODULES, SIMS
from data_site import COVERS, SITE

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MOD = {n: (slug, title) for n, slug, title in MODULES}

PALETTE = ("deep ocean blue #14416B, water blue #1E78B0, pale sky blue #9FC4E6, "
           "forest green #2E6B4F, off-white #F6F7F4, olive-grey earth #6E6A5E")

STYLE = {
 'A': ("Editorial digital painting with gentle photographic realism, like a documentary photo "
       "lightly retouched by an illustrator. Soft natural light, slightly desaturated, calm and "
       "trustworthy. Colours lean on " + PALETTE + ". Water reads as clear blue to blue-grey, "
       "never teal or turquoise. Earth and soil are muted olive-grey, never saturated brown or orange. "
       "Any people are small in the frame, in work clothes, seen from behind or the side, with no "
       "recognisable faces."),
 'B': ("Clean technical illustration in the style of a premium engineering textbook: flat vector "
       "shapes with soft gradients, thin 1.5 px dark-ink outlines (#1C2A33), side-section or "
       "isometric cutaway, generous negative space on an off-white #F6F7F4 background with very "
       "faint pale grey topographic contour lines. Water in layered blues #0F2C44, #1E78B0, #9FC4E6. "
       "Soil and rock in olive-grey #4F4B41, #6E6A5E, #8A8474 with fine stipple. Vegetation in "
       "#2E6B4F and #3E9A6E. Flow shown with slim clean arrows. Orange #E8913C only for an energy line "
       "or a force arrow, red #D2452F only for danger."),
 'C': ("A two-panel side-by-side comparison in the same clean technical illustration style as a "
       "premium engineering textbook: flat vector shapes, soft gradients, thin dark-ink outlines "
       "#1C2A33, off-white #F6F7F4 background with faint contour lines, water in blues #0F2C44, "
       "#1E78B0, #9FC4E6, soil in olive-grey #6E6A5E. A thin vertical divider separates the panels. "
       "The LEFT panel (the common assumption) is slightly faded and desaturated with a thin muted red "
       "#D2452F frame and a small red circle-slash icon in its top corner. The RIGHT panel (what really "
       "happens) is crisp and fully saturated with a thin green #3E9A6E frame and a small green check "
       "mark icon in its top corner. Both panels share the same viewpoint and scale so the difference "
       "is obvious."),
 'D': ("Wide atmospheric banner illustration in a layered paper-cut and topographic contour style: "
       "soft depth between layers, subtle paper grain, smooth gradients from deep ocean blue #0F2C44 "
       "and #14416B into water blue #1E78B0 and pale blue #9FC4E6, with small touches of forest green "
       "#3E9A6E and one tiny orange #E8913C highlight. Calm, premium, uncluttered."),
}

NEVER = ("any text, letters, numbers, labels, equations, logos, watermarks or signatures; teal or "
         "turquoise water; saturated brown or orange soil; neon colours; clutter; dramatic disaster "
         "or injury imagery")

FAMILY_NAME = {'A': 'In the field', 'B': 'Concept cutaway', 'C': 'Common trap', 'D': 'Module cover', 'E': 'Site'}
WHERE = {
 'A': "Sim page, directly under the title and blurb, as a wide banner (or inside the theory panel under \"Where you meet it in practice\").",
 'B': "Theory panel, at the top of the first section (\"What this is\"), with the labels below overlaid in HTML.",
 'C': "Theory panel, in the \"Common trap\" section, with the two short labels overlaid in HTML above each panel.",
}
SUFFIX = {'A': 'field', 'B': 'concept', 'C': 'trap'}

def split_labels(txt, fam):
    if fam == 'C':
        i = txt.find(' Right:')
        return [txt[:i].strip().rstrip('.'), txt[i:].strip()] if i > 0 else [txt]
    out = []
    for chunk in txt.split('. '):
        chunk = chunk.strip().rstrip('.')
        if not chunk: continue
        if ':' in chunk: out.append(chunk)
        else: out += [c.strip() for c in chunk.split(', ') if c.strip()]
    return [o[0].upper() + o[1:] for o in out]

def fence(txt):
    return "```text\n" + txt.strip() + "\n```"

def prompt_A(s):
    a = s['A']
    return f"""Create a 3:2 landscape image (1536x1024).
STYLE: {STYLE['A']}
SCENE: {a['subject']}
COMPOSITION: Main subject in the central two thirds, eye-level or gently elevated viewpoint, a calmer band of sky, water or wall near the top so the image still reads when cropped to a wide 2.4:1 banner. Natural depth of field.
DO NOT include: {NEVER}; readable signage or brand names; close-up faces."""

def prompt_B(s):
    b = s['B']
    return f"""Create a 3:2 landscape image (1536x1024).
STYLE: {STYLE['B']}
SUBJECT: {b['subject']}
LABEL SPACE: Leave clean empty margins and quiet areas next to each key element so these labels can be added afterwards in HTML: {b['labels']}. Do not draw the labels yourself.
COMPOSITION: Centred, balanced, nothing touching the edges, readable at small size on a phone.
DO NOT include: {NEVER}; photographic textures; 3D render gloss."""

def prompt_C(s):
    c = s['C']
    return f"""Create a 3:2 landscape image (1536x1024).
STYLE: {STYLE['C']}
LEFT PANEL (the assumption): {c['left']}
RIGHT PANEL (what really happens): {c['right']}
LABEL SPACE: Leave a clear empty strip across the top of each panel for a short caption to be added afterwards in HTML.
DO NOT include: {NEVER}; letters inside the icons (use shapes only)."""

def prompt_D(n):
    d = COVERS[n]
    return f"""Create a 3:2 landscape image (1536x1024).
STYLE: {STYLE['D']}
SUBJECT: {d['subject']}
COMPOSITION: Keep every important element inside the middle horizontal band (about 40 percent of the height) so the image survives a crop to a 3:1 banner and to a small 4:3 tile thumbnail. Leave the left quarter calmer for a module title.
DO NOT include: {NEVER}; people."""

def write(path, md):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(md)

def page(id_, title, fam, file_, where, aspect, prompt, extra, alt, cap, sim=None):
    lines = [f"# {id_} · {title}", "",
             "| | |", "|---|---|",
             f"| **Family** | {fam} · {FAMILY_NAME[fam]} |"]
    if sim:
        lines.append(f"| **Simulator** | `{sim['k']}` · {sim['name']} (deep link `#/{sim['k']}`) |")
    lines += [f"| **Save as** | `{file_}` |",
              f"| **Where it goes** | {where} |",
              f"| **Size in ChatGPT** | {aspect} |",
              f"| **Export** | WebP, 1200 px wide, quality about 78, aim for under 150 kB |",
              "", "## Prompt", "",
              "Paste everything in the box into ChatGPT as one message.", "",
              fence(prompt), ""]
    lines += extra
    lines += ["## Alt text", "", alt, "", "## Caption for the page", "", cap, "",
              "## If the first result is off", "",
              "- Text or numbers crept in: reply *\"Same image, but remove every letter, number and label.\"*",
              "- Water turned teal: reply *\"Make all water a clear blue to blue-grey, no green or teal tint.\"*",
              "- Soil turned brown: reply *\"Make all soil and earth a muted olive-grey.\"*",
              "- Style drifted from earlier images: attach your best previous image and say *\"Match the exact style, palette and line weight of this image.\"*",
              ""]
    return "\n".join(lines)

index_rows = []
count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

if os.path.isdir(OUT):
    for d in os.listdir(OUT):
        p = os.path.join(OUT, d)
        if os.path.isdir(p) and d[:2].isdigit() and d[2] == '-': shutil.rmtree(p)

# site
for s in SITE:
    path = os.path.join(OUT, '00-site', f"{s['id']}.md")
    md = page(s['id'], s['title'], 'E', s['file'], s['where'], s['aspect'], s['prompt'], [], s['alt'], s['cap'])
    write(path, md)
    count['E'] += 1
    index_rows.append(('00', s['id'], s['title'], 'E', s['file'], f"00-site/{s['id']}.md"))

# module covers
for n, slug, title in MODULES:
    id_ = f"m{n}-cover"
    fn = f"img/m{n}-cover.webp"
    where = (f"Module page `#/m/{n}` header banner, and a cropped thumbnail as the background of the "
             f"\"{title}\" tile in Browse by topic on the home page (keep it faint behind the text).")
    md = page(id_, f"Module {n} cover: {title}", 'D', fn, where,
              '3:2 landscape, 1536x1024, cropped to 3:1 and 4:3', prompt_D(n), [],
              COVERS[n]['alt'], '(decorative, no caption)')
    path = os.path.join(OUT, f"{n}-{slug}", f"{id_}.md")
    write(path, md)
    count['D'] += 1
    index_rows.append((n, id_, f"Module {n} cover", 'D', fn, f"{n}-{slug}/{id_}.md"))

# sims
for s in SIMS:
    n = s['m']; slug, title = MOD[n]
    for fam, builder in (('A', prompt_A), ('B', prompt_B), ('C', prompt_C)):
        if fam not in s: continue
        id_ = f"{s['k']}-{SUFFIX[fam]}"
        fn = f"img/{id_}.webp"
        extra = []
        if fam in 'BC':
            extra = ["## Labels to add in HTML afterwards", "",
                     "AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:", "",
                     "- " + "\n- ".join(split_labels(s[fam]['labels'], fam)), ""]
        nice = {'A': 'in the field', 'B': 'how it works', 'C': 'the common trap'}[fam]
        md = page(id_, f"{s['name']}, {nice}", fam, fn, WHERE[fam], '3:2 landscape, 1536x1024',
                  builder(s), extra, s[fam]['alt'], s[fam]['cap'], sim=s)
        write(os.path.join(OUT, f"{n}-{slug}", f"{id_}.md"), md)
        count[fam] += 1
        index_rows.append((n, id_, s['name'], fam, fn, f"{n}-{slug}/{id_}.md"))

total = sum(count.values())

# index
idx = []
idx.append(f"""# Water Lab image prompt library

{total} ready-to-paste ChatGPT image prompts, one Markdown file per image. Each file has the prompt, where the image goes, the file name to save it as, alt text, a caption, and (for diagrams) the labels to overlay afterwards.

Want everything on one page? Open **[ALL_PROMPTS.md](ALL_PROMPTS.md)**.

Read **[STYLE_GUIDE.md](STYLE_GUIDE.md)** once before you start. It explains the five image families, the palette, why the images are text-free, and how to keep a consistent look across {total} generations.

## What is in here

| Family | What it is | Count | Where it lives on the site |
|---|---|---:|---|
| **A · In the field** | Realistic editorial scene of where the topic shows up in real life, Sri Lankan setting where it fits | {count['A']} | Banner under each sim title |
| **B · Concept cutaway** | Clean textbook cutaway that explains the mechanism, text-free | {count['B']} | Top of each theory panel |
| **C · Common trap** | Two panels: what people assume vs what really happens | {count['C']} | "Common trap" section of the theory panel |
| **D · Module cover** | Atmospheric banner per topic | {count['D']} | Module page header and home topic tiles |
| **E · Site** | Hero backdrop, social card, About, 404, onboarding | {count['E']} | Shell pages |
| | | **{total}** | |

## Suggested order

1. **Site and covers first** (17 images). They fix the look of the whole site and give you reference images to attach when style drifts.
2. **Family B for the ten popular sims**: `catchment`, `manning`, `openchannel`, `calib`, `reliability`, `pipeflow`, `hammer`, `freqlab`, `specific-energy`, `weir`. These carry the most teaching value per image.
3. **Family C**: the traps are the images students remember.
4. **Family A** last. They are the most decorative.

## Full index
""")
cur = None
for n, id_, name, fam, fn, rel in index_rows:
    if n != cur:
        cur = n
        heading = 'Site' if n == '00' else f"{n} · {MOD[n][1]}"
        idx.append(f"\n### {heading}\n\n| Image | Simulator / page | Family | Save as |\n|---|---|---|---|")
    idx.append(f"| [{id_}]({rel}) | {name} | {fam} · {FAMILY_NAME[fam]} | `{fn.split(' ')[0]}` |")
idx.append("")
write(os.path.join(OUT, 'README.md'), "\n".join(idx))
print(count, total)

# ---------------------------------------------------------------- combined document
def strip_page(md):
    md = md.split("\n## If the first result is off")[0].rstrip()
    md = md.replace("Paste everything in the box into ChatGPT as one message.\n\n", "")
    md = md.replace("AI image tools still garble text, so the picture stays text-free and these go on top as real, selectable, translatable text:\n\n", "")
    out = []
    for line in md.split("\n"):
        if line.startswith("## "): line = "#### " + line[3:]
        elif line.startswith("# "): line = "### " + line[2:]
        out.append(line)
    return "\n".join(out)

doc = [f"""# Water Lab image prompts

All {total} ChatGPT image prompts in one document. Copy the text in each grey box into ChatGPT as one message, then save the image under the name given.

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
| A · In the field | Realistic scene of where the topic shows up | {count['A']} |
| B · Concept cutaway | Textbook cutaway of the mechanism | {count['B']} |
| C · Common trap | Assumption vs reality, two panels | {count['C']} |
| D · Module cover | Banner per topic | {count['D']} |
| E · Site | Home, social card, About, 404, onboarding | {count['E']} |
"""]
cur = None
for n, id_, name, fam, fn, rel in index_rows:
    if n != cur:
        cur = n
        doc.append("\n---\n\n## " + ('Site images' if n == '00' else f"{n} · {MOD[n][1]}") + "\n")
    with open(os.path.join(OUT, rel)) as f:
        doc.append(strip_page(f.read()) + "\n")
write(os.path.join(OUT, 'ALL_PROMPTS.md'), "\n".join(doc))
