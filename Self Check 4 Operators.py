# gcd function

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def show(self):
        print(self.num, "/", self.den)
        
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
        self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num
    
    def __mul__(self, of):
        num = self.num * of.num
        denum = self.den * of.den
        return Fraction(num, denum)
    
    def __truediv__(self, othfrac):
        n = self.num * othfrac.den
        d = self.den * othfrac.num
        return Fraction(n, d)
    
    def __sub__(self, ot):
        n1 = self.num * ot.den - ot.num * self.den
        d1 = self.den * ot.den
        return Fraction(n1, d1)
    
    def __gt__(self, othefract):
        float1 = self.num / self.den
        float2 = othefract.num / othefract.den
        return(float1 > float2)
    
    def __lt__(self, otherfraction):
        float1 = self.num / self.den
        float2 = otherfraction.num / otherfraction.den
        return(float1 < float2)
        
        
x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
print(x * y)
print(x / y)
print(x-y)
print(x > y)
print(x < y)