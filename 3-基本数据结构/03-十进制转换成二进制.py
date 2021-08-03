# -*- coding: utf-8 -*-

from pythonds.basic import Stack


def decimal2bin(decimal_number):
    stack = Stack()

    while decimal_number > 0:
        rem = decimal_number % 2
        stack.push(rem)
        decimal_number //= 2

    res_list = []
    while not stack.is_empty():
        res_list.append(str(stack.pop()))

    return ''.join(res_list)


if __name__ == '__main__':
    print(decimal2bin(233))
