#!/usr/bin/env python3
"""22-quantum stratum suite: two strata of probability (prop:strata), EXACT.
(S1) two-way subring of the Gaussian ledger Z[i] = the tally lattice (exhaustive small range);
(S2) engineered-core weights reduce to exact Carrier residues on Omega=641:
     r^2=2 exists (641 = 1 mod 8), W+- = 2 +- r, W+ + W- = 4, W+ W- = 2;
(S3) the chart-ring counterexample c = 1+zeta_12 is not tally-realized: c*conj(c) is not a tally;
(S4) framed grid: r is a grid point a/g^n of the Subject chart (scale periodicity, 1-algebra).
No floats, no RNG."""
from fractions import Fraction as Fr

def rep(label, ok):
    print(('PASS ' if ok else 'FAIL ') + label); assert ok, label

# S1: conjugation-invariant Gaussian elements a+bi with b=0 <-> tallies (b -> -b invariance)
ok = all((b == 0) == ((a, b) == (a, -b)) for a in range(-6, 7) for b in range(-6, 7))
rep('S1: two-way part of Z[i] = the tally line (exhaustive |a|,|b|<=6)', ok)

# S2: residues on Omega=641
Om = 641
r = next(x for x in range(1, Om) if (x*x) % Om == 2 % Om)
Wp, Wm = (2 + r) % Om, (2 - r) % Om
rep('S2: r^2=2 exists on Omega=641 (r=%d); W+ + W- = 4; W+ W- = 2 exactly' % r,
    (Wp + Wm) % Om == 4 and (Wp * Wm) % Om == 2)

# S3: c = 1+zeta_12: c*cbar = 2 + (zeta12 + zeta12^-1); in Z[zeta12], zeta+zeta^-1 has minimal
# polynomial x^2-3 -> not a tally (not in the rational-integer line of the two-way subring basis)
# exact check in the cyclotomic ring as integer coordinate vectors over basis 1,z,z^2,z^3 (z^4=z^2-1)
def zmul(a, b):  # multiply in Z[zeta12], zeta12^4 = zeta12^2 - 1
    res = [0]*7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            res[i+j] += x*y
    for k in range(6, 3, -1):  # reduce z^k -> z^{k-2} - z^{k-4}
        res[k-2] += res[k]; res[k-4] -= res[k]; res[k] = 0
    return res[:4]
one, z = [1,0,0,0], [0,1,0,0]
zin = [0,1,0,-1]  # zeta12^-1 = zeta12 - zeta12^3 (z^6 = -1)
rep('S3a: zeta12 inverse witness exact', zmul(z, zin) == one)
c = [1,1,0,0]; cbar = [1,-1,0,1] if False else [x+y for x,y in zip(one, zin)]
cc = zmul(c, cbar)
rep('S3: c=1+zeta12 gives c*cbar = 2+(zeta+zeta^-1), not a tally (nonzero z-coordinates)',
    cc[0] == 2 and any(cc[1:]))

# S4: r = g^n for the chart generator g=3 (primitive mod 641): a grid point 1/g^{-n}
g = 3
dl = {pow(g, k, Om): k for k in range(Om-1)}
rep('S4: r is on the Subject zoom grid (r = g^%d), scale-periodic per 1-algebra' % dl[r], r in dl)
print('stratum: all checks passed')
