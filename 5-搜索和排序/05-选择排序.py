# -*- coding: utf-8 -*-

# 选择排序
def selection_sort(arr):
    n = len(arr)
    for pass_num in range(n - 1, 0, -1):
        idx = pass_num  # 本轮排序最大值的索引
        for i in range(pass_num):
            if arr[i] > arr[idx]:
                idx = i
        arr[idx], arr[pass_num] = arr[pass_num], arr[idx]

    return arr


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = selection_sort(arr[:])
    print(f'选择排序的结果: {seq}')
