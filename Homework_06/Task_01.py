# 1- Определить, присутствует ли в заданном списке строк, некоторое число

def is_int(input_number:str):
    #print(input_number)
    try:
        int(input_number)
        return True
    except ValueError:
        return False

string_list = ["Янапишу некоторое число", "Я ввел число: 1234321", "Можно ли будет ввести мое число (1234321)?"]

for item in string_list:
    temp_num = "".join(list(filter(lambda x: is_int(x) == True, item)))
    #print(temp_num)
    if len(temp_num) == 0:
        print("Чисел не нашлось")
    else:
        print(f"Нашлось число: {temp_num}")
