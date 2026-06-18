# Validation suite — *Standard-Model Interactions over Finite Substrate*

This folder holds the computational verification for the paper *Standard-Model Interactions over a Finite Substrate* (`../main.tex`). Every
quantitative and algebraic claim in the paper is checked by one of the scripts below,
in **exact arithmetic** wherever the claim is exact (integer, finite-field, or
cyclotomic), and against the lattice Green's function or measured constants where the
claim is a continuum reading. The scripts are standalone, deterministic, and print a
human-readable verdict; none takes input or writes files.

The map below is the executable form of the paper's reproducibility map
(Appendix *Reproducibility map*) and of §*Reproducibility*.

## Requirements

- Python 3.10+
- `numpy` and `sympy` (only some scripts need them — see the table)
- no other dependencies; no network, no data files

```bash
pip install numpy sympy
```

## Running

Each script is run directly and prints its result:

```bash
python3 p1.py
```

To run the whole suite:

```bash
for f in *.py; do echo "=== $f ==="; python3 "$f"; done
```

All scripts exit 0 and complete in seconds, except `enumerate_maxwell.py`
(~30 s — an exact finite-field rank over the order-48 point group).

## Script → claim map

The "Proposition / Theorem" column refers to the labelled results in `../main.tex`.

| script | paper result | what it verifies | arithmetic | deps |
|---|---|---|---|---|
| `em1_prototype.py` | EM ledger (Table); charge & Coulomb props | finite U(1) gauge structure: gauge-invariant plaquette flux, quantised winding charge, Coulomb coefficient vs the lattice Green's function, and the EM-repels/gravity-attracts sign dichotomy | integer + lattice solve | numpy |
| `enumerate_maxwell.py` | O1 uniqueness theorem | exhaustive enumeration over the order-48 hypercubic point group: the relevant adjacency-local gauge functional is **2-dimensional**, splitting into one Maxwell (transverse-projector) operator + one irrelevant O(k⁴) artifact | exact finite-field rank | numpy |
| `o2_numbers.py` | bare-coupling prop | the electromagnetic coupling as phase-channel capacity; the α_bare = 1/4π bookkeeping and the 10³⁶ EM/gravity hierarchy as a reading of Ω | rational/float | — |
| `ew1.py` | electroweak-breaking theorem; ρ=1; Weinberg angle | drive/torus misalignment over 𝔽₁₃: massless photon (drive-fixed Cartan), gapped W±, custodial ρ=1, and sin²θ_W = Tr(T₃²)/Tr(Q²) = 3/8 | exact (𝔽₁₃, rationals) | sympy |
| `qcd.py` | colour SU(3) & confinement props | SU(3,𝔽_q) as the special unitary group of a Hermitian three-form (\|SU(3,2)\|=216), the Z₃ triality centre when 3∣q+1, and the saturated-regime area law | exact (finite field) | numpy |
| `generation.py` | the generation theorem | one generation as the spinor 16 = 1⊕5̄⊕10 of the rank-5 frame: hypercharges (traceless), electric charges, and the ΣY = ΣY³ = 0 anomaly cancellation | exact rationals | — |
| `p1.py` | running prop | one-loop RG with b = (41/10, −19/6, −7): α₁=α₂ near 10¹³ GeV, sin²θ_W = 3/8 there exactly, the ~13% α₃ near-miss, and 3/8 running to 0.231 at M_Z | float (RG) | — |
| `p2.py` | bare-coupling prop | the order-one coefficient is exactly 1: α_bare = 1/4π from channel unity and charge = action = phase quantum | rational | — |
| `p3.py` | weak-connection prop | the cell-local SU(2,𝔽₃) connection: Wilson action gauge-invariant by plaquette-trace conjugation (exhaustive over the group), doublet covariantly coupled | exact (𝔽₉) | — |
| `p4.py` | parity-violation prop | maximal V−A from drive coherence: the drive-aligned branch sums coherently, the Frobenius branch decouples by character orthogonality (Σ = 0 exactly) | exact (roots of unity) | — |
| `p5.py` | gluon-connection prop | the cell-local SU(3) gluon connection: exact Wilson gauge invariance, the self-coupling as non-abelian curvature (U₁U₂U₁⁻¹U₂⁻¹ ≠ I), masslessness | exact / numeric | numpy |
| `p6.py` | asymptotic-freedom prop | b₀ = 11 − (2/3)n_f > 0, Λ_QCD = M_P exp(−2π/b₀α_s) by dimensional transmutation, and (m_p/M_P)² = exp(−88) | rational + math | — |
| `p7.py` | mass prop | what the substrate fixes (seesaw scale ~0.05 eV, b–τ unification, top y~1, the FN winding-distance hierarchy) and what is open (the spectrum/mixings) | float | — |
| `p8.py` | unification prop | the rank-5 frame and the SU(5)/SO(10) representation arithmetic for simple unification | integer | — |
| `p8b.py` | unification prop (a-priori) | the X,Y bookkeeping: dim SU(5) − dim(SM) = 24 − 12 = 12 = the 3×2 off-block (colour–isospin reframings); 16 irreducible under SO(10) | integer | — |
| `p9.py` | Galois-conjugate prop | generations as Galois conjugates: orbit size = field-extension degree for q = 2, 3, 5 | integer | — |
| `p9b.py` | three-generations prop (frontier Q1) | the closed role ladder's 1+3 split: counting = bosonic carrier, the three generative roles = three fermion generations; the mass ordering | integer | — |
| `p10.py` | chirality-selection prop | the orientation-flip 𝕚_t ↦ −𝕚_t invariance: absolute handedness is a relabelling with no frame-independent meaning | exact | — |
| `p11.py` | substrate-residue prop | Ω ≡ 5 (mod 12) as the CRT conjunction of 4∣Ω−1 (quarter-turn) and 3∣Ω+1 (triality), and its Dirichlet density 1/4 | exact (sympy) | sympy |
| `audit_finitism.py` | §Finitism | re-runs the load-bearing EM/O1 claims in exact arithmetic — no random sampling, no FFT, no floating point, no transcendentals — confirming the answers are unchanged (gauge identity exhaustive, rank = 2, Wilson action cyclotomic, Green's function = 257/7680 on the L=4 Z[i] torus) | exact (ℤ, 𝔽_p, ℚ(ζ_M), ℤ[i]) | numpy, sympy |

## Representative expected output

- `enumerate_maxwell.py` → "into exactly ONE relevant operator — the Maxwell action … plus one irrelevant O(k⁴) … artifact."
- `ew1.py` → sin²θ_W = 3/8, ρ = 1 exactly.
- `p1.py` → α₁ = α₂ at ~10¹³ GeV, α_GUT⁻¹ ≈ 42, α₃⁻¹ ≈ 37 (~13% near-miss).
- `p8b.py` → dim SU(5) − dim(SM) = 12 == X,Y count: True.
- `em1_prototype.py` → "EM like-charges REPEL: True / gravity ATTRACTS: True."
- `audit_finitism.py` → "1 − cos(2π F/M) = 1 − √2/2 … the action is an algebraic (cyclotomic) number, not a float."

## Conventions and notes

- **Exact where exact.** Claims marked *exact* in the paper are computed in integer,
  finite-field (𝔽_p), or cyclotomic (ℚ(ζ_M), ℤ[i]) arithmetic and verified exhaustively
  over a basis or group, never by sampling. `audit_finitism.py` is the cross-check that
  no exact claim secretly depends on a floating-point or continuum step.
- **Continuum readings.** The Coulomb 1/4πr coefficient and the comparison of α and
  sin²θ_W to measured values are degenerate-idealisation readings; these use the lattice
  Green's function or PDG constants and are reported as such.
- **Determinism.** No script uses randomness; results are reproducible bit-for-bit.
- **Orientation.** The convention 𝕀_t = g_t^{−t} is used throughout (see `p10.py`);
  do not flip it.
