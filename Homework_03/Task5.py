# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

k = int(input("Введите k: "))
result_list = [0] * (k * 2 + 1)

for i in range(k + 1):
    if i == 0:
        continue
    elif i == 1:
        result_list[k + i] = 1
        result_list[k - i] = 1
    else:
        result_list[k + i] = result_list[k + i - 1] + result_list[k + i - 2]
        result_list[k - i] = result_list[k - i + 2] - result_list[k - i + 1]
    
print(result_list)