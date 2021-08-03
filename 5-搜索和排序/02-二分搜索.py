# -*- coding: utf-8 -*-

# 迭代版本
def binary_search(arr, item):
    left, right = 0, len(arr) - 1
    found = False

    while left <= right and not found:
        mid = left + (right - left) // 2
        if arr[mid] == item:
            found = True
        elif arr[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return found


# 递归版本
def rec_binary_search(arr, item):
    if len(arr) == 0:
        return False
    mid = len(arr) // 2
    if arr[mid] == item:
        return True
    elif arr[mid] > item:
        return rec_binary_search(arr[:mid], item)
    else:
        return rec_binary_search(arr[mid:], item)


if __name__ == '__main__':
    arr = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    print(binary_search(arr, 54))
    print(rec_binary_search(arr, 54))
