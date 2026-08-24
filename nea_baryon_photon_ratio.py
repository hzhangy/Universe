#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 光子-重子比 η = n_b/n_γ 修正版
"""
import numpy as np
from math import pi, sqrt, exp

# 常数
k_B = 1.380649e-23       # J/K
hbar = 1.054571817e-34   # J s
c = 299792458.0          # m/s
m_p_kg = 1.67262192369e-27  # kg
G_obs = 6.67430e-11      # m^3 kg^-1 s^-2
Omega_b_nea = 0.050957
T_CMB_nea = 2.7287       # K

# N.E.A. H0
H0_nea = 68.040 * 1e3 / 3.085677581e22  # s^-1

# 光子数密度
n_gamma = (2 * 1.202056) / (pi**2) * (k_B * T_CMB_nea / (hbar * c))**3

# 临界能量密度
rho_crit = 3 * H0_nea**2 * c**2 / (8 * pi * G_obs)

# 重子能量密度
rho_b = Omega_b_nea * rho_crit

# 重子数密度 = 能量密度 / (m_p c^2)
n_b = rho_b / (m_p_kg * c**2)

eta = n_b / n_gamma

print("="*80)
print("  N.E.A. 光子-重子比 η = n_b/n_γ 修正版")
print("="*80)
print(f"  T_CMB = {T_CMB_nea:.4f} K")
print(f"  H0_nea = {H0_nea:.6e} s^-1")
print(f"  Ω_b_nea = {Omega_b_nea:.6f}")
print(f"  光子数密度 n_γ = {n_gamma:.6e} m^-3")
print(f"  重子数密度 n_b = {n_b:.6e} m^-3")
print(f"  η = n_b/n_γ = {eta:.6e}")
print(f"  观测 η ≈ 6.1e-10")
print(f"  偏差 = {abs(eta/6.1e-10 - 1)*100:.2f}%")
print("="*80)