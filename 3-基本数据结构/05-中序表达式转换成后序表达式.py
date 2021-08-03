# -*- coding: utf-8 -*-

import string

from pythonds.basic import Stack


def infix2postfix(infix):
    prec = {
        '(': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
    }

    stack = Stack()
    infix_list, postfix_list = infix.split(), []

    for char in infix_list:
        if char in string.ascii_uppercase:
            postfix_list.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            token = stack.pop()
            while token != '(':
                postfix_list.append(token)
                token = stack.pop()
        else:
            while not stack.is_empty() and prec[stack.peek()] >= prec[char]:
                postfix_list.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix_list.append(stack.pop())

    return ' '.join(postfix_list)


if __name__ == '__main__':
    print(infix2postfix('( A + B ) * ( C + D )'))
    print(infix2postfix('( A + B ) * C'))
    print(infix2postfix('A + B * C'))

    print(infix2postfix('( A + B ) * ( C + D ) * ( E + F )'))
    print(infix2postfix('A + ( ( B + C ) * ( D + E ) )'))
    print(infix2postfix('A * B * C * D + E + F'))
