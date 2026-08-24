#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nea_ratio_projection_test.py
检验 x_gen / x_dec 是否由投影因子 2√3/π 锁定
"""
import numpy as np
from math import pi, sqrt

sqrt3 = sqrt(3)

U_EM = 0.4 * pi
a = 4/5
b = 1/100

# 退耦点由 f_ext = 1/U_EM 决定
f_dec = 1/U_EM
x_dec = 100*(a - f_dec)

# 假设 x_gen = x_dec * (2√3/π)
projection = 2*sqrt3/pi
x_gen_pred = x_dec * projection

# 从这个 x_gen 计算 n_s
f_gen = a - b*x_gen_pred
eps_gen = 3*b*x_gen_pred/f_gen
ns_pred = 1 - 2*eps_gen

print("="*70)
print("  检验：x_gen/x_dec = 2√3/π")
print("="*70)
print(f"  x_dec = {x_dec:.6f} (退耦条件 f_ext=1/U_EM)")
print(f"  投影因子 2√3/π = {projection:.6f}")
print(f"  预测 x_gen = {x_gen_pred:.6f}")
print(f"  实际 x_gen = 0.463963")
print(f"  偏差 = {abs(x_gen_pred/0.463963-1)*100:.4f}%")
print()
print(f"  由预测 x_gen 计算 n_s：")
print(f"    f_ext = {f_gen:.6f}")
print(f"    epsilon = {eps_gen:.6f}")
print(f"    n_s = {ns_pred:.6f}")
print(f"    目标 = 0.965000")
print(f"    偏差 = {abs(ns_pred/0.965-1)*100:.4f}%")
print()
print("="*70)
print("  如果预测 x_gen 与 0.463963 接近，且 n_s 仍接近 0.965，")
print("  则 x_gen 和 x_dec 之间的拓扑关系成立。")
print("="*70)