# -*- coding: utf-8 -*-

# 简单的模式匹配器
def simple_matcher(pattern, text):
    if (pattern_end := len(pattern)) == 0:
        return 0

    i, j, match = 0, 0, False
    while i < (text_end := len(text)) and not match:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            i -= j - 1
            j = 0
        if j == pattern_end:
            match = True

    return i - j if match else -1


# 生成mismatch表，该表记录了指定位置匹配失败时下一次匹配开始的位置
def mismatch_table(pattern):
    cur, pre = 0, -1
    table = [-1] * (n := len(pattern))

    while cur < n - 1:
        if pre == -1 or pattern[cur] == pattern[pre]:
            cur += 1
            pre += 1
            table[cur] = pre
        else:
            pre = table[pre]

    return table


# KMP算法
def kmp_matcher(pattern, text):
    if (pattern_end := len(pattern)) == 0:
        return 0

    i, j, match = 0, 0, False
    table = mismatch_table(pattern)
    while i < (text_end := len(text)) and not match:
        if j == -1 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = table[j]
        if j == pattern_end:
            match = True

    return i - j if match else -1


if __name__ == '__main__':
    pattern = 'ACATA'
    text = 'ACGACACATA'
    text2 = 'ACGACACAT'
    print(simple_matcher(pattern, text))
    print(simple_matcher(pattern, text2))
    print(kmp_matcher(pattern, text))
    print(kmp_matcher(pattern, text2))
