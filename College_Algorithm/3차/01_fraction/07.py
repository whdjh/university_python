def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                     self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num
        
    def __sub__(self, other_fraction):        #메소드 재정의!!
        new_num = self.num * other_fraction.den - \
                     self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __mul__(self, other_fraction):        #메소드 재정의!!
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)
    
    def __truediv__(self, other_fraction):    #메소드 재정의!!
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)