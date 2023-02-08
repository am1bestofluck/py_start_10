

import re
from string import digits
from typing import Tuple


class Complex():
    #проверка ввода до этого этапа
    def __init__(self, stringified_val):
        self.value = Complex('1+1').prepare_number(stringified_val)

    def prepare_number(cls,user_input_i:str) -> Tuple[float]:
        devisor ='.'
        user_input_m = user_input_i.replace(",",devisor)
        ops = "+-"
        acceptableChars = digits + ops+ devisor
        for char  in user_input_m:
            if char not in acceptableChars:
                user_input_m = user_input_m.replace(char,"")
        tmp =[float(i) for i in re.findall(f"[0123456789.]+", user_input_m)]
        sign = 1 if "+" in user_input_m else -1
        q =complex(real=tmp[0],imag=tmp[1]*sign)
        return q


    def __add__(self, other_rational:'Complex'):
        return self.value + other_rational.value

    def __substract__(self, other_rational:'Complex'):
        return self.value - other_rational.value
    
    def __divide__(self, other_rational:'Complex'):
        return self.value / other_rational.value

    def __multiply__(self, other_rational:'Complex'):
        return self.value * other_rational.value

a = Complex("123+12rew")
print(a.value)