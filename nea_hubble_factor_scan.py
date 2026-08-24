#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N.E.A. 哈勃常数精确因子扫描
从 t_Tick = hbar / Z 出发，使用引力稀释因子 alpha_G = R/N_max^5，
扫描简单拓扑/几何因子，寻找能命中观测值 H0 ≈ 2.2e-18 s^-1 的组合。
"""
import numpy as np
from math import pi, sqrt, exp

# ========================
# 基础拓扑常数
# ========================
Delta   = 1 - sqrt(3)/2
R       = 1 / (1 + pi)
N_max   = exp(10 * sqrt(3))
f_geo   = 1 + Delta / (4 * pi)

# ========================
# 物理常数
# ========================
Z_MeV   = 0.406640
Z_J     = Z_MeV * 1e6 * 1.602176634e-19
hbar_SI = 1.054571817e-34

# ========================
# 观测哈勃常数 (s^-1)
# H0 ≈ 70 km/s/Mpc
# ========================
H0_obs = 70.0 * 1e3 / 3.085677581e22  # 约 2.27e-18 s^-1
# 更常用：H0 ≈ 2.2e-18 s^-1
H0_obs = 2.2e-18

# ========================
# 原生 Tick 时间
# ========================
t_Tick = hbar_SI / Z_J

# ========================
# 候选因子库
# ========================
factors = {
    '1': 1.0,
    '2': 2.0,
    '3': 3.0,
    'pi': pi,
    '4pi': 4*pi,
    '1/(4pi)': 1/(4*pi),
    'R': R,
    '1/R': 1/R,
    'sqrt(R)': np.sqrt(R),
    '1/sqrt(R)': 1/np.sqrt(R),
    '1+R': 1+R,
    '1/(1+R)': 1/(1+R),
    'f_geo': f_geo,
    '1/f_geo': 1/f_geo,
    'Delta': Delta,
    '1/Delta': 1/Delta,
    '12/6': 12/6,
    'sqrt(3)': sqrt(3),
    '2sqrt3/pi': 2*sqrt(3)/pi,
    'pi/2': pi/2,
}

# ========================
# 扫描
# ========================
print("="*80)
print("  哈勃常数精确因子扫描")
print("="*80)
print(f"  t_Tick = {t_Tick:.6e} s")
print(f"  1/t_Tick = {1/t_Tick:.6e} s^-1")
print(f"  H0_obs  = {H0_obs:.6e} s^-1")
print()

# 核心：H0_core = (1/t_Tick) * alpha_G = (1/t_Tick) * (R/N_max^5)
alpha_G = R / (N_max ** 5)
H0_core = (1 / t_Tick) * alpha_G

print(f"  alpha_G = {alpha_G:.6e}")
print(f"  H0_core = {H0_core:.6e} s^-1")
print(f"  H0_core / H0_obs = {H0_core/H0_obs:.4f}")
print()

# 使用两个因子乘积
best = None
best_ratio = None

keys = list(factors.keys())
for i in range(len(keys)):
    for j in range(i, len(keys)):
        f1 = factors[keys[i]]
        f2 = factors[keys[j]]
        H0 = H0_core * f1 * f2
        ratio = H0 / H0_obs

        log_dev = abs(np.log10(ratio))
        if best_ratio is None or log_dev < best_ratio:
            best_ratio = log_dev
            best = (keys[i], keys[j], f1, f2, H0, ratio)

if best:
    name1, name2, f1, f2, H0, ratio = best
    print(f"  最优双因子组合：")
    print(f"    {name1} × {name2}")
    print(f"    H0 = {H0:.6e} s^-1")
    print(f"    ratio = {ratio:.6e}")
    print(f"    log10(ratio) = {np.log10(ratio):.4f}")
    print()

print("="*80)
print("  扫描完成。")
print("="*80)