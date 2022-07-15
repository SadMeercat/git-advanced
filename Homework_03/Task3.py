# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.561, 10.01] => 0.56 или 56

my_list = [1.1, 1.2, 3.1, 5.561, 10.01]
min = int(str(my_list[0]).split('.')[1])
max = int(str(my_list[0]).split('.')[1])

for i in range(len(my_list)):
    tmp_val = int(str(my_list[i]).split('.')[1])
    if(min > tmp_val):
        min = tmp_val
    if(max < tmp_val):
        max = tmp_val

print(f"Наибольший: {max} \r\nНаименьший: {min}")
print(f"Разница между наибольшим и наименьшим: {max - min}")
