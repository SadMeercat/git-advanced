# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. 
# При декодировании попробуйте сделать через четный-нечетный элемент.


from matplotlib.pyplot import bar_label


def Encode(string):
    result = ""
    count = 1
    for i in range(len(string)):
        letter = string[i]
        if i != len(string) - 1:
            if string[i + 1] == letter:
                count += 1
            else:
                result += letter + str(count)
                count = 1
        else:
            result += letter + str(count)
            count = 1
    return result

def Decode(string):
    result = ""
    i = 0
    while i < len(string):
        main_letter = string[i]
        str_num = ""
        count = 1
        while string[i + count].isnumeric() and i + count < len(string):
            str_num += string[i + count]
            count += 1
            if i + count >= len(string):
                break
        i += count
        for j in range(int(str_num)):
            result += main_letter
    return result

with open("text1.txt", 'r') as data:
    inpt_string = data.read()

print(f"Исходная строка:\r\n{inpt_string}")

outpt_string = Encode(inpt_string)
print(f"Вот что из этого вышло:\r\n{outpt_string}")

with open("text2.txt", 'w') as data:
    data.writelines(outpt_string)

with open("text2.txt", 'r') as data:
    inpt_string = data.read()

print(f"Прочитано из файла: \r\n{inpt_string}")

outpt_string = Decode(inpt_string)

print(f"Вот что из этого вышло:\r\n{outpt_string}")