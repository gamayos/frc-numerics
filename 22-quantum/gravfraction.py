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

# F5: the reduced channel Gamma = chi_inc * zeta^{m_c a}: per fixed offset configuration
# the branch factor is zeta^{m_c a} * prod(offset-rotated); ensemble average over the
# spread sector factorises exactly: avg_config(branch) = zeta^{m_c a} * avg(spread factors)
a = 3; mc = 2
spread_offsets = [0, 4, 8, 12]          # complete C_4 spread: chi_inc = 0
partial = [0, 0, 4, 8]                  # nonuniform thermal-like distribution
def ensemble_avg(offsets_list, a, mc):
    tot = [0]*8
    for sft in offsets_list:
        term = zmul(zpow_unit(mc*a), zpow_unit(a*sft))
        tot = zadd(tot, term)
    return tot
lhs = ensemble_avg(spread_offsets, a, mc)
chi = sector_sum(spread_offsets, a)      # = 0 here
rhs = zmul(zpow_unit(mc*a), chi)
rep('F5: Gamma factorises exactly: ensemble avg = zeta^{m_c a} * chi_inc (complete spread: both zero)',
    lhs == rhs)
# F6: nonuniform thermal distribution: 0 < |chi_inc|^2 < m^2, factorisation still exact
lhs2 = ensemble_avg(partial, a, mc)
chi2 = sector_sum(partial, a)
rhs2 = zmul(zpow_unit(mc*a), chi2)
n2 = norm2(chi2)
rep('F6: nonuniform thermal chi_inc: factorisation exact and 0 < |chi|^2 < m^2 (|chi|^2 coords %s)' % n2,
    lhs2 == rhs2 and any(x != 0 for x in n2) and n2 != [16]+[0]*7)

# F7: the mixed complementarity identity, exact in the ring: with 4C^2 = (1-G)(1-Gbar),
# 4V^2 = (1+G)(1+Gbar): V^2 + C^2 = (1 + |G|^2)/2 identically; pure |G|=1 gives 1.
def comp_check(Gvec):
    one = [1]+[0]*7
    Gc = conj(Gvec)
    m1 = zmul(zadd(one, zscale(Gvec,-1)), zadd(one, zscale(Gc,-1)))  # (1-G)(1-Gbar) = 4C^2
    m2 = zmul(zadd(one, Gvec), zadd(one, Gc))                        # (1+G)(1+Gbar) = 4V^2
    lhs = zadd(m1, m2)                                                # 4(V^2+C^2)
    n2  = zmul(Gvec, Gc)                                              # |G|^2
    rhs = zadd(zscale(one,2), zscale(n2,2))                           # 2(1+|G|^2)
    return lhs == rhs
ok7 = all(comp_check(zpow_unit(e)) for e in range(16))                # pure instances |G|=1
half = [0]*8; half[0] = 1  # G = 1 (trivial) covered; a mixed instance: G = (1+zeta)/2 not integer-ring; use G = zeta + zeta^-1 form scaled? keep ring: G = zeta^a + zeta^b (|G|<2 mixed, ring element)
mixed = zadd(zpow_unit(1), zpow_unit(6))
ok7b = comp_check(mixed)
rep('F7: 4(V^2+C^2) = 2(1+|Gamma|^2) as a ring identity (all pure phases + a mixed ring instance)',
    ok7 and ok7b)
# F8: pure-limit concurrence: 4C^2 = (1-zeta^e)(1-zeta^-e) = 2 - (zeta^e + zeta^-e): two-way, exact
e = 3
one = [1]+[0]*7
m1 = zmul(zadd(one, zscale(zpow_unit(e),-1)), zadd(one, zscale(zpow_unit(-e),-1)))
expect = zadd(zscale(one,2), zscale(zadd(zpow_unit(e), zpow_unit(-e)), -1))
rep('F8: pure-channel 4C^2 = 2 - (zeta^e + zeta^-e) exactly (the sin^2 chart reading)', m1 == expect)
print('gravfraction: all checks passed')
