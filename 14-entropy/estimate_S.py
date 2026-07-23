#!/usr/bin/env python3
# estimate_S.py -- reproduces every numeral of 14-entropy (Estimating the
# de Sitter Entropy), and runs the continuum-token census on main.tex.
#
# All observational values are [approx] chart readings; the exact faces are
# the counts Om = 4S+1 and the admissibility congruences, verified here in
# exact integer arithmetic on the instantiated Carrier. No fitting, no RNG;
# transcendental library calls (sqrt, atanh, tanh, pi) appear only as the
# labelled chart functions applied to [approx]/[LCDM] quantities.
#
# Exit status: 0 iff the exact checks and the census both pass.

import re
import sys
from math import pi, sqrt, atanh, tanh
from pathlib import Path

failures = 0

# ---------------------------------------------------------------- exact faces
# Instantiated Carrier of the lab universe (37-sim): exact integer counts.
S_LAB = 602_140
OM_LAB = 4 * S_LAB + 1


def is_prime(n: int) -> bool:          # deterministic trial division, exact
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


print("exact faces (counts): Om = 4S+1; S even; S = 1 mod 3; 4S+1 prime")
checks = [
    ("Om = 4S+1", OM_LAB == 2_408_561),
    ("S even (octant sector Z_8 exists: 8 | 4S iff 2 | S)", S_LAB % 2 == 0),
    ("S = 1 mod 3", S_LAB % 3 == 1),
    ("4S+1 prime", is_prime(OM_LAB)),
    ("octant count S/2 is an integer", (S_LAB // 2) * 2 == S_LAB),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  (lab Carrier Om={OM_LAB})")
    failures += 0 if ok else 1

# ------------------------------------------------------------ chart channel
# laboratory channel [I]
lP = 1.616255e-35      # Planck length, m
c = 2.99792458e8       # m/s
Gyr = 3.1557e16        # s
Mpc = 3.0857e22        # m


def S_of(rH):          # S = pi (r_H / l_P)^2   [approx]
    return pi * (rH / lP) ** 2


LAM_FACE = {"1", "4b"}          # rows reading the Lambda face
GAUGE = {"4a"}                  # gauge reading: displayed, excluded from stats
rows = []
sigma = {}                      # per-row relative uncertainty on sqrt(S)

# 1. expansion geometry: Lambda from the LCDM fit (Planck 2018)
Lam = 1.088e-52                                   # m^-2, ~2% -> 1% on sqrt(S)
rows.append(("1", "Lambda (CMB, Planck alone)", sqrt(3.0 / Lam)))
sigma["1"] = 0.010

# 2. local distance ladder (published stat+sys)
for H0, dH, lab, key in ((73.0, 1.0, "Cepheid", "2a"), (69.8, 1.7, "TRGB", "2b")):
    rows.append((key, f"ladder H0={H0} ({lab})", c / (H0 * 1e3 / Mpc)))
    sigma[key] = dH / H0

# 3. rotation curves through the bridge a0 = c H / 2 pi
a0, da0 = 1.20e-10, sqrt(0.02**2 + 0.24**2) * 1e-10   # SPARC knee, sys-dominated
rows.append(("3", "rotation curves a0", c / (2 * pi * a0 / c)))
sigma["3"] = da0 / a0

# 4. stellar ages through age = horizon distance (Valcin et al. 2025)
t_star, dt = 13.39 * Gyr, sqrt(0.10**2 + 0.23**2) / 13.39
rows.append(("4a", "stellar age, raw ct [gauge]", c * t_star))
rows.append(("4b", "stellar age, octant (4/pi)ct", (4 / pi) * c * t_star))
sigma["4a"] = sigma["4b"] = dt

print(f"\n{'#':3s}{'instrument':32s} {'r_H [m]':>12s} {'S':>10s} {'sqrt(S)':>10s} {'sig%':>6s}")
Svals = {}
for key, name, rH in rows:
    S = S_of(rH)
    Svals[key] = S
    print(f"{key:3s}{name:32s} {rH:12.3e} {S:10.2e} {sqrt(S):10.2e} {100*sigma[key]:6.1f}")

EVIDENCE = [k for k, _, _ in rows if k not in GAUGE]   # five evidence readings
sq = {k: sqrt(Svals[k]) for k in EVIDENCE}
m = sum(sq.values()) / len(sq)
half = 100 * (max(sq.values()) - min(sq.values())) / 2 / m
fac = (max(sq.values()) / min(sq.values())) ** 2
print(f"\nconcordance (5 evidence readings, gauge 4a excluded): sqrt(S) ="
      f" {min(sq.values()):.2e} .. {max(sq.values()):.2e}"
      f"  (+/- {half:.1f}% half-range about the mean)")
print(f"on S itself: full-range spread = factor {fac:.2f}")
assert abs(half - 16.6) < 0.5 and abs(fac - 1.94) < 0.05
print("[PASS] concordance: +/-17% half-range, factor 1.9 on S")

# the two-cluster ratio is the chart identity (H_rate/H0)^2 / OmL -- the
# definition of OmL read on the rows, NOT framework content (round-02 F1).
OmL = 0.685
H0_PLANCK = 67.36
for key, H in (("2a", 73.0), ("2b", 69.8)):
    lhs = Svals["1"] / Svals[key]
    rhs = (H / H0_PLANCK) ** 2 / OmL
    assert abs(lhs / rhs - 1) < 2e-3, (key, lhs, rhs)
print("[PASS] chart identity S_L/S_rate = (H/H0)^2/OmL verified per row"
      " (the cluster ratio displays the Hubble tension; no framework content)")

# circularity audit: the age ratio depends on the single fitted Omega_Lambda
ratio = (2 / 3) * atanh(sqrt(OmL))                # [LCDM]
OmL_pi4 = tanh(1.5 * pi / 4) ** 2                 # inversion of pi/4 [LCDM]
dev = abs(ratio - pi / 4) / (pi / 4) * 100
sig = abs(OmL - OmL_pi4) / 0.007
print(f"\naudit: t0*H_L = (2/3) artanh(sqrt(OmL)) = {ratio:.4f};  pi/4 = {pi / 4:.4f}"
      f"  (deviation {dev:.2f}%)")
print(f"       pi/4 corresponds to OmL = {OmL_pi4:.4f}  (fitted: {OmL}; a {sig:.2f}-sigma landing)")
print("       => the ~0.2% landing restates the fitted OmL: consistency, not evidence")
print("       (sub-0.1% figures need the radiation correction the flat matter+Lambda form omits)")

# octant lemma prediction: Omega_Lambda as an output of the bridge set
print(f"\noctant lemma: t_age = (pi/4) r_H/c  =>  predicted OmL = tanh^2(3pi/8) = {OmL_pi4:.4f}"
      f"  (fitted {OmL}: {sig:.2f} sigma)")
print("saturation test (fit-independent): oldest-object ages cap at (pi/4) r_H/c = 13.8 Gyr,"
      " at every observational frame chronon")

# the entailed rate: the framework content the cluster apparatus concealed.
# OmL = tanh^2(3pi/8) from the octant + measured Lambda => H0 = H_L/tanh(3pi/8)
H_L = sqrt(Lam * c ** 2 / 3) * Mpc / 1e3          # km/s/Mpc [approx]
H0_ent = H_L / tanh(3 * pi / 8)
dH0 = H0_ent * 0.016 / 2                          # from the ~1.6% Lambda error
sig_shoes = (73.0 - H0_ent) / sqrt(1.0 ** 2 + dH0 ** 2)
sig_trgb = (69.8 - H0_ent) / sqrt(1.7 ** 2 + dH0 ** 2)
sig_planck = (67.36 - H0_ent) / sqrt(0.54 ** 2 + dH0 ** 2)
print(f"\nentailed rate: H_Lambda = {H_L:.1f} => H0 = {H0_ent:.1f} +/- {dH0:.1f} km/s/Mpc"
      f"  (Planck {abs(sig_planck):.1f} sigma; TRGB {abs(sig_trgb):.1f} sigma;"
      f" Cepheid {abs(sig_shoes):.1f} sigma)")
assert abs(H0_ent - 67.4) < 0.15 and abs(sig_shoes - 5.0) < 0.15 and abs(sig_trgb - 1.4) < 0.1
print("[PASS] entailed H0 = 67.4 +/- 0.5: tension resolves toward CMB/TRGB;"
      " Cepheid ladder 5.0 sigma adverse, in plain view")

# temporal-face confrontation: octant bound vs Valcin et al. 2026 (IV) [LCDM]
t_oct = (pi / 4) * sqrt(3.0 / Lam) / c / Gyr
dv = sqrt(0.25 ** 2 + 0.23 ** 2)
sig_gc = (t_oct - 13.61) / dv
sig_tu = (t_oct - 13.81) / dv
print(f"\noctant bound {t_oct:.2f} Gyr vs Valcin IV: oldest population {sig_gc:+.2f} sigma,"
      f" inferred cosmic age {sig_tu:+.2f} sigma (approached; saturated; nowhere violated)")
assert abs(sig_gc - 0.53) < 0.05 and abs(sig_tu + 0.06) < 0.05
print("[PASS] Valcin IV confrontation: population 0.5 sigma below the bound;"
      " cosmic age on it (0.06 sigma)")

# floor-running confrontation: MUSE-DARK III (Ciocan et al. 2026) [LCDM]
Om_m = 0.315
Hz = sqrt(Om_m * 8 + (1 - Om_m))                  # H(z=1)/H0, flat LCDM
a0_pred = (a0 * Hz) * 1e10                        # e-10 units
sig_end = (2.38 - a0_pred) / sqrt(0.10**2 + (da0 * 1e10 * Hz) ** 2)
slope_pred = a0 * 1e10 * (Hz - 1)
sig_slope = (1.59 - slope_pred) / sqrt(0.10**2 + (da0 * 1e10 * (Hz - 1)) ** 2)
print(f"\nfloor running: a0(z=1) predicted {a0_pred:.2f}e-10 vs measured 2.38+/-0.10"
      f" ({sig_end:.1f} sigma with anchor systematics); linear rate predicted"
      f" {slope_pred:.2f} vs 1.59+/-0.10 e-10/z ({sig_slope:.1f} sigma pre-systematics)")
assert abs(sig_end - 0.5) < 0.1 and abs(sig_slope - 3.0) < 0.1
print("[PASS] Ciocan confrontation: constant floor dead; endpoint 0.5 sigma;"
      " linear rate ~3 sigma open")

# bound channel
print("\nbound: registered entropy budget ~1e104 << S  (headroom ~1e18 to saturation)")

# ------------------------------------------------------------------- census
# Continuum-token census of main.tex: every pi, trigonometric, hyperbolic,
# and square-root token is counted per class, and every paragraph carrying
# such a token must carry a register label ([approx], [LCDM], [I]) or a
# named count/chart designation. Mirrors the corpus grep-gate discipline.

TOKEN_CLASSES = {
    "pi":    re.compile(r"\\pi\b"),
    "trig":  re.compile(r"\\(?:cos|sin|tan)\b|\\artanh\b|\\tanh\b|artanh|atanh|\btanh\b"),
    "sqrt":  re.compile(r"\\sqrt\b"),
    "integral": re.compile(r"\\int(?![a-zA-Z])"),
}
LABELS = re.compile(
    r"\\apx\b|\\lcdm\b|\\imp\b|\bchart\b|\bcount\b|\bdictionary\b|\\Lambda\$?CDM|\$\\Lambda\$CDM"
)


def census(tex_path: Path) -> int:
    src = tex_path.read_text(encoding="utf-8")
    body = src.split(r"\begin{document}", 1)[1]
    body = re.sub(r"(?<!\\)%.*", "", body)               # strip comments
    paragraphs = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    counts = {k: 0 for k in TOKEN_CLASSES}
    unlabelled = []
    for i, para in enumerate(paragraphs, 1):
        hits = {k: len(rx.findall(para)) for k, rx in TOKEN_CLASSES.items()}
        for k, n in hits.items():
            counts[k] += n
        if any(hits.values()) and not LABELS.search(para):
            unlabelled.append((i, para.strip()[:90]))
    print(f"\ncensus of {tex_path.name}: "
          + ", ".join(f"{k} x{v}" for k, v in counts.items()))
    bad = 0
    for tok, fix in (("epoch", "observational frame chronon"),
                     ("seat", "register / role / sector / residue")):
        n = len(re.findall(tok, body, re.IGNORECASE))
        print(f"  [{'PASS' if n == 0 else 'FAIL'}] banned token '{tok}' x{n}"
              f" (use: {fix})")
        bad += n
    if bad:
        return bad
    if unlabelled:
        print(f"  [FAIL] {len(unlabelled)} paragraph(s) carry continuum tokens without a register label:")
        for i, head in unlabelled:
            print(f"    para {i}: {head}...")
        return len(unlabelled)
    print("  [PASS] every continuum-token paragraph carries a register label")
    return 0


tex = Path(__file__).resolve().parent.parent / "main.tex"
if tex.exists():
    failures += census(tex)
else:
    print(f"\n[FAIL] {tex} not found; census not run")
    failures += 1

sys.exit(1 if failures else 0)
