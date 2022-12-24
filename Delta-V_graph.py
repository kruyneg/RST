# -*- coding:1251 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots()

I = int(input("Удельный импульс: "))
M0 = int(input("Масса незаправленной ракеты: "))

t = np.linspace(2000, 100000, 100)
#v = - 9.806 * I * math.log((M0 + t) / M0)
v =[0] * 100
j = 0
for i in t:
    v[j] = - 9.806 * I * math.log(1 - i / (i + M0))
    j += 1

ax.plot(t, v)
plt.show()
