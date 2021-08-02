# -*- coding: utf-8 -*-

# 牛顿迭代法求解平方根
def square_root(n):
    root = n / 2
    for _ in range(20):
        root = (root + n / root) / 2

    return root


if __name__ == '__main__':
    print(square_root(9))
    print(square_root(4563))
