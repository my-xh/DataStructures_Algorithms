# -*- coding: utf-8 -*-

# 简单的字符串散列函数
def hash_string(s, size):
    total = 0
    for pos in range(len(s)):
        total += ord(s[pos])

    return total % size


# 带权重的字符串散列函数
def hash_str(s, size):
    total = 0
    for pos in range(len(s)):
        total += (pos + 1) * ord(s[pos])

    return total % size


if __name__ == '__main__':
    table_size = 11
    print(f'hash_simple("cat") = {hash_string("cat", table_size)}')
    print(f'hash_simple("tac") = {hash_string("tac", table_size)}')
    print('*' * 50)
    print(f'hash("cat") = {hash_str("cat", table_size)}')
    print(f'hash("tac") = {hash_str("tac", table_size)}')
