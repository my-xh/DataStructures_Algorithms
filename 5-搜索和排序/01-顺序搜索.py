# -*- coding: utf-8 -*-

# 无序列表的顺序搜索
def sequential_search(arr, item):
    pos, n = 0, len(arr)
    found = False

    while pos < n and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1

    return found


# 有序列表的顺序搜索
def ordered_sequential_search(arr, item):
    pos, n = 0, len(arr)
    found, stop = False, False

    while pos < n and not found and not stop:
        if arr[pos] == item:
            found = True
        elif arr[pos] > item:
            stop = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    arr1 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    print(sequential_search(arr1, 31))
    print(sequential_search(arr1, 50))

    arr2 = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
    print(ordered_sequential_search(arr2, 54))
    print(ordered_sequential_search(arr2, 50))
