# 14-entropy — validation suite

Paper: *Estimating the de Sitter Entropy: Channels, Faces, and the Circularity Audit* (`main.tex`).
Repository: `https://github.com/gamayos/frc-numerics/tree/main/14-entropy`.

## Discipline

Exact claims live in integer arithmetic and are checked exhaustively; the continuum appears only as a labelled degenerate idealisation. Script classes: **EXACT** (float-free, integer/finite arithmetic), **MIXED** (an exact block plus labelled chart blocks), **[APPROX]** (chart computations only, no exact claim). Every float in the suite is a comparison-chart reading of `[approx]`/`[ΛCDM]`-labelled observational data; no exact claim traces through a float.

## Scripts

| script | class | pass | verifies | deps |
|---|---|---|---|---|
| `estimate_S.py` | MIXED | 5/5 exact + census PASS, exit 0 | exact faces (Ω=4S+1, S even, S≡1 mod 3, 4S+1 prime, octant count S/2 integral, on the instantiated Carrier Ω=2,408,561); the six-row channel table (with per-row σ, stat+sys) from (Λ, H₀, a₀, t⋆=13.39 Valcin 2025); concordance over the 5 evidence rows, gauge 4a excluded (±17% half-range on √S, factor 1.9 on S; role-corrected ±7%, factor 1.33); audit identity t₀H_Λ=(2/3)artanh√Ω_Λ, π/4 inversion (Ω_Λ=0.6837, 0.19σ); octant prediction tanh²(3π/8); two-cluster ratio 1.68±0.21 vs 1.46, 1.1σ (evidence rows, propagated errors); Valcin confrontation (+1.6σ/+0.8σ below octant bound); Ciocan floor-running confrontation (endpoint 0.5σ, linear rate ~3σ); entropy-budget bound; continuum-token census of `main.tex` | python3 stdlib |
| `make-wedge-2.py` | MIXED | 4 [PASS] lines + asserts, exit 0 | the registrable-wedge figures (§ wedge): audit identities asserted before drawing (octant/t_P identity, two-cluster ratio, r_H split); the diagonal regression k=3.032 over 13 mid-wedge objects with coefficient ρ̃=1.00×10³ kg/m³ [approx], constrained k=3 fit ρ̃=0.97×10³, sensitivity k=3.007 (15 incl. wall residents), over-closure band (1.4–2.8)×10⁸ M☉ across the 4 fit variants, width identity log₁₀(r_H/ℓ_P)=log₁₀√(S/π) exact; wall intersections (Compton entry 5.3×10⁻¹² m, over-closure exit 1.8×10⁸ M☉); electron/Sgr A* wall residency <0.01 dex; generates `registrable-wedge-plain-20260722` and `wall-channels-20260722` (run from `figures/`) | python3 + matplotlib |

## Float catalogue (finitism audit)

One row per continuum construct; verdicts per the corpus finitism-audit standard.

| construct | site | verdict |
|---|---|---|
| `math.pi`, `math.sqrt` | `estimate_S.py`: `S_of`, channel rows, concordance | comparison chart: `[approx]` readings of published data; the exact face is the count S=(Ω−1)/4 |
| `math.atanh`, `math.tanh` | `estimate_S.py`: audit block | `[ΛCDM]`: rival-chart identities, confrontation only |
| float division/means | `estimate_S.py`: two-cluster block | comparison chart on `[approx]` row values |
| integer arithmetic | `estimate_S.py`: exact-faces block | EXACT: congruences, primality (deterministic trial division), octant integrality |
| `log10`, OLS sums, float tolerances | `make-wedge-2.py` | comparison chart: `[approx]` log-chart of published object data; asserts document CODATA rounding; no exact (T) claim rests on any float |

Retired to `_to_delete/`: `s-estimate.py` (pre-protocol draft of `estimate_S.py`), `make-wedge.py`, `make-wedge-1.py` (superseded wedge generations), `planck-triangle.png` (reference image).

No relapse: no exact (T-tagged) claim is computed through continuum machinery. The census block enforces the in-paper labelling: every continuum-token paragraph of `main.tex` must carry a register label; exit 1 otherwise.

## Run

```
python3 validation/estimate_S.py    # exit 0 = exact checks + census green
```
