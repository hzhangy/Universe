#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 暗能量密度验证：从拓扑 H0 和 G 推导 rho_Lambda
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
m_p_kg = 1.67262192369e-27

# 观测值
H0_obs = 2.2e-18          # s^-1
rho_obs = 6.0e-10         # J/m^3
Omega_Lambda_obs = 0.68   # 近似

# 1. 拓扑 H0
t_Tick = hbar_SI / Z_J
alpha_G = R / (N_max**5)
# 1. 修正 H0
H0_nea = (1 / t_Tick) * alpha_G * np.sqrt(R) * (1 + R) / f_geo

print("="*80)
print("  从拓扑 H0 和 G 推导暗能量密度")
print("="*80)
print(f"  H0_nea = {H0_nea:.6e} s^-1")
print(f"  H0_obs = {H0_obs:.6e} s^-1")
print(f"  偏差 = {abs(H0_nea/H0_obs-1)*100:.3f}%")
print()

# 2. 拓扑 m_p
m_p_nea = Z_MeV * f_geo * (np.sqrt(R)/(1+R)) * np.sqrt(N_max)  # MeV
m_p_kg_nea = m_p_nea * 1e6 * 1.602176634e-19 / c_SI**2  # kg
print(f"  m_p_nea = {m_p_nea:.4f} MeV")
print(f"  m_p_obs = {m_p_MeV:.4f} MeV")
print(f"  偏差 = {abs(m_p_nea/m_p_MeV-1)*100:.3f}%")
print()

# 3. 拓扑 G
G_nea = (R / (N_max**5)) * (hbar_SI * c_SI) / (m_p_kg_nea**2)
print(f"  G_nea  = {G_nea:.6e} m^3 kg^-1 s^-2")
print(f"  G_obs  = {6.67430e-11:.6e} m^3 kg^-1 s^-2")
print(f"  偏差 = {abs(G_nea/6.67430e-11-1)*100:.3f}%")
print()

# 4. 从 H0 和 G 推导 rho_Lambda
rho_Lambda_nea = (3 * H0_nea**2 * c_SI**2) / (8 * pi * G_nea) * Omega_Lambda_obs
print("="*80)
print("  暗能量密度")
print("="*80)
print(f"  rho_Lambda_nea = {rho_Lambda_nea:.6e} J/m^3")
print(f"  rho_obs       = {rho_obs:.6e} J/m^3")
print(f"  ratio         = {rho_Lambda_nea/rho_obs:.4f}")
print(f"  log10(ratio)  = {np.log10(rho_Lambda_nea/rho_obs):.4f}")
print()