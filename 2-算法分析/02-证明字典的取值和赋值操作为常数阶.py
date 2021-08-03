# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import timeit

x, y1, y2 = range(10000, 1000001, 10000), [], []
for i in x:
    t1 = timeit.Timer(f'mp[random.randrange({i})]', 'from __main__ import random, mp')
    t2 = timeit.Timer(f'mp[random.randrange({i})] = 1', 'from __main__ import random, mp')
    mp = {k: None for k in range(i)}
    y1.append(t1.timeit(1000))
    y2.append(t2.timeit(1000))

plt.ylim(top=0.01)
plt.ylabel('RunTime(ms)')
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
