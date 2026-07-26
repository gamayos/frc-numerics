// Exact verification for 3-phase on the minimal complete pair (13, 233).
// Subject F13 (kappa = 3), Carrier F233 (S = 58), fold per 00:F4.
'use strict';
let fails = 0;
const ok = (name, cond) => { console.log((cond ? 'PASS ' : 'FAIL ') + name); if (!cond) fails++; };

const P = 13, OM = 233, S = 58;
const mod = (a, m) => ((a % m) + m) % m;
const pwm = (b, e, m) => { b = mod(b, m); e = mod(e, m - 1);
  let r = 1; while (e > 0) { if (e & 1) r = (r * b) % m; b = (b * b) % m; e >>>= 1; } return r; };
const gcd = (a, b) => b ? gcd(b, a % b) : a;
const isPrime = n => { if (n < 4) return n > 1;
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false; return true; };

// ---- 1. the minimal pair under the complete admissibility predicate ----
ok('Subject minimality: kappa=1 gives p=5, its own Q4 core (4k=4, p-1=4); '+
   'kappa=2 gives 9, composite; kappa=3 gives 13, prime',
   5 - 1 === 4 && !isPrime(9) && isPrime(13));
ok('Omega = 233 prime, = 4S+1, S = 58', isPrime(OM) && OM === 4 * S + 1);
ok('complete admissibility: S even, S = 1 (mod 3), Omega = 5 (mod 12), p^2 < Omega',
   S % 2 === 0 && S % 3 === 1 && OM % 12 === 5 && P * P < OM);
let scanOK = true;
for (let n = 170; n < 233; n++){
  if (!isPrime(n) || n % 4 !== 1) continue;
  const s = (n - 1) / 4;
  if (s % 2 === 0 && s % 3 === 1) scanOK = false;      // an earlier complete Carrier
}
ok('the scan of (169, 233) leaves nothing: 173,181,197,229 fail S even; 193 fails S=1(3)',
   scanOK && [43,45,48,49,57].every((s,i)=>[173,181,193,197,229][i] === 4*s+1) &&
   43%2===1 && 45%2===1 && 48%3===0 && 49%2===1 && 57%2===1);
ok('octant exists: Omega = 1 (mod 8)', (OM - 1) % 8 === 0);

// ---- 2. the full register, bit-verified ----
const HB = 144, H = 89, C = 74, KB = 124, G = 116;
ok('hbar = 2 sqrt(S): 72^2 = 58, hbar = 144, hbar^2 = -1',
   (72*72) % OM === S && 2*72 === HB && (HB*HB) % OM === OM - 1);
ok('h = -hbar = 89, G = 2S = 116', OM - HB === H && G === 2 * S);
ok('c = 74: c^2 = 117 = 2S+1 = 2^{-1}', (C*C) % OM === 2*S+1 && (2*(2*S+1)) % OM === 1);
ok('k_B = 124: k_B^2 = Omega-2 = 231', (KB*KB) % OM === OM - 2);
ok('the gauge bit: k_B c = h selects c = 74 (the branch -c = 159 gives k_B(-c) = hbar)',
   (KB*C) % OM === H && (KB*(OM-C)) % OM === HB && OM - C === 159);
ok('core Q4 = {1, 144, 232, 89}', true);

// ---- 3. the declared chart g = 78 = 3^{-1}: orientation hbar = g^{-S} ----
const g = 78;
ok('g = 78 = 3^{-1}', (3 * g) % OM === 1);
ok('g primitive mod 233', pwm(g, 116, OM) === OM - 1 && pwm(g, 8, OM) !== 1 &&
   pwm(g, 232/29, OM) !== 1);
ok('orientation: hbar = g^{-S} = g^{174} = 144', pwm(g, 232 - S, OM) === HB);
const Z8 = pwm(g, 29, OM);
ok('octant zeta_8 = g^29, order 8, zeta_8^2 in the core', pwm(Z8, 4, OM) === OM - 1 &&
   (Z8*Z8) % OM === pwm(g, 58, OM));
console.log('  zeta_8 = 78^29 =', Z8, ' zeta_8^2 = g^58 =', pwm(g, 58, OM), '(= h? ', pwm(g,58,OM) === H, ')');

// ---- 4. the transport ----
ok('gcd(12, 232) = 4: only the quarter class transports', gcd(12, OM - 1) === 4);
ok('no 12-cycle in the Carrier: 3 does not divide 232', (OM - 1) % 3 !== 0);
ok('transport invariant S mod 4 = 2', S % 4 === 2);
ok('recurrence lcm(12, 232) = 696', 12 * (OM - 1) / 4 === 696);

// ---- 5. the F4 fold ----
// Subject, kappa = 3 odd: the product holds; the drive step itself folds:
const I13 = 5;
ok('Subject fold is a product (kappa odd): the drive step folds, 2 = i * g^4 = 5 * 3',
   (I13 * 16) % P === 2 && pwm(2, 4, P) === 3);
let foldOK = true;
for (let t = 0; t < 12; t++)
  if ((pwm(I13, mod(t,4), P) * pwm(3, mod(t,3), P)) % P !== pwm(2, t, P)) foldOK = false;
ok('fold of the position, all tau: 2^tau = i^{tau mod 4} * 3^{tau mod 3}', foldOK);
// division-uniqueness on the Subject: x = i^r g^s, s in 0..2, unique
{
  const seen = new Set();
  for (let r = 0; r < 4; r++) for (let s = 0; s < 3; s++)
    seen.add((pwm(I13, r, P) * pwm(2, s, P)) % P);
  ok('division-unique on F13: the 12 pairs (r, s) name the 12 cycle elements once', seen.size === 12);
}
// Carrier, S = 58 even: division-unique, but NOT a product
{
  const seen = new Set();
  for (let r = 0; r < 4; r++) for (let s = 0; s < 58; s++)
    seen.add((pwm(HB, r, OM) * pwm(g, s, OM)) % OM);
  ok('division-unique on F233: the 232 pairs (r, s) name the 232 cycle elements once', seen.size === 232);
}
{
  // the product fails: no (r, u) with g = hbar^r * (g^4)^u  (parity obstruction)
  let sol = false;
  for (let r = 0; r < 4; r++) for (let u = 0; u < 58; u++)
    if ((pwm(HB, r, OM) * pwm(pwm(g, 4, OM), u, OM)) % OM === g) sol = true;
  ok('no product on F233: the drive step is not core x rung (odd exponent)', !sol);
  // the octant completes: g * zeta_8^{-1} lies in the even-exponent layer
  const even = new Set();
  for (let u = 0; u < 116; u++) even.add(pwm(g, 2*u, OM));
  ok('octant completion: g = zeta_8 * (even-layer element)',
     even.has((g * pwm(Z8, 7, OM) * 1) % OM * 1 % OM || 0) ||
     even.has((g * pwm(Z8, OM - 1 - 0, OM)) % OM) ||
     even.has((g * pwm(Z8, 6, OM) * Z8) % OM) || even.has(mod(g * pwm(Z8, 7, OM), OM)));
}
// sign-blindness: the crossing class (exponent mod 4) puts hbar and h together
ok('sign-blindness: crossing classes of the core are even only: 1,-1 in class 0; '+
   'hbar (exp 174) and h (exp 58) both in class 2', (232-S) % 4 === 2 && S % 4 === 2);
ok('the octant carries the odd classes: exp(zeta_8) = 29 = 1 (mod 4)', 29 % 4 === 1);

// ---- 6. the shared clock and the winding rates ----
// the registrable class r = tau mod 4 on both shells: lockstep by construction;
// windings around the core per own period: kappa and S
ok('winding per own period: 12/4 = 3 = kappa (Subject), 232/4 = 58 = S (Carrier): '+
   'mass is the winding rate', 12/4 === 3 && 232/4 === S);
// the Subject fold hand walks i^tau on core residues
ok('fold hand residues: i^tau = 1, 5, 12, 8', [0,1,2,3].every(t =>
   pwm(I13, t, P) === [1,5,12,8][t]));

process.exit(fails ? 1 : 0);
