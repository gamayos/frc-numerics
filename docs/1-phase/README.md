# 4-phase: Schrödinger dynamics as finite arithmetic symmetry shell rotation

Single-file interactive visualisation: `index.html`. No dependencies.
External verification: `verify-233.js` (44 instance checks) and
`verify-f13.js` (25 dynamics checks), both node, all passing.

The correction over 3-phase: the state is not a point on the ring. The
wavefunction is an instantaneous, space-like object: the residue vector
of the frame's prime great circle, displayed as the comb on the
shell. The instance, the panels, and the fold doctrine carry over from
3-phase unchanged; what is new is the comb and its exact laws.

## The instance: (13, 233), jointly minimal

- Subject F13 with frame (tau; 0, 1, 2): kappa = 3, i = -g^3 = 5, pi = 6,
  e = 6, Q4 = {1, 5, 12, 8}. Minimal in its slot: kappa = 1 gives p = 5,
  which is its own Q4 core; kappa = 2 gives 9, composite; kappa = 3 gives
  13, prime.
- Carrier F233, S = 58, the first complete configuration above p^2 = 169:
  S even, S = 1 (mod 3), Omega = 5 (mod 12), p^2 < Omega. The scan of
  (169, 233) leaves nothing: 173 and 181 fail S even (43, 45), 193 fails
  S = 1 (mod 3) (48), 197 and 229 fail S even (49, 57).
- The complete register, bit-verified: G = 116, c = 74 (c^2 = 117 =
  2S+1 = 2^{-1}), hbar = 144 = 2*72 (72^2 = 58), h = 89 = -hbar,
  k_B = 124 (k_B^2 = 231), with the one gauge bit selecting c = 74
  through k_B c = h (the branch -c = 159 would give k_B(-c) = hbar).
  S even puts Omega = 1 (mod 8), so the octant exists: zeta_8 = 97,
  zeta_8^2 = h.
- Declared Carrier chart g = 78 = 3^{-1} (the reframing gauge), under
  which hbar = g^{-S} = g^174 and the drive runs clockwise with hbar at
  the top cardinal.

## The wavefunction comb (the content of this episode)

The wavefunction is space-like: an instantaneous configuration, not a
history. Its seat is the frame's prime great circle, the additive line
through the Observer: thirteen cells, the fixed 0 at the pole and the
twelve units. The state at chronon tau is the whole residue vector

    psi_tau(a) = a * g^tau,   a in F13,

not any single component of it. The drive multiplies every component at
once: psi_{tau+1} = g * psi_tau, the zonal theorem of 8-dirac read on
the full circle instead of one orbit point.

The display: the comb on the shell, integrated in the left view.
Each cell of the great circle carries the 4-state phase vector i^r of
its registered residue, r = dlog(x) mod 4 in the F4 fold x = i^r * g^s.
The arrow is orthogonal to the meridian fiber. The phase is a fiber
datum: it displaces nothing along the space-like base, so the arrow
carries no component along the meridian. The transverse plane at each
cell is spanned by the two directions orthogonal to the fiber: the
surface radial and the latitude tangent (the zonal direction). The
imaginary axis is zonal, because the class is a shell operation:
i = g^9, nine drive steps, one counterclockwise quarter along the
latitudes. The real axis is the one direction orthogonal to both zonal
and meridional: the radial. The four states: radial out (1), zonal
counterclockwise (i), radial in (-1), zonal clockwise (-i). Drawn in
3D and projected through the same linear map as every node
(orthographic, so the direction is exact; foreshortening never reaches
zero). The tint completes the registration: each arrow is coloured by
its rung s = dlog(x) mod 3, in the three fibre colours of the phase
panel, and since (r, s) determines the residue, direction and tint
together display the complete value of every cell. The unit cell's
tint is the lit fibre alpha = tau mod 3. Per chronon the tint advances
one rung as the direction advances one quarter: the diagonal law,
visible on the comb itself. The pole cell holds 0, ringed gold, no arrow: the meridians
converge there and the latitude shrinks to a point, so the origin has
no fiber plane; its fixedness and its phaselessness are one fact. The
comb never hides: cells on the far side of the sphere draw dim.

The exact laws of the comb, all verified:

- The class profile. r(a) for a = 1..12 is 0,1,0,2,1,1,3,3,0,2,3,2, and
  the classes equipartition: exactly three cells per class.
- The rung profile. s(a) for a = 1..12 is 0,1,1,2,0,2,2,0,2,1,1,0, the
  rungs equipartition (four cells per rung), and the twelve (r, s)
  pairs are distinct: the arrow's direction and tint read the whole
  value.
- The rigid turn. r(a * g^tau) = r(a) + tau (mod 4): one drive step is
  a global phase, every arrow turns one quarter about its meridian
  fiber at once, i^tau on the whole comb. The comb corkscrews around
  the space-like circle: the transverse-wave picture of the continuum
  recovered exactly, Re radial, Im zonal.
- The rate law. Per chronon the comb makes a quarter fiber-turn while
  the frame sweeps 30 degrees about the polar axis. Over one shell
  period the frame makes one turn and the comb makes kappa = 3: the
  winding rate, mass, visible as arrow speed.
- The antipode law. r(-a) = r(a) + 2: the fiber half-turn, -x = i^2 x.
  Opposite cells sit two quarters apart in their fiber planes; in
  ambient terms the zonal states land exactly parallel and the radial
  states are mirrored through the horizontal plane.
- Space-like completeness. At every tau the comb cells 0, a g^tau,
  -a g^tau register all thirteen residues exactly once: the
  instantaneous slice always holds the whole field.

In the Carrier view the comb rides the sweeping frame meridian over the
standing residues; in the Subject view it stands on the static meridian
while the residues evolve under it. One wavefunction, two charts.

The right panel is unchanged and re-scoped: its inner tags are the
fold-table occupancy on the exponent cycle, the time-like reading of
the same step (one depth per (r, s) cell, the diagonal law), and the
shared clock registers the comb's one transported datum, the class r.
The hand is the unit component's lift i^tau.

The vector is residue-valued: the registration layer. K-valued
amplitudes on these thirteen cells, and with them superposition and the
mode ladder, enter the series when an Object contributes a mode.

## The panels

Left, the shell: the F13 arithmetic symmetry sphere of 8-dirac Figure 1,
with the Carrier/Subject view toggle and now the wavefunction comb on
the frame's prime great circle. Carrier view: the residues stand, the
frame turns clockwise, one step per chronon, the comb riding it.
Subject view: the frame stands, the residues evolve x -> gx, slot
(m, a) reading a * g^{m + tau}, the comb standing with the frame.
M0 blue, M_kappa red, L1 green, L4 = L_{kappa+1} purple, the comb gold.
Exact states only, no interpolation.

Right, the phase on the F4 fold, per 00:F4, unchanged:

- The shared Q4 clock at the centre: the class r = tau mod 4, one
  quarter per chronon, one clock for both shells.
- The twelve depth tags inside the Subject ring: the fold-table
  occupancy, one depth per (r, s) cell, moving with the drive; the
  unit's tag ringed. The time-like reading of the same step.
- The Subject (kappa = 3 odd) folds as a true product: 2 = i * 3, one
  oriented quarter-turn times one rung per chronon. The fold hand lifts
  the unit component's class to the exact core residue i^tau, walking
  1, 5, 12, 8. The twelve nodes are tinted by fibre and the current
  fibre alpha = tau mod 3 is lit.
- The Carrier (S = 58 even) has no product: sign-blind crossing classes
  (1, -1 in class 0; hbar and h together in class 2), the octant
  zeta_8 = 97 carrying the odd classes. The ring shows the 232 exact
  ticks, cardinals gold, octant ticks purple, the current crossing class
  combed brighter, rotating one tick per chronon.
- Mass is the winding rate: per own period the phase winds the core
  kappa = 3 times (Subject) against S = 58 times (Carrier); per chronon
  both advance the one shared quarter, the [i hbar] composition.

## Time

The chronon tau is a cycle position: the shell returns every 12, the
Carrier every 232, the pair recurs at lcm(12, 232) = 696, where the
counter wraps. The transport invariant is S = 2 (mod 4). The display
never interpolates: every frame drawn is an exact state.

## Honesty constraints

No Object, no winding parameter, no Born claims: the mode spectrum, the
plane waves, and the dispersion enter the series when an Object
contributes a mode. The exact claims here are the rotation, the fold,
the comb laws (profile, equipartition, the rigid turn, the antipode,
completeness), the fold-table laws (occupancy, bijection, the
diagonal), the unitarity, and the periods.

## Verification

verify-233.js: the joint minimality (both slots, with the full scan),
the complete admissibility predicate, the bit-verified register with the
gauge bit, the chart orientation on g = 78, the octant, the transport,
the F4 fold (product on F13 with the drive-step factorisation; division-
unique on both shells; no product on F233 with the parity obstruction;
octant completion; sign-blindness), the winding rates, the fold-table
section (the dlog table, the occupancy law at every tau, the bijection
onto the twelve fold cells at every tau, the diagonal law, the fixed
origin), and the wavefunction-comb section (the class profile,
equipartition, the rigid turn at every tau, the antipode law,
space-like completeness at every tau, the zonal action i = g^9 with
9 = -3 (mod 12), the fiber half-turn at the antipode, and the tint
section: the rung profile, rung equipartition, and the distinctness of
the twelve (r, s) pairs).
verify-f13.js: the frame congruences, the sphere node rule, the rotation
and re-registration laws, the zonal theorem, dispersion and isotropy,
nu = g = 2, |N^1| = 14, alpha_fwd = 4w, and the order-13 Cayley example
as full matrix arithmetic over F169 with exact unitarity.
