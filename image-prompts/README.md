# Water Lab image prompt library

122 ready-to-paste ChatGPT image prompts, one Markdown file per image. Each file has the prompt, where the image goes, the file name to save it as, alt text, a caption, and (for diagrams) the labels to overlay afterwards.

Read **[STYLE_GUIDE.md](STYLE_GUIDE.md)** once before you start. It explains the five image families, the palette, why the images are text-free, and how to keep a consistent look across 122 generations.

## What is in here

| Family | What it is | Count | Where it lives on the site |
|---|---|---:|---|
| **A · In the field** | Realistic editorial scene of where the topic shows up in real life, Sri Lankan setting where it fits | 41 | Banner under each sim title |
| **B · Concept cutaway** | Clean textbook cutaway that explains the mechanism, text-free | 41 | Top of each theory panel |
| **C · Common trap** | Two panels: what people assume vs what really happens | 23 | "Common trap" section of the theory panel |
| **D · Module cover** | Atmospheric banner per topic | 10 | Module page header and home topic tiles |
| **E · Site** | Hero backdrop, social card, About, 404, onboarding | 7 | Shell pages |
| | | **122** | |

## Suggested order

1. **Site and covers first** (17 images). They fix the look of the whole site and give you reference images to attach when style drifts.
2. **Family B for the ten popular sims**: `catchment`, `manning`, `openchannel`, `calib`, `reliability`, `pipeflow`, `hammer`, `freqlab`, `specific-energy`, `weir`. These carry the most teaching value per image.
3. **Family C**: the traps are the images students remember.
4. **Family A** last. They are the most decorative.

## Full index


### Site

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [site-hero-backdrop](00-site/site-hero-backdrop.md) | Home hero backdrop | E · Site | `img/site-hero-backdrop.webp` |
| [site-social-card](00-site/site-social-card.md) | Social share card (Open Graph) | E · Site | `img/site-social-card.webp` |
| [site-about-banner](00-site/site-about-banner.md) | About page banner | E · Site | `img/site-about-banner.webp` |
| [site-not-found](00-site/site-not-found.md) | Lost route (404 / unknown hash) | E · Site | `img/site-not-found.webp` |
| [site-apps-header](00-site/site-apps-header.md) | All simulators page header | E · Site | `img/site-apps-header.webp` |
| [site-how-to-use](00-site/site-how-to-use.md) | How to read a simulator (onboarding) | E · Site | `img/site-how-to-use.webp` |
| [site-study-aid](00-site/site-study-aid.md) | Study-aid strip / Curious LK footer art | E · Site | `img/site-study-aid.webp` |

### 01 · Foundations: Energy and Momentum

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m01-cover](01-foundations/m01-cover.md) | Module 01 cover | D · Module cover | `img/m01-cover.webp` |

### 02 · Pressure Pipe Systems and Networks

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m02-cover](02-pipe-networks/m02-cover.md) | Module 02 cover | D · Module cover | `img/m02-cover.webp` |

### 03 · Pumps and Pump Systems

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m03-cover](03-pumps/m03-cover.md) | Module 03 cover | D · Module cover | `img/m03-cover.webp` |

### 04 · Precipitation and Design Rainfall

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m04-cover](04-precipitation/m04-cover.md) | Module 04 cover | D · Module cover | `img/m04-cover.webp` |

### 05 · Rainfall-Runoff and Design Flows

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m05-cover](05-runoff/m05-cover.md) | Module 05 cover | D · Module cover | `img/m05-cover.webp` |

### 06 · Open Channel: Uniform and Critical Flow

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m06-cover](06-open-channel/m06-cover.md) | Module 06 cover | D · Module cover | `img/m06-cover.webp` |

### 07 · Profiles and Rapidly Varied Flow

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m07-cover](07-profiles/m07-cover.md) | Module 07 cover | D · Module cover | `img/m07-cover.webp` |

### 08 · Sediment and Scour

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m08-cover](08-sediment/m08-cover.md) | Module 08 cover | D · Module cover | `img/m08-cover.webp` |

### 09 · Probability and Risk for Design

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m09-cover](09-risk/m09-cover.md) | Module 09 cover | D · Module cover | `img/m09-cover.webp` |

### 10 · Catchment Modelling Studio

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [m10-cover](10-catchment/m10-cover.md) | Module 10 cover | D · Module cover | `img/m10-cover.webp` |

### 01 · Foundations: Energy and Momentum

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [egl-field](01-foundations/egl-field.md) | EGL / HGL Pipeline Explorer | A · In the field | `img/egl-field.webp` |
| [egl-concept](01-foundations/egl-concept.md) | EGL / HGL Pipeline Explorer | B · Concept cutaway | `img/egl-concept.webp` |
| [egl-trap](01-foundations/egl-trap.md) | EGL / HGL Pipeline Explorer | C · Common trap | `img/egl-trap.webp` |
| [venturi-field](01-foundations/venturi-field.md) | Venturi and Pitot Virtual Bench | A · In the field | `img/venturi-field.webp` |
| [venturi-concept](01-foundations/venturi-concept.md) | Venturi and Pitot Virtual Bench | B · Concept cutaway | `img/venturi-concept.webp` |
| [thrust-field](01-foundations/thrust-field.md) | Thrust Block Designer | A · In the field | `img/thrust-field.webp` |
| [thrust-concept](01-foundations/thrust-concept.md) | Thrust Block Designer | B · Concept cutaway | `img/thrust-concept.webp` |
| [jet-field](01-foundations/jet-field.md) | Jet and Vane Momentum Lab | A · In the field | `img/jet-field.webp` |
| [jet-concept](01-foundations/jet-concept.md) | Jet and Vane Momentum Lab | B · Concept cutaway | `img/jet-concept.webp` |
| [siphon-field](01-foundations/siphon-field.md) | Siphon and Cavitation Sim | A · In the field | `img/siphon-field.webp` |
| [siphon-concept](01-foundations/siphon-concept.md) | Siphon and Cavitation Sim | B · Concept cutaway | `img/siphon-concept.webp` |
| [siphon-trap](01-foundations/siphon-trap.md) | Siphon and Cavitation Sim | C · Common trap | `img/siphon-trap.webp` |

### 02 · Pressure Pipe Systems and Networks

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [pipeflow-field](02-pipe-networks/pipeflow-field.md) | Pipe Network Solver | A · In the field | `img/pipeflow-field.webp` |
| [pipeflow-concept](02-pipe-networks/pipeflow-concept.md) | Pipe Network Solver | B · Concept cutaway | `img/pipeflow-concept.webp` |
| [serpar-field](02-pipe-networks/serpar-field.md) | Series and Parallel Pipes | A · In the field | `img/serpar-field.webp` |
| [serpar-concept](02-pipe-networks/serpar-concept.md) | Series and Parallel Pipes | B · Concept cutaway | `img/serpar-concept.webp` |
| [serpar-trap](02-pipe-networks/serpar-trap.md) | Series and Parallel Pipes | C · Common trap | `img/serpar-trap.webp` |
| [moody-field](02-pipe-networks/moody-field.md) | Moody Chart Navigator | A · In the field | `img/moody-field.webp` |
| [moody-concept](02-pipe-networks/moody-concept.md) | Moody Chart Navigator | B · Concept cutaway | `img/moody-concept.webp` |
| [hammer-field](02-pipe-networks/hammer-field.md) | Water Hammer Simulator | A · In the field | `img/hammer-field.webp` |
| [hammer-concept](02-pipe-networks/hammer-concept.md) | Water Hammer Simulator | B · Concept cutaway | `img/hammer-concept.webp` |
| [hammer-trap](02-pipe-networks/hammer-trap.md) | Water Hammer Simulator | C · Common trap | `img/hammer-trap.webp` |

### 03 · Pumps and Pump Systems

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [pump-field](03-pumps/pump-field.md) | Pump-System Operating Point | A · In the field | `img/pump-field.webp` |
| [pump-concept](03-pumps/pump-concept.md) | Pump-System Operating Point | B · Concept cutaway | `img/pump-concept.webp` |
| [pump-trap](03-pumps/pump-trap.md) | Pump-System Operating Point | C · Common trap | `img/pump-trap.webp` |
| [pumpbuild-field](03-pumps/pumpbuild-field.md) | Pump Station Builder | A · In the field | `img/pumpbuild-field.webp` |
| [pumpbuild-concept](03-pumps/pumpbuild-concept.md) | Pump Station Builder | B · Concept cutaway | `img/pumpbuild-concept.webp` |
| [npsh-field](03-pumps/npsh-field.md) | NPSH and Cavitation Check | A · In the field | `img/npsh-field.webp` |
| [npsh-concept](03-pumps/npsh-concept.md) | NPSH and Cavitation Check | B · Concept cutaway | `img/npsh-concept.webp` |
| [npsh-trap](03-pumps/npsh-trap.md) | NPSH and Cavitation Check | C · Common trap | `img/npsh-trap.webp` |
| [impeller-field](03-pumps/impeller-field.md) | Impeller and Specific Speed | A · In the field | `img/impeller-field.webp` |
| [impeller-concept](03-pumps/impeller-concept.md) | Impeller and Specific Speed | B · Concept cutaway | `img/impeller-concept.webp` |

### 04 · Precipitation and Design Rainfall

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [idf-field](04-precipitation/idf-field.md) | IDF Curve Lab | A · In the field | `img/idf-field.webp` |
| [idf-concept](04-precipitation/idf-concept.md) | IDF Curve Lab | B · Concept cutaway | `img/idf-concept.webp` |
| [thiessen-field](04-precipitation/thiessen-field.md) | Areal Rainfall Studio | A · In the field | `img/thiessen-field.webp` |
| [thiessen-concept](04-precipitation/thiessen-concept.md) | Areal Rainfall Studio | B · Concept cutaway | `img/thiessen-concept.webp` |
| [thiessen-trap](04-precipitation/thiessen-trap.md) | Areal Rainfall Studio | C · Common trap | `img/thiessen-trap.webp` |
| [designstorm-field](04-precipitation/designstorm-field.md) | Design Storm Builder | A · In the field | `img/designstorm-field.webp` |
| [designstorm-concept](04-precipitation/designstorm-concept.md) | Design Storm Builder | B · Concept cutaway | `img/designstorm-concept.webp` |
| [infil-field](04-precipitation/infil-field.md) | Infiltration and Runoff Split | A · In the field | `img/infil-field.webp` |
| [infil-concept](04-precipitation/infil-concept.md) | Infiltration and Runoff Split | B · Concept cutaway | `img/infil-concept.webp` |

### 05 · Rainfall-Runoff and Design Flows

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [rational-field](05-runoff/rational-field.md) | Rational Method Explorer | A · In the field | `img/rational-field.webp` |
| [rational-concept](05-runoff/rational-concept.md) | Rational Method Explorer | B · Concept cutaway | `img/rational-concept.webp` |
| [rational-trap](05-runoff/rational-trap.md) | Rational Method Explorer | C · Common trap | `img/rational-trap.webp` |
| [uh-field](05-runoff/uh-field.md) | Unit Hydrograph Convolution | A · In the field | `img/uh-field.webp` |
| [uh-concept](05-runoff/uh-concept.md) | Unit Hydrograph Convolution | B · Concept cutaway | `img/uh-concept.webp` |
| [uh-trap](05-runoff/uh-trap.md) | Unit Hydrograph Convolution | C · Common trap | `img/uh-trap.webp` |
| [scs-field](05-runoff/scs-field.md) | SCS Curve Number Explorer | A · In the field | `img/scs-field.webp` |
| [scs-concept](05-runoff/scs-concept.md) | SCS Curve Number Explorer | B · Concept cutaway | `img/scs-concept.webp` |
| [scs-trap](05-runoff/scs-trap.md) | SCS Curve Number Explorer | C · Common trap | `img/scs-trap.webp` |
| [scsuh-field](05-runoff/scsuh-field.md) | SCS Synthetic Unit Hydrograph | A · In the field | `img/scsuh-field.webp` |
| [scsuh-concept](05-runoff/scsuh-concept.md) | SCS Synthetic Unit Hydrograph | B · Concept cutaway | `img/scsuh-concept.webp` |

### 06 · Open Channel: Uniform and Critical Flow

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [manning-field](06-open-channel/manning-field.md) | Manning Normal Depth | A · In the field | `img/manning-field.webp` |
| [manning-concept](06-open-channel/manning-concept.md) | Manning Normal Depth | B · Concept cutaway | `img/manning-concept.webp` |
| [manning-trap](06-open-channel/manning-trap.md) | Manning Normal Depth | C · Common trap | `img/manning-trap.webp` |
| [specific-energy-field](06-open-channel/specific-energy-field.md) | Specific Energy Playground | A · In the field | `img/specific-energy-field.webp` |
| [specific-energy-concept](06-open-channel/specific-energy-concept.md) | Specific Energy Playground | B · Concept cutaway | `img/specific-energy-concept.webp` |
| [specific-energy-trap](06-open-channel/specific-energy-trap.md) | Specific Energy Playground | C · Common trap | `img/specific-energy-trap.webp` |
| [froude-field](06-open-channel/froude-field.md) | Froude Wave Tank | A · In the field | `img/froude-field.webp` |
| [froude-concept](06-open-channel/froude-concept.md) | Froude Wave Tank | B · Concept cutaway | `img/froude-concept.webp` |
| [froude-trap](06-open-channel/froude-trap.md) | Froude Wave Tank | C · Common trap | `img/froude-trap.webp` |
| [weir-field](06-open-channel/weir-field.md) | Weir and Flume Lab | A · In the field | `img/weir-field.webp` |
| [weir-concept](06-open-channel/weir-concept.md) | Weir and Flume Lab | B · Concept cutaway | `img/weir-concept.webp` |
| [compound-field](06-open-channel/compound-field.md) | Compound Channel Capacity | A · In the field | `img/compound-field.webp` |
| [compound-concept](06-open-channel/compound-concept.md) | Compound Channel Capacity | B · Concept cutaway | `img/compound-concept.webp` |

### 07 · Profiles and Rapidly Varied Flow

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [openchannel-field](07-profiles/openchannel-field.md) | Open Channel Modeller | A · In the field | `img/openchannel-field.webp` |
| [openchannel-concept](07-profiles/openchannel-concept.md) | Open Channel Modeller | B · Concept cutaway | `img/openchannel-concept.webp` |
| [profiles-field](07-profiles/profiles-field.md) | Water Surface Profiles | A · In the field | `img/profiles-field.webp` |
| [profiles-concept](07-profiles/profiles-concept.md) | Water Surface Profiles | B · Concept cutaway | `img/profiles-concept.webp` |
| [profiles-trap](07-profiles/profiles-trap.md) | Water Surface Profiles | C · Common trap | `img/profiles-trap.webp` |
| [jump-field](07-profiles/jump-field.md) | Hydraulic Jump Lab | A · In the field | `img/jump-field.webp` |
| [jump-concept](07-profiles/jump-concept.md) | Hydraulic Jump Lab | B · Concept cutaway | `img/jump-concept.webp` |
| [jump-trap](07-profiles/jump-trap.md) | Hydraulic Jump Lab | C · Common trap | `img/jump-trap.webp` |
| [sluice-field](07-profiles/sluice-field.md) | Sluice Gate and Discharge | A · In the field | `img/sluice-field.webp` |
| [sluice-concept](07-profiles/sluice-concept.md) | Sluice Gate and Discharge | B · Concept cutaway | `img/sluice-concept.webp` |
| [stepmethod-field](07-profiles/stepmethod-field.md) | Standard Step Method | A · In the field | `img/stepmethod-field.webp` |
| [stepmethod-concept](07-profiles/stepmethod-concept.md) | Standard Step Method | B · Concept cutaway | `img/stepmethod-concept.webp` |

### 08 · Sediment and Scour

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [shields-field](08-sediment/shields-field.md) | Shields Threshold of Motion | A · In the field | `img/shields-field.webp` |
| [shields-concept](08-sediment/shields-concept.md) | Shields Threshold of Motion | B · Concept cutaway | `img/shields-concept.webp` |
| [shields-trap](08-sediment/shields-trap.md) | Shields Threshold of Motion | C · Common trap | `img/shields-trap.webp` |
| [scour-field](08-sediment/scour-field.md) | Bridge Pier Scour | A · In the field | `img/scour-field.webp` |
| [scour-concept](08-sediment/scour-concept.md) | Bridge Pier Scour | B · Concept cutaway | `img/scour-concept.webp` |
| [scour-trap](08-sediment/scour-trap.md) | Bridge Pier Scour | C · Common trap | `img/scour-trap.webp` |
| [traplife-field](08-sediment/traplife-field.md) | Reservoir Trap Efficiency and Life | A · In the field | `img/traplife-field.webp` |
| [traplife-concept](08-sediment/traplife-concept.md) | Reservoir Trap Efficiency and Life | B · Concept cutaway | `img/traplife-concept.webp` |
| [traplife-trap](08-sediment/traplife-trap.md) | Reservoir Trap Efficiency and Life | C · Common trap | `img/traplife-trap.webp` |

### 09 · Probability and Risk for Design

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [montecarlo-field](09-risk/montecarlo-field.md) | Monte Carlo Design Risk | A · In the field | `img/montecarlo-field.webp` |
| [montecarlo-concept](09-risk/montecarlo-concept.md) | Monte Carlo Design Risk | B · Concept cutaway | `img/montecarlo-concept.webp` |
| [risk-field](09-risk/risk-field.md) | Risk and Return Period | A · In the field | `img/risk-field.webp` |
| [risk-concept](09-risk/risk-concept.md) | Risk and Return Period | B · Concept cutaway | `img/risk-concept.webp` |
| [risk-trap](09-risk/risk-trap.md) | Risk and Return Period | C · Common trap | `img/risk-trap.webp` |
| [freqfit-field](09-risk/freqfit-field.md) | Frequency Fitting Studio | A · In the field | `img/freqfit-field.webp` |
| [freqfit-concept](09-risk/freqfit-concept.md) | Frequency Fitting Studio | B · Concept cutaway | `img/freqfit-concept.webp` |
| [freqfit-trap](09-risk/freqfit-trap.md) | Frequency Fitting Studio | C · Common trap | `img/freqfit-trap.webp` |
| [freqlab-field](09-risk/freqlab-field.md) | Flood Frequency Lab | A · In the field | `img/freqlab-field.webp` |
| [freqlab-concept](09-risk/freqlab-concept.md) | Flood Frequency Lab | B · Concept cutaway | `img/freqlab-concept.webp` |
| [reliability-field](09-risk/reliability-field.md) | Reliability and Redundancy | A · In the field | `img/reliability-field.webp` |
| [reliability-concept](09-risk/reliability-concept.md) | Reliability and Redundancy | B · Concept cutaway | `img/reliability-concept.webp` |
| [reliability-trap](09-risk/reliability-trap.md) | Reliability and Redundancy | C · Common trap | `img/reliability-trap.webp` |

### 10 · Catchment Modelling Studio

| Image | Simulator / page | Family | Save as |
|---|---|---|---|
| [catchment-field](10-catchment/catchment-field.md) | The Living Catchment | A · In the field | `img/catchment-field.webp` |
| [catchment-concept](10-catchment/catchment-concept.md) | The Living Catchment | B · Concept cutaway | `img/catchment-concept.webp` |
| [catchment-trap](10-catchment/catchment-trap.md) | The Living Catchment | C · Common trap | `img/catchment-trap.webp` |
| [calib-field](10-catchment/calib-field.md) | Calibration Arena | A · In the field | `img/calib-field.webp` |
| [calib-concept](10-catchment/calib-concept.md) | Calibration Arena | B · Concept cutaway | `img/calib-concept.webp` |
| [calib-trap](10-catchment/calib-trap.md) | Calibration Arena | C · Common trap | `img/calib-trap.webp` |
