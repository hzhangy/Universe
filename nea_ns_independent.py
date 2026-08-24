#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nea_ns_independent.py
独立计算谱指数 n_s，不使用观测 n_s 作为输入。

逻辑链：
1. 拓扑常数
2. 带宽磨损 f_ext(x) = 4/5 - x/100
3. 退耦条件 f_ext(x_dec) = 1/U_EM  => x_dec
4. 投影锁 x_gen = x_dec * (2√3/π)   => x_gen
5. 慢滚参数 ε = 3*(x/100) / f_ext(x)
   - 因子 3：三维体积对数导数
   - x/100：带宽磨损项
   - f_ext：当前外部带宽
6. n_s = 1 - 2 ε

最终得到 n_s，与 Planck 观测比较。
"""
import numpy as np
from math import pi, sqrt

# ---------- 拓扑常数 ----------
U_EM    = 0.4 * pi
U_weak  = 10.0 * sqrt(3.0)
N_max   = np.exp(U_weak)
R       = 1.0 / (1.0 + pi)
Delta   = 1.0 - sqrt(3.0) / 2.0

# ---------- 带宽磨损方程 ----------
def f_ext(x):
    return 4.0 / 5.0 - x / 100.0

# ---------- 1. 退耦点 ----------
# 由 f_ext(x_dec) = 1/U_EM 解出 x_dec
f_dec = 1.0 / U_EM
x_dec = 100.0 * (4.0 / 5.0 - f_dec)

# ---------- 2. 投影锁 ----------
# x_gen / x_dec = 2√3/π
proj = 2.0 * sqrt(3.0) / pi
x_gen = x_dec * proj

# ---------- 3. 慢滚参数 ----------
f_at_gen = f_ext(x_gen)
wear     = x_gen / 100.0
epsilon  = 3.0 * wear / f_at_gen

# ---------- 4. 谱指数 ----------
ns = 1.0 - 2.0 * epsilon

# ---------- 观测值 ----------
ns_obs = 0.9649

print("="*72)
print("  N.E.A. 谱指数独立计算")
print("="*72)
print(f"  拓扑常数:")
print(f"    U_EM   = {U_EM:.6f}")
print(f"    U_weak = {U_weak:.6f}")
print(f"    N_max  = {N_max:.6e}")
print()
print(f"  1. 退耦条件:")
print(f"     f_dec = 1/U_EM = {f_dec:.6f}")
print(f"     x_dec = 100*(4/5 - f_dec) = {x_dec:.6f}")
print()
print(f"  2. 投影锁:")
print(f"     proj = 2√3/π = {proj:.6f}")
print(f"     x_gen = x_dec * proj = {x_gen:.6f}")
print()
print(f"  3. 慢滚参数:")
print(f"     f_ext(x_gen) = {f_at_gen:.6f}")
print(f"     wear = x_gen/100 = {wear:.6f}")
print(f"     ε = 3*wear/f_ext = {epsilon:.6f}")
print()
print(f"  4. 谱指数:")
print(f"     n_s = 1 - 2ε = {ns:.6f}")
print()
print(f"  观测:  n_s = {ns_obs}")
print(f"  偏差:  {abs(ns - ns_obs)/ns_obs*100:.4f}%")
print("="*72)