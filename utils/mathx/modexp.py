# -*- coding: utf-8 -*-

"""
计算x^n(mod p), 同内置函数pow(base, exp, mod)
"""


# 朴素版模幂算法
def naive_modexp(x, n, p=None):
    res = 1
    for i in range(n):
        res *= x
        if p is not None:
            res %= p

    return res


# 快速模幂算法
def modexp(x, n, p=None):
    def mod(a, b):
        return a % b if b is not None else a

    if n == 0:
        return 1
    tmp = modexp(mod(x * x, p), n // 2, p)
    if n % 2 != 0:
        tmp = mod(x * tmp, p)
    return tmp


if __name__ == '__main__':
    # print(naive_modexp(3, 1254906))
    res = modexp(3, 1254906)
    # print(res)
    print(res == pow(3, 1254906))
    print(modexp(3, 1254906, 10) == pow(3, 1254906, 10))
