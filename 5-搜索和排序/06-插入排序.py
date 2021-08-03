# -*- coding: utf-8 -*-

# 插入排序
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        idx = i  # 本轮排序元素插入的位置
        val = arr[i]  # 本轮排序元素的值
        while idx > 0 and arr[idx - 1] > val:
            arr[idx] = arr[idx - 1]
            idx -= 1
        arr[idx] = val

    return arr


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = insertion_sort(arr[:])
    print(f'插入排序的结果: {seq}')
