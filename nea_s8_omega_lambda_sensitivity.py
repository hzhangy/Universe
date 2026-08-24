#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. S8 与 Ω_Λ 敏感性诊断
"""
from math import pi, sqrt, exp, log

# N.E.A. 锁定参数
h_nea = 0.680398
sigma8_nea = 0.8094
n_s_nea = 0.965000
T_CMB_nea = 2.7287

# 拓扑比
r_nea = 0.187361

# 情况A：N.E.A. 反推 Ω_Λ
Omega_Lambda_A = 0.677070
Omega_m_A = 1 - Omega_Lambda_A
Omega_b_A = Omega_m_A * r_nea / (1 + r_nea)
Omega_c_A = Omega_m_A / (1 + r_nea)

# 情况B：观测 Ω_Λ
Omega_Lambda_B = 0.6847
Omega_m_B = 1 - Omega_Lambda_B
Omega_b_B = Omega_m_B * r_nea / (1 + r_nea)
Omega_c_B = Omega_m_B / (1 + r_nea)

def eta_from_omega_b(Omega_b, Omega_m, h):
    # 粗略 η 反算，保持与之前脚本一致的比例
    # 直接用之前 η=6.427e-10 @ Ω_b=0.050957, h=0.680398
    ref_Omega_b = 0.050957
    ref_h = 0.680398
    ref_eta = 6.427287e-10
    eta = ref_eta * (Omega_b / ref_Omega_b) * (h / ref_h)**2 / ((Omega_m / 0.322930) ** 0)  # η ∝ Ω_b h^2
    return eta

def DH_from_eta(eta):
    return 2.6e-5 * (eta / 6.0e-10)**(-1.6)

def z_eq_from(Omega_m, h):
    Omega_r_h2 = 2.469e-5 + 1.711e-5
    Omega_r = Omega_r_h2 / h**2
    return Omega_m / Omega_r - 1

# 计算
eta_A = eta_from_omega_b(Omega_b_A, Omega_m_A, h_nea)
DH_A = DH_from_eta(eta_A)
z_eq_A = z_eq_from(Omega_m_A, h_nea)
S8_A = sigma8_nea * sqrt(Omega_m_A / 0.3)

eta_B = eta_from_omega_b(Omega_b_B, Omega_m_B, h_nea)
DH_B = DH_from_eta(eta_B)
z_eq_B = z_eq_from(Omega_m_B, h_nea)
S8_B = sigma8_nea * sqrt(Omega_m_B / 0.3)

print("="*80)
print("  N.E.A. S8 与 Ω_Λ 敏感性诊断")
print("="*80)

for tag, OmL, Omm, Omb, eta, DH, zeq, S8 in [
    ("NEA Ω_Λ=0.6771", Omega_Lambda_A, Omega_m_A, Omega_b_A, eta_A, DH_A, z_eq_A, S8_A),
    ("观测 Ω_Λ=0.6847", Omega_Lambda_B, Omega_m_B, Omega_b_B, eta_B, DH_B, z_eq_B, S8_B),
]:
    print(f"\n[{tag}]")
    print(f"  Ω_m = {Omm:.6f}")
    print(f"  Ω_b = {Omb:.6f}")
    print(f"  η   = {eta:.6e}  (obs ≈6.1e-10)")
    print(f"  D/H = {DH:.5e}  (obs ≈2.55e-5)")
    print(f"  z_eq = {zeq:.2f}  (obs ≈3402)")
    print(f"  S_8 = {S8:.4f}  (Planck ≈0.832)")

print()
print("  观测参考：")
print("  S_8 ≈ 0.832 (Planck 2018), 弱透镜 ≈ 0.78-0.80")
print("="*80)