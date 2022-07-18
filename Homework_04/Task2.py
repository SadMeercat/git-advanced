# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Ведите N: "))

result = []

while(number != 1):
    for i in range(2, number + 1):
        if(number % i == 0):
            result.append(i)
            number //= i
            break

print(set(result))