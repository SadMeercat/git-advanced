# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def DeleteStr(inpt: str):
    index = inpt.find("x")
    if(index == -1):
        return inpt
    else:
        return inpt[:index]

file1_path = "file1.txt"
file2_path = "file2.txt"

with open(file1_path, 'r') as data:
    data_file1 = data.read()

with open(file2_path, 'r') as data:
    data_file2 = data.read()

list1 = data_file1.split(" + ")[::-1]
list2 = data_file2.split(" + ")[::-1]

if len(list1) > len(list2):
    for i in range(len(list1) - len(list2)):
        list2.append('0')
else:
    for i in range((len(list2) - len(list1))):
        list1.append('0')

for i in range(len(list1)):
    list1[i] = DeleteStr(str(list1[i]))
    list2[i] = DeleteStr((list2[i]))
    
summ_list = [0] * len(list1)

for i in range(len(list1)):
    summ_list[i] = int(list1[i]) + int(list2[i])

print(f"Сумма множеств: \r\n{summ_list}")