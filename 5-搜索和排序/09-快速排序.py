# -*- coding: utf-8 -*-

# 使用额外空间的快速排序
def simple_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = [], []
    pivot = arr[0]
    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return simple_quick_sort(left) + [pivot] + simple_quick_sort(right)


# 通过基准值对列表元素进行划分
def partition(arr, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < pivot:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot

    return left


# 原地快速排序
def quick_sort(arr, first=0, last=None):
    if last is None:
        last = len(arr) - 1

    if first < last:
        split_point = partition(arr, first, last)
        quick_sort(arr, first, split_point - 1)
        quick_sort(arr, split_point + 1, last)


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    seq = simple_quick_sort(arr[:])
    print(f'快速排序的结果: {seq}')

    quick_sort(arr)
    print(f'原地快速排序的结果: {arr}')
