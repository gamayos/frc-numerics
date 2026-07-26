# 3-phase: Schrodinger dynamics is rotation (the minimal complete pair)

Single-file interactive visualisation: `index.html`. No dependencies.
External verification: `verify-233.js` (28 instance checks) and
`verify-f13.js` (25 dynamics checks), both node, all passing.

The emergence of the phase itself: Subject and Carrier only, no Object.
The dynamics is the zonal theorem of 8-dirac (the free evolution is the
drive); the phase is the fold class on the shared Q4 core (00:F4).

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

## The panels

Left, the shell (unchanged from the (13, 173) build): the F13 arithmetic
symmetry sphere of 8-dirac Figure 1, with the Carrier/Subject view
toggle. Carrier view: the residues stand, the frame turns clockwise, one
step per chronon. Subject view: the frame stands, the residues evolve
x -> gx, slot (m, a) reading a * g^{m + tau}. M0 blue, M_kappa red, L1
green, L4 = L_{kappa+1} purple. Exact states only, no interpolation.

Right, the phase, per 00:F4. Every cycle position folds as
x = i^r * g^s: the class r is the registrable phase, the rung s the
outcome index, and observation resolves cosets, never points within one.

- The shared Q4 clock at the centre: the class r = tau mod 4, one
  quarter per chronon, one clock for both shells.
- The Subject (kappa = 3 odd) folds as a true product: the drive step
  itself factors, 2 = i * 3, one oriented quarter-turn times one rung
  per chronon. The fold hand lifts the class to the exact core residue
  i^tau, walking 1, 5, 12, 8. The twelve nodes are tinted by fibre (the
  three cosets of Q4) and the current fibre alpha = tau mod 3 is lit.
- The Carrier (S = 58 even) has no product: the core is not a direct
  factor, the crossing classes of the core are even only (1, -1 in class
  0; hbar and h together in class 2), so the quotient chart is
  sign-blind, and the octant zeta_8 = 97 carries the odd classes: the
  doctrinally general case, which is exactly what complete admissibility
  demands. The ring shows the 232 exact ticks, cardinals gold, the four
  odd-octant ticks purple, and the current crossing class combed
  brighter, rotating one tick per chronon.
- The drive positions survive only as dim dots: the point inside the
  coset, which observation never resolves.
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
the unitarity, and the periods.

## Verification

verify-233.js: the joint minimality (both slots, with the full scan),
the complete admissibility predicate, the bit-verified register with the
gauge bit, the chart orientation on g = 78, the octant, the transport,
the F4 fold (product on F13 with the drive-step factorisation; division-
unique on both shells; no product on F233 with the parity obstruction;
octant completion; sign-blindness), and the winding rates.
verify-f13.js: the frame congruences, the sphere node rule, the rotation
and re-registration laws, the zonal theorem, dispersion and isotropy,
nu = g = 2, |N^1| = 14, alpha_fwd = 4w, and the order-13 Cayley example
as full matrix arithmetic over F169 with exact unitarity.
