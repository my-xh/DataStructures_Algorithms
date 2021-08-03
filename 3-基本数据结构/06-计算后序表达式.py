# -*- coding: utf-8 -*-

import string

from operator import add, sub, mul, truediv

from pythonds.basic import Stack


def postfix_eval(postfix):
    op_map = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
    }

    stack = Stack()
    postfix_list = postfix.split()

    for char in postfix_list:
        if char in string.digits:
            stack.push(int(char))
        else:
            operand_b = stack.pop()
            operand_a = stack.pop()
            result = op_map[char](operand_a, operand_b)
            stack.push(result)

    return stack.pop()


if __name__ == '__main__':
    print(postfix_eval("4 5 6 * +"))
    print(postfix_eval("7 8 + 3 2 + /"))
