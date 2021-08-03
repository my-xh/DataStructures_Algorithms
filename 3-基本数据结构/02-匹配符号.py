# -*- coding: utf-8 -*-

from pythonds.basic import Stack


def matches(open_symbol, close_symbol):
    opens = '([{'
    closes = ')]}'
    return opens.index(open_symbol) == closes.index(close_symbol)


def par_checker(symbol_string):
    stack = Stack()
    idx, n, balanced = 0, len(symbol_string), True

    while idx < n and balanced:
        symbol = symbol_string[idx]
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.is_empty() or not matches(stack.pop(), symbol):
                balanced = False
        idx += 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(par_checker('{{([][])}()}'))
    print(par_checker('[[{{(())}}]]'))
    print(par_checker('[][][](){}'))

    print(par_checker('([)]'))
    print(par_checker('((()]))'))
    print(par_checker('[{()]'))
