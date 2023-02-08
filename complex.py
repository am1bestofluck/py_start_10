class Complex():
    #проверка ввода до этого этапа
    def __init__(self, stringified_val):
        self.value = float(stringified_val.replace(",","."))
    

    def __add__(self, other_rational:'Complex'):
        return self.value + other_rational.value

    def __substract__(self, other_rational:'Complex'):
        return self.value - other_rational.value
    
    def __divide__(self, other_rational:'Complex'):
        return self.value / other_rational.value

    def __multiply__(self, other_rational:'Complex'):
        return self.value * other_rational.value
