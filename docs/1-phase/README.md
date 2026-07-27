# 5-phase: Schrödinger dynamics as finite arithmetic symmetry shell rotation

Single-file interactive visualisation: `index.html`. No dependencies.
External verification: `verify-233.js` (64 instance checks, including an
end-to-end comparison against the sibling `index.html` — repository
consistency; the live deployment is compared by diff outside the script)
and `verify-f13.js` (25 dynamics checks), both node, all passing. The
deployed page and the full scripts live in the numeric validation
suite [4].

The state is an instantaneous, space-like object: the residue vector of
the frame's prime great circle, displayed as the comb on the shell — the
active register R_tau, whose passive dual through the inverse table is
the coefficient wavefunction [1, 2]. The instance is the minimal
non-trivial pair (13, 233).

## Revisions in 5-phase

This episode revises 4-phase in response to an independent external
evaluation. Every adopted finding was re-verified by exact arithmetic.

- The fold notation is corrected. The page wrote x = i^r g^s with
  g = 2; with r = dlog(x) mod 4 and s = dlog(x) mod 3 this fails at
  eight of the twelve exponents. The CRT fold is x = i^r 3^s with
  3 = g^4 the rung base, and the page now says so everywhere. The
  division form (remainders g^s, s < 3) is a distinct, also-exact
  naming and is verified separately.
- The animated operator is stated exactly. One step is the basis-label
  permutation P2|a> = |2a>: unitary, order 12, origin fixed; in
  component form the drive pullback (P2 psi)(a) = psi(2^{-1} a), the
  operator D of the zonal theorem [2]. The scalar reading 2I is not
  the operator content: the register vector is isotropic (sum of
  a^2 = 0 mod 13, the zonal theorem's own isotropy of the winding
  lines), and unitarity is carried by the permutation. The free
  evolution is not a Cayley step of any Hamiltonian with
  Frobenius-fixed spectrum [2]; the interacting Cayley sector
  U = (I - wH)^{-1}(I + wH) is machine-verified off-screen (exact
  unitarity, order 13) and enters the display with the Object.
- The mode statement is sharpened. No Object mode winding is present;
  the fixed shell winding numbers kappa = 3 and S = 58 remain. Read as
  a K-valued function the comb is g^tau chi_1: the identity register
  is the shell's fundamental character, and Object modes are k != 1
  selections read against it.
- The transport is stated as a quotient [3]. F13 is not inside F233
  and C12 is not a subgroup of C232: the two phase charts register
  through the one common C4 class quotient (gcd(12, 232) = 4), with
  shell-specific lifts: the Subject lifts all four classes in its Q4,
  the sign-blind Carrier core lifts the even classes only and the
  octant supplies the odd pair. The joint registration recurrence
  (00:F2) is the fibre product C696 = C12 x_{C4} C232: the trajectory
  tau -> (tau mod 12, tau mod 232) visits every class-compatible pair
  exactly once, verified.
- The admissibility predicate is strengthened. The octant completion
  needs S = 2 (mod 4): the octant sits at chart exponent S/2, odd
  precisely then. S even alone admits Omega = 257 (S = 64), whose
  octant sits in the even classes; the guard is a verifier check. The
  full predicate is S = 2 (mod 4), S = 1 (mod 3), Omega = 5 (mod 12),
  p^2 < Omega, jointly Omega = 41 (mod 48). The scan of (169, 233) is
  unchanged and (13, 233) stays jointly minimal.
- The verification layer is repaired. The core Q4 check is now a real
  computation (it was a stated constant). verify-f13.js is ported to
  the current Carrier (233, 58); it carried the former pair (173, 43).
  A new end-to-end section reads index.html and compares the deployed
  ORB, INV, WCLS, WRNG tables, the register labels, the fold notation,
  and the episode self-label against recomputation, so the page and
  the verifiers can no longer agree by duplication.
- The clock is wall-time exact. The tick rate is speed/5 steps per
  second on every display, independent of the refresh rate; throttled
  tabs resume without a step burst. The states remain discrete.
- Accessibility: the canvases carry descriptions, the view buttons
  carry pressed-state semantics, and the caption bands use the
  higher-contrast ink.

One recommendation of the evaluation is declined, with the reason on
the page: the suggestion to retitle away from Schrödinger dynamics
identifies the Schrödinger propagator with the Cayley step. That
inverts the manuscript's own structure [2]: the zonal theorem is
titled "the free evolution is the drive", the sector corollary proves
the free evolution is not a Cayley step, and the shell reading tags
Schrödinger dynamics as the exact zonal evolution. The evaluation's
own repair, the permutation P2, is component-for-component the drive
pullback D, so the animated rotation is the manuscript's free
Schrödinger operator acting on basis labels.

## The instance: (13, 233), jointly minimal

- Subject F13 with frame (tau; 0, 1, 2): kappa = 3, i = -g^3 = 5,
  pi = 6, e = 6, Q4 = {1, 5, 12, 8} [1]. Minimal in its slot:
  kappa = 1 gives p = 5, its own Q4 core; kappa = 2 gives 9,
  composite; kappa = 3 gives 13, prime.
- Carrier F233, S = 58, the first complete configuration above
  p^2 = 169: S = 2 (mod 4), S = 1 (mod 3), Omega = 5 (mod 12),
  p^2 < Omega; jointly Omega = 41 (mod 48). The scan of (169, 233)
  leaves nothing: 173 and 181 fail S even (43, 45), 193 fails
  S = 1 (mod 3) (48), 197 and 229 fail S even (49, 57).
- The complete register, bit-verified [1]: G = 116, c = 74 (c^2 =
  117 = 2S+1 = 2^{-1}), hbar = 144 = 2*72 (72^2 = 58), h = 89 =
  -hbar, k_B = 124 (k_B^2 = 231), with the one gauge bit selecting
  c = 74 through k_B c = h. S even puts Omega = 1 (mod 8), so the
  octant exists: zeta_8 = 97, zeta_8^2 = h.
- The Carrier is a timeless torsor: no generator, no origin [1]. The
  ring display uses the Subject's declared chart (78 = 3^{-1}, the
  reframing gauge), under which hbar sits at the top cardinal and the
  registration sweeps one tick per chronon, clockwise.

## The wavefunction comb

The wavefunction is space-like: an instantaneous configuration, not a
history. Its seat is the frame's prime great circle, the additive line
through the Observer: thirteen cells, the fixed 0 at the pole and the
twelve units. The state at chronon tau is the whole residue vector

    psi_tau(a) = a * g^tau,   a in F13,

not any single component of it. The drive multiplies every component
at once: psi_{tau+1} = g * psi_tau, the zonal theorem of [2] read on
the full circle instead of one orbit point.

The display: the comb on the shell, integrated in the left view. Each
cell of the great circle carries the 4-state phase vector i^r of its
registered residue, r = dlog(x) mod 4 in the F4 fold x = i^r 3^s [1].
The arrow is orthogonal to the meridian fiber: the phase is a fiber
datum and carries no component along the space-like base. The
transverse plane is spanned by the surface radial (the real axis) and
the latitude tangent (the imaginary axis; zonal, because i = g^9 acts
as the drive quarter along the latitudes [2]). The four states: radial
out (1), zonal counterclockwise (i), radial in (-1), zonal clockwise
(-i). The tint completes the registration: each arrow is coloured by
its rung s = dlog(x) mod 3 in the three fibre colours of the phase
panel, and since (r, s) determines the residue, direction and tint
together display the complete value of every cell. The pole cell holds
0, ringed gold, no arrow: the origin has no fiber plane; its fixedness
and its phaselessness are one fact.

The exact laws of the comb, all verified: the class profile
0,1,0,2,1,1,3,3,0,2,3,2 with three cells per class; the rung profile
0,1,1,2,0,2,2,0,2,1,1,0 with four cells per rung and the twelve (r, s)
pairs distinct; the rigid turn r(a g^tau) = r(a) + tau (the global
phase, one quarter on every arrow per chronon); the rate law (kappa =
3 fiber turns per shell period against one frame turn: mass as the
winding rate); the antipode law r(-a) = r(a) + 2 (the fiber half-turn:
zonal states parallel, radial states mirrored); and space-like
completeness (the instantaneous slice holds all thirteen residues at
every tau).

## The panels

Left, the shell: the F13 arithmetic symmetry sphere of [2], Figure 1,
with the Subject/Carrier view toggle and the register comb on the
frame's prime great circle. Subject view (default): the frame stands,
the residues evolve x -> gx, the comb standing with the frame. Carrier
view: the residues stand, the frame turns clockwise, one step per
chronon, the comb riding it. M0 blue, M_kappa red, L1 green, L4
purple. Exact states only, no interpolation.

Right, the phase on the F4 fold, per 00:F4 [1]: the common C4 fold
clock (the class r = tau mod 4, one class for both shells, lifts
shell-specific); the middle ring, the shell's L1 time latitude exactly
as drawn in green on the sphere and view-synced with it (Carrier view:
the charts stand, the frame rays and registration dots turn; Subject
view: the frame stands, every latitude cell re-registers by g per
chronon and the C232 chart turns one tick per chronon under the fixed
registration; the gold-ringed cell holds the pullback name
1 = g^{-tau}; the cells carry the time-domain phase comb, the same
i^r arrows and rung tints as the sphere's space-like comb with the
ring's radial as the real axis and the zonal tangent as the imaginary,
every arrow turning one quarter counterclockwise per chronon in the
Subject view); the Subject's product fold 2 = i * 3
with the fold hand walking i^tau = 1, 5, 12, 8 on whichever cell now
holds it; the Carrier's sign-blind classes with the octant
zeta_8 = 97 carrying the odd classes; and mass as the winding rate,
kappa = 3 vs S = 58 windings per own period.

Both panels carry the same Subject/Carrier button pair and share one
view state: either toggle switches both, so the frame data (rays,
registration dots) and the two charts stay in exact correspondence
across the sphere and the rings.

## Time

The chronon tau is a cycle position: the shell returns every 12, the
Carrier every 232, and the joint registration recurrence (00:F2) is
the fibre product C696 = C12 x_{C4} C232, where the counter wraps;
it is bookkeeping of the Subject's registration, internal to neither
shell. The transport
invariant is S = 2 (mod 4) [3]. The display never interpolates: every
frame drawn is an exact state, stepped on the wall clock.

## Honesty constraints

No Object, no mode winding, no Born claims: the winding ladder, the
plane waves, and the dispersion enter the series when an Object
contributes a k != 1 selection. The exact claims here are the
rotation, the fold, the comb laws, the fold-table laws, the operator
statement (P2 = the drive pullback), the unitarity, and the periods.
Probability enters the series later, through registration counting [3].

## Revisions after review 2 (27 July 2026)

Review 2 (`reviews/98-lab-1-phase-20260726-2.pdf`) raised the episode
to 7/10, withdrew its earlier Cayley-propagator objection via the
8-dirac zonal theorem, and concentrated the remainder in one exact
distinction. All adopted findings executed and re-verified:

- The register/coefficient split is stated exactly. The comb is the
  active register R_tau(a) = a g^tau, evolving by D^{-1}; the
  coefficient wavefunction Psi_tau = D^tau Psi_0 is its passive dual
  through the inverse table, and the word wavefunction now refers to
  the coefficient side alone. The state paragraph cites 00:C1 for the
  register section and 00:F4 for the coefficient fold, and states the
  zero extension (origin summand fixed, D on the units).
- The verifier regression is closed: the self-label check reads the
  stable marker `data-episode="1-phase" data-rev="5"`, not the mutable
  title; the end-to-end section is worded as repository consistency,
  deployment compared by diff outside the script.
- Three checks added (60 -> 63): the D^{-1} composition identity with
  the one-cell witness (comb 1 -> 2 vs (D chi_1)(1) = 7); the trivial
  pair (5, 41), admissible in full while F_5 is its own fold, naming
  (13, 233) the minimal non-trivial pair; the Carrier core's even-only
  chart classes {0, 2, 0, 2} (mod 4) with the odd octant exponent 29.
- Exact wording: common C4 fold clock with shell-specific lifts
  (Subject full Q4; Carrier even classes, octant odd); C696 is the
  joint registration recurrence (00:F2), bookkeeping internal to
  neither shell; Cayley kinetic sector replaces interacting sector;
  norm preservation on the single register vector stated as
  nondiagnostic, unitarity carried by the permutation; the badge
  carries the ledger-status legend (exact counts vs row-cited
  identifications D2, 00:F4, 00:B7).
- One stale comment fixed: the Subject-view label reads m + tau,
  matching the code.

## Verification

verify-233.js (64 checks): the minimal non-trivial pair with the full
scan and the strengthened predicate (S = 2 (mod 4), the Omega = 257
guard, Omega = 41 (mod 48)); the bit-verified register with the gauge bit and
the real core-Q4 computation; the Subject's declared chart and its
orientation; the octant; the transport; the F4 fold (the product on
F13, division-unique naming on both shells, no product on F233, octant
completion, sign-blindness); the winding rates; the fold-table laws;
the comb laws; the tint laws; the operator section (P2 bijection and
order, register-vector isotropy, the zonal eigenrelation D chi_k =
g^{-k} chi_k for all windings, and the animated step as D^{-1} on the
comb); the fibre-product recurrence; the review-2 residuals (the D^{-1}
composition identity, the trivial pair (5, 41), the octant lift
classes); and the end-to-end sibling-file comparison against
index.html (repository consistency).
verify-f13.js (25 checks, on the current pair 233/58): the frame
congruences, the sphere node rule, the rotation and re-registration
laws, the zonal theorem, dispersion and isotropy, nu = g = 2,
|N^1| = 14, alpha_fwd = 4w, and the order-13 Cayley example as full
matrix arithmetic over F169 with exact unitarity.

## References

[1] Akhtman, Y. Relativistic Algebra over Finite Ring Continuum.
    Axioms 2025, 14, 636.
    https://doi.org/10.3390/axioms14080636
[2] Akhtman, Y. Schrödinger and Dirac Dynamics over Finite Substrate.
    Preprints 2025, 2025101486.
    https://doi.org/10.20944/preprints202510.1486.v3
[3] Akhtman, Y.; Voether, E. Quantum Observation over Finite
    Relational Substrate. Preprints 2026, 2026061160.
    https://doi.org/10.20944/preprints202606.1160.v2
[4] Akhtman, Y. FRC Numerics: the numeric validation suite. GitHub.
    https://github.com/gamayos/frc-numerics/tree/main/docs/1-phase
