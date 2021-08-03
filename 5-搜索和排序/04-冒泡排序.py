# -*- coding: utf-8 -*-

# 基本冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


# 短冒牌排序
def short_bubble_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1, 0, -1):
        exchange = False  # 记录本轮排序是否发生过元素交换
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                exchange = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if not exchange:
            break

    return arr


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = bubble_sort(arr[:])
    print(f'冒泡排序结果: {seq}')
    seq2 = short_bubble_sort(arr[:])
    print(f'短冒泡排序结果: {seq2}')
