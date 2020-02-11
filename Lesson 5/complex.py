"""Module of complex numbers"""

from math import sqrt


class Complex:
    """Class of complex numbers"""

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        out = ''

        if self.im >= 0:
            out = '{:.2f}+{:.2f}i'.format(self.re, self.im)
        else:
            out = '{:.2f}{:.2f}i'.format(self.re, self.im)

        return out

    def __add__(self, other):
        tmp_re = self.re + other.re
        tmp_im = self.im + other.im
        return Complex(tmp_re, tmp_im)

    def __sub__(self, other):
        tmp_re = self.re - other.re
        tmp_im = self.im - other.im
        return Complex(tmp_re, tmp_im)

    def __mul__(self, other):
        tmp_re = self.re * other.re - self.im * other.im
        tmp_im = self.im * other.re + self.re * other.im
        return Complex(tmp_re, tmp_im)

    def __truediv__(self, other):
        tmp_re = (self.re * other.re + self.im * other.im) / \
                 (other.re ** 2 + other.im ** 2)
        tmp_im = (self.im * other.re - self.re * other.im) / \
                 (other.re ** 2 + other.im ** 2)
        return Complex(tmp_re, tmp_im)

    def __abs__(self):
        tmp_re = sqrt(self.re ** 2 + self.im ** 2)
        return Complex(tmp_re, 0)
