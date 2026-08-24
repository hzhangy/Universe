#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 声学峰间隔 ℓ_A = π / θ_*
"""
from math import pi

# 来自之前 N.E.A. 结果
theta_star_nea = 0.010869   # rad
ell1_nea = 220.4276

# 声学峰间隔
ell_A_nea = pi / theta_star_nea

# 观测近似
ell_A_obs = 300.0   # 典型声学峰间隔
ell1_obs = 220.6
ratio_nea = ell1_nea / ell_A_nea
ratio_obs = ell1_obs / ell_A_obs

print("="*80)
print("  N.E.A. 声学峰间隔 ℓ_A")
print("="*80)
print(f"  θ_* = {theta_star_nea:.6f} rad")
print(f"  ℓ_A = π / θ_* = {ell_A_nea:.2f}")
print(f"  观测 ℓ_A ≈ {ell_A_obs:.0f}")
print(f"  偏差 = {abs(ell_A_nea/ell_A_obs - 1)*100:.2f}%")
print()
print(f"  ℓ_1 / ℓ_A (NEA) = {ratio_nea:.4f}")
print(f"  ℓ_1 / ℓ_A (obs) = {ratio_obs:.4f}")
print(f"  比值偏差 = {abs(ratio_nea/ratio_obs - 1)*100:.2f}%")
print("="*80)