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

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + \
                     self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        
        return Fraction(new_num // common, new_den // common)
    
    def __radd__(self, other_fraction):
        new_num = other_fraction.num * self.den + \
					 other_fraction.den * self.num
        new_den = other_fraction.den * self.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num
    
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
print(f1 + f2)