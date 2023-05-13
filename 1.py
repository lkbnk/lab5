num = [5,7,3,2,0]
user_num = int(input("Введите число: "))
for i in range(len(num)):
    if num[i] == user_num:
        print(num,"  -  ", user_num, "  -  Вы угадали!")
        break
if not num[i] == user_num: print(num,"  -  ", user_num, " -   Нет такого числа!")