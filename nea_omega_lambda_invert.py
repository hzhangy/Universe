#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 反推 Ω_Λ
用拓扑 H0 和拓扑 G，从观测暗能量密度 rho_obs 反推 Ω_Λ
"""
import numpy as np
from math import pi, sqrt, exp

# 拓扑常数
Delta = 1 - sqrt(3)/2
R = 1 / (1 + pi)
N_max = exp(10 * sqrt(3))
f_geo = 1 + Delta / (4 * pi)

# 物理常数
Z_MeV = 0.406640
Z_J = Z_MeV * 1e6 * 1.602176634e-19
hbar_SI = 1.054571817e-34
c_SI = 299792458.0
m_p_MeV = 938.272

# 观测值
H0_obs = 2.2e-18        # s^-1
rho_obs = 6.0e-10       # J/m^3
Omega_Lambda_obs = 0.68 # Planck 近似

# 1. 拓扑 H0（含 f_geo 修正）
t_Tick = hbar_SI / Z_J
alpha_G = R / (N_max**5)
H0_nea = (1 / t_Tick) * alpha_G * np.sqrt(R) * (1 + R) / f_geo

# 2. 拓扑 m_p
m_p_nea = Z_MeV * f_geo * (np.sqrt(R)/(1+R)) * np.sqrt(N_max)  # MeV
m_p_kg_nea = m_p_nea * 1e6 * 1.602176634e-19 / c_SI**2  # kg

# 3. 拓扑 G
G_nea = (R / (N_max**5)) * (hbar_SI * c_SI) / (m_p_kg_nea**2)

# 4. 反推 Ω_Λ
# rho_Λ = 3 H0^2 c^2 / (8π G) * Ω_Λ
# → Ω_Λ = 8π G rho_obs / (3 H0^2 c^2)
Omega_Lambda_nea = (8 * pi * G_nea * rho_obs) / (3 * H0_nea**2 * c_SI**2)

print("="*80)
print("  N.E.A. 反推 Ω_Λ")
print("="*80)
print(f"  拓扑 H0 = {H0_nea:.6e} s^-1")
print(f"  拓扑 G  = {G_nea:.6e} m^3 kg^-1 s^-2")
print()
print(f"  反推 Ω_Λ(nea) = {Omega_Lambda_nea:.6f}")
print(f"  观测 Ω_Λ(obs) = {Omega_Lambda_obs:.6f}")
print(f"  比值 = {Omega_Lambda_nea/Omega_Lambda_obs:.4f}")
print(f"  偏差 = {abs(Omega_Lambda_nea/Omega_Lambda_obs-1)*100:.3f}%")
print("="*80)