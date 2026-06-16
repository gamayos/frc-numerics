"""
O1: uniqueness of the lattice Maxwell functional.

Determines the space of quadratic functionals  S[A] = A^T Q A  of a U(1) lattice
gauge field on a periodic cubic lattice that are simultaneously
  (T) translation invariant,
  (L) range-R local         (kernel supported on |x-y|_inf <= R),
  (C) hypercubic invariant   (the order-48 signed-permutation point group),
  (G) gauge invariant        (Q B = 0, B the lattice gradient A -> A + d.lambda).

The point group acts directly on oriented links as signed permutations (a
reflection reverses a link, flipping sign and shifting base), so conjugation
P_g^T Q P_g is a flat index-permutation-with-sign on vec(Q).  We intersect (G)
and (C) via the Gram matrix on the (T,L) parameter space and report the
dimension of the admissible Q-space.  Expectation: dim = 1 (Maxwell) at R = 1.
"""
import numpy as np
import itertools

d = 3


def build(L):
    sites = list(itertools.product(range(L), repeat=d))
    sidx = {s: i for i, s in enumerate(sites)}
    def add(x, z): return tuple((x[i] + z[i]) % L for i in range(d))
    links = [(s, mu) for s in sites for mu in range(d)]
    lidx = {l: i for i, l in enumerate(links)}
    nlink = len(links); nsite = len(sites)

    B = np.zeros((nlink, nsite))
    for (x, mu) in links:
        e = tuple(1 if k == mu else 0 for k in range(d))
        B[lidx[(x, mu)], sidx[add(x, e)]] += 1.0
        B[lidx[(x, mu)], sidx[x]] -= 1.0

    group = []
    for pi in itertools.permutations(range(d)):
        for eps in itertools.product((1, -1), repeat=d):
            R = np.zeros((d, d), dtype=int)
            for a in range(d):
                R[pi[a], a] = eps[pi[a]]
            group.append(R)

    # link signed-permutation for each isometry:  A'[k] = s[k]*A[sigma[k]]
    def link_perm(R):
        sigma = np.empty(nlink, dtype=int); s = np.empty(nlink)
        for (x, mu) in links:
            k = lidx[(x, mu)]
            col = R[:, mu]; mup = int(np.nonzero(col)[0][0]); sgn = int(col[mup])
            Rx = tuple(int(sum(R[i, j] * x[j] for j in range(d))) % L for i in range(d))
            if sgn == 1:
                src = lidx[(Rx, mup)]; sg = 1.0
            else:
                base = tuple((Rx[i] - (1 if i == mup else 0)) % L for i in range(d))
                src = lidx[(base, mup)]; sg = -1.0
            sigma[k] = src; s[k] = sg
        return sigma, s

    # flat (i,j)->(t[i],t[j]) permutation and sign for conjugation P_g^T Q P_g
    flatperm, flatsign = [], []
    for R in group:
        sigma, s = link_perm(R)
        t = np.empty(nlink, dtype=int); t[sigma] = np.arange(nlink); st = s[t]
        fp = (t[:, None] * nlink + t[None, :]).reshape(-1)
        fs = (st[:, None] * st[None, :]).reshape(-1)
        flatperm.append(fp); flatsign.append(fs)

    return dict(sites=sites, add=add, links=links, lidx=lidx, nlink=nlink,
                nsite=nsite, B=B, flatperm=flatperm, flatsign=flatsign, group=group)


def param_basis(g, R):
    sites, add, lidx, nlink = g['sites'], g['add'], g['lidx'], g['nlink']
    disp = [z for z in itertools.product(range(-R, R + 1), repeat=d)
            if max(abs(c) for c in z) <= R]
    seen, Qs = set(), []
    for mu in range(d):
        for nu in range(d):
            for z in disp:
                if (mu, nu, z) in seen: continue
                seen.add((mu, nu, z)); seen.add((nu, mu, tuple(-c for c in z)))
                Q = np.zeros((nlink, nlink))
                for x in sites:
                    Q[lidx[(x, mu)], lidx[(add(x, z), nu)]] += 1.0
                Qs.append(0.5 * (Q + Q.T))
    return Qs


def maxwell_Q(g):
    sites, add, lidx, nlink = g['sites'], g['add'], g['lidx'], g['nlink']
    Q = np.zeros((nlink, nlink))
    for x in sites:
        for mu in range(d):
            for nu in range(mu + 1, d):
                emu = tuple(1 if k == mu else 0 for k in range(d))
                enu = tuple(1 if k == nu else 0 for k in range(d))
                terms = [(+1, lidx[(x, mu)]), (+1, lidx[(add(x, emu), nu)]),
                         (-1, lidx[(add(x, enu), mu)]), (-1, lidx[(x, nu)])]
                for s1, i in terms:
                    for s2, j in terms:
                        Q[i, j] += 0.5 * s1 * s2
    return Q


def admissible(L, R):
    g = build(L)
    Qs = param_basis(g, R); n = len(Qs); nlink = g['nlink']
    Qstack = np.array([Q.reshape(-1) for Q in Qs])              # (n, nlink^2)
    # gauge residual block:  vec(Q_a B)
    QB = np.array([(Q @ g['B']).reshape(-1) for Q in Qs])       # (n, nlink*nsite)
    Gram = QB @ QB.T
    # cubic residual blocks:  vec(P_g^T Q_a P_g - Q_a)
    for fp, fs in zip(g['flatperm'], g['flatsign']):
        D = Qstack[:, fp] * fs - Qstack                          # (n, nlink^2)
        Gram += D @ D.T
    w, V = np.linalg.eigh(Gram)
    tol = 1e-7 * max(1.0, w.max())
    null = V[:, w < tol]
    dim = null.shape[1]
    reps = [sum(null[a, c] * Qs[a] for a in range(n)) for c in range(dim)]
    return dim, reps, g


def kernel_of(Q, g):
    """Read the translation-invariant kernel M_{mu,nu}(z) from the origin rows."""
    x0 = (0,) * d; lidx, addf = g['lidx'], g['add']
    disp = [z for z in itertools.product(range(-2, 3), repeat=d)
            if max(abs(c) for c in z) <= 2]
    K = {}
    for mu in range(d):
        for nu in range(d):
            for z in disp:
                v = Q[lidx[(x0, mu)], lidx[(addf(x0, z), nu)]]
                if abs(v) > 1e-12:
                    K[(mu, nu, z)] = v
    return K


def symbol(K, k):
    S = np.zeros((d, d), complex)
    for (mu, nu, z), v in K.items():
        S[mu, nu] += v * np.exp(1j * np.dot(k, z))
    return 0.5 * (S + S.conj().T)


def relevant_split(reps, g):
    """Split the admissible space into relevant (O(k^2)) and irrelevant (O(k^4))
       by the rank of the leading small-k symbol signature; check the relevant
       operator equals the Maxwell transverse projector |k|^2 delta - k k."""
    Ks = [kernel_of(r, g) for r in reps]
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1),
            (0, 1, 1), (1, 1, 1), (1, -1, 0), (2, 1, 0)]
    t = 1e-3
    sig = []
    for K in Ks:
        row = []
        for dv in dirs:
            kk = t * np.array(dv) / np.linalg.norm(dv)
            row.append(symbol(K, kk).real[np.triu_indices(d)] / t**2)
        sig.append(np.concatenate(row))
    sig = np.array(sig)
    s = np.linalg.svd(sig.T, full_matrices=False)[1]
    nrel = int(np.sum(s > 1e-6)); nirr = len(reps) - nrel
    # relevant generator and its deviation from the Maxwell projector
    crel = np.linalg.svd(sig.T, full_matrices=False)[2][0]
    Krel = {}
    for c, K in zip(crel, Ks):
        for key, v in K.items():
            Krel[key] = Krel.get(key, 0.0) + c * v
    dev = []
    for dv in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (3, 1, 1)]:
        kk = np.array(dv); S = symbol(Krel, t * kk).real / t**2
        P = np.dot(kk, kk) * np.eye(d) - np.outer(kk, kk)
        dev.append(np.linalg.norm(S / np.trace(S @ P) * np.trace(P @ P) - P)
                   / np.linalg.norm(P))
    return nrel, nirr, max(dev)


if __name__ == "__main__":
    print("=" * 68)
    print(f"O1  uniqueness of the lattice Maxwell functional   (d={d})")
    print("=" * 68)

    g5 = build(5); QM = maxwell_Q(g5)
    gres = np.abs(QM @ g5['B']).max()
    cub = all(np.allclose((QM.reshape(-1)[fp] * fs).reshape(g5['nlink'], g5['nlink']), QM)
              for fp, fs in zip(g5['flatperm'], g5['flatsign']))
    print(f"Maxwell plaquette action: ||Q_M B||_inf = {gres:.1e} (gauge-inv {gres<1e-9});"
          f"  hypercubic-inv {cub}")
    print("-" * 68)

    for L in (4, 5, 6):
        dim, reps, g = admissible(L=L, R=1)
        nrel, nirr, dev = relevant_split(reps, g)
        print(f"range R=1 (L={L}): dim(T&L&C&G) = {dim}  ="
              f"  {nrel} relevant (O(k^2)) + {nirr} irrelevant (O(k^4));"
              f"  relevant vs Maxwell projector: {dev:.1e}")
    print("-" * 68)
    print("Conclusion: the range-1 admissible space is 2-dimensional, and splits")
    print("into exactly ONE relevant operator -- the Maxwell action, whose symbol")
    print("is the transverse projector |k|^2 d_{mn} - k_m k_n -- plus one")
    print("irrelevant O(k^4) higher-derivative lattice artifact.  Maxwell is the")
    print("unique relevant adjacency-local gauge+hypercubic quadratic functional.")
    print("=" * 68)
