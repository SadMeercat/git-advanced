# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from functools import reduce


def Calc(inpt, el):
    print (inpt, el)
    return inpt * el * -3

N = int(input("Введите N: "))

my_list = [1] * N

f = lambda x, y: x * y * (-3)

for i in range(1,len(my_list)):
    my_list[i] = f(my_list[i], my_list[i-1])
print(my_list)