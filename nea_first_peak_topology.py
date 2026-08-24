#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nea_first_peak_topology.py
第一声学峰 l1 的拓扑形式检查

不引入标准宇宙学的声学半径，只问：
NEA 已有的拓扑量能否自然生成 l1 ≈ 220？

旧公式（拓扑语言）：
  l1 = 8 * BitWidth * (2√3/π)

这里 BitWidth = 10√3/ln2 ≈ 24.988
"""
import numpy as np

# 基础拓扑量
pi = np.pi
sqrt3 = np.sqrt(3)
ln2 = np.log(2)

U_weak = 10*sqrt3
BitWidth = U_weak / ln2

# 旧公式
l1_old = 8 * BitWidth * (2*sqrt3/pi)
l1_obs = 220.6

print("="*70)
print("  第一声学峰 l1 的拓扑形式")
print("="*70)
print(f"  BitWidth = 10√3/ln2 = {BitWidth:.6f}")
print(f"  旧公式 l1 = 8 × BitWidth × (2√3/π)")
print(f"           = {l1_old:.4f}")
print(f"  观测 l1   = {l1_obs}")
print(f"  偏差      = {abs(l1_old/l1_obs-1)*100:.4f}%")
print()

# 检查几个等价的拓扑写法
forms = {
    "8 * (10√3/ln2) * (2√3/π)": 8 * (10*sqrt3/ln2) * (2*sqrt3/pi),
    "16 * (10√3/ln2) * (√3/π)": 16 * (10*sqrt3/ln2) * (sqrt3/pi),
    "(80/π) * (3/ln2)": (80/pi) * (3/ln2),
    "240/(π ln2)": 240/(pi*ln2),
    "12 * (20√3/ln2) / π": 12 * (20*sqrt3/ln2) / pi,
    "2π * (BitWidth) * (√3/π)^2?": 2*pi * BitWidth * (sqrt3/pi)**2,
    "8 * BitWidth * 1.102657": 8 * BitWidth * 1.102657,
}

print("  等价拓扑形式：")
for name, val in forms.items():
    print(f"    {name:38s} = {val:.4f}")
print()

# 数值拆解
projection = 2*sqrt3/pi
print(f"  投影因子 2√3/π = {projection:.6f}")
print(f"  裸共振 8 × BitWidth = {8*BitWidth:.6f}")
print(f"  最终 l1 = {8*BitWidth*projection:.4f}")
print("="*70)