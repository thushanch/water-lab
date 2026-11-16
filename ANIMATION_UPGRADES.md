# Animation upgrades for Water Lab

A review of how the 41 simulators move today, and what to add. The proposals keep to the house rules: one shared clock, particles capped at 160, animations stop when the user leaves, `prefers-reduced-motion` respected, nothing blinks faster than 2 Hz, and the file stays under about 1.3 MB. Everything here is plain canvas, CSS and browser APIs. No libraries.

This is a proposal, not a work item. Where an idea belongs inside an item that is still open in the master plan, that is noted so it can be folded in rather than done twice.

## Status

| Item | State |
|---|---|
| F1 · six loose loops on `Anim` | **Done** 2026-11-16. froude, jump, shields, jet, siphon and scour now run on the shared loop. |
| F2 · global pause switch | **Done** 2026-11-16. Pause button in the header; pauses every sim loop and every CSS animation; remembered across visits; hidden when the system already asks for reduced motion. While paused, every input still redraws one frame. |
| F3 · off-screen pause | **Done** 2026-11-16. Loops skip drawing while none of the sim's canvases is on screen, checked every 0.4 s, and resume on return. |
| Everything else | Proposed, not started. |

---

## 1. Where the app stands

I read every `sim*()` function and sorted them by how they animate.

| How it moves today | Sims | What that means |
|---|---|---|
| **Shared `Anim` loop** (17) | catchment, designstorm, egl, hammer, impeller, npsh, pipeflow, rational, reliability, scs, scsuh, serpar, stepmethod, thiessen, thrust, traplife, weir | Good. Pauses in a hidden tab and draws one frame per input under reduced motion. |
| **Own `requestAnimationFrame` loop** (6) | froude, jump, shields, jet, siphon, scour | Stops on leave, but **ignores reduced motion** and keeps drawing in a hidden tab. *Fixed by F1: all six are now on `Anim`.* |
| **`setInterval` playback** (4) | uh, openchannel, montecarlo, traplife | Plays in visible steps (uh ticks once every 0.9 s), so motion jumps instead of easing, and there is no scrubbing. |
| **Static, redrawn only on input** (17) | manning, compound, venturi, pump, pumpbuild, idf, infil, moody, risk, sluice, specific-energy, calib, profiles, freqfit, freqlab, plus the scenes of uh and openchannel outside playback | **No living water.** In a hydraulics app, still water in a canal reads as a diagram, not a simulation. |

So about four in ten simulators do not move at all, and six that do move skip the accessibility rules the shared kit already handles.

---

## 2. Foundations (do first, every sim benefits)

Small shared pieces, each a few dozen lines, roughly 8 to 15 kB together.

### F1 · Put the six loose loops on `Anim`
froude, jump, shields, jet, siphon and scour each keep their own `raf`. Swapping them to `Anim(draw)` gives them hidden-tab pause and reduced-motion handling for free. Mechanical, low risk, half a session.

### F2 · A global "pause motion" switch
A small toggle in the header (a pause icon) that stops every ambient animation site-wide and remembers the choice in `localStorage`. `Anim.start()` checks it the same way it checks `REDUCED`. This is WCAG 2.2.2 (Pause, Stop, Hide): anything that moves for more than five seconds needs a user control, and several sims loop forever.

### F3 · Stop drawing what nobody can see
Many sims have a scene canvas plus two or three charts below the fold. Give `Anim` an optional element to watch with `IntersectionObserver`, and skip frames while it is off-screen. On a phone this is the biggest battery win available.

### F4 · `tween()`: ease every jump
Today a slider or preset change snaps the scene to the new state. A tiny helper that interpolates numeric state over 250 to 400 ms with an ease-out (instant under reduced motion) makes every sim feel physical: water levels settle, operating points glide along curves, channel shapes morph. Use the same helper to count readout numbers up or down instead of swapping them.

### F5 · One shared `Timeline` control
The catchment already has the right pattern (play, pause, scrub, 1x to 8x). Lift it into a component and use it wherever time exists: uh, openchannel, montecarlo, traplife, designstorm, hammer, scour, risk. It replaces the `setInterval` players, so playback becomes continuous and scrubbable. Add a 0.25x setting: slow motion is how students see the physics event.

### F6 · Ambient water layer for the static sims
Section 1.1 of the plan already specifies the deepPanel surface (two sines, at most 3 px), a specular line and faint caustics. Wrap that in one function, `waterSurface(ctx, path, t)`, and apply it to the 17 static sims. Paint the static part of each scene once into an offscreen canvas and only redraw the water each frame, so cost stays near zero.

### F7 · Link the equations to the scene
Hover or tap a term in the "Equations, live" strip and the matching thing in the scene pulses: hover `R` in Manning and the wetted perimeter glows; hover `h_f` in egl and the friction drop between two piezometers highlights; hover `I_a` in scs and the canopy and puddles light up. One small registry (`linkTerm('R', highlightFn)`) per sim. This is probably the single most effective teaching upgrade on this list: it ties the symbols to the water.

### F8 · "The moment" effect
Section 1.4 reserves fast motion for the event a sim teaches. Make that a shared effect: when the event happens (cavitation starts, the siphon breaks, the jump sweeps out, the flume chokes, the levee overtops) the sim eases to about 0.3x for a second, drops a callout chip on the spot, then resumes. Fire it once per crossing, not continuously.

### F9 · Record a clip
A small "Record 10 s" button that runs `canvas.captureStream()` into `MediaRecorder` and downloads a WebM. Lecturers can then drop a real simulation into their slides. Chrome, Edge and Firefox support it; hide the button where `MediaRecorder` is missing.

### F10 · Page transitions and the home page
- **Route changes:** wrap the route swap in `document.startViewTransition()` where supported, so the card's icon and title morph into the sim header. Unsupported browsers just swap, as now.
- **Scroll reveal:** topic tiles and popular cards fade and rise as they enter, using CSS `animation-timeline: view()` behind `@supports`, so it costs no JavaScript.
- **Card hover:** each popular card's icon plays a tiny loop (water dripping, an impeller turning) in pure CSS. The existing `@media (prefers-reduced-motion)` rule already turns these off.

### F11 · Optional extras, off by default
- **Haptics:** `navigator.vibrate(12)` on phones when the F8 moment fires.
- **Sonification:** a soft WebAudio tone whose pitch follows flow or pressure, toggled from the header. Useful for hammer and pumps, and for students with low vision. Never on by default.

---

## 3. Per-simulator upgrades

**Impact:** how much it helps a student understand. **Effort:** S under half a session, M about one, L more than one.

### 01 Foundations

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| egl | Tracers whose speed follows V in each segment, so the narrow pipe visibly races. Piezometer columns ease to new heights (F4). Bubbles fizz at the crown wherever pressure goes below zero. | High | S |
| venturi | Currently static. Tracers bunch and accelerate through the throat. Piezometer and manometer columns settle with a damped spring after each change. Pitot inset: particles pile up and stop at the stagnation point. | High | M |
| thrust | When the block is undersized, animate the failure: the bend creeps, the block slides, the soil wedge heaves (F8). The resultant arrow breathes with pressure. | Medium | S |
| jet | Move onto `Anim` (F1). Moving-vane mode: the cart recoils and the jet's relative velocity arrow shrinks as the cart speeds up, which is the whole point of the moving-vane case. | Medium | S |
| siphon | Move onto `Anim` (F1). Make the break the hero event: a vapour pocket grows at the crown, the column tears, both legs drain back (F8 with slow motion). | High | M |

### 02 Pressure pipes and networks

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| pipeflow | **Solver replay:** a button that animates the iterations. Pipe widths and arrows start from the first guess and settle as loop corrections are applied, with the residual shrinking on a small chart. Students see the method converge rather than just the answer. | High | M |
| serpar | Ease standpipe levels and flow split when switching series and parallel. Start-up transient: water fills the pipes from the tank on first open. | Medium | S |
| moody | Currently static. Animate the lookup: a dot runs along the Re axis, meets the relative-roughness curve, then slides across to read f. Inset pipe beside the chart shows laminar layers turning into eddies as Re passes 2000 to 4000. | High | M |
| hammer | Already the strongest animation. Add a 0.25x button (F5), an optional "exaggerate wall strain" toggle so the bulge is easy to see, and a four-phase strip under the pipe that lights the current phase of the 4L/a cycle. | Medium | S |

### 03 Pumps

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| pump | Currently static. The operating point glides along both curves when anything changes (F4). Impeller glyph spins at a rate set by N. Throttling visibly closes the valve and slides the system curve up. | High | S |
| pumpbuild | Currently static. **Wet-well cycle:** inflow fills the well, the duty pump starts at its float, the level falls, it stops, repeat. Raise inflow and the assist pump joins; fail the duty pump and the standby wakes. This turns a static schematic into how a station actually runs. | High | M |
| npsh | Zoom inset on one collapsing bubble with its micro-jet. A "run for hours" scrub that pits the vane progressively while the margin is negative. | Medium | M |
| impeller | Continuous morph of the impeller shape as Ns slides, plus velocity triangles at inlet and outlet that rotate and stretch with it. | Medium | M |

### 04 Precipitation

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| idf | Currently static. Rain falls over a small ground strip at a density set by the hovered point on the curves, so 10 minutes at T=100 visibly pours. The curve family draws in from left to right when T changes. (Fold into open item WL-4.2.) | Medium | S |
| thiessen | **Moving storm:** a storm cell drifts across the basin over a few seconds, gauge totals tick up as it passes, and the three areal estimates update live. Polygons and isohyets morph while a gauge is dragged instead of redrawing. | High | M |
| designstorm | When the pattern changes, the hyetograph bars **re-sort themselves** into the new order (same bars, new positions) and the hydrograph redraws behind a time cursor. Seeing the same blocks rearranged is the lesson. | High | S |
| infil | Currently static. Wetting front descends in time; the surface ponds the moment rain exceeds capacity, and a time cursor rides the Horton curve in sync. (Fold into open item WL-4.5.) | High | M |

### 05 Rainfall-runoff

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| rational | **Time of concentration, made visible:** raindrops from every part of the catchment travel to the outlet along the drainage lines; isochrone bands light up one by one; the outlet hydrograph rises until the drop from the farthest point arrives, then flattens. This is the reason the method works. | High | M |
| uh | Replace the 0.9 s ticks with continuous convolution on the shared Timeline: each excess block launches its scaled copy of the UH, which slides into position and stacks onto the running sum in its own blue. (Fold into open item WL-5.2.) | High | M |
| scs | A storm-progress cursor: the initial abstraction fills first (canopy drips, puddles form) and only then does the overland sheet start to move. Today the split appears all at once. | Medium | S |
| scsuh | Morph between the curvilinear UH and its triangle. A drop travels the longest flow path on the map at lag-time speed, landing on the hydrograph peak. | Medium | S |

### 06 Open channel

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| manning | Currently static. Living surface (F6), tracers that run fastest at the surface centre and crawl at the bed and walls, depth that settles to the new normal depth (F4). F7 link from `R` to the wetted perimeter. (Fold into open item WL-6.1.) | High | S |
| specific-energy | Currently static. A marker rides the E-y curve as the hump rises. Past the critical hump height, the choke plays as an event: the upstream pool rises and the curve marker jumps branch (F8). (Fold into WL-6.2.) | High | M |
| froude | Move onto `Anim` (F1). Tap anywhere on the water to drop a pebble and watch the rings: concentric below Fr=1, a standing front at 1, a V-wedge above. (Fold into WL-6.3.) | High | S |
| weir | Animate the measurement itself: a point gauge lowers to touch the surface about 4H upstream, then the rating curve marker lands on the reading. | Low | S |
| compound | Currently static. Stage rises and the water spills onto the floodplain; slow shear vortices roll along the main channel and floodplain interface, which is the physical reason the divided channel method exists. | Medium | M |

### 07 Profiles and rapidly varied flow

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| openchannel | Tracers with speed from local velocity (this is open item WL-7.1). Show the profile being computed: the surface draws section by section from each control, so students see the direction of computation. | High | M |
| profiles | Currently fully static. Arrows show each profile easing toward its normal or critical asymptote; a "relax" animation lets the surface settle from a flat guess into the correct M1, M2 or S2 curve. (This is open item WL-7.2, the explainer rebuild.) | High | L |
| jump | Move onto `Anim` (F1). Roller particles and toe oscillation; an energy bar drains across the jump. Lower tailwater and the jump sweeps out of the basin as an F8 event. | High | S |
| sluice | Currently static. Streamlines contract under the gate to the vena contracta. Raise tailwater and the jump travels upstream until it drowns the gate. | High | M |
| stepmethod | Show the trial-and-error inside one step: the trial depth bounces and converges before the next section is placed. | Medium | S |

### 08 Sediment and scour

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| shields | Move onto `Anim` (F1). Grains roll and hop with a probability that rises past the threshold, so motion begins as a few twitchers rather than a switch. Hovering the Shields diagram moves the bed state. | High | S |
| scour | Move onto `Anim` (F1). A horseshoe vortex of particles wraps the pier; a time scrub deepens the hole toward equilibrium; a "flood recedes" button refills it with lighter sediment (pairs with the scour trap image). | High | M |
| traplife | Replace the interval player with the Timeline (F5). Sediment particles settle by size: coarse drops early into the delta, fines drift to the dam. | Medium | S |

### 09 Probability and risk

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| montecarlo | Replace `setInterval` with `Anim`. Each sample falls as a dot into its histogram bin; the running estimate converges and its confidence band visibly narrows. | High | S |
| risk | Currently static. A design life plays out year by year as a 10 by 10 grid fills, floods dropping in at random. A "run 200 lifetimes" button stacks the outcomes so the formula's answer appears as a count. | High | M |
| freqfit | Currently static. **Resampling:** every second draw a fresh record from the true distribution and refit; the fitted curves wobble, and their faint ghosts build up into a confidence fan. This shows sampling uncertainty better than any formula. | High | M |
| freqlab | A data tool, so keep motion subtle: on load, points slide from their year order into their ranked plotting positions, then the fits draw in. | Low | S |
| reliability | Small multiples: after a run, shrink it into a strip and stack several lifetimes so the overtopping count reads at a glance. | Low | S |

### 10 Catchment modelling

| Sim | Upgrade | Impact | Effort |
|---|---|---|---|
| catchment | A cloud shadow sweeping the hillslope as the storm passes; evaporation wisps rising in dry spells; a "zoom to soil column" mode that magnifies the wetting front; auto-pause with a callout at the hydrograph peak (F8). | Medium | M |
| calib | **Optimiser walker:** a dot walks the response surface (random search or a simple hill-climb), leaving a trail, while the simulated hydrograph updates with each step. It ends up wandering along the ridge, which teaches equifinality directly. (Fold into open item WL-11.5.) | High | M |

---

## 4. Using the generated images in motion

The images from `image-prompts/` can move too, cheaply and in CSS.

- **Field banners (family A):** a slow Ken Burns pan (scale 1.0 to 1.06 over 20 s) on the banner under each sim title. Paused under reduced motion and by F2.
- **Trap images (family C):** reveal the right-hand panel with a draggable wipe, so the student commits to the assumption first, then uncovers the reality.
- **Concept cutaways (family B):** labels fade in one by one in reading order the first time the theory panel opens, with a small dot on each element they point to.
- **Module covers (family D):** a gentle parallax on the module page header, the layered paper-cut style suits it.
- **Video:** ChatGPT and Sora can make short clips, but keep them out of the simulators. The canvas is the source of truth and a video cannot respond to a slider. If one is used on the home page, keep it a muted, looping WebM under 1 MB in `img/`, with a poster image, playing only while on screen.

---

## 5. Suggested order

**Sprint 1, foundations (about 2 sessions).** F1, F2, F3, F4 and F6. Every sim feels more alive and the accessibility gaps close.

**Sprint 2, the ten that teach the most (about 6 to 8 sessions).** rational (time of concentration), uh (continuous convolution), designstorm (re-sorting bars), freqfit (resampling fan), calib (optimiser walker), montecarlo (falling dots), pipeflow (solver replay), pumpbuild (wet-well cycle), siphon (the break) and moody (the lookup). Add F7 equation linking to each as it is touched.

**Sprint 3, polish (about 2 sessions).** F5 Timeline across the time-based sims, F8 moments, F9 clip recording, F10 transitions, image motion from section 4.

Several items above sit inside work the master plan already lists as open (WL-4.2, 4.5, 5.2, 6.1, 6.2, 6.3, 7.1, 7.2 and 11.5). Doing the animation inside those items rather than separately avoids touching the same sims twice.

## 6. Checks for every animation change

Add these to the existing smoke list:

- Leave the sim and confirm CPU drops to idle.
- Turn on reduced motion in the OS: the sim draws once per input and nothing loops.
- Switch tabs and back: no catch-up burst of motion.
- Toggle the global pause (F2): everything stops, sliders still update the scene.
- Particle count never exceeds 160 (`Particles` already caps it).
- Nothing flashes faster than twice a second.
