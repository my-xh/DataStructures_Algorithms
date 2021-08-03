# -*- coding: utf-8 -*-

def to_str(n, base=10):
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


if __name__ == '__main__':
    print(to_str(769))
    print(to_str(10, 2))
