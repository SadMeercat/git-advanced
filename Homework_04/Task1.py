# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

from numpy import zeros

def roundNum(d: str, number: str):
    count_zeros = len(d) - (d.find('.'))
    int_index = number.find('.')
    return str(number)[:count_zeros + int_index]



d = input("Введите точность: ")

pi = str(math.pi)
print(roundNum(d, pi))
