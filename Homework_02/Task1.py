# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def SummFigures(input_num):
    result_sum = 0

    for figure in str(input_num):
        if figure == "," or figure == ".":
            continue
        result_sum += int(figure)
    return result_sum

number = input("Введите число: ")

print(f"Сумма цифр: {SummFigures(number)}")
