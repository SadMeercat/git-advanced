#2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

boolarray =[
    [False, False, False],
    [True, False, False],
    [False, True, False],
    [True, True, False],
    [False, False, True],
    [True, False, True],
    [False, True, True],
    [True, True, True]]

flag = False
for i in range(len(boolarray)):
    if not(boolarray[i][0] and boolarray[i][1] and boolarray[i][2]) != (not boolarray[i][0] 
    or not boolarray[i][1] or not boolarray[i][2]):
        print("Утверждение не истинно")
        flag = True
        break

if not flag:
    print("Утверждение истинно")