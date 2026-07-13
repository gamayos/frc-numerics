# 13-epi validation suite

Float-free discipline (paper-ready protocol, Step 8): an exact (T) claim is checked in integer or rational arithmetic; a continuum object may appear only as the declared object of study (the IEEE-754 readout itself) or as an [approx]-tagged statistical reading.

| script | class | status | claims backed |
|---|---|---|---|
| `validate_towers.py` | EXACT (int + Fraction only; brackets self-certified) | **49/49 PASS** (run 13 Jul 2026) | Prop. tower-e, Prop. tower-pi, Cayley identities (Def. cayley), orientation rule (Rem. orient) |
| `validate_e.py` | MIXED | full run recorded in `results_e.txt` (source run, zero failures) | Thms enclosure-e, readout-e, wall-e, antiperiod; Prop. duals; Exp. blind; Prop. calib; Exp. null |
| `validate_pi.py` | MIXED | full run recorded in `results_pi.txt` (zero failures) | Thms enclosure, readout-pi, window, halfwall, secondorder; Prop. lucas |
| `validate_pi2.py` | EXACT (int + Fraction only) | full run recorded in `results_pi2.txt` (zero failures) | Thms quarter, vanish, super; proof ingredients (A+B=2L, Lerch, binomial transfer) |
| `kurepa_wall.c` | EXACT (`__int128` modular) | 22,043 primes < 2.5e5, zero failures (source run) | Thm wall-e (D-form + non-vanishing) |

MIXED classification, catalogued:
- `validate_e.py`: (a) the binary64 constant obtained as a Python float is the *object of study* of Thm readout-e (the readout), compared exactly against rationals — sanctioned; (b) a 500-digit Decimal reference for e is a controlled bounded-error reference — sanctioned, queued for re-basing on the chain's own certified brackets at the promotion pass; (c) the calibration scan and null-experiment statistics are [approx] by declaration in-paper.
- `validate_pi.py`: same pattern (binary64 readout as object; high-precision reference for the enclosure comparisons; Wieferich search and quotient moments are exact congruence arithmetic).

Provenance: `validate_e.py`, `validate_pi.py`, `validate_pi2.py`, `kurepa_wall.c` are the verbatim scripts of the source memoranda (`reports/epi-report-2/`, `reports/epi-report-3/`), renamed to the canonical suite form; their recorded outputs ship alongside. `validate_towers.py` is new with the manuscript. Full-suite re-run gate before snapshot promotion.

Run: `python3 validate_towers.py`; `python3 validate_e.py`; `python3 validate_pi.py`; `python3 validate_pi2.py`; `cc -O2 kurepa_wall.c -o kurepa_wall && ./kurepa_wall`.
