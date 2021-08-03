# -*- coding: utf-8 -*-

from pythonds.basic import Stack


def par_checker(symbol_string):
    stack = Stack()
    index, length, balanced = 0, len(symbol_string), True

    while index < length and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        index += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(par_checker('(()()()())'))
    print(par_checker('(((())))'))
    print(par_checker('(()((())()))'))

    print(par_checker('((((((())'))
    print(par_checker('()))'))
    print(par_checker('(()()(()'))
