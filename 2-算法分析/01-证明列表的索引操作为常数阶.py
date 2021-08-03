# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import timeit

x, y = range(10000, 1000001, 10000), []
for i in x:
    t = timeit.Timer(f'arr[random.randrange({i})]', 'from __main__ import random, arr')
    arr = list(range(i))
    y.append(t.timeit(1000))

plt.ylim(top=0.01)
plt.ylabel('RunTime(ms)')
plt.plot(x, y)
plt.show()
