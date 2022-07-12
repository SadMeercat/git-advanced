# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

from operator import xor
import time


def RndNumber(len_num):
    result = ""
    curr_time = str(time.time_ns())[::-1]
    curr_time = curr_time[3:len(curr_time)]
    key = "489432456783"

    for figure in curr_time:
        result += str((int(figure) + round(time.time() * 1000)) ^ int(key[int(figure)]) % 10)
    
    if len_num > len(result):
        count = 1
        while (len(result) < len_num):
            result += str((int(result[count % 10]) * (len_num + int(curr_time) % 10)) + int(key[count % 10]) % 10)
            count += 1
            count *= count
    if len_num == 1:
        return int(result[0:len_num])
    else:
        rnd_num = RndNumber(1)
        return int(result[rnd_num:len_num + rnd_num])

def ShuffleArr(array):

    return array

print(RndNumber(30))
n = 10
array = [0] * n
for i in range(n):
    array[i] = RndNumber(6)

print(f"Исходный массив: \r\n {array}")