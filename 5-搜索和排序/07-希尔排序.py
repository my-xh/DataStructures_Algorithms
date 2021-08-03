# -*- coding: utf-8 -*-


# 指定增量的插入排序
def gap_insertion_sort(arr, start, step):
    n = len(arr)
    for i in range(start + step, n, step):
        idx = i  # 本轮排序元素插入的位置
        val = arr[idx]  # 本轮排序元素的值
        while idx > start and arr[idx - step] > val:
            arr[idx] = arr[idx - step]
            idx -= step
        arr[idx] = val

    return arr


# 希尔排序
def shell_sort(arr):
    step = len(arr) // 2
    while step > 0:
        # 对step组子列表分别进行插入排序
        for start_pos in range(step):
            arr = gap_insertion_sort(arr, start_pos, step)
        print(f'After increments of size {step}, the list is {arr}')
        step //= 2

    return arr


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = shell_sort(arr[:])
    print(f'希尔排序的结果: {seq}')
