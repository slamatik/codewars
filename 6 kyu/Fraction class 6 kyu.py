# Something goes Here ...

class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        common = self.bottom * other.bottom
        new_numerator = self.top * other.bottom + other.top * self.bottom
        if self.greatest_common_divisor(new_numerator, common):
            divisor = self.greatest_common_divisor(new_numerator, common)
            return Fraction(int(new_numerator // divisor), int(common // divisor))
        return Fraction(new_numerator, common)

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def greatest_common_divisor(self, left, right):
        while right != 0:
            left, right = right, left % right
        return left


print(Fraction(1, 8) + Fraction(4, 5))


