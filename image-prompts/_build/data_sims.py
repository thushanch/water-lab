# Per-simulator image content. A = in the field, B = concept cutaway, C = common trap (optional).
# Keep captions and alt text free of em dashes (house rule for user-facing copy).

MODULES = [
 ('01', 'foundations',  'Foundations: Energy and Momentum'),
 ('02', 'pipe-networks','Pressure Pipe Systems and Networks'),
 ('03', 'pumps',        'Pumps and Pump Systems'),
 ('04', 'precipitation','Precipitation and Design Rainfall'),
 ('05', 'runoff',       'Rainfall-Runoff and Design Flows'),
 ('06', 'open-channel', 'Open Channel: Uniform and Critical Flow'),
 ('07', 'profiles',     'Profiles and Rapidly Varied Flow'),
 ('08', 'sediment',     'Sediment and Scour'),
 ('09', 'risk',         'Probability and Risk for Design'),
 ('10', 'catchment',    'Catchment Modelling Studio'),
]

SIMS = [
# ---------------------------------------------------------------- 01
dict(k='egl', m='01', name='EGL / HGL Pipeline Explorer',
 A=dict(
  subject="A gravity water supply main running down a terraced tea-estate hillside in the central highlands of Sri Lanka. A large-diameter blue-painted steel pipe on concrete saddles follows the slope from a small concrete service reservoir at the top, past a dark green air-release valve chamber on a hump in the line, down to a village water tower far below in the valley. Morning mist in the lower valley, neat rows of tea bushes, silver oak shade trees. Two small engineers in hard hats inspect the valve chamber, seen from behind.",
  alt="A blue steel water main running down a terraced tea-estate hillside from a reservoir at the top to a village in the valley.",
  cap="Every gravity main is a story told in head: it starts with height and spends it on friction all the way down."),
 B=dict(
  subject="A clean side-section diagram of a pipeline connecting a high reservoir on the left to a lower reservoir on the right. The pipe changes diameter twice along its length (wide, narrow, medium) and climbs over one gentle hump in the middle. Seven slim vertical glass piezometer tubes rise from the pipe crown at even spacing, each filled with blue water to a different height: the water levels step down smoothly from left to right, dropping fastest along the narrow section. The blue line runs exactly through the water level in every tube: it STARTS at the upper reservoir water surface on the left and ENDS exactly at the lower reservoir water surface on the right, so the lower reservoir surface sits level with the end of the blue line, not below it. An orange line runs parallel above the blue line, a small gap above it, the gap widest along the narrow section; it also starts at the upper reservoir surface. Both lines slope down from left to right. Faint flow arrows inside the pipe point from the high reservoir to the low one.",
  labels="Energy grade line (orange), hydraulic grade line (blue), velocity head gap, friction loss over each segment, the hump where pressure is lowest",
  alt="Side section of a pipeline between two reservoirs with glass tubes showing the water pressure falling along the pipe, and two sloping lines above it.",
  cap="The piezometer tubes draw the hydraulic grade line for you. The energy line sits one velocity head above it."),
 C=dict(
  left="The pipe climbs over a hill that pokes above the blue hydraulic grade line, and the water inside the pipe is drawn as stopped, still and empty past the hump, as if flow simply cannot pass.",
  right="The same pipe and hill, but water keeps flowing through the hump. The section above the grade line is tinted pale red to show suction (sub-atmospheric pressure), tiny air bubbles gather at the crown, and a small air-release valve sits on top of the hump.",
  labels="Left: what students assume, flow stops. Right: flow continues under suction, air comes out of solution, the valve matters",
  alt="Two panels: a pipe over a hill drawn empty on the left, and flowing under suction with bubbles at the crown on the right.",
  cap="A pipe above the HGL still flows. It just runs under suction, which invites air, cavitation and dirty groundwater in."),
),
dict(k='venturi', m='01', name='Venturi and Pitot Virtual Bench',
 A=dict(
  subject="Inside the pipe gallery of a modern water treatment plant in Sri Lanka. A large flanged steel pipeline painted in deep blue runs along the floor and narrows smoothly into a venturi section, with small instrument tubing connecting the throat and the inlet to a grey differential pressure transmitter on a wall panel. Clean concrete floor, yellow safety railings in soft focus, soft daylight from high clerestory windows, a hint of filter beds through a glass window in the background.",
  alt="A blue steel pipeline in a treatment plant gallery narrowing into a venturi meter with instrument tubing to a pressure transmitter.",
  cap="A venturi meter has no moving parts. It measures flow by reading how much pressure the water spends to speed up."),
 B=dict(
  subject="A precise cutaway of a horizontal venturi tube: a straight inlet, a smooth converging cone, a short narrow throat, then a long gentle diverging cone back to full size. Blue water inside with streamlines squeezing together through the throat and spreading again. Two vertical glass piezometer tubes rise from the inlet and from the throat, the throat tube visibly lower. In a separate smaller inset on the right, a Pitot-static tube points upstream into a flow, with a stagnation point at its nose and a U-tube manometer below showing a height difference in darker blue fluid.",
  labels="Inlet, throat, diverging cone, head difference between the tubes, stagnation point on the Pitot nose, manometer deflection",
  alt="Cutaway of a venturi meter with two pressure tubes, and an inset of a Pitot tube with a manometer.",
  cap="Faster at the throat means lower pressure there. That pressure drop is the flow measurement."),
),
dict(k='thrust', m='01', name='Thrust Block Designer',
 A=dict(
  subject="An open trench in a suburban street near Colombo during pipe laying. At the bottom of the trench, a large ductile iron pipe makes a 45 degree horizontal bend. Behind the outside of the bend, a freshly cast grey concrete thrust block is wedged against the undisturbed trench wall, its timber formwork partly stripped. Trench shoring on the sides, a small excavator arm at the edge of the frame, coconut palms and low houses in the background, overcast sky.",
  alt="A ductile iron pipe bend at the bottom of a trench with a freshly cast concrete thrust block behind it.",
  cap="Water changing direction pushes on the bend. The block hands that push to the soil."),
 B=dict(
  subject="A plan-view (seen from above) engineering illustration of a horizontal pipe bend buried in soil. Blue flow arrows enter from the left and leave at an angle. Two pressure force arrows along each pipe leg combine into one thick orange resultant force arrow pointing outward from the bend. Behind the bend, a grey concrete thrust block bears against undisturbed olive-grey soil, with soft fan-shaped pressure contour bands spreading into the soil behind the block. Soil drawn with fine stipple texture.",
  labels="Pressure force on each leg, resultant thrust, bearing area of the block, passive soil resistance zone",
  alt="Plan view of a buried pipe bend with force arrows combining into a resultant that pushes into a concrete block and the soil behind it.",
  cap="The block area is the thrust divided by what the soil can safely bear."),
),
dict(k='jet', m='01', name='Jet and Vane Momentum Lab',
 A=dict(
  subject="A small run-of-river mini-hydro power house in a forested valley in the Sri Lankan hill country, its side wall cut away to reveal a polished steel Pelton wheel with rows of double cup buckets. A high-speed water jet from a nozzle strikes the buckets and splits into two white curling sprays. Wet stone walls, a green generator housing beside the wheel, rainforest and a stream visible through a doorway.",
  alt="A Pelton wheel inside a small hydro power house being struck by a water jet that splits into two sprays.",
  cap="A Pelton bucket turns the jet almost all the way back. Reversing momentum is how it takes nearly all the force."),
 B=dict(
  subject="A clean side-view diagram of a horizontal water jet leaving a nozzle on the left and striking a curved vane mounted on a small cart with wheels on a rail. The jet follows the vane surface and leaves at a deflection angle. Blue velocity arrows show the incoming and outgoing jet, an orange arrow shows the force on the vane, and a faint dashed outline of a control volume box surrounds the vane.",
  labels="Incoming jet velocity, outgoing jet velocity, deflection angle, force on the vane, control volume, cart velocity",
  alt="A water jet striking a curved vane on a wheeled cart, with velocity and force arrows and a control volume around the vane.",
  cap="Force equals the rate of momentum change. Draw the box, count what crosses it."),
),
dict(k='siphon', m='01', name='Siphon and Cavitation Sim',
 A=dict(
  subject="A traditional village irrigation tank (wewa) in the dry zone of Sri Lanka at golden hour. A farmer, seen from behind and small in the frame, has laid a long black flexible siphon pipe over the grassy earth bund, one end in the calm tank water and the other end pouring a steady stream into a channel feeding green paddy fields below. Palmyrah palms, a white egret in the shallows, water lilies on the tank.",
  alt="A farmer using a flexible pipe to siphon water over an earth tank bund into paddy fields.",
  cap="A siphon lifts water over the bund with no pump, but only so high before the column breaks."),
 B=dict(
  subject="A side-section cutaway of a siphon pipe rising out of an upper tank, arching over a hill crest, and dropping into a lower tank. Water fills the pipe. A smooth colour gradient inside the pipe shows pressure: normal blue near the tanks, fading to pale near the crown. At the very top of the arch a small cluster of vapour bubbles forms. A thin dashed vertical dimension line from the upper tank surface to the crown shows the lift height.",
  labels="Upper tank level, crown (lowest pressure), lift height, outlet level, total head driving the flow, vapour forms here",
  alt="Cutaway of a siphon arching over a hill between two tanks, with the lowest pressure and a few vapour bubbles at the crown.",
  cap="The crown is where the siphon is most at risk. Pressure there falls with every metre of lift and every bit of speed."),
 C=dict(
  left="A siphon over a very tall hill, the arch rising far above the upper tank (clearly more than the height of a three storey building), drawn flowing happily from tank to tank.",
  right="The same tall siphon, but at the crown the water column has torn apart: a large pale vapour gap fills the top of the arch and both legs have drained partly back toward their tanks, the flow stopped.",
  labels="Left: what people assume, any height works. Right: above roughly 7 to 8 m of lift, the column breaks",
  alt="Two panels: a very tall siphon drawn flowing, and the same siphon with its water column broken by a vapour gap at the top.",
  cap="Air pressure can only push water up about 10 m, and less in practice. Ask a siphon to lift more and it simply quits."),
),
# ---------------------------------------------------------------- 02
dict(k='pipeflow', m='02', name='Pipe Network Solver',
 A=dict(
  subject="An elevated view over a small hillside town in Sri Lanka at dusk, with a cylindrical concrete service reservoir on the hilltop. The image is a semi-cutaway: the streets are partly transparent like an x-ray, revealing a glowing blue network of water pipes beneath them forming connected loops between blocks of houses, with small junction nodes at street corners. Warm house lights, rooftops with clay tiles, palms.",
  alt="A hillside town at dusk with its streets shown semi-transparent, revealing a looped blue water network fed from a hilltop reservoir.",
  cap="Under every town is a network where each loop must balance and each junction must add up."),
 B=dict(
  subject="A clean isometric diagram of a looped pipe network on a pale grid: one elevated reservoir on the left feeding a network of eight round junction nodes connected by pipes into two closed loops plus one dead-end branch. Pipes are drawn with thickness proportional to flow, darker blue for bigger flows, with small arrowheads showing direction. Two curved circular arrows inside the loops indicate loop direction. Each junction has a small downward drop icon showing water being drawn off.",
  labels="Reservoir head, junction demands, pipe flows, loop 1 and loop 2, head loss around each loop sums to zero",
  alt="Isometric diagram of a looped pipe network fed by a reservoir, with arrows showing flow direction and junction demands.",
  cap="Two rules solve any network: flow in equals flow out at every node, and head loss around every loop adds to zero."),
),
dict(k='serpar', m='02', name='Series and Parallel Pipes',
 A=dict(
  subject="A rural road in Sri Lanka where a second large blue water pipeline is being laid in a trench right beside an existing older pipeline, both running parallel into the distance toward low green hills. Pipe sections stacked on the verge, a small crew far away, red earth muted to an olive grey tone, overcast monsoon sky.",
  alt="A new water pipeline being laid in a trench parallel to an existing one along a rural road.",
  cap="Duplicating a main is a parallel pipe problem. The gain is real, and smaller than most people guess."),
 B=dict(
  subject="A two-row comparison diagram. Top row: three pipes of different diameters joined end to end in series between two tanks, each pipe drawn to scale, with a stepped water level in small standpipes showing head falling fastest along the thinnest pipe. Bottom row: two pipes of different diameters running side by side between a common inlet manifold and a common outlet manifold, standpipes at each manifold showing the same head drop across both branches, more flow arrows in the larger pipe.",
  labels="Series: same flow, losses add. Parallel: same head loss, flows add. The thin pipe dominates",
  alt="Top: three pipes in series with head stepping down. Bottom: two pipes in parallel sharing one head drop.",
  cap="In series the flow is shared and losses add. In parallel the head loss is shared and flows add."),
 C=dict(
  left="One pump feeding a single pipe, and beside it the same pump feeding two identical pipes in parallel, with the parallel case drawn delivering twice as many fat flow arrows as the single pipe.",
  right="The same comparison, but the parallel case delivers only modestly more flow (a few extra arrows), because the shared pump and the fixed lift still set the limit. A small pump curve icon sits beside each.",
  labels="Left: two pipes, double the flow. Right: more flow, but well short of double",
  alt="Two panels comparing one pipe and two parallel pipes: drawn as double the flow on the left, only a modest increase on the right.",
  cap="Add a second pipe and friction falls, but the pump and the static lift do not care. Flow rises, it does not double."),
),
dict(k='moody', m='02', name='Moody Chart Navigator',
 A=dict(
  subject="A university hydraulics laboratory in Sri Lanka. A long pipe friction test rig runs along a wall: transparent and steel pipes of different diameters mounted on a frame, connected by small tubes to a board of manometer columns with coloured fluid at different heights. A sump tank and a small blue pump underneath. Soft afternoon light through tall windows, a notebook and calculator on a workbench in the foreground (pages blank).",
  alt="A pipe friction test rig in a hydraulics lab with pipes of different sizes and a manometer board.",
  cap="Every curve on the Moody chart was once a rig like this, run for hours and read by hand."),
 B=dict(
  subject="A split illustration of the inside of a pipe cut lengthwise. Left half: laminar flow, smooth parallel streamlines in neat layers with a parabolic velocity profile drawn as arrow lengths. Right half: turbulent flow, swirling eddies of many sizes with a flatter velocity profile. Below the right half, a circular magnified inset of the pipe wall shows small roughness bumps poking through a very thin calm layer of fluid next to the wall.",
  labels="Laminar: friction set by viscosity. Turbulent: eddies and wall roughness. Viscous sublayer, roughness height",
  alt="Pipe interior split into laminar flow with smooth layers and turbulent flow with eddies, plus a close-up of wall roughness.",
  cap="Whether roughness matters depends on whether the bumps poke through the thin calm layer at the wall."),
),
dict(k='hammer', m='02', name='Water Hammer Simulator',
 A=dict(
  subject="A steep steel penstock pipe descending a forested mountainside to a hydropower station in the Sri Lankan hill country, with a tall cylindrical concrete surge tower standing on the ridge where the pipe begins its descent. Mist drifting through the forest, a reservoir glimpsed at the top, the power house with its tailrace at the bottom. Wide documentary view.",
  alt="A steel penstock running down a forested mountainside to a power station, with a surge tower on the ridge above.",
  cap="The surge tower exists for one moment: when the turbine valve shuts and the water in the penstock has nowhere to go."),
 B=dict(
  subject="A four-step horizontal storyboard, one step above the next, of the same straight pipe running from a reservoir on the left to a valve on the right. Step 1: valve just closed, a high-pressure zone shown as a slightly bulging, darker section of pipe begins at the valve. Step 2: the bulging high-pressure zone has travelled halfway back toward the reservoir. Step 3: the pressure wave reaches the reservoir and reflects. Step 4: a pale low-pressure zone travels back toward the valve, the pipe wall slightly contracted. Small arrows show the wave direction in each step.",
  labels="Valve closes, wave travels at speed a, reflection at the reservoir, low pressure returns, one cycle takes 4L/a",
  alt="Four-step storyboard of a pressure wave running from a closed valve back to a reservoir and returning as low pressure.",
  cap="Close a valve suddenly and a pressure wave runs the length of the pipe, reflects, and comes back inverted."),
 C=dict(
  left="A hand slamming a large valve wheel shut in an instant, with a violent pressure spike drawn as a tall jagged red shape rising from the pipe and the pipe wall visibly bulging.",
  right="The same valve being turned slowly over a long time (suggested by a small clock with a long arc), with only a gentle low hump of pressure above the pipe.",
  labels="Left: closed faster than 2L/a, full Joukowsky rise. Right: closed over many wave periods, small rise",
  alt="Two panels: a valve slammed shut causing a tall pressure spike, and a valve closed slowly causing only a gentle rise.",
  cap="Close faster than one wave round trip and you get the full pressure rise, whatever the valve looks like."),
),
# ---------------------------------------------------------------- 03
dict(k='pump', m='03', name='Pump-System Operating Point',
 A=dict(
  subject="The interior of a clean municipal water pumping station: three large horizontal centrifugal pumps painted deep blue sit in a row on concrete plinths, each coupled to a grey electric motor, with large flanged suction and delivery pipes and gate valves. Overhead crane rail, a pressure gauge on each delivery pipe, soft industrial daylight, polished floor reflections.",
  alt="Three blue centrifugal pumps with motors in a row inside a pumping station.",
  cap="A pump does not choose its flow. It runs wherever its curve meets the pipeline's."),
 B=dict(
  subject="A two-part illustration. Left: a cutaway centrifugal pump showing the curved-vane impeller inside a spiral volute casing, water entering at the eye and spiralling out to the delivery. Right: a minimal text-free chart with a falling blue curve (pump head) and a rising orange curve (system head) crossing at one highlighted glowing point, with faint dashed lines from that point down to the horizontal axis and across to the vertical axis.",
  labels="Impeller eye, volute, delivery. Pump curve, system curve, operating point, static lift",
  alt="Cutaway of a centrifugal pump beside a chart where a falling pump curve crosses a rising system curve.",
  cap="Where the two curves cross is the only place the pump and the pipes agree."),
 C=dict(
  left="A huge oversized pump connected to a modest pipeline, drawn delivering an enormous gush of water out of the pipe end.",
  right="The same oversized pump, but a valve on its delivery is almost closed to hold it back, the pump glowing faintly warm, and only a normal stream leaves the pipe. A small chart icon shows the operating point far to the left of the pump's best efficiency zone.",
  labels="Left: bigger pump, more water. Right: the system curve decides; an oversized pump gets throttled and wastes energy",
  alt="Two panels: an oversized pump imagined delivering a huge flow, and in reality throttled by a nearly closed valve.",
  cap="Buying a bigger pump buys a bigger electricity bill. The pipeline still sets the flow."),
),
dict(k='pumpbuild', m='03', name='Pump Station Builder',
 A=dict(
  subject="A stormwater pumping station beside a canal in a low-lying area of Colombo during monsoon rain. A compact concrete building with louvres, large discharge pipes arching over the canal embankment and releasing water, an electrical control kiosk, and the canal running high with greyish water. Wet road, a few umbrellas far away, dense urban buildings behind.",
  alt="A stormwater pumping station beside a high canal in Colombo during monsoon rain, discharging over the embankment.",
  cap="When the canal is high, gravity drainage stops and the duty pumps take over."),
 B=dict(
  subject="A side-section cutaway of a wet-well pumping station. Incoming sewer or drain pipe enters a deep concrete wet well holding blue water. Three submersible pumps stand on the floor, two running (small motion lines) and one idle as standby. Four float switches hang on cables at different heights marking stop, duty start, assist start and high-level alarm. Discharge pipes rise from each pump into a common header with non-return valves, leaving the station to the right.",
  labels="Inlet, duty pump, assist pump, standby pump, float levels: stop, start, assist, alarm, common discharge header",
  alt="Cutaway of a wet-well pump station with three pumps, float switches at different levels and a common discharge header.",
  cap="Float levels decide which pumps run. The standby only wakes when something fails."),
),
dict(k='npsh', m='03', name='NPSH and Cavitation Check',
 A=dict(
  subject="A dramatic close-up of a bronze centrifugal pump impeller removed for inspection, resting on a workshop bench under a work lamp. The leading edges of the vanes near the eye are badly pitted and eroded into a spongy, cratered texture by cavitation, while the rest of the metal is smooth. A gloved hand points at the damage (only the glove visible). Shallow depth of field.",
  alt="A bronze pump impeller with its vane edges pitted and cratered by cavitation damage.",
  cap="Cavitation damage looks like the metal was eaten. In a sense, it was: by millions of collapsing bubbles."),
 B=dict(
  subject="A side-section cutaway of a pump drawing water from an open sump below it. The water surface in the sump, the suction pipe rising to the pump, and the impeller eye are clearly drawn. Inside the suction pipe a colour gradient shows pressure falling as the water rises and accelerates. At the impeller eye, small white vapour bubbles form, are carried along the vane, and then collapse near the vane surface, drawn as tiny star bursts with micro-jets hitting the metal.",
  labels="Sump level, suction lift, friction in the suction pipe, lowest pressure at the eye, bubbles form, bubbles collapse",
  alt="Cutaway of a pump lifting water from a sump, with vapour bubbles forming at the impeller eye and collapsing on the vane.",
  cap="NPSH available is what the suction side offers. NPSH required is what the impeller demands. Keep a margin."),
 C=dict(
  left="The outside of a running pump installed high above its sump, looking perfectly calm and normal, painted blue, with a green check-shaped indicator light glowing.",
  right="The same pump with its casing cut away, revealing the impeller inside churning with vapour bubbles and visible pitting on the vanes, a small red warning glow.",
  labels="Left: it runs, so it is fine. Right: inside, cavitation is eating the impeller",
  alt="Two panels: a pump that looks fine from outside, and its cutaway showing cavitation bubbles and pitting inside.",
  cap="A cavitating pump often keeps running for months. The damage is quiet until it is expensive."),
),
dict(k='impeller', m='03', name='Impeller and Specific Speed',
 A=dict(
  subject="Three pump impellers displayed on a dark grey workshop bench in a row under soft studio light: a narrow radial-flow centrifugal impeller with long curved vanes, a mixed-flow impeller with angled vanes, and an axial-flow propeller impeller with three broad blades. Machined bronze and stainless steel, crisp reflections, product-photography feel.",
  alt="Three impellers on a workbench: a radial centrifugal impeller, a mixed-flow impeller and an axial propeller.",
  cap="High head and low flow wants a radial impeller. Low head and huge flow wants a propeller. Specific speed tells you which."),
 B=dict(
  subject="A horizontal morphing sequence of five impeller cross sections (meridional view, half section) from left to right: a wide flat radial impeller where flow turns 90 degrees outward, gradually changing through mixed-flow shapes where the outlet tilts, to an axial impeller where flow passes straight through. A curved arrow under the sequence suggests increasing specific speed. Small blue flow-path arrows in each section.",
  labels="Radial, mixed flow, axial. Low specific speed to high specific speed. Flow path through each",
  alt="Five impeller cross sections morphing from radial to mixed flow to axial.",
  cap="Specific speed is one number that predicts the shape of the impeller before anyone draws it."),
),
# ---------------------------------------------------------------- 04
dict(k='idf', m='04', name='IDF Curve Lab',
 A=dict(
  subject="An intense afternoon monsoon downpour over a busy Colombo street, rain falling in heavy grey sheets, roadside drains overflowing at the kerb, tuk-tuks with headlights on in soft focus. In the sharp foreground stands a standard cylindrical copper-and-steel rain gauge on a short concrete post in a small fenced plot, raindrops splashing on its funnel rim.",
  alt="A heavy monsoon downpour over a Colombo street with a rain gauge standing in the foreground.",
  cap="Short storms are fierce, long storms are gentle. An IDF curve puts a number on how fierce, for how long, and how rare."),
 B=dict(
  subject="An illustrated row of five rain clouds over identical small squares of ground, arranged from left to right: a small, very dark, compact cloud releasing extremely dense rain for a short time, then progressively larger and lighter clouds releasing gentler rain for longer, ending with a broad pale cloud with light drizzle. Under each, a vertical bar shows intensity (tallest on the left), and a horizontal bar shows duration (longest on the right). A faint smooth curve connects the tops of the intensity bars, falling from left to right.",
  labels="Intensity, duration, the falling IDF curve, shorter means fiercer, rarer storms sit on higher curves",
  alt="Five rain clouds from short and intense to long and gentle, with bars showing intensity falling as duration grows.",
  cap="The same rare storm is fierce over ten minutes and gentle over a day. The curve is that trade-off."),
),
dict(k='thiessen', m='04', name='Areal Rainfall Studio',
 A=dict(
  subject="A wide elevated view over a green river basin in Sri Lanka from a hilltop: paddy fields, villages, patches of forest and a winding river. Scattered across the landscape, small but clearly visible, are rain gauges: a few standard cylinder gauges in fenced plots and one automatic tipping-bucket weather station with a small solar panel. Faint dotted lines drawn over the landscape suggest the boundaries between gauge zones. A grey rain shower falls over one part of the basin while the rest is in sunshine.",
  alt="An elevated view over a river basin with rain gauges scattered across it and a shower falling over one part.",
  cap="Each gauge sees one point. The question is how much rain fell on everything in between."),
 B=dict(
  subject="A top-down map illustration of an irregular river basin outline on off-white paper. Seven gauge points are marked as small dark circles. The basin is split down the middle: the left half is divided into flat-tinted polygon cells around each gauge in different shades of blue (Thiessen polygons, cell edges as thin lines), the right half shows smooth curved contour bands of rainfall in graded blues (isohyets), darkest where rain was heaviest. The river network drawn as thin pale lines.",
  labels="Gauges, Thiessen polygons (left), isohyets (right), basin boundary, heavier rain darker",
  alt="Map of a river basin with seven gauges, divided into polygon cells on the left and smooth rainfall contours on the right.",
  cap="Polygons give each gauge the area nearest to it. Isohyets let the rainfall field bend between gauges."),
 C=dict(
  left="A hilly basin cross-section where all the rain gauges sit in the lowland valley near the town and river, under light rain, with a small bar chart icon showing modest rainfall.",
  right="The same basin with the full storm visible: very heavy rain on the windward ridges and mountain slopes where no gauge stands, and only light rain over the valley gauges.",
  labels="Left: what the gauges report. Right: the orographic rain they never saw",
  alt="Two panels: rain gauges all in a valley reporting light rain, while heavy rain falls on the ungauged ridges.",
  cap="Gauges are put where people live, not where rain falls hardest. Every averaging method inherits that bias."),
),
dict(k='designstorm', m='04', name='Design Storm Builder',
 A=dict(
  subject="A dramatic monsoon storm front approaching across wide green paddy fields in Sri Lanka: a towering dark blue-grey cloud wall with a sharp leading edge and a curtain of rain under it on the left half of the sky, while the right half still has soft late sunlight on the fields. A lone farmhouse and a line of coconut palms on a field bund, wind bending the rice.",
  alt="A dark monsoon storm front with a rain curtain advancing across paddy fields.",
  cap="Two storms can drop the same depth. When the heaviest part arrives decides the flood."),
 B=dict(
  subject="A grid of four small identical catchments, each with a rain hyetograph drawn as blue vertical bars hanging above it and a flood hydrograph drawn as a filled blue shape beside it. The four rain patterns have the same total but different timing: heaviest at the start, heaviest in the middle, heaviest at the end, and evenly spread. The hydrographs differ: the end-loaded storm gives the tallest sharpest peak, the even storm the lowest broadest one.",
  labels="Front loaded, centre loaded, back loaded, uniform. Same depth, different peaks",
  alt="Four catchments with rain bar charts of equal total but different timing, each producing a differently shaped flood.",
  cap="Rain that arrives late falls on wet ground. That is why back-loaded storms make bigger floods."),
),
dict(k='infil', m='04', name='Infiltration and Runoff Split',
 A=dict(
  subject="Close-up, low angle, of heavy rain falling on a grassy field edge next to a dirt track. Raindrops splash on the ground, small puddles have formed in a shallow depression and thin sheets of muddy water have started to flow across the track surface. The soil shown in muted olive-grey earth tones. Dark overcast sky, droplets frozen mid-splash.",
  alt="Heavy rain on a field edge with puddles forming and thin sheets of runoff starting to flow across a track.",
  cap="Runoff starts the moment the rain falls faster than the soil can take it in."),
 B=dict(
  subject="A tall rectangular soil column cutaway in olive-grey earth tones, like a lab specimen. Rain falls on top. In the upper soil, a darker wet zone extends downward with a sharp wavy wetting front marking its lower edge, above dry lighter soil. On the surface a thin pond of water has formed and a small arrow shows excess water running off to the side. Beside the column, a small inset curve shows infiltration capacity falling quickly at first then levelling off.",
  labels="Rain, ponding, runoff, wet zone, wetting front, dry soil, infiltration capacity falling with time",
  alt="Cutaway soil column with rain on top, a wet zone and wetting front moving down, and runoff from a surface pond.",
  cap="Dry soil drinks fast, then slows. Rain that exceeds the current rate becomes runoff."),
),
# ---------------------------------------------------------------- 05
dict(k='rational', m='05', name='Rational Method Explorer',
 A=dict(
  subject="A high aerial view over a dense suburb near Colombo during steady rain: clay-tile and metal roofs, narrow roads shining wet, roadside drains carrying water, all converging to a large concrete box culvert under a main road where a stream of runoff gushes out. Patches of garden green and a few trees between buildings. Soft grey light.",
  alt="An aerial view of a wet suburb with drains converging to a culvert under a main road.",
  cap="Every drain in a town like this was sized with Q = CiA, whether the designer knew the name or not."),
 B=dict(
  subject="A top-down illustration of a small leaf-shaped catchment draining to an outlet at the bottom. The catchment is divided into curved bands (isochrones) shaded from pale blue near the outlet to deeper blue at the far edge, showing equal travel-time zones. A thin highlighted path runs from the most remote point at the top to the outlet, with small footprint-like dots along it. Small rooftops and trees are scattered across the catchment in a mix.",
  labels="Outlet, isochrones, the longest flow path, time of concentration, runoff coefficient from land cover",
  alt="Top-down catchment with curved travel-time bands and the longest flow path from the farthest point to the outlet.",
  cap="The peak comes when water from the farthest point finally reaches the outlet: the time of concentration."),
 C=dict(
  left="A catchment where the entire area is lit up as contributing to the outlet from the very first minute of rain, with arrows from everywhere at once.",
  right="The same catchment a few minutes into the storm: only the band nearest the outlet is lit and contributing, the rest still grey, and a clock icon shows that full contribution has not arrived yet.",
  labels="Left: the whole catchment from minute one. Right: only the area within the travel time contributes until t_c",
  alt="Two panels: a whole catchment drawn contributing at once, and only the band near the outlet contributing early in the storm.",
  cap="Choose a storm shorter than t_c and part of the catchment never gets to join in."),
),
dict(k='uh', m='05', name='Unit Hydrograph Convolution',
 A=dict(
  subject="A river gauging station on a medium-sized Sri Lankan river during a rising flood: a tall white staff gauge with graduated bands (no readable numbers) stands in brown-grey swirling water that has already covered its lower half, next to a small concrete gauge house with a cableway above the river. Debris floating, overcast sky, green riverbank trees.",
  alt="A staff gauge standing in a rising flood beside a small gauge house and a cableway over the river.",
  cap="The unit hydrograph is read from records like this: the river's signature response to one unit of rain."),
 B=dict(
  subject="A layered illustration showing convolution. At the top, four blue rain bars of different heights in sequence. Below, four identical-shaped translucent hydrograph humps, each scaled to its rain bar's height and shifted right by one time step, in four different blues. At the bottom, the four humps stacked and summed into one larger smooth flood hydrograph outline drawn in dark ink.",
  labels="Rainfall excess blocks, one scaled and delayed unit hydrograph per block, the sum is the flood",
  alt="Four rain bars each producing a scaled, delayed copy of the same hydrograph shape, stacked into one flood hydrograph.",
  cap="Each block of rain launches its own copy of the unit hydrograph. The flood is all the copies added up."),
 C=dict(
  left="A small flood hydrograph and a huge flood hydrograph drawn as exact scaled-up copies of each other, same timing, same shape, just taller, over a simple river channel.",
  right="The huge flood arriving earlier and peaking more sharply than the scaled copy, with the river spilling onto its floodplain in a small inset, a faint ghost outline of the scaled copy behind it for comparison.",
  labels="Left: linearity assumed. Right: extreme floods run faster than the UH predicts",
  alt="Two panels: a big flood drawn as a scaled copy of a small one, and in reality arriving earlier and peaking sharper.",
  cap="A unit hydrograph built from ordinary floods tends to be too slow for extreme ones. The bias has a known direction."),
),
dict(k='scs', m='05', name='SCS Curve Number Explorer',
 A=dict(
  subject="A panoramic view across a Sri Lankan landscape during light rain showing three land covers side by side from left to right: dense natural forest on a hillside, terraced green paddy fields in the middle, and a growing town of concrete roofs and tarmac roads on the right. Rainwater visibly runs off the roads and roofs into a drain, while the forest floor looks absorbent and calm.",
  alt="A landscape in rain with forest on the left, paddy fields in the middle and a town on the right.",
  cap="Same rain, three surfaces, three very different amounts of runoff. The curve number is that difference in one index."),
 B=dict(
  subject="A side-section illustration of rain falling on a strip of ground that changes from forest on the left to grassland in the middle to paved town on the right. The rain is split into three visible paths shown with arrows in different blues: water caught by leaves and small surface hollows (initial abstraction), water soaking down into olive-grey soil, and water running off over the surface. The runoff arrow grows dramatically from left to right while the infiltration arrow shrinks.",
  labels="Initial abstraction, infiltration, runoff. Low CN forest, medium CN grass, high CN town",
  alt="Rain falling on forest, grass and town, splitting into abstraction, infiltration and runoff, with runoff growing toward the town.",
  cap="Nothing runs off until the initial abstraction is filled. After that, the soil and the surface share what is left."),
 C=dict(
  left="Two identical catchments each receiving the same daily rain total, one storm compressed into a single intense hour and one spread across a whole day, both drawn producing an identical tall flood peak at the outlet.",
  right="The same two storms: the one-hour storm producing a sharp tall flood peak, the all-day storm producing a low broad hydrograph, while a small bucket icon beside each shows that their runoff volumes are similar.",
  labels="Left: CN gives the peak. Right: CN gives volume only; timing sets the peak",
  alt="Two panels: two storms with the same daily total drawn giving the same flood, and in reality very different peaks with similar volumes.",
  cap="The curve number method knows nothing about intensity. Use it for runoff volume, not for the peak."),
),
dict(k='scsuh', m='05', name='SCS Synthetic Unit Hydrograph',
 A=dict(
  subject="A remote, ungauged small catchment in the dry zone of Sri Lanka seen from a low hill: scrub jungle, rocky outcrops, a few seasonal streams converging into a small village tank in the middle distance, no gauge or station in sight. A lone engineer with a field tablet and a measuring wheel stands small on a dirt track, seen from behind. Hazy afternoon heat.",
  alt="An ungauged dry-zone catchment of scrub and rock draining into a small tank, with an engineer on a track.",
  cap="Most catchments were never gauged. A synthetic unit hydrograph builds their response from the map."),
 B=dict(
  subject="A two-part illustration. Left: a top-down catchment sketch with the divide drawn as a dashed line, contour lines inside it, the longest flow path highlighted with arrows to the outlet, and a small wedge symbol showing average slope. Right: a smooth bell-like hydrograph curve with a simple triangle of the same area overlaid on it, the triangle's peak aligned with the curve's peak.",
  labels="Area, longest flow path, slope, curve number, lag time, time to peak, base time of the triangle",
  alt="A catchment map with its longest flow path and slope beside a smooth hydrograph overlaid with an equivalent triangle.",
  cap="Area, length, slope and land cover. Four numbers off a map give you a hydrograph."),
),
# ---------------------------------------------------------------- 06
dict(k='manning', m='06', name='Manning Normal Depth',
 A=dict(
  subject="A long, straight concrete-lined trapezoidal irrigation canal of a Mahaweli-style scheme in Sri Lanka, running toward the horizon between green paddy fields and a service road. The water flows smooth and steady at uniform depth, reflecting the sky. A small foot bridge crosses in the middle distance, palmyrah palms, a clear morning sky.",
  alt="A long straight lined irrigation canal flowing at uniform depth between paddy fields.",
  cap="Down a long straight canal, gravity and friction strike a balance. That depth is normal depth."),
 B=dict(
  subject="A clean cross-section of a trapezoidal channel filled with water, with concentric curved velocity contour bands inside the water: deepest blue fastest band just below the surface in the middle, fading to pale near the bed and sloping sides. The wetted perimeter (bed plus wetted sides) is traced with a bold orange line. Small hatch marks on the concrete lining. A faint side-view wedge in a corner shows the bed slope.",
  labels="Flow area, wetted perimeter, hydraulic radius, bed slope, roughness n, fastest flow near the surface centre",
  alt="Trapezoidal channel cross-section with velocity contours fastest near the surface centre and the wetted perimeter highlighted.",
  cap="Area over wetted perimeter is the hydraulic radius. Friction lives on the perimeter."),
 C=dict(
  left="A clean concrete-lined canal with a material swatch icon of smooth concrete beside it, drawn with a single low roughness indicator.",
  right="The same concrete canal after years of service: weeds and grass growing on the side slopes, silt deposits on the bed, floating debris, and a bend in the alignment, with a much higher roughness indicator.",
  labels="Left: n is set by the lining. Right: weeds, silt, debris and bends raise n far above the textbook value",
  alt="Two panels: a clean new concrete canal, and the same canal with weeds, silt and debris that raise its roughness.",
  cap="Manning's n describes the channel you will actually have, not the one in the drawings."),
),
dict(k='specific-energy', m='06', name='Specific Energy Playground',
 A=dict(
  subject="A long glass-walled laboratory flume in a university hydraulics lab with blue-tinted water flowing over a smooth raised hump fixed to the flume floor. The water surface visibly dips as it passes over the hump. A pointer gauge on a carriage above the flume, a technician's hand adjusting a valve at the far end (hand only). Clean lab lighting, glass reflections.",
  alt="A glass laboratory flume with water flowing over a raised hump, the surface dipping above it.",
  cap="Raise the floor and slow, deep water drops over it. That surprises almost everyone the first time."),
 B=dict(
  subject="A longitudinal side-section of a rectangular flume with a smooth raised hump on the floor. Upstream the water is deep and calm, over the hump the water surface dips noticeably, and downstream it returns to its original depth. A perfectly horizontal dashed line runs above the water along the whole length showing constant energy. Small vertical dimension markers show depth upstream, over the hump and the hump height.",
  labels="Upstream depth, hump height, depth over the hump, energy line stays level, subcritical flow",
  alt="Side section of a flume where water dips over a floor hump while a level energy line runs above.",
  cap="With no losses, energy stays level. Raising the floor takes energy out of the depth."),
 C=dict(
  left="A channel with a raised floor hump where the water surface simply dips over the hump, drawn the same way for a very high hump that nearly fills the channel.",
  right="The same very high hump, but the flow has choked: water backs up into a much deeper pool upstream, then pours over the hump at critical depth and races away shallow and fast downstream.",
  labels="Left: a bigger hump just means a bigger dip. Right: past the critical height, the flow chokes and backs up upstream",
  alt="Two panels: water dipping over a very tall hump, and in reality the flow choking and backing up upstream.",
  cap="Every channel has a limit. Raise the hump past it and the upstream water must rise to get over."),
),
dict(k='froude', m='06', name='Froude Wave Tank',
 A=dict(
  subject="Two streams side by side in a split composition. Left: a slow, calm lowland stream where a dropped pebble creates concentric ripples that spread in all directions, including upstream. Right: a fast, shallow mountain stream rushing over smooth rocks, where a single protruding stone leaves a sharp V-shaped wake trailing only downstream. Clear water, natural stones, soft daylight, both from a similar elevated angle.",
  alt="Left: ripples spreading in all directions on a slow stream. Right: a sharp V wake behind a stone in a fast stream.",
  cap="If ripples can climb upstream, the flow is subcritical. If they are swept away in a V, it is supercritical."),
 B=dict(
  subject="Three square panels viewed from above, each showing water flowing left to right with a small disturbance point. Panel 1: a set of ripple circles shifted slightly downstream but still enclosing the source on all sides. Panel 2: circles whose upstream edges all line up on one vertical line through the source. Panel 3: circles swept far downstream forming a sharp V-shaped wedge behind the source, nothing upstream of it. Flow arrows at the top of each panel get longer from panel 1 to panel 3.",
  labels="Fr < 1 subcritical, Fr = 1 critical, Fr > 1 supercritical, wave speed versus flow speed",
  alt="Three overhead panels of ripple rings from a point source as flow speed rises, ending in a V-shaped wedge.",
  cap="The Froude number compares how fast the water moves with how fast a wave can travel through it."),
 C=dict(
  left="A fast, shallow channel with a gate partly lowered far downstream, and imagined ripple signals drawn travelling upstream from the gate to warn the water above, which adjusts its level.",
  right="The same fast channel, but the ripple signals from the gate are swept downstream and never reach the water above, which stays unaware until a hydraulic jump forms right at the gate.",
  labels="Left: downstream changes travel up. Right: in supercritical flow, no information goes upstream",
  alt="Two panels: signals drawn travelling upstream in a fast channel, and in reality swept downstream with a jump forming at the gate.",
  cap="In supercritical flow the water upstream cannot know what lies ahead. Control comes from upstream."),
),
dict(k='weir', m='06', name='Weir and Flume Lab',
 A=dict(
  subject="A sharp-crested rectangular measuring weir across a concrete irrigation channel in Sri Lanka. A thin steel plate crest with a clean transparent sheet of falling water (the nappe) springing clear of the plate and falling into a pool below, air visible beneath the falling sheet. A small staff gauge set upstream on the channel wall, green paddy fields and a farmer's bicycle in the background.",
  alt="A sharp-crested weir in an irrigation channel with a clear sheet of water springing off its crest.",
  cap="Measure the head above the crest and the weir tells you the flow. That is what a weir is for."),
 B=dict(
  subject="A side-section of a sharp-crested weir plate across a channel. Upstream the water approaches calmly; at the crest the water surface draws down and springs off as a curved nappe, with a pocket of air drawn under the nappe against the downstream face of the plate. A small vent pipe connects the air pocket to the atmosphere. Upstream at a distance of about four times the head, a point gauge touches the water surface. The tailwater pool sits low below.",
  labels="Head over crest H, measure about 4H upstream, crest height p, nappe, aerated pocket, vent, tailwater",
  alt="Side section of a sharp-crested weir with a curved nappe, an aerated pocket below it and a head gauge upstream.",
  cap="Read the head upstream, before the surface starts to draw down, or the rating will lie to you."),
),
dict(k='compound', m='06', name='Compound Channel Capacity',
 A=dict(
  subject="A Sri Lankan river in flood during the southwest monsoon: the main channel runs fast and dark with debris, and the water has spilled over its banks onto wide floodplain paddy fields on both sides, where it spreads shallow and slow, with rice tops and fence posts poking through. A road embankment and a line of trees in the distance, heavy grey sky.",
  alt="A river in flood spilling out of its main channel onto wide floodplain paddy fields.",
  cap="Once the river leaves its banks, two very different flows share one cross-section."),
 B=dict(
  subject="A cross-section of a compound channel: a deep main channel in the centre with wide shallow floodplains on both sides, all filled with water. Thin vertical dashed lines divide the section into three zones at the main channel banks. The main channel water is a deeper, faster blue with long flow arrows; the floodplain water is paler with short flow arrows. At the junctions between zones, small swirling vortex shapes indicate shear.",
  labels="Main channel, left and right floodplain, division lines, fast and slow zones, shear at the interface",
  alt="Cross-section of a main channel with floodplains on both sides, divided into fast and slow zones with vortices between them.",
  cap="Treat the floodplain and the main channel separately, then add the flows. Lumping them together underestimates capacity."),
),
# ---------------------------------------------------------------- 07
dict(k='openchannel', m='07', name='Open Channel Modeller',
 A=dict(
  subject="A long irrigation canal descending in steps through a gently sloping Sri Lankan landscape, seen from a raised viewpoint: a series of concrete drop structures where the water falls a short height into stilling pools, with calm reaches between them. Paddy fields and coconut groves on both sides, a vehicle track along the bund.",
  alt="An irrigation canal stepping down through a landscape with a series of small drop structures.",
  cap="Build a channel of reaches and structures, and each one sets the water surface of its neighbours."),
 B=dict(
  subject="A long-section illustration of a channel along its length: the bed changes slope twice, with a sluice gate near the left, a mild reach, a steeper reach in the middle and a weir at the right end. The water surface curves smoothly between controls: rising behind the weir, drawing down toward the slope break, and showing a small hydraulic jump below the gate. Two thin dashed reference lines run along each reach for normal and critical depth.",
  labels="Gate, mild reach, steep reach, weir, normal depth, critical depth, backwater, drawdown, jump",
  alt="Long section of a channel with a gate, two slopes and a weir, the water surface curving between them.",
  cap="Controls hold the water surface; the reaches between them bend it toward normal depth."),
),
dict(k='profiles', m='07', name='Water Surface Profiles',
 A=dict(
  subject="A traditional stone anicut (diversion weir) across a wide, slow river in Sri Lanka in the dry season. Upstream of the weir the river is backed up into a long calm mirror-like reach extending far into the distance, while water spills smoothly over the weir crest. Large trees reflected in the backwater, a few cattle grazing on the bank.",
  alt="A stone diversion weir across a river with a long calm backwater reach extending far upstream.",
  cap="A weir raises the river for kilometres upstream. That long gentle curve is a backwater profile."),
 B=dict(
  subject="Two separate long side-section panels stacked one above the other, water flowing from left to right in both, on the same gently sloping (mild) channel bed. TOP PANEL: the channel ends at a concrete dam at the right edge of the panel. Far upstream on the left the water is at its natural uniform depth; moving right toward the dam the water gets steadily deeper, its surface curving gently upward until it is level with the reservoir behind the dam. Nothing is drawn downstream of the dam. BOTTOM PANEL: the same channel ends in a free overfall at the right edge, a sharp drop where water pours off the end. Far upstream the water is at its natural uniform depth; moving right toward the brink the surface curves gently downward, the water getting shallower, and pours over the edge. In both panels a dashed line parallel to the bed marks the natural uniform (normal) depth, and a second, lower dashed line parallel to the bed marks critical depth.",
  labels="Normal depth line, critical depth line, M1 backwater behind the dam (top), M2 drawdown at the fall (bottom), mild slope",
  alt="Long section of a river with a curved backwater behind a dam and a drawdown curve toward a free overfall.",
  cap="Every profile is the water surface easing from what a control demands toward what the channel prefers."),
 C=dict(
  left="A river reach behind a dam with the water surface drawn level with the dam only very close to it, and parallel to the bed (uniform depth) everywhere else, as if the dam's influence ends a few metres upstream.",
  right="The same reach with the backwater curve extending far upstream, many kilometres, flooding a village and a bridge far away, with a faint ghost of the uniform-depth surface for comparison.",
  labels="Left: the dam only affects its immediate surroundings. Right: on a mild slope, backwater reaches far upstream",
  alt="Two panels: a dam's effect drawn as short, and in reality a backwater curve reaching a distant village and bridge.",
  cap="On a mild river, a new weir can raise flood levels in a town many kilometres away."),
),
dict(k='jump', m='07', name='Hydraulic Jump Lab',
 A=dict(
  subject="The stilling basin at the foot of a concrete dam spillway during a release: fast smooth water shoots down the spillway chute, then abruptly erupts into a churning white roller of foam and spray in the basin, and leaves calmer and deeper downstream. Concrete baffle blocks just visible in the basin, mist hanging in the air, forested hills around.",
  alt="A hydraulic jump erupting into white foam in the stilling basin at the foot of a dam spillway.",
  cap="The stilling basin is built to make a jump. Its job is to destroy energy before it reaches the riverbed."),
 B=dict(
  subject="A side-section of a horizontal rectangular channel showing a hydraulic jump: on the left a thin, fast supercritical stream with long arrows, then a steep turbulent roller where the depth rises sharply with swirling eddies and entrained air bubbles, then on the right a deep, slow subcritical flow with short arrows. Two vertical dimension markers show the shallow depth before and the deep depth after. A thin energy line above drops sharply across the jump.",
  labels="Supercritical inflow y1, roller, subcritical outflow y2, sequent depths, energy lost in the jump",
  alt="Side section of a hydraulic jump from shallow fast flow through a turbulent roller to deep slow flow.",
  cap="Momentum is conserved across a jump. Energy is not, and that loss is the point."),
 C=dict(
  left="A stilling basin below a spillway with the jump sitting neatly inside the basin, drawn as a permanent fixed feature.",
  right="The same basin with low tailwater: the jump has been swept out of the basin and sits far downstream on the unprotected riverbed, which is badly eroded with scattered riprap.",
  labels="Left: the jump stays put. Right: too little tailwater and the jump sweeps out of the basin",
  alt="Two panels: a jump held inside a stilling basin, and the jump swept downstream onto an eroded riverbed when tailwater is low.",
  cap="Tailwater holds the jump in place. Get it wrong and the jump goes looking for the riverbed."),
),
dict(k='sluice', m='07', name='Sluice Gate and Discharge',
 A=dict(
  subject="A steel vertical-lift sluice gate in the concrete headworks of an irrigation canal off a large Sri Lankan reservoir: the gate is raised a short way and a powerful jet of water rushes out underneath it into the canal, forming whitewater a short distance downstream. A grey gate hoist mechanism on the deck above, the reservoir water calm behind the gate, a mountain in the distance.",
  alt="A vertical-lift sluice gate raised slightly with a powerful jet of water rushing out underneath into a canal.",
  cap="Under a gate, depth is traded for speed. Where that fast water slows down decides the rest."),
 B=dict(
  subject="A two-row side-section comparison of flow under a vertical sluice gate. Top row (free flow): deep water upstream, a jet under the gate that contracts to its smallest depth a short distance downstream (vena contracta), then a hydraulic jump further downstream. Bottom row (drowned flow): the same gate with high tailwater, the jump has moved upstream and submerged the jet right against the gate, with turbulent water over it.",
  labels="Upstream depth, gate opening, vena contracta, free jump, drowned outlet, tailwater level",
  alt="Two side sections of flow under a sluice gate: a free jet with a jump downstream, and a drowned jet under high tailwater.",
  cap="Free or drowned changes the discharge. The tailwater decides which one you have."),
),
dict(k='stepmethod', m='07', name='Standard Step Method',
 A=dict(
  subject="A survey team, small figures seen from the side, measuring river cross-sections along a gentle Sri Lankan river in the dry season: one person holds a levelling staff in the shallow water, another stands at an automatic level on a tripod on the bank, colourful ranging poles mark a line across the river. Several such section lines continue upstream, marked by poles. Green banks, clear sky.",
  alt="A survey team measuring a river cross-section with a levelling staff and an automatic level on the bank.",
  cap="The step method marches from section to section. Every section was first a line of poles like these."),
 B=dict(
  subject="An oblique three-dimensional illustration of a river reach sliced into five evenly spaced vertical cross-section planes, like glass panes. Each pane shows the channel shape and the water level at that section. Curved arrows hop from the most downstream pane to the next one upstream, one step at a time. The water surface connecting the panes is drawn as a smooth translucent ribbon that rises gently upstream.",
  labels="Known section, next section, step length, water surface computed section by section, march direction",
  alt="A river reach sliced into cross-section planes with arrows stepping upstream from one to the next.",
  cap="Start where you know the depth, then balance energy one step at a time."),
),
# ---------------------------------------------------------------- 08
dict(k='shields', m='08', name='Shields Threshold of Motion',
 A=dict(
  subject="An underwater macro view at bed level in a clear, flowing gravel-bed stream: a carpet of rounded pebbles and coarse sand, with a few of the smaller grains lifting off the bed and rolling or hopping downstream in the current, while the larger pebbles stay put. Sunlight caustic patterns ripple across the stones. Natural grey-olive stone colours.",
  alt="Underwater view of a gravel stream bed with a few small grains starting to roll downstream while larger pebbles stay.",
  cap="At the threshold, only some grains move, and only some of the time. Shields put a number on that moment."),
 B=dict(
  subject="A close-up side-view diagram of one rounded grain resting in a pocket between neighbouring grains on a stream bed. Flow passes over it from left to right with a velocity profile drawn as arrows growing with height. Force arrows act on the grain: a horizontal drag arrow, an upward lift arrow, and a downward weight arrow, with a small pivot point marked where the grain touches the downstream neighbour.",
  labels="Flow, drag, lift, submerged weight, pivot point, bed shear stress",
  alt="A single grain on a stream bed with drag, lift and weight arrows and a pivot point against its neighbour.",
  cap="The grain moves when drag and lift can roll it over its pivot against its own weight."),
 C=dict(
  left="A deep, calm river pool with a lot of water above the bed, the gravel bed beneath moving vigorously as if deep water alone sets the grains in motion.",
  right="The same deep calm pool with a perfectly still bed, beside a shallow, steep riffle where the water is thin but fast, and gravel is actively rolling.",
  labels="Left: deeper water moves more sediment. Right: shear stress depends on depth times slope; the steep riffle wins",
  alt="Two panels: a deep pool drawn moving its bed, and in reality a still pool beside a shallow steep riffle where gravel moves.",
  cap="It is shear stress, depth times slope, that moves grains, not depth on its own."),
),
dict(k='scour', m='08', name='Bridge Pier Scour',
 A=dict(
  subject="A road bridge with round concrete piers over a fast-flowing Sri Lankan river in flood. At the base of the nearest pier, the muddy water swirls in a visible horseshoe-shaped eddy wrapping around the upstream face, with a turbulent wake trailing downstream. Floating debris caught against the pier. Overcast sky, green banks.",
  alt="A bridge pier in a flooded river with water swirling around its base and a turbulent wake behind it.",
  cap="The most dangerous thing a river does to a bridge happens underwater, at the foot of its piers."),
 B=dict(
  subject="A three-dimensional cutaway of a cylindrical bridge pier standing in a riverbed, with the bed and water cut open to reveal what happens below. Flow approaches from the left; at the upstream face a downward flow dives to the bed and rolls into a horseshoe-shaped vortex that wraps around both sides of the pier. A cone-shaped scour hole is excavated around the pier base, deepest at the front. Small wake vortices peel off behind the pier.",
  labels="Approach flow, down flow, horseshoe vortex, scour hole, wake vortices, foundation depth",
  alt="Cutaway of a bridge pier with a horseshoe vortex wrapping around its base and a scour hole dug around it.",
  cap="Flow diving down the front of the pier rolls into a horseshoe vortex and digs the hole."),
 C=dict(
  left="A bridge pier after a flood, seen in a cutaway: the riverbed around the pier looks flat and normal, and an inspector's torch beam shows nothing unusual.",
  right="The same cutaway with layers revealed: a deep scour hole that formed at the flood peak, now refilled with loose, lighter-coloured sediment, and the pier's foundation exposed and undermined beneath the refill.",
  labels="Left: the bed looks fine after the flood. Right: the hole that formed at the peak has been refilled with loose sediment",
  alt="Two panels: a normal looking bed after a flood, and the cutaway revealing a refilled scour hole that undermined the foundation.",
  cap="Scour holes refill as floods recede. A post-flood inspection can miss the depth that nearly took the bridge."),
),
dict(k='traplife', m='08', name='Reservoir Trap Efficiency and Life',
 A=dict(
  subject="A large reservoir in the Sri Lankan hills during a dry spell with low water: at the upstream end, where a river enters, a broad grey-olive sediment delta has built out into the reservoir, cracked silt flats with scattered green weeds, the river meandering across it. The dam is visible far away at the other end of the lake. Hazy hills, low sun.",
  alt="A reservoir at low water with a large silt delta built out where the river enters.",
  cap="Every reservoir is slowly filling with soil. Trap efficiency tells you how fast."),
 B=dict(
  subject="A long-section illustration of a reservoir from the river inflow on the left to the dam on the right. Coarse sediment (drawn as larger grey-olive particles) settles first as a delta with a steep front near the inflow; finer sediment (small pale particles) travels further and settles as a thin layer along the bed toward the dam. A small plume of the finest particles passes over the dam crest with the outflow. Faint horizontal bands mark the live storage and dead storage zones.",
  labels="Inflow with sediment, delta (coarse), bottomset (fine), dead storage, live storage, sediment passing the dam",
  alt="Long section of a reservoir with a coarse sediment delta near the inflow and fine silt settling toward the dam.",
  cap="Coarse grains drop first and build a delta. Fines travel to the dam. Some escape downstream."),
 C=dict(
  left="A brand-new reservoir full of clear blue water behind its dam, with a symbol suggesting it lasts forever.",
  right="The same reservoir a few decades later from the same viewpoint: a large sediment delta has crept down the lake, the water area is noticeably smaller, and the intake tower stands close to the encroaching silt.",
  labels="Left: storage is permanent. Right: sediment eats live storage year after year",
  alt="Two panels: a new full reservoir, and the same reservoir decades later with a sediment delta shrinking it.",
  cap="A reservoir's capacity is a stock being drawn down. Design life is part of the design."),
),
# ---------------------------------------------------------------- 09
dict(k='montecarlo', m='09', name='Monte Carlo Design Risk',
 A=dict(
  subject="A rural road crossing a seasonal stream in Sri Lanka through a box culvert, seen from the downstream side in the dry season. Painted onto the image as faint translucent blue horizontal lines across the culvert headwall are many possible flood water levels, clustered thickly in the middle and sparse at the top and bottom, like ghosted futures. Scrub vegetation, dry stream bed, warm afternoon light.",
  alt="A box culvert under a rural road with faint ghosted lines showing many possible flood levels across its headwall.",
  cap="Every input is uncertain, so the answer is a spread of futures, not a single line."),
 B=dict(
  subject="An abstract illustration of a Monte Carlo simulation: on the left, three small input distribution bell curves stacked vertically, each with dots being drawn out of it like balls from a machine. In the middle, a stream of many small dots flows through a simple funnel-shaped model box. On the right, the dots pile up into a histogram of outcomes, with a thin vertical line marking a design limit and the dots beyond it tinted red.",
  labels="Uncertain inputs, random samples, model, distribution of outcomes, design limit, probability of failure",
  alt="Dots sampled from three input distributions flow through a model box and pile up into a histogram with a failure tail.",
  cap="Sample the inputs thousands of times and count how often the design fails. That count is the risk."),
),
dict(k='risk', m='09', name='Risk and Return Period',
 A=dict(
  subject="The weathered whitewashed wall of an old riverside building in a Sri Lankan town, with several historical flood high-water marks painted as horizontal lines at different heights, some with small blank metal plaques beside them (no readable text). A river flows calmly past in the background, a bicycle leaning against the wall, soft morning light, gentle documentary realism.",
  alt="An old building wall with several historical flood high-water marks painted at different heights.",
  cap="Some of these marks sit only a few years apart. A 100-year flood is a probability, not a timetable."),
 B=dict(
  subject="A calendar-like grid of 100 small squares in ten rows of ten, each square one year, pale off-white. A handful of squares contain a blue water drop icon marking flood years, scattered randomly: two drops sit in adjacent squares, and a long stretch of rows has no drops at all. Above the grid, a small horizontal bar shows the probability of seeing at least one flood during a project lifetime.",
  labels="One square per year, annual exceedance probability 1/T, design life n, risk of at least one exceedance",
  alt="A grid of 100 year-squares with a few randomly scattered flood drops, two of them in consecutive years.",
  cap="Over a 100-year life, a 100-year flood has about a two in three chance of turning up at least once."),
 C=dict(
  left="A timeline of 300 years with 100-year floods drawn as neat evenly spaced markers exactly every 100 years, like a clock.",
  right="The same 300-year timeline with flood markers placed randomly: two in back-to-back years, then a gap of over 150 years, then another.",
  labels="Left: once every 100 years. Right: a 1 percent chance each year, in any order",
  alt="Two timelines: floods evenly spaced every 100 years, and floods randomly clustered with two in consecutive years.",
  cap="The river does not keep a diary. Last year's flood does not make this year safer."),
),
dict(k='freqfit', m='09', name='Frequency Fitting Studio',
 A=dict(
  subject="An archive room at a hydrology office: shelves of old bound streamflow record ledgers and long paper chart rolls from a mechanical water-level recorder, one chart unrolled on a wooden table showing a hand-drawn ink trace of river level rising and falling (no readable text or numbers). A desk lamp, a magnifying glass, dust in the light.",
  alt="An archive of old river record ledgers with a paper water-level chart unrolled on a table.",
  cap="A frequency curve is only as good as the record behind it, and records are short."),
 B=dict(
  subject="A clean text-free chart illustration: a cloud of dark dots representing annual flood peaks plotted against a horizontal axis of rarity. A smooth fitted curve passes through the dots and continues to the right beyond the last dot. Past the data, a shaded uncertainty fan opens up around the curve, getting very wide toward the far right. Two or three alternative fitted curves in different line styles diverge in the fan region.",
  labels="Observed annual maxima, fitted distribution, record length, extrapolation region, widening uncertainty",
  alt="Annual flood peaks with a fitted curve that continues past the data into a widening uncertainty fan.",
  cap="Inside the record, every distribution agrees. Outside it, they argue."),
 C=dict(
  left="A fitted flood frequency curve extended far beyond a short cloud of data points to a very rare event, with one confident thin line and a precise glowing dot at the far end.",
  right="The same data and extrapolation, but the far end is surrounded by a huge shaded uncertainty band, with several different fitted curves spreading apart.",
  labels="Left: a confident 1000-year flood from 30 years of data. Right: the honest uncertainty",
  alt="Two panels: one confident extrapolated curve to a rare flood, and the same with a wide band of disagreeing curves.",
  cap="Thirty years of data cannot tell you the 1000-year flood to the nearest cubic metre."),
),
dict(k='freqlab', m='09', name='Flood Frequency Lab',
 A=dict(
  subject="A student's study desk at night, viewed over their shoulder (no face visible): a laptop showing a blank spreadsheet grid and a scatter chart with a curve (no readable numbers), a printed table of annual peaks with highlighter marks, a scientific calculator, a cup of tea, and a window showing rain on the glass and city lights beyond.",
  alt="A student's desk at night with a laptop showing a spreadsheet and a flood frequency chart, rain on the window.",
  cap="Bring your own record. The real work is defending the fit you choose."),
 B=dict(
  subject="A left-to-right workflow illustration in four stages connected by arrows: a river gauge station icon; a vertical bar chart of annual peak flows by year; the same bars sorted from largest to smallest with rank numbers suggested by dot markers; and finally a scatter of points on probability paper with a fitted straight-ish line through them.",
  labels="Gauge record, annual maximum series, rank and plotting position, fit on probability paper",
  alt="Four stage workflow from a river gauge to annual peaks, sorted ranks, and points with a fitted line.",
  cap="Pick the annual maxima, rank them, give each a probability, then fit and argue."),
),
dict(k='reliability', m='09', name='Reliability and Redundancy',
 A=dict(
  subject="A grassy earthen flood levee protecting a small Sri Lankan village during high river levels: the river on the left runs swollen and close to the levee crest, while houses and paddy fields sit lower on the right, protected. Sandbags stacked along one section of the crest, a few people small in the distance checking the bank. Grey sky with a break of light.",
  alt="An earth levee holding back a swollen river close to its crest, with a village sitting lower behind it.",
  cap="A levee is designed for a chosen flood. Reliability asks how often nature exceeds the choice."),
 B=dict(
  subject="A side-section of an earth levee with the river on the left. Instead of a single water level, a sideways bell-shaped probability curve rises from the riverbed, showing the spread of possible annual flood levels, its upper tail extending above the levee crest. The part of the tail above the crest is shaded in red. The freeboard between the design level and the crest is marked with a small dimension line.",
  labels="Distribution of flood levels, design level, freeboard, crest, probability of overtopping",
  alt="Earth levee section with a sideways bell curve of possible flood levels, its tail above the crest shaded red.",
  cap="Overtopping probability is the area of the tail that peeks over the crest."),
 C=dict(
  left="A long levee drawn uniformly strong along its whole length, all sections glowing a healthy green.",
  right="The same long levee seen from above with one short low spot (a road crossing ramp) and one section weakened by an animal burrow, water breaking through at that one weak point while the rest holds.",
  labels="Left: strong almost everywhere means safe. Right: a series system fails at its weakest link",
  alt="Two panels: a uniformly strong levee, and the same levee failing at one low road crossing.",
  cap="Systems fail where you did not look. One low spot sets the reliability of the whole line."),
),
# ---------------------------------------------------------------- 10
dict(k='catchment', m='10', name='The Living Catchment',
 A=dict(
  subject="A sweeping aerial panorama of a Sri Lankan hill-country catchment: misty forested ridges at the top, tea estates and home gardens on the middle slopes, a village and paddy terraces in the valley, a river winding down to a reservoir with a dam in the lower right. Patches of rain falling from a cloud over the ridges, sunlight on the valley. Cinematic yet calm.",
  alt="An aerial panorama of a hill-country catchment from forested ridges through tea and villages down to a river and reservoir.",
  cap="One catchment, one storm, every millimetre accounted for."),
 B=dict(
  subject="A detailed side-section cutaway of a single hillslope draining to a river channel on the right. Above: a rain cloud. Rain falls on a forest canopy, some caught on leaves, some evaporating upward as faint wisps. On the ground: an olive-grey soil layer with a darker moist zone, arrows showing infiltration down into soil, percolation further down to a groundwater zone with a gently sloping water table, groundwater seeping slowly toward the stream as baseflow, and a thin sheet of overland flow running down the surface to the channel. Each flux shown as a clean arrow in a distinct shade of blue or green.",
  labels="Rain, interception, evapotranspiration, infiltration, soil store, percolation, groundwater, baseflow, overland flow, channel flow",
  alt="Cutaway hillslope showing rain, interception, evaporation, infiltration, groundwater, baseflow and overland flow to a river.",
  cap="Every arrow is a flux the model tracks, and the ledger must balance."),
 C=dict(
  left="A forested catchment under an extreme multi-day storm, the river beside it calm and well within its banks, a shield icon over the forest.",
  right="The same forested catchment under the same extreme storm with saturated soils: the river is in flood and spilling over its banks, though a faint ghost line shows the flood would have been even higher without the forest.",
  labels="Left: forests stop floods. Right: forests damp moderate floods; extreme storms on wet soil still flood",
  alt="Two panels: a forested catchment drawn as flood-proof, and in reality still flooding under an extreme storm, though less than if cleared.",
  cap="Forest buys storage, and storage fills. In the biggest storms it helps, but it cannot stop the flood."),
),
dict(k='calib', m='10', name='Calibration Arena',
 A=dict(
  subject="A hydrologist, seen from behind and small, standing on the bank at a river gauging station at dusk with a rugged laptop open on a field case, comparing a screen showing two overlapping hydrograph curves (no readable text) with the river flowing in front. A staff gauge in the river, a cableway above, warm last light on the water.",
  alt="A hydrologist at a river gauging station at dusk comparing two hydrograph curves on a laptop.",
  cap="A model earns trust by matching the river, and by showing how many other models match it just as well."),
 B=dict(
  subject="A three-dimensional landscape illustration representing a model performance surface: a smooth terrain in graded blues with a long, narrow, curving bright ridge running diagonally across it instead of a single peak. Several small glowing dots sit at different positions along the ridge top, each representing a different parameter set with an almost equal score. Faint contour lines on the terrain.",
  labels="Parameter 1, parameter 2, score (NSE or KGE), the ridge of equally good parameter sets",
  alt="A 3D performance surface with a long bright ridge instead of a single peak, and several dots along the ridge.",
  cap="The best score is not a summit, it is a ridge. Many parameter sets fit almost equally well."),
 C=dict(
  left="A single winning parameter set shown as one gold trophy on a podium, with one model diagram above it, presented as the catchment's true values.",
  right="Five quite different model diagrams (different store sizes and arrow thicknesses) side by side, each producing a near-identical hydrograph curve that overlaps the observed one.",
  labels="Left: calibration finds the true parameters. Right: equifinality, many different models fit equally well",
  alt="Two panels: one trophy-winning parameter set, and five different models all producing the same good hydrograph.",
  cap="A calibrated parameter set is one plausible explanation, not the catchment's truth."),
),
]
