# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from cmath import sqrt

inpt = input("Введите координаты (через пробел): ").split(" ")

while len(inpt) != 4:
    inpt = input("Введите координаты (через пробел): ").split(" ")

inpt = list(map(float, inpt))
distance = sqrt((inpt[2] - inpt[0])**2 + (inpt[3] - inpt[1])**2)
print(f"Расстояние между точками: {round(distance.real, 3)}")
