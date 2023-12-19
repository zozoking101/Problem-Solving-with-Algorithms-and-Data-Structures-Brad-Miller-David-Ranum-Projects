def __truediv__(self, othfrac):
        n = self.num * othfrac.den
        d = self.den * othfrac.num
        return Fraction(n, d)