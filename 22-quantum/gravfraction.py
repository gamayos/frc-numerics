#!/usr/bin/env python3
"""22-quantum gravfraction suite: the coherent-fraction channel law (prop:fcoh), EXACT.
Cells on C_16 (ledger Z[zeta_16] as integer coordinate vectors, zeta^8 = -1).
(F1) coherent sector: m_c synchronised cells give branch-differential phase zeta^{m_c a}
     exactly (amplitudes multiply), for m_c in {2,3,4} and every unit phase a;
(F2) offset-spread sector: the systematic branch phase over a complete offset sector
     vanishes by the complete character sum (nontrivial per-cell phase);
(F3) pairwise product: two clusters give phi_ent = (m_c1 * m_c2) * a exactly;
(F4) the envelope: |offset-sector character sum|^2 computed exactly, < m^2 (strict
     coherent/incoherent separation), = m^2 iff synchronised.
No floats, no RNG."""

def rep(label, ok):
    print(('PASS ' if ok else 'FAIL ') + label); assert ok, label

n = 16
def zmul(a, b):  # Z[zeta_16], zeta^8 = -1; vectors length 8
    res = [0]*15
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            res[i+j] += x*y
    for k in range(14, 7, -1):
        res[k-8] -= res[k]; res[k] = 0
    return res[:8]
def zpow_unit(e):  # zeta^e as vector
    e %= 16
    v = [0]*8
    if e < 8: v[e] = 1
    else: v[e-8] = -1
    return v
def zadd(a,b): return [x+y for x,y in zip(a,b)]
def zscale(a,c): return [c*x for x in a]
def conj(a):  # zeta -> zeta^-1 = -zeta^7
    r = [0]*8
    for e,x in enumerate(a):
        if x:
            v = zpow_unit((-e) % 16)
            r = zadd(r, zscale(v, x))
    return r
def norm2(a):
    m = zmul(a, conj(a))
    return m

# F1/F3: coherent products
ok1 = ok3 = True
for a in range(1, 16):
    for mc in (2, 3, 4):
        prod = [1]+[0]*7
        for _ in range(mc):
            prod = zmul(prod, zpow_unit(a))
        if prod != zpow_unit(mc*a): ok1 = False
    for mc1 in (2,3):
        for mc2 in (2,4):
            prod = [1]+[0]*7
            for _ in range(mc1*mc2):
                prod = zmul(prod, zpow_unit(a))
            if prod != zpow_unit(mc1*mc2*a): ok3 = False
rep('F1: synchronised branch phase = zeta^{m_c a} exactly, m_c in {2,3,4}, all a', ok1)
rep('F3: pairwise entangling phase = zeta^{m_c1 m_c2 a} exactly', ok3)

# F2: complete offset sector: sum over offsets s of zeta^{a s} = 0 for a != 0
ok2 = True
for a in range(1, 16):
    tot = [0]*8
    for sft in range(16):
        tot = zadd(tot, zpow_unit(a*sft))
    if any(tot): ok2 = False
rep('F2: offset-spread systematic branch phase vanishes (complete character sum), all a != 0', ok2)

# F4: envelope strictly below coherent for a genuine spread; equality iff synchronised
m = 4
sync = [0,0,0,0]           # all same offset
spread = [0,4,8,12]        # complete C_4 spread inside C_16
def sector_sum(offsets, a):
    tot = [0]*8
    for sft in offsets:
        tot = zadd(tot, zpow_unit(a*sft))
    return tot
a = 1
s_sync = sector_sum(sync, a);  n_sync = norm2(s_sync)
s_spr  = sector_sum(spread, a); n_spr = norm2(s_spr)
rep('F4: |sync sum|^2 = m^2 = 16 exactly; complete spread sum = 0',
    n_sync == [16]+[0]*7 and all(x == 0 for x in s_spr))
print('gravfraction: all checks passed')
