# 1-phase-1: Schrödinger dynamics as shell rotation, with the Carrier's quarter-turn

Single-file interactive visualisation: `index.html`. No dependencies.
External verification: `verify-233.js` (82 instance checks) and
`verify-f13.js` (25 dynamics checks), both node, all passing. The
instance is the minimal non-trivial pair (13, 233): Subject F13
(kappa = 3), Carrier F233 (S = 58), fold per 00:F4.

## What it shows

Left, the shell: the F13 arithmetic symmetry sphere with the
Subject/Carrier view toggle and the register comb on the frame's
prime great circle. Subject view: the frame stands and the residues
evolve x -> gx, one quarter of phase and one rung of tint per
chronon. Carrier view: the residues stand at their chart cells, the
frame walks, and the whole shell drifts one Carrier tick-angle per
chronon.

Right, the phase: the C232 chart of the Carrier with its cardinals
{1, h, -1, hbar}, the shell's L1 time latitude as the middle ring
carrying the time-domain phase comb, and the common C4 fold clock.
The views lock across both panels.

## The mechanism (00:C15, 00:C17, 00:C18; the physical face 00:Y2)

The two cycles share the C4 class quotient, and the registered state
is the pair of cycle positions, each a residue of its own shell. The
bridge between the shells is the quadratic extension: the coefficient
plane K = F169 of the zonal theorem [2], counted by the Carrier. The
octant is the homomorphic bridge between the plane's units and the
Carrier's, gcd(168, 232) = 8: an octant-equivariant counting
transports the flip exactly, the image and the remaining 64 cells
each closed under the flip, the remainder eight full octant fibres --
in general 8(S/2 - kappa(2 kappa + 1)) cells, whole fibres always.

The Carrier evolves in itself over its complete period. Each quarter
(58 ticks) multiplies the chart by 78^58 = h with h^2 = -1: the
Fourier flip of the plane, position and momentum exchanging roles.
The four cardinals of the C232 ring are the quarter operators
{1, h, -1, hbar}; the flip's chirality is the C14 bit,
Subject-selected: the odd-member rule gives h = 89 as it gives i = 5
on the shell, and the gauge bit k_B c = h concurs. The orientation is
orbit-relative, on both sides.

Against this the Subject's orbit precesses: 12 ticks per orbit
against the 58-tick quarter, 6/29 of a quarter per revolution -- the
apsidal fraction is the winding ratio kappa/S, the mass-ratio reading
of D2 (00:C18). The frame returns to minus itself at the pair event
(home, 116), the chart reading dlog(-1), the Carrier's own -1
carrying the spinor sign, and closes at (home, home), the pair space
exhausted between closures (00:F2): the double cover as event
structure within the totality. The standing conjecture (00:Y2): this
precession is the face of gravitational apsidal advance (00:E4),
Mercury to the S2 star; at kappa = 3 the rate is the Schwarzschild
leading form for an orbit of semi-latus rectum S gravitational radii.

## The display

Both views step whole chronons: exact states only. In the Carrier
view both panels carry the precessing q/p axes dial (one tick-angle
per chronon, quarter and perihelion counters), and the shell draws
the q/p reference basis in the comb's transverse plane at the unit
cell: the phase arrow jumps its registered quarter while the
reference precesses. The Subject ring and sphere drift one
tick-angle per chronon against the fixed cardinals, dual to the
Carrier chart's one-tick slide in the Subject view; the quarter takes
exactly S chronons, q standing where p stood at tau = 58, the chart
closing at Omega - 1 = 232. The frame ray moves at the composed rate
1/12 + 1/232 with coprime numerator kappa + S = 61, home exactly at
(home, home) and antipodal at (home, 116), prograde like the
astronomical advance. The controls carry the pair (shell a/12,
Carrier b/232), the perihelion tick, and the pair-derived sheet sign.

## Verification

verify-233.js: the admissibility predicate and the full (169, 233)
scan; the bit-verified register with the gauge bit; the declared
chart and its orientation; the octant; the transport and the
pair-space walk; the F4 fold on both shells; the comb, tint and
operator laws; the sibling-page end-to-end comparison; the
quarter-turn mechanism and the precession events; the perihelion
trace and the cardinal drift; the composed frame-ray rate; the
octant bridge with the explicit plane construction and the remainder
fibres; the chirality selection; the pair-native state (CRT rebuild,
pair-derived sheet, the winding-ratio theorem with the trivial-pair
concurrence). verify-f13.js: the frame congruences, the sphere node
rule, the rotation and re-registration laws, the zonal theorem,
dispersion and isotropy, and the order-13 Cayley example as full
matrix arithmetic over F169 with exact unitarity.

## References

[1] Relativistic Algebra over Finite Ring Continuum, Axioms 2025, 14, 636.
[2] Schroedinger and Dirac Dynamics over Finite Substrate, pp202510.1486.
[3] Quantum Observation over Finite Relational Substrate, pp202606.1160.
[4] https://github.com/gamayos/frc-numerics/tree/main/docs/1-phase-1
