# 1-phase-4: Schrodinger dynamics with the frame dilation

Single-file interactive visualisation: `index.html`. No dependencies.
External verification: `verify-233.js` (82 checks: the pair dynamics,
the events, the oriented octant bridge, the precession theorem),
`verify-sky.js` (27 checks: the sky map, the fibered covers, the
radial ladder with the tau+2 completion as sets), `verify-space.js`
(23 checks: the register, the cone arithmetic, the PGL2/SL2 frame
counts), `verify-hopf.js` (9 checks: the finite Hopf fibration -- the free
boost action, the unique factorization, the global section, the
horizon-circle fiber coordinate, at p = 13 and Omega-blind at p = 5,
with the SL2 spin contrast), and `verify-render.js` (16 checks: the
production rendering itself -- the pair sweep over both sky
representations, the caption-free canvases, the label laws, the
double-cover closures in the Carrier view, the drive-hiding of the
Subject view, the wrap continuity in both views, the Hopf lighting
laws, the primitive-arc fiber rendering, the section test: nodes
and labels identical across the toggle, the single-stroke helix
guide loops, the frame leak: standing Carrier chart, the
quarter turn in S chronons, the q hand riding to h, the
one drive sense across the panels: the Carrier-view sky steps
clockwise with the drive, as the shell and the chart, and the
interpolated mode: exact endpoints, +1 quarter class per chronon,
on-tick data, and the frame dilation in the sheet-fair chart:
bead-on-fiber at every phase, the congruent parity image wF = -w
at the half, the dual's radial band at the quarter, home at the
cycle, the ensemble breathing without collapse, the Subject view
unflowed);
node, all passing, all integer arithmetic in the exact suites. The screen projection is
a labelled chart approximation; every state shown is exact and
discrete. The instance is the minimal non-trivial pair (13, 233),
kappa = 3, Objectless.

## What it shows

The drive x -> gx as the shell's exact unitary evolution -- the
Schrodinger evolution of the windings [3], with its unitary and
spinor structure from [2] -- read through three complementary
square panels of one state, at one scale, under one Subject/Carrier
toggle:

The symmetry shell: the F13 arithmetic symmetry sphere -- meridians,
latitudes, the rotating frame, and the register comb on the frame's
great circle, each cell showing its whole value through the phase
arrow i^r and the rung tint s.

The phase chart: the Carrier ring of 232 ticks, the standing
backdrop of both views; the L1 time latitude with the time-domain
comb, and the shared fold clock r = tau mod 4 with the unit's
lift as its hand; the Subject ring precessing with the Carrier
count under the q/p dial -- the frame leak (00:C17, 00:C18).

The sky: kappa = 3 nested fibers on the radial ladder at the axial
radii R sin(2a pi/p), the Observer at the center; each shell the
complete double-helix fiber -- twelve cells by two routes on one
smooth closed loop through both poles, the sign of -1 distributed
over the orbit; consecutive fibers one rung apart, x3 = g^4, mounted
120 degrees apart about the main axis; 3 x 48 + 12 = 156 = p(p-1),
the totality of the observable (00:Y3).

## The Hopf representation (00:C19, 00:Y3, 00:Y4)

The sky panel carries a representation toggle: Double helix / Hopf
fibers. The two representations share one sky: the same node
computation, the same marks, the same labels -- the toggle switches
the fibers and only the fibers. The helix mode draws the drive
orbits (the time factor); the Hopf mode draws the fiber orbits (the
boost factor) as a global structure. The chart: the guard
projection (center at w0 = 1.1 outside S3) maps the whole S3 onto
the ball whose silhouette is the horizon sphere, so the sky ball is
a chart of the whole S3 (00:Y4). The chart is two-sheeted -- the
ray through a sky point meets S3 twice -- and the node's spinor
sheet selects the preimage. Each node lifts to its S3 preimage and
carries the exact Hopf circle through it, the leaf of the global
foliation e^{it}(z1, z2), projected back as one closed curve
through the node, node-on-fiber exact. The lift rides the far sheet
-- one fixed chart convention, so the foliation's axial symmetry
makes the leaves rotate rigidly with the nodes (coherence residual
1e-15). The rung ladder is the foliation depth: the three copies of
one event lift to three nested leaves, the inner rung riding the
horizon-circle level (|z2| = 0.14 at the equator), the mid rung at
0.69, the outer rung deep at 0.86 -- the radial ladder of the sky
read as the depth of the S3 foliation, the holographic statement of
00:Y4 made visible. The fiber layer is kept bare and rides the
helix guide style at half strength (the leaves are denser than the
loops): guide grey #8a877f, each leaf split at the two antipodal
roots of its homogeneous depth numerator into one front arc (alpha
0.35) and one back arc (0.12), both primitive elliptical arcs; the
node is the leaf's only marked point (the section point),
identity stays on the node layer. Shown are the 24 outer-rung
leaves, the inner-rung leaves hidden behind the SHOW_INNER flag.
A per-fiber color coding, if ever wanted, keys on the address: the
two routes of one cell share a hue -- the echo pair (00:C7) -- as
a selective-highlight mode, not a full palette. The nodes are the section of the finite fibration PGL2/C14
(00:C19); motion along a fiber is a boost, it changes the observer,
and is unobservable -- observation is the Hopf section (00:Y3). The
13 marks on the outer fibers are the C14 boost points, the node the
fourteenth: the fiber coordinate t -> t(infinity), the cells plus
infinity. The observer lifts to the pole (0, +-i), the degenerate
leaf: the clock fiber (tau, 0) is the polar axis segment, the
stabilizer, the pure drive. The screen map per leaf is projective
in the circle parameter, so every leaf is an exact ellipse, in
closed form from the conic C = M^-T diag(1,1,-1) M^-1 and drawn as
primitive elliptical arcs: 48 strokes per frame (front and back per
leaf), no fiber polylines, node-on-ellipse to 1e-6 px over the full
state sweep. The
section test in verify-render.js renders a paused state in both
representations and checks every node dot and every label
identical; the combinatorics is carried by verify-hopf.js. The
guard chart is the labelled approximation; the silhouette radius
206 clears the outer shell (node radius 200.5) with margin.

## The frame dilation (00:Y5)

The leak per chronon is an element of the frame group, and by C19
it factors uniquely into a Borel part and a boost part. The Borel
part is the azimuthal drift the panels already draw. The boost part
is motion along the Hopf fiber -- unobservable to the Subject
(00:Y3), so absent from the Subject view and resolved only by the
harness: the frame dilation, the mass phase of 00:Y5. The rate is
forced by the dial: the flip is x h per Carrier quarter, so the
flow runs at the dial's full tick-angle per chronon, prograde, phi
= -(bC + F) pi/116, interpolation-ready and closing exactly at the
Carrier wrap with no sheet bit. The realisation is the pure fiber
flow rendered in the sheet-fair chart: each point projects from
the guard on its own side of S3 (denominator W0 - |q4|), so the
antipodal map is the ball's exact point reflection and no chart
constant enters any station. Every bead rides its own leaf at
every phase -- bead-on-fiber always -- and the helix guide loops
flow pointwise into smooth screwed curves, the pole crossings
passing the center along the observer's axis leaf, as they must.
Stations, exact and gauge-free: at the Carrier quarter the sharp
shell disperses into a radial band, the Fourier dual's spread
(the dual has the units of the inverse: localized to dispersed);
at the half the pattern reassembles as the congruent parity image,
wF = -w exactly at full scale; home with the Carrier cycle, the
pattern with the pair at 696. The chart radius along a leaf is
bounded below by the flow-invariant |z1|, so the ensemble breathes
and never collapses. The leaves keep the established closed-ellipse
rendering at the release density in both views. Each event's drawn
fiber is the foliation leaf through its CURRENT bead (the ball
carries the standing chart foliation; re-lifting the flowed
position selects the leaf): the nodes precess along the fibers at
machine precision through the whole cycle, and the fiber family
precesses with them -- at the half the entire fibration stands as
its congruent parity image. The mid-sphere (the q4 = 0 great
sphere, chart radius S3H/W0) is the seam where the atlas's two
projective charts glue, C0 but not C1, so flowed curves bend
exactly there -- the declared signature of the two-chart atlas,
kept in preference to a smoothing gauge that would cost the
conic-exact rendering; the seam is left undrawn.
The visibility profiles follow the flowed positions, in sync with
the guide loops' front/back passes. The clock bead rides
the axis leaf: the Subject's own dilation. The rung-ladder
exchange stays as the discrete arithmetic face of the same
inversion; with the exact per-tick boost step (which C14 element,
via the octant bridge) it is the open derivation that would also
promote 00:Y5.

## Interpolated mode

The control card carries an Interpolated switch, on by default. It
smooths all chart motion between chronons by the sub-chronon
fraction: the drive sweep, the leak drifts, the chart turn, the
hand, the fold clock, the pullback ring, the dial, the sky's drive
and drift, and every phase arrow, which rotates exactly one quarter
per chronon (dlog + 1) and so lands on the next quarter at the
tick. Every angle advances by a constant per-chronon step, so the
interpolation is exact at both endpoints; the smoothing is a chart
convention [approx]. All data stays on the tick: values, labels,
rank tints, and cardinal marks switch only at integer chronons,
riding the interpolated guides. Two exclusions follow from the
data/geometry split: the phase comb's arrows stand in the Carrier
view (the residues stand, so there is nothing to interpolate), and
the Subject view's C232 chart turn steps on the tick (the ring is
232-fold self-similar, so the one-tick turn maps its marks onto
themselves and interpolating it would only wobble). Off restores
exact tick-stepping.

## Layout

The three panels are exactly square, at the same principal-circle
scale (R = 202 of 520), and hold visuals only: all captions sit
under the panels. The control card -- with the unified view toggle
-- sits above the panels so it stays reachable in the portrait mode,
where the panels stack vertically; in landscape they span the full
width.

## Revision 2 (review-1)

The octant bridge is oriented by the corpus rule: dlog(3w) = 105 = 1
(mod 8), whence i = gen^42 = 5 and c(iu) = h c(u) with the half-lift
carrying one octant step. The totality decomposition completes over
{tau, tau+2}, checked as disjoint sets with full union; the 48 per
shell counts the 24 simultaneous images with their two spinor lifts.
The two covers share exactly the one sign, gcd(24, 26) = 2, fibered
product 24 x 26 / 2 = 2 x 156. The observable frame group is
PGL2(F13): its Borel is the affine group AGL(1, 13) of 156 cells,
its nonsplit C14 acts regularly on the fourteen points of P1, 2184 =
156 x 14 stabilizer times transversal; SL2 is the spin double cover.
The sky's leak drift is a half-angle on the Carrier's spinor
cover (C464 inside F_233^2, 464 | 54288): the sheet sigC flips at
the Carrier wrap, the drift steps uniformly through it, and the
sky closes with the pair's spinor recurrence, 2 x 696.

## The frame leak (00:C17, 00:C18)

No Subject is an ideal of the Carrier: a field has no proper
ideals, so the Subject's register never closes inside F_233 and
the Carrier's count passes through it -- every observer inherits
the Carrier clock, every frame is mortal. The panels draw the
consequence. One relative winding, one tick-angle per chronon, and
each view holds its own frame. Subject view: the register and the
sky stand (the sky is register-anchored: both azimuth components
are register data; the drive is hidden by re-registration; the
whole geometry is static and only the values walk), while the
Carrier's chart {1, hbar, -1, h} turns counterclockwise under them
(hbar = 144 the i-oriented quarter and h = 89 the (-i)-oriented,
per the standing audit). Carrier view: the quarters stand (hbar on
top), the drive turns the frame ray and the sky, and the register
drifts clockwise past them, prograde -- the sky at the half rate on
the spinor cover (the sheet sigC carrying continuity through the
Carrier wrap, closure at the spinor recurrence 2 x 696). The q/p
dial is one instrument, identical in both views: it reports q's
Carrier address -- a relational datum of the pair -- turning
clockwise one tick-angle per chronon, the address flipping x h per
quarter: q lands on the h cardinal at tau = S = 58. The
frame returns at 232 but the pair phase does not: closure only at
696, spinor 2 x 696; at cosmological S the recurrence is beyond
every Subject year and the dephasing is monotone -- C18's winding
read as the arrow of time.

## Provenance

1-phase-4 extends the stable episode 1-phase-3 (kept frozen as the
stable release) with the frame dilation: the Hopf flow of the node
layer and the helix guides in the Carrier view, the leaf-riding
beads, and the clock bead. 1-phase-3 in turn extends 1-phase-2
(frozen) with the Hopf representation toggle, the frame-leak view
semantics, and the interpolated mode; the shell and phase panels
derive from the standing episode 1-phase-1 (review-2 line), the
sky panel from the standing episode 1-space (rev 18). All source
episodes remain frozen; the doctrine sections below the panels
carry their standing constructive descriptions.

## References

[1] Akhtman, Y. Relativistic Algebra over Finite Ring Continuum. Axioms 2025, 14, 636.
[2] Schroedinger and Dirac Dynamics over Finite Substrate, pp202510.1486.
[3] Quantum Observation over Finite Relational Substrate, pp202606.1160.
[4] Gravitation as Phase Synchronisation over a Finite Relational Substrate, pp202606.1018.
[5] https://github.com/gamayos/frc-numerics/tree/main/docs/1-phase-4
