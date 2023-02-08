class Rational():

    def __init__(self, stringified_val):
        self.value = float(stringified_val.replace(",","."))
    
    def __add__(self, other_rational:'Rational'):
        return round(self.value + other_rational.value, 6)

    def __iadd__(self, other_rational:'Rational'):
        return round(self.value + other_rational.value, 6)

    def __sub__(self, other_rational:'Rational'):
        return round(self.value - other_rational.value, 6)

    def __isub__(self, other_rational:'Rational'):
        return round(self.value - other_rational.value, 6)
    
    def __truediv__(self, other_rational:'Rational'):
        return round(self.value / other_rational.value, 6)

    def __itruediv__(self, other_rational:'Rational'):
        return round(self.value / other_rational.value, 6)

    def __mul__(self, other_rational:'Rational'):
        return round(self.value * other_rational.value, 6)

    def __imul__(self, other_rational:'Rational'):
        return round(self.value * other_rational.value, 6)

    def __mod__(self, other_rational:'Rational'):
        return round(self.value % other_rational.value, 6)

    def __imod__(self, other_rational:'Rational'):
        return round(self.value % other_rational.value, 6)
    
    def __floordiv__(self, other_rational:'Rational'):
        return round(self.value // other_rational.value, 6)

    def __ifloordiv__(self, other_rational:'Rational'):
        return round(self.value // other_rational.value, 6)
    
    def __neg__(self):
        return -self.value
