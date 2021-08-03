# -*- coding: utf-8 -*-

import random


def partition(arr):
    pivot, left, right, cnt = arr[0], [], [], 0
    for val in arr[1:]:
        if val < pivot:
            left.append(val)
            cnt += 1
        else:
            right.append(val)
    return left, pivot, right, cnt


def select(arr, k):
    if not arr:
        return None
    lo, pi, hi, cnt = partition(arr)
    if cnt == k - 1:
        return pi
    elif cnt > k - 1:
        return select(lo, k)
    else:
        return select(hi, k - cnt - 1)


def select_2(arr, k):
    if not arr:
        return None
    return sorted(arr)[k - 1]


if __name__ == '__main__':
    arr = [random.randint(1, 20) for _ in range(10)]
    k = random.randrange(10)
    print(arr, k)
    print(select(arr, k))
    print(select_2(arr, k))
