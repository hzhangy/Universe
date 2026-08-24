#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 宇宙学平坦性审计与 Ω 参数估计
"""
import numpy as np
from math import pi, sqrt, exp

# 拓扑常数
Delta = 1 - sqrt(3)/2
R = 1/(1+pi)
N_max = exp(10*sqrt(3))
f_geo = 1 + Delta/(4*pi)

# 物理常数
Z_MeV = 0.406640
Z_J = Z_MeV * 1e6 * 1.602176634e-19
hbar_SI = 1.054571817e-34
c_SI = 299792458.0
m_p_MeV = 938.272

# 观测值（Planck 2018 近似）
H0_obs = 2.1927e-18       # s^-1，约 67.66 km/s/Mpc
Omega_Lambda_obs = 0.6847
Omega_b_obs = 0.0490
Omega_c_obs = 0.2610

# 1. 拓扑 H0, m_p, G
t_Tick = hbar_SI / Z_J
alpha_G = R / (N_max**5)
H0_nea = (1/t_Tick) * alpha_G * sqrt(R) * (1+R) / f_geo

m_p_nea_MeV = Z_MeV * f_geo * (sqrt(R)/(1+R)) * sqrt(N_max)
m_p_nea_kg = m_p_nea_MeV * 1e6 * 1.602176634e-19 / c_SI**2

G_nea = alpha_G * (hbar_SI * c_SI) / (m_p_nea_kg**2)

# 2. 平坦性：Ω_Λ + Ω_m = 1
# ρ_crit = 3 H0^2 c^2 / (8π G)
rho_crit_nea = 3 * H0_nea**2 * c_SI**2 / (8 * pi * G_nea)
# 如果 ρ_Λ = ρ_crit * Ω_Λ，则 Ω_Λ 可直接反推
Omega_Lambda_nea = (8 * pi * G_nea * rho_crit_nea) / (3 * H0_nea**2 * c_SI**2) * (Omega_Lambda_obs)  # 这显然是Ω_Λ_obs

# 更简单：直接用观测 ρ_Λ = rho_crit(obs) * Ω_Λ_obs
rho_crit_obs = 3 * H0_obs**2 * c_SI**2 / (8 * pi * G_nea)
rho_Lambda_obs = rho_crit_obs * Omega_Lambda_obs

Omega_Lambda_from_obs = (8 * pi * G_nea * rho_Lambda_obs) / (3 * H0_nea**2 * c_SI**2)

print("="*80)
print("  N.E.A. 宇宙学平坦性审计")
print("="*80)
print(f"  H0_nea = {H0_nea:.6e} s^-1   (obs {H0_obs:.6e})")
print(f"  m_p_nea = {m_p_nea_MeV:.4f} MeV")
print(f"  G_nea = {G_nea:.6e} m^3 kg^-1 s^-2")
print()
print(f"  rho_crit(nea) = {rho_crit_nea:.6e} J/m^3")
print(f"  rho_crit(obs) = {rho_crit_obs:.6e} J/m^3")
print()

# 3. 用观测 ρ_Λ 反推 Ω_Λ
Omega_Lambda_nea = (8 * pi * G_nea * rho_Lambda_obs) / (3 * H0_nea**2 * c_SI**2)
print(f"  用观测 ρ_Λ 反推 Ω_Λ(nea) = {Omega_Lambda_nea:.6f}")
print(f"  观测 Ω_Λ = {Omega_Lambda_obs:.6f}")
print(f"  偏差 = {abs(Omega_Lambda_nea/Omega_Lambda_obs-1)*100:.3f}%")
print()

# 4. 平坦性：1 - Ω_Λ 应等于 Ω_b + Ω_c
Omega_m_nea = 1 - Omega_Lambda_nea
print(f"  平坦性给出 Ω_m(nea) = {Omega_m_nea:.6f}")
print(f"  观测 Ω_b + Ω_c = {Omega_b_obs+Omega_c_obs:.6f}")
print(f"  偏差 = {abs(Omega_m_nea/(Omega_b_obs+Omega_c_obs)-1)*100:.3f}%")
print()

print("="*80)