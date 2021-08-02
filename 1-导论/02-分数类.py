# -*- coding: utf-8 -*-

from functools import total_ordering


# 求a和b的最大公约数
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


@total_ordering
class Fraction:
    """分数"""

    def __init__(self, top, bottom):
        if not isinstance(top, int):
            raise TypeError('分子必须是整数！')
        if not isinstance(bottom, int):
            raise TypeError('分母必须是整数！')
        common = gcd(top, bottom)  # 求得分子和分母的最大公约数
        # 化简得到最简分数
        self.__num = top // common  # 分子
        self.__den = bottom // common  # 分母

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'Fraction<{self.num}/{self.den}>'

    def __add__(self, other: "Fraction"):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __radd__(self, other: "Fraction"):
        return self + other

    def __iadd__(self, other: "Fraction"):
        return self + other

    def __sub__(self, other: "Fraction"):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other: "Fraction"):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other: "Fraction"):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __eq__(self, other: "Fraction"):
        return self.num * other.den == other.num * self.den

    def __lt__(self, other: "Fraction"):
        return self.num * other.den < other.num * self.den


if __name__ == '__main__':
    f1 = Fraction(1, 4)
    print(f1)
    print(repr(f1))
    print(f'({f1}) 的分子是{f1.num}, 分母是{f1.den}')

    f2 = Fraction(-1, -2)
    print(f'({f1}) + ({f2}) = {f1 + f2}')
    print(f'({f1}) - ({f2}) = {f1 - f2}')
    print(f'({f2}) - ({f1}) = {f2 - f1}')
    print(f'({f1}) * ({f2}) = {f1 * f2}')
    print(f'({f1}) ÷ ({f2}) = {f1 / f2}')

    f3 = Fraction(-2, 4)
    print(f'({f2}) = ({f3}): {f2 == f3}')
    print(f'({f2}) > ({f3}): {f2 > f3}')
    print(f'({f2}) ≥ ({f3}): {f2 >= f3}')
    print(f'({f2}) < ({f3}): {f2 < f3}')
    print(f'({f2}) ≤ ({f3}): {f2 <= f3}')
    print(f'({f2}) ≠ ({f3}): {f2 != f3}')

    # f4 = Fraction(1.2, 2)
    # f5 = Fraction(1, 2.5)

    print(f2 + f1)
    f1 += f2
    print(f1)
