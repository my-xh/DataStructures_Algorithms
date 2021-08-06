# -*- coding: utf-8 -*-


def rot13_encrypt(raw_str: str, key=13):
    enc_list = []

    for char in raw_str:
        base = None
        if char.islower():
            base = ord('z')
        elif char.isupper():
            base = ord('Z')
        if base is not None:
            code = ord(char) + key
            if code > base:
                code -= 26
            char = chr(code)
        enc_list.append(char)

    return ''.join(enc_list)


def rot13_decrypt(enc_str: str, key):
    dec_list = []

    for char in enc_str:
        base = None
        if char.islower():
            base = ord('a')
        elif char.isupper():
            base = ord('A')
        if base is not None:
            code = ord(char) - key
            if code < base:
                code += 26
            char = chr(code)
        dec_list.append(char)

    return ''.join(dec_list)


if __name__ == '__main__':
    raw_str = 'helloworld'
    enc_str = rot13_encrypt(raw_str)
    print(f'raw: {raw_str}')
    print(f'encrypt: {enc_str}')

    key = 13
    dec_str = rot13_decrypt(enc_str, key)
    print(f'decrypt: {dec_str}')
