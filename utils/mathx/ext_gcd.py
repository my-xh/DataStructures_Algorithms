# -*- coding: utf-8 -*-

"""
正整数x关于模y的逆元a满足ax ≡ 1(mod y), 且仅当x和y互质, 即gcd(x, y)=1时存在逆元。

存在整数a和b，使得ax + by = 1，则a是x关于y的逆元。
当y = 0时，满足条件的一个解为：a = 1, b = 0；
当y > 0时，已知a′y + b′(x % y) = 1 --> a′y + b′(x - (x//y) * y) = 1
可以推出：b′x + (a′ - b′(x//y))y = 1, 即：a = b′, b = a′ - b′(x//y)
"""


# 扩展欧几里得算法
def ext_gcd(x, y):
    """
    求两数的最大公约数，以及其中一个数以另一个数为模的逆元

    Args:
        x: 第一个数
        y: 第二个数

    Returns:
        x和y的最大公约数, x关于模y的逆元，y关于模x的逆元
    """
    if y == 0:
        return x, 1, 0
    else:
        d, a, b = ext_gcd(y, x % y)
        return d, b, a - b * (x // y)


if __name__ == '__main__':
    print(ext_gcd(3, 7))
    print(ext_gcd(7, 3))
