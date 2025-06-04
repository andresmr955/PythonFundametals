from math import gcd

class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_fraction):
        
        common_den = self.y * other_fraction.y // (gcd(self.y, other_fraction.y))

        new_self_X = self.x * (common_den // self.y)
        new_other_x = other_fraction.x * (common_den // other_fraction.y)
        result_num = new_self_X + new_other_x

        return Fraction(result_num, common_den)
    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
fraction1 = Fraction(5,6)
fraction2 = Fraction(7,9)
fraction3 = fraction1 + fraction2
print(fraction3)

print(gcd(65,50))