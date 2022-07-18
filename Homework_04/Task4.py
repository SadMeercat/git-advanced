# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def Generate(k):
    result_str = ""
    for i in range(k, -1, -1):
        if i == 0:
            result_str += str(random.randint(0, 100))
        else:
            result_str += f"{random.randint(0, 100)}x^{i} + "
    return(result_str)

k = int(input("Введите степень k: "))

result_str = Generate(k)

print(result_str)

with open("file1.txt", 'a') as data:
    data.writelines(Generate(random.randint(5,10)))

with open("file2.txt", 'a') as data:
    data.writelines(Generate(random.randint(5,10)))