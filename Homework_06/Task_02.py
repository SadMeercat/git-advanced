# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce


my_nums = [1, 2, 3, 4, 5, 6, 7]

result = reduce(lambda x, y: x + y, my_nums[::2])
print(result)

