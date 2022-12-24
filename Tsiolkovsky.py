# -*- coding: cp1251 -*-
import math

def sumj(x, i):
    s = 0
    for j in range(i, len(x)):
        s += x[j]
    return s
m0 = int(input("Введите массу полезной нагрузки: "))
n = int(input("Введите количество ступеней ракеты: "))
I = [0] * n
m1 = [0] * n
m2 = [0] * n
for i in range(0, n):
    print("ракетный импульс двигателя ", i + 1, "-й ступени: ", sep="")
    I[i] = int(input())
    print("масса заправленной ", i + 1, "-й ступени: ", sep="")
    m1[i] = int(input())
    print("масса ", i + 1, "-й ступени без топлива: ", sep="")
    m2[i] = int(input())
for i in range(0, n):
    v = sum(I) + math.log( (m0 + sumj(m1, i)) / (m0 + m2[i] - m1[i] + sumj(m1, i)) )
    print("Характеристическая скорость ", i + 1, "-й ступени ракеты:", v, sep="")
