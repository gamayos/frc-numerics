// Production-render verification for 1-phase-2: loads index.html itself,
// runs the three production draw functions in a canvas-recording sandbox,
// and checks the rendered output -- positions, labels, counts, and the
// Carrier-view continuity -- against the exact laws. This suite consumes
// the production code directly; any FAIL exits nonzero.
// Run: node verify-render.js   (from the episode directory)
'use strict';
const fs = require('fs'), vm = require('vm');
let fails = 0;
const ok = (name, cond) => { console.log((cond ? 'PASS ' : 'FAIL ') + name); if (!cond) fails++; };

const html = fs.readFileSync(__dirname + '/index.html', 'utf8');
const src = html.replace(/^[\s\S]*?<script>\n/m, '').replace(/<\/script>[\s\S]*$/m, '');
const recs = { sph: [], rings: [], spc: [] };
const mk = tag => { let style = '', alpha = 1;
  return new Proxy({}, {
    get: (t, p) => {
      if (p === 'measureText') return () => ({ width: 0 });
      return (...a) => {
        if (p === 'fillText') recs[tag].push(['txt', String(a[0]), a[1], a[2]]);
        if (p === 'stroke' || p === 'fill') recs[tag].push([p, style, alpha]);
        if (p === 'ellipse') recs[tag].push(['ell', a[0], a[1], a[2], a[3], a[4]]);
        if (p === 'arc') recs[tag].push(['arc', a[0], a[1], a[2]]);
        if (p === 'lineTo') recs[tag].push(['seg']);
        return undefined; };
    },
    set: (t, p, v) => { if (p === 'strokeStyle' || p === 'fillStyle') style = v;
      if (p === 'globalAlpha') alpha = v; return true; } }); };
const els = {};
const el = id => els[id] ||= (() => {
  const e = { getContext: () => mk(recs[id] ? id : 'spc'), setAttribute: () => {},
              value: 5, style: {}, className: '' };
  Object.defineProperty(e, 'onclick', { set(){}, get(){ return null; } });
  Object.defineProperty(e, 'textContent', { set(){}, get(){ return ''; } });
  return e; })();
const sandbox = { document: { getElementById: el }, requestAnimationFrame: () => {}, Math, console, Proxy };
vm.createContext(sandbox);
vm.runInContext(src, sandbox);

const render = (v, s, c, sg, mode) => { for (const k in recs) recs[k].length = 0;
  vm.runInContext(`view = "${v}"; tS = ${s}; tC = ${c}; sigC = ${sg || 0};` +
    `skyMode = "${mode || 'helix'}";` +
    'drawSphere(tS, tC); drawRings(tS, tC); drawSpace(tS, tC);', sandbox); };

// 1. the full pair sweep, both views, three panels
let swept = true;
try {
  for (const mode of ['helix', 'hopf'])
    for (const v of ['subject', 'carrier'])
      for (let t = 0; t < 696; t++)
        render(v, t % 12, t % 232, Math.floor(t / 232) % 2, mode);
} catch (e) { swept = false; }
ok('the full 696-state pair sweep renders all three panels, both views, '+
   'both sky representations', swept);

// 2. captions live under the panels: the canvases carry geometry only
render('subject', 0, 0);
const foot = k => recs[k].filter(r => r[0] === 'txt' && r[3] >= 478 &&
                                 (r[2] <= 20 || r[2] >= 500)).length;
ok('the canvases carry no caption text: geometry and data labels only',
   foot('sph') + foot('rings') + foot('spc') === 0);

// 3. the sky labels match the exact law from the production rendering
const md = (a, n) => ((a % n) + n) % n;
const ORB = vm.runInContext('ORB.slice()', sandbox);
const lab = recs.spc.filter(r => r[0] === 'txt' && /^\d+$/.test(r[1]) && r[1] !== '0');
const want = [];
for (const e of [1, -1]) for (let k = 1; k <= 12; k++)
  want.push((md(e * k, 13) * ORB[md(0 - k, 12)]) % 13);
const ms = xs => xs.map(String).sort().join();
ok('the outer fiber\'s twenty-four labels match the exact retarded values',
   lab.length === 24 && ms(lab.map(r => +r[1])) === ms(want));

// 4. the sky closures on the rendered positions, at a fixed Carrier
// state (the drive isolated from the leak): in the Carrier view the
// drive turns the sky -- half a circuit at t24 + 12, the antipodal
// spinor sign, closure at t24 + 24; in the Subject view the drive is
// hidden by re-registration -- the same three states render
// identically
const pos = rs => rs.filter(r => r[0] === 'txt' && /^\d+$/.test(r[1]) && r[1] !== '0')
  .map(r => Math.round(r[2]) + ',' + Math.round(r[3])).sort().join();
render('carrier', 0, 0);  const C0 = pos(recs.spc);
render('carrier', 6, 0);  const C6 = pos(recs.spc);
render('carrier', 12, 0); const C12 = pos(recs.spc);
ok('the double cover on the rendered sky (Carrier view, fixed Carrier '+
   'state): positions close at t24 + 24 and stand antipodal at t24 + 12',
   C12 === C0 && C6 !== C0);
render('subject', 0, 0);   const S0 = pos(recs.spc);
render('subject', 1, 0);   const S1 = pos(recs.spc);
render('subject', 6, 0);   const S6 = pos(recs.spc);
render('subject', 12, 0);  const S12 = pos(recs.spc);
render('subject', 5, 117); const SB = pos(recs.spc);
render('subject', 3, 51, 1); const SC = pos(recs.spc);
ok('the Subject view holds the register: the sky geometry is fully '+
   'static -- identical across every drive phase, Carrier tick, and '+
   'sheet -- with the values walking through it',
   S1 === S0 && S6 === S0 && S12 === S0 && SB === S0 && SC === S0 &&
   S0.length > 0);

// 5. the wrap continuity: the leak is a half-angle on the Carrier's
// spinor cover, carried by the sheet sigC; across the wrap (tau 695
// -> 696) every Carrier-view label moves by a small step, with no
// 180-degree branch jump; the Subject view stands exactly
const labxy = rs => { const m = new Map();
  rs.filter(r => r[0] === 'txt' && /^\d+$/.test(r[1]) && r[1] !== '0')
    .forEach((r, i) => m.set(i, [r[2], r[3]])); return m; };
const step = v => {
  render(v, 11, 231, 0); const A = labxy(recs.spc);
  render(v, 0, 0, 1);    const B = labxy(recs.spc);
  let maxstep = 0;
  for (const [i, a] of A){ const b = B.get(i);
    if (b) maxstep = Math.max(maxstep, Math.hypot(b[0]-a[0], b[1]-a[1])); }
  return maxstep;
};
const cStep = step('carrier'), sStep = step('subject');
ok('the wrap: the Carrier sky steps continuously through tau 695 -> '+
   '696 (a single-step size under 80 px, the sheet carrying the '+
   'half-angle branch) and the Subject sky stands exactly',
   cStep > 0 && cStep < 80 && sStep === 0);

// 6. panel activity: all three panels draw substantively
render('carrier', 3, 51, 0);
ok('all three panels draw substantively in the Carrier view',
   recs.sph.length > 100 && recs.rings.length > 200 && recs.spc.length > 200);

// 7. the Hopf representation: the lit fibers carry the exact values
render('subject', 0, 0, 0, 'hopf');
const hlab = recs.spc.filter(r => r[0] === 'txt' && /^\d+$/.test(r[1]) && r[1] !== '0');
const hwant = [];
for (let k = 1; k <= 12; k++) for (const e of [1, -1]){
  const m = md(0 - k, 12), b = md(e * k, 13);
  hwant.push((b * ORB[m]) % 13);
}
ok('the Hopf mode lights twenty-four fibers labelled with the exact '+
   'event values (m, b) -> b g^m', hlab.length === 24 &&
   ms(hlab.map(r => +r[1])) === ms(hwant));
render('subject', 5, 5, 0, 'hopf');
const hlab2 = recs.spc.filter(r => r[0] === 'txt' && /^\d+$/.test(r[1]) && r[1] !== '0');
const hwant2 = [];
for (let k = 1; k <= 12; k++) for (const e of [1, -1]){
  const m = md(5 - k, 12), b = md(e * k, 13);
  hwant2.push((b * ORB[m]) % 13);
}
ok('the Hopf lighting follows the drive: at another chronon the lit '+
   'values track (tau - k, ek) exactly', hlab2.length === 24 &&
   ms(hlab2.map(r => +r[1])) === ms(hwant2));

// 9. the leaves in the helix guide style at half strength: 24
// outer-rung leaves, each split into a front and a back primitive
// elliptical arc (48 arc strokes), guide grey, front alpha 0.35 and
// back 0.12 -- half the helix loop convention -- with no fiber
// voxels; the inner-rung leaves
// hidden; the only line segments are the node arrows, the polar axis,
// and the observer's degenerate leaf (72 x 3 + 2 = 218); every leaf
// bounded by the chart silhouette
let ellOK = true;
for (const [v, s, c, sg] of [['subject',0,0,0],['subject',7,113,0],['carrier',11,231,1]]){
  render(v, s, c, sg, 'hopf');
  const ells = recs.spc.filter(r => r[0] === 'ell');
  const nseg = recs.spc.filter(r => r[0] === 'seg').length;
  const rimOK = ells.every(r =>
    Math.hypot(r[1]-260, r[2]-260) + Math.max(r[3], r[4]) < 300);
  const pairs = [];
  for (let i = 0; i < recs.spc.length - 1; i++)
    if (recs.spc[i][0] === 'ell' && recs.spc[i+1][0] === 'stroke')
      pairs.push({ style: recs.spc[i+1][1], alpha: recs.spc[i+1][2] });
  const nF = pairs.filter(p => Math.abs(p.alpha - 0.35) < 1e-9).length;
  const nB = pairs.filter(p => Math.abs(p.alpha - 0.12) < 1e-9).length;
  const greyOK = pairs.every(p => p.style === '#8a877f');
  const vox = recs.spc.filter(r => r[0] === 'arc' && r[3] < 1.2).length;
  if (ells.length !== 48 || pairs.length !== 48 || nF !== 24 || nB !== 24 ||
      !greyOK || nseg !== 218 || !rimOK || vox !== 0) ellOK = false;
}
ok('the Hopf leaves ride the helix guide style at half alpha: 24 '+
   'outer-rung leaves as 48 primitive front/back arcs, guide grey, '+
   'alphas 0.35/0.12, no fiber voxels, inner-rung leaves hidden, the '+
   'observer on the degenerate axis leaf, every leaf bounded by the '+
   'chart silhouette', ellOK);

// 10. the section test: at a paused state the two representations
// share every node dot and every label exactly -- the toggle switches
// the fibers and only the fibers
let invOK = true;
for (const [v, s, c, sg] of [['subject',0,0,0],['subject',7,113,0],['carrier',11,231,1]]){
  const grab = mode => { render(v, s, c, sg, mode);
    return {
      labs: recs.spc.filter(r => r[0] === 'txt')
        .map(r => r[1] + '@' + r[2].toFixed(2) + ',' + r[3].toFixed(2))
        .sort().join('|'),
      dots: recs.spc.filter(r => r[0] === 'arc' && r[3] > 1.2)
        .map(r => r[1].toFixed(2) + ',' + r[2].toFixed(2) + ',' + r[3].toFixed(2))
        .sort().join('|') }; };
  const H = grab('helix'), F = grab('hopf');
  if (!(H.labs === F.labs && H.dots === F.dots && H.dots.length > 0)) invOK = false;
}
ok('the section test: pausing and toggling the representation keeps '+
   'every node dot and every label fixed; only the fibers change',
   invOK);

// 11. the helix guide loops are single strokes: two depth passes per
// shell, six grey strokes in all -- no per-segment strokes, so the
// joints carry no segment overlaps
let helixOK = true;
for (const [v, s, c, sg] of [['subject',0,0,0],['carrier',5,117,1]]){
  render(v, s, c, sg, 'helix');
  const grey = recs.spc.filter(r => r[0] === 'stroke' && r[1] === '#8a877f');
  if (grey.length !== 6) helixOK = false;
}
ok('the helix guide loops draw as six single strokes (two depth '+
   'passes per shell), with no per-segment stroking', helixOK);

// 12. the frame leak (00:C17, 00:C18): each view holds its own frame.
// Subject view: the register stands (east slot reads 1 at every bC)
// and the Carrier chart turns counterclockwise -- hbar = 144 (the
// i-oriented quarter) on top at bC = 0, and after the S = 58 quarter
// the Carrier's h = 89 arrives at the register's 1 (east). Carrier
// view: the quarters stand (hbar on top at every bC), the q hand of
// the glued q/p dial stands at east, and the register drifts
// clockwise: its i = 5 arrives at q (east) at bC = 58 -- the Fourier
// x hbar exchange
const near = (rs, x, y, tol) => rs.filter(r => r[0] === 'txt' &&
  Math.hypot(r[2] - x, r[3] - y) < tol).map(r => r[1]);
const HBAR = 'ħ = 144', H = 'h = 89';
let leakOK = true;
{
  render('subject', 0, 0);
  const sTop0 = near(recs.rings, 260, 39, 8);
  const sReg0 = near(recs.rings, 408, 260, 8);
  const sQ0 = near(recs.rings, 64 + 39, 66, 8);
  render('subject', 0, 58);
  const sReg1 = near(recs.rings, 408, 260, 8);
  const sChart1 = near(recs.rings, 481, 260, 8);
  const sQ1 = near(recs.rings, 64, 66 + 39, 8);
  render('carrier', 0, 0);
  const cTop0 = near(recs.rings, 260, 39, 8);
  const cQ0 = near(recs.rings, 64 + 39, 66, 8);
  render('carrier', 0, 58);
  const cTop1 = near(recs.rings, 260, 39, 8);
  const cQ1 = near(recs.rings, 64, 66 + 39, 8);
  const cReg1 = near(recs.rings, 408, 260, 8);
  leakOK = sTop0.join() === HBAR &&
           sReg0.includes('1') && sReg1.includes('1') &&
           sChart1.join() === H &&
           sQ0.includes('q') && sQ1.includes('q') &&
           cTop0.join() === HBAR && cTop1.join() === HBAR &&
           cQ0.includes('q') && cQ1.includes('q') &&
           cReg1.some(t => t.includes('i = 5'));
}
ok('the frame leak: the Subject view holds the register (east reads '+
   '1 at every bC) while the Carrier chart turns counterclockwise, h '+
   'reaching east at bC = 58; the Carrier view holds the quarters '+
   '(hbar on top) while the register drifts clockwise, its i = 5 '+
   'reaching east at bC = 58; the q/p dial reads identically in both '+
   'views, q sweeping clockwise to the h cardinal (south) at bC = 58',
   leakOK);

// 13. the drive sense is one across the panels: in the Carrier view
// the sky's world azimuth steps clockwise with the drive, matching
// the shell's frame sweep and the chart hand -- from tau = 0 to tau
// = 4 the k = 1 node advances -(4 x 15 deg) plus the small drift,
// the same sign and quarter-step as the rings' hand
const senseP = vm.runInContext(`
(() => {
  view = "carrier"; sigC = 0;
  const n0 = skyState(0, 0).nodes.find(n => n.outer && n.e === 1 && n.k === 1);
  const n1 = skyState(4, 4).nodes.find(n => n.outer && n.e === 1 && n.k === 1);
  const a0 = Math.atan2(n0.w[1], n0.w[0]), a1 = Math.atan2(n1.w[1], n1.w[0]);
  let d = a1 - a0;
  while (d > Math.PI) d -= 2*Math.PI;
  while (d < -Math.PI) d += 2*Math.PI;
  return d;
})()`, sandbox);
ok('the drive sense is one across the panels: the Carrier-view sky '+
   'steps clockwise with the drive, one quarter-step from tau = 0 to '+
   'tau = 4 within a drift margin, as on the shell and the chart',
   senseP < 0 && Math.abs(senseP + Math.PI/3) < 0.12);

// 14. the interpolated mode is exact at the endpoints and on-tick in
// its data: the sub-chronon fraction moves geometry linearly (the
// midpoint azimuth is the exact average of the two tick azimuths, and
// frac = 1 reproduces the next tick's geometry), the quarter class
// advances by exactly +1 per chronon for every node (the arrow
// handoff), and no label or tint reads the fraction
const interpP = vm.runInContext(`
(() => {
  view = "carrier"; sigC = 0;
  const ang = S => { const n = S.nodes.find(n => n.outer && n.e === 1 && n.k === 1);
    return Math.atan2(n.w[1], n.w[0]); };
  frac = 0;   const a0 = ang(skyState(0, 0));
  frac = 0;   const a1 = ang(skyState(1, 1));
  frac = 0.5; const am = ang(skyState(0, 0));
  frac = 1;   const ah = ang(skyState(0, 0));
  frac = 0;
  const w = x => { let d = x; while (d > Math.PI) d -= 2*Math.PI;
                   while (d < -Math.PI) d += 2*Math.PI; return d; };
  let clsOK = true;
  for (let tau = 0; tau < 12; tau++){
    const A = skyState(tau % 12, tau % 232).nodes;
    const B = skyState((tau + 1) % 12, (tau + 1) % 232).nodes;
    for (let i = 0; i < A.length; i++)
      if (B[i].cls !== (A[i].cls + 1) % 4) clsOK = false;
  }
  return { mid: Math.abs(w(am - (a0 + w(a1 - a0)/2))),
           hand: Math.abs(w(ah - a1)), clsOK };
})()`, sandbox);
render('subject', 3, 51, 0);
const L0 = recs.spc.filter(r => r[0] === 'txt').map(r => r[1]).sort().join('|');
vm.runInContext('frac = 0.5', sandbox);
render('subject', 3, 51, 0);
const Lh = recs.spc.filter(r => r[0] === 'txt').map(r => r[1]).sort().join('|');
const D0 = pos(recs.spc);
vm.runInContext('frac = 0', sandbox);
render('subject', 3, 51, 0);
ok('the interpolated mode: midpoint geometry is the exact average of '+
   'the tick geometries, frac = 1 hands off to the next tick, the '+
   'quarter class steps +1 per chronon everywhere, and the labels and '+
   'the Subject-view positions read the tick alone',
   interpP.mid < 1e-9 && interpP.hand < 1e-9 && interpP.clsOK &&
   Lh === L0 && D0 === pos(recs.spc));

console.log(fails ? `\n${fails} FAILURES` : '\nall checks pass');
process.exit(fails ? 1 : 0);
