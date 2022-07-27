# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from functools import reduce
import math

my_nums = [1, 2, 3, 4, 5, 6, 7]

len_list = round(len(my_nums)/2)
first_list = my_nums[:len_list]
sec_list = my_nums[len_list:]

sec_list = sec_list[::-1]

if len(first_list) > len(sec_list):
    sec_list.append(first_list[len(first_list) - 1])

new_list = list(zip(first_list, sec_list))

new_list = list(map(lambda x, y: x * y, first_list, sec_list))
print(new_list)