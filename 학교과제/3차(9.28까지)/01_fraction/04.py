def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    """Fraction 클래스"""

    def __init__(self, top, bottom):
        """생성자 메서드
        top: 분자
        bottom: 분모
        """
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

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

x=Fraction(1, 1000000)
y=Fraction(0, 1)

for _ in range(1000000):
    y += x

print(f"y = {y}")
print(y == Fraction(1,1))