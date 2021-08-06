# -*- coding: utf-8 -*-

# 字符串转16进制串
def str2hex(s: str):
    hex_list = []
    for char in bytes(s, encoding='utf-8'):
        hex_list.append(f'{char:02x}')

    return ''.join(hex_list)


# 16进制串转字符串
def hex2str(hex_str: str):
    return bytearray.fromhex(hex_str).decode(encoding='utf-8')


if __name__ == '__main__':
    s = 'hello'
    hex_s = str2hex(s)
    print(hex_s)
    new_s = hex2str(hex_s)
    print(new_s)
