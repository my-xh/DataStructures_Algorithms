# -*- coding: utf-8 -*-

from utils.stringx import str2hex, hex2str


# 字符串转chunk列表
def str2chunk(s, chunk_size):
    hex_s = str2hex(s)
    chunk_list = []
    chunk_size *= 2  # 每个字节的16进制串长度为2
    for i in range(0, len(hex_s), chunk_size):
        chunk = int(hex_s[i:i + chunk_size], 16)
        chunk_list.append(chunk)

    return chunk_list


# chunk列表转字符串
def chunk2str(chunk_list):
    hex_list = []
    for chunk in chunk_list:
        hex_s = hex(chunk)[2:]
        # 16进制串长度不为偶数时，在前面补0
        if len(hex_s) % 2 != 0:
            hex_list.append('0')
        hex_list.append(hex_s)

    return hex2str(''.join(hex_list))


if __name__ == '__main__':
    s = 'hello'
    c = str2chunk(s, 3)
    print(c)
    new_s = chunk2str(c)
    print(new_s)
