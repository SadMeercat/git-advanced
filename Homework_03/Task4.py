# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from sqlalchemy import true


def DecToBin(number):
    result = ""

    while(true):
        result += str(number % 2)
        number = number // 2
        
        if(number == 1 or number == 0):
            result += str(number)
            break
    
    return result[::-1]

number = int(input("Введите десятичное число: "))

print(f"Число {number} в двоичном виде: {DecToBin(number)}")