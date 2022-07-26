# 3-Создайте два списка — один с названиями языков программирования, другой
#  — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, 
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 1092, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (1092,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы. 
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.

def FirstFunc(langs, nums):
    for i in range(len(langs)):
        langs[i] = langs[i].upper()
    return list(zip(nums, langs))
def SecFunc(inpt_list: list):
    result_list = []
    for i in inpt_list:
        summ = 0
        word = i[1]
        for letter in word:
            hex_code = ord(letter)
            summ += int(hex_code)
        if summ % i[0] == 0:
            result_list.append((summ, i[1]))
    return result_list

languages = ["python", "c#", "java", "pascal", "php"]
numbers = [i for i in range(1, len(languages) + 1)]

my_first_list = FirstFunc(languages, numbers)

print(f"Вывод первой функции:\r\n{my_first_list}")

print(SecFunc(my_first_list))