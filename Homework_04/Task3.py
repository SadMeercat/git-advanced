# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

my_list = input("Введите последовательность (через запятую): \r\n")\
.replace(' ','').split(',')

result_list = []

for i in my_list:
    flag = False
    for j in result_list:
        if j == i:
            flag = True
            break
    if flag:
        continue
    else:
        result_list.append(i)

print(result_list)