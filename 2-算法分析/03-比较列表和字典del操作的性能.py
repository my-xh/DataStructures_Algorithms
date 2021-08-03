# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import timeit

x, y1, y2 = range(10000, 1000001, 10000), [], []
for i in x:
    t = timeit.Timer(f'del seq[0]', 'from __main__ import random, seq')
    seq = list(range(i))
    y1.append(t.timeit(1))
    seq = {k: None for k in range(i)}
    y2.append(t.timeit(1))

plt.ylim(top=0.001)
plt.ylabel('RunTime(ms)')
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
