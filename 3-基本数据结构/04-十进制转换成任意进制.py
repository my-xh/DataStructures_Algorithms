# -*- coding: utf-8 -*-

from pythonds.basic import Stack


def base_converter(decimal_number, base=10):
    digits = '0123456789ABCDEF'
    assert base <= 16
    stack = Stack()

    while decimal_number > 0:
        rem = decimal_number % base
        stack.push(rem)
        decimal_number //= base

    res_list = []
    while not stack.is_empty():
        res_list.append(digits[stack.pop()])

    return ''.join(res_list)


if __name__ == '__main__':
    print(base_converter(233))
    print(base_converter(233, 2))
    print(base_converter(233, 8))
    print(base_converter(233, 16))
