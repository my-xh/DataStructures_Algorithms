# -*- coding: utf-8 -*-

# 使用切片的归并排序
def merge_sort(arr):
    print(f'Splitting {arr}')
    if len(arr) <= 1:
        return arr

    # 将列表分成两个子列表并分别进行归并排序
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # 将两个子列表合并成一个有序列表
    i, j, k = 0, 0, 0
    ni, nj = len(left_arr), len(right_arr)
    while i < ni and j < nj:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # 添加其中一个子列表中剩余的元素
    while i < ni:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < nj:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    print(f'Merging {arr}')
    return arr


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = merge_sort(arr[:])
    print(f'归并排序的结果: {seq}')
