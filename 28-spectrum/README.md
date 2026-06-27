# Validation suite — *The Fermion Spectrum over a Finite Substrate*

**Repository:** <https://github.com/gamayos/frc-numerics/tree/main/28-spectrum>

This folder holds the computational verification for *The Fermion Spectrum over a Finite Substrate* (`../main.tex`). The scripts are standalone, deterministic, take no input, and print a human-readable verdict with a pass count; each is cited inline at the claim it backs in the paper's reproducibility paragraph (§Predictions and reproducibility).

## Framed-rational discipline

Every script is classed by how its asserted checks are computed:

- **EXACT** — every asserted check is performed in integer, modular `𝔽_p`, `𝔽_{p²}`, or cyclotomic (`ℚ(ω,√2)`, `ℤ[ℤ/3×ℤ/p]`) arithmetic. No floating point enters an asserted claim, and nothing exceeds the totality `Ω`. These carry the load-bearing exact identities of the mass sector.
- **MIXED** — an exact framed-rational core, with continuum constructs (`exp`, `log`, trig, `√` as a real number, measured PDG masses, random-coefficient robustness draws) confined to clearly-labelled `[approx]` comparisons. The exact claim never depends on the float part.
- **[APPROX]** — by construction a continuum / degenerate-idealisation comparison (a dimensional-transmutation estimate, a coupling-running anchor, the fine-structure reading). These are not exact framed-rational claims; they are the observer-chart reading of an `Ω`-hard object.

This is the corpus rule: an exact claim lives in finite, finite-field, or cyclotomic arithmetic; the continuum enters only as an explicitly labelled profinite / degenerate-idealisation approximation, and no realized magnitude exceeds `Ω`.

**Status.** All 15 scripts run and pass. The two **EXACT** scripts establish every load-bearing identity of the mass sector directly in framed-rational arithmetic, with the continuum reading held as a labelled `[approx]`:

- `exact_core.py` — the float-free core (25/25): the Koide identity natively over framed rationals in `𝔽_{p²}/𝔽_p` (the quarter-turn the rational `N(b)/a² = 1/2`, `Q = 2/3` exact on three shells); the amplitude diagonal `r² = N(1−ζ_n) = 2, 3` as integers in `𝔽_p`; the `π/12` boundary as an exact rational multiple of `π`; the Gauss-sum reality and `π/3`-quantisation as integer identities in the group ring `ℤ[ℤ/3×ℤ/p]`; the trimaximal magic matrix with maximal Jarlskog `J = 1/(6√3)` in `ℚ(ω)`.
- `framed_koide.py` — the Koide and circulant facts natively over framed rationals: the "`√2` amplitude" is the framed rational `N(b)/a² = 1/2` and `ω` is the finite cube root, not a continuum complex number.

Class counts: **EXACT 2, MIXED 10, [APPROX] 3.**

## Requirements

- Python 3.10+
- `numpy`, `sympy`; `scipy` only for `tm2_jointfit.py` (the joint mixing fit)
- no other dependencies; no network, no data files

```bash
pip install numpy sympy scipy
```

## Running

```bash
python3 exact_core.py                                  # one script
for f in *.py; do echo "=== $f ==="; python3 "$f"; done  # whole suite
```

All scripts exit 0 and complete in seconds.

## Script → claim map

"Paper result" refers to the labelled results in `../main.tex`. "Class" is the framed-rational class above.

| script | class | pass | paper result | what it verifies | deps |
|---|---|---|---|---|---|
| `exact_core.py` | EXACT | 25/25 | §Finitism; Koide, amplitudes, boundary, Gauss sums | the float-free core: Koide over `𝔽_{p²}/𝔽_p`, `r²=N(1−ζ_n)=2,3` as integers, `π/12` rational-`π` boundary, Gauss-sum reality and `π/3`-quantisation as integer group-ring identities, maximal Jarlskog in `ℚ(ω)` | sympy |
| `framed_koide.py` | EXACT | float-free | Koide form (Prop circulant) | the `√2` amplitude as the framed rational `N(b)/a²=1/2`; `ω` the finite cube root | — |
| `tier_b.py` | MIXED | 17/17 | Tier-A/B figures (Table status) | Koide identities and figures, the `λ`-power and Gatto checks, the Georgi–Jarlskog double ratio, the lopsided/seesaw mixing comparison | numpy, sympy |
| `m10.py` | MIXED | 12/12 | winding kernel (Props circulant, pi12) | the circulant construction and eigenvalue identity, symbolic `Q=⅓+r²/6` and `r=√2`, the `π/12` boundary and LO spectrum, the per-sector extraction | numpy |
| `delta.py` | MIXED | 10/10 | cross-sector lock (§winding) | the phase lock `δ_ℓ:δ_d:δ_u=1:½:⅓` and its robustness, the reality of the symmetric cubic overlap and its drive-breaking, the `π/3`-quantisation of small-shell phases | numpy |
| `neutrino.py` | MIXED | 7/7 | seesaw, `Q_ν=2/3`, `Σm_ν` (§neutrino) | the seesaw-of-circulants identity float-free, the `Q_ν=2/3` mass prediction with robustness and seesaw consistency (labelled `[approx]`) | sympy |
| `pmns_cp.py` | MIXED | 6/6 | leptonic CP (§cp) | the trimaximal magic matrix and its maximal Jarlskog, the TM2 `δ_CP` at the observed angles | numpy |
| `tm2_jointfit.py` | MIXED | 9/9 | TM2 realisation (§cp) | the trivial-singlet protection, the dissolved solar tension, the joint fit at `χ²≈0` with the CP in `δ_ν` (the fit numeric, the structural checks exact) | numpy, scipy |
| `quark_amp.py` | MIXED | 6/6 | quark amplitudes (Rem. 23-tori) | the Georgi–Jarlskog down dressing `Q→0.745`, the up `r_u≈√3`, the `n`-fold cyclotomic-norm diagonal | numpy |
| `up_doubling.py` | MIXED | 11/11 | up-sector doubling (Prop doubling) | the `(4,2)/(4,2)/(8,4)` pattern with up `=2×` down, the `10·10` derivation (structural integer; PDG data labelled `[approx]`) | — |
| `spurion.py` | MIXED | 4/4 | Cabibbo spurion (Prop gatto) | the Gatto relation, `λ` from the down circulant, `λ≈δ_0≈2/9` | numpy |
| `theta13.py` | MIXED | 4/4 | reactor angle (§cp) | `θ_13≈θ_C/√2`, the quark–lepton complementarity sum rule, the fold onto `δ_0/√2` | numpy |
| `scale_a.py` | [APPROX] | — | overall scale (§stability) | the forced `y_t≈1`, the descent of `λ` to the scale-invariant point, the transmutation exponent `v/M_P=e^{−38}` (dimensional estimate; the exact coefficient is `Ω`-hard) | numpy |
| `coupling_anchor.py` | [APPROX] | — | coupling anchor (§stability) | the gauge couplings descending from the bare `1/4π` at the substrate; the lattice→continuum matching | numpy |
| `alpha_probe.py` | [APPROX] | 6/6 | `α` ledger (App. AL) | the fine-structure faces table; `ln(M_P/H_0)=140.3=½lnΩ` (cutoff = coherence horizon); the bare `4π` framed-exact, the digit `Ω`-hard | numpy |

## Finitism audit

`../reports/finitism-audit/` is the standing cross-check that every load-bearing **EXACT** claim rests on integer / finite-field / cyclotomic arithmetic with no float or continuum step, and that the **MIXED** / **[APPROX]** continuum operations are labelled comparisons on which no exact claim depends. The audit re-does the three identified float relapses in `exact_core.py`; this README is kept in sync with it and with the in-paper reproducibility map.
