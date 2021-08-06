# -*- coding: utf-8 -*-

from random import random
from faker import Faker

from utils import ext_gcd, modexp, str2chunk, chunk2str

"""
选两个大素数p, q
n = p * q
随机选择加密秘钥e, 使得e与(p - 1) * (q - 1)互质
解密秘钥d为e关于(p - 1) * (q - 1)的逆元

加密: c = m^e(mod n)
解密: m = c^d(mod n)
"""


# 生成RSA秘钥
def rsa_gen_keys(p, q):
    n = p * q
    pqminus = (p - 1) * (q - 1)
    e = int(random() * n)
    r, a, b = ext_gcd(e, pqminus)
    while e <= 1 or r != 1:
        e = int(random() * n)
        r, a, b = ext_gcd(e, pqminus)
    d = a if a >= 0 else a + pqminus
    return e, d, n


# RSA加密
def rsa_encrypt(msg, e, n):
    enc_list = []
    mess_chunk = str2chunk(msg, n.bit_length() // 8)
    for chunk in mess_chunk:
        enc_list.append(modexp(chunk, e, n))
    return enc_list


# RSA解密
def rsa_decrypt(chunk_list, d, n):
    dec_list = []
    for chunk in chunk_list:
        dec_list.append(modexp(chunk, d, n))
    return chunk2str(dec_list)


if __name__ == '__main__':
    e, d, n = rsa_gen_keys(5563, 8191)
    # m = 'goodbye girl'
    fake = Faker()
    m = fake.text()
    print(f'raw_message: {m}')
    print('*' * 100)
    c = rsa_encrypt(m, e, n)
    print(f'cipher_data: {c}')
    print('*' * 100)
    m = rsa_decrypt(c, d, n)
    print(f'dec_message: {m}')
