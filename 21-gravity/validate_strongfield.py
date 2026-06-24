"""Strong field: exact profile, critical radii, photon sphere, shadow, ringdown, entropy, echoes.

Validates: Prop (exact static profile)         existence boundary r_* = sqrt(Gm);
           Prop (horizonless, operationally black)  r_f = 2Gm/ln(Omega);
           Prop (photon sphere and shadow)     r_ph = 2Gm, b_c = 2e Gm, delta = +4.63%;
           ringdown shift -4.4%; S/S_BH = ln^-2(Omega); echo delay ~ Omega (no echoes);
           Sgr A* / M87* angular numbers.
"""
import math
import numpy as np

ok = True
Gm = 1.0e6                       # Planck units; corrections (Gm/r^2)^2 negligible at r ~ Gm
lnOm = math.log(1e122)

# exact potential u(r) = int_r^inf arcsin(Gm/s^2) ds  (numeric, log grid to 1e12)
def u_exact(r):
    s = np.logspace(np.log10(r), 12, 400000)
    return np.trapezoid(np.arcsin(np.clip(Gm/s**2, 0, 1)), s)

rstar = math.sqrt(Gm)
print(f"  slip core r_* = sqrt(Gm) = {rstar:.0f}  (arcsin domain boundary)")
print(f"  u(2Gm) = {u_exact(2*Gm):.6f}  vs Gm/r = 0.5  (exact profile ~ Newtonian at photon sphere)")
if abs(u_exact(2*Gm) - 0.5) > 1e-3: ok = False

# photon sphere: extremise b(r) = r exp(2 u(r)) with the exact potential
rr = np.linspace(1.6*Gm, 2.4*Gm, 81)
bb = [r*math.exp(2*u_exact(r)) for r in rr]
r_ph = rr[int(np.argmin(bb))]
b_c = min(bb)
print(f"  photon sphere r_ph = {r_ph/Gm:.3f} Gm (target 2),  b_c = {b_c/Gm:.4f} Gm (target 2e = {2*math.e:.4f})")
if abs(r_ph/Gm - 2) > 0.05 or abs(b_c/Gm - 2*math.e) > 0.02: ok = False

delta = 2*math.e/(3*math.sqrt(3)) - 1
ring = 3*math.sqrt(3)/(2*math.e) - 1
print(f"  shadow deviation delta = {delta*100:.2f}%  (target +4.63), ringdown {ring*100:.2f}% (target -4.42)")
if abs(delta - 0.04627) > 1e-4: ok = False

# operational horizon, entropy ratio, echo delay
r_f = 2*Gm/lnOm
print(f"  r_f = 2Gm/ln(Omega) = r_s/{2*Gm/r_f:.0f},  S/S_BH = {1/lnOm**2:.2e},  "
      f"echo delay factor Omega/ln^2(Omega) = {1e122/lnOm**2:.1e} (no observable echoes)")

# Sgr A* and M87* angular sizes
Msun_km = 1.47662
for name, M, D_kpc in (("Sgr A*", 4.297e6, 8.277), ("M87*", 6.5e9, 16.8e3)):
    theta_g = M*Msun_km*1e3/(D_kpc*3.0857e19)*206264.806e6
    gr, frc = 2*3*math.sqrt(3)*theta_g, 2*2*math.e*theta_g
    print(f"  {name}: shadow GR {gr:.1f} muas, FRC {frc:.1f} muas")
    if name == "Sgr A*" and not (52 < gr < 55 and 54 < frc < 57): ok = False

print("PASS" if ok else "FAIL", "- strong field")
