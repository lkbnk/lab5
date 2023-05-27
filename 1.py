num_list = [5,7,3,2,0]
user_num = int(input("Введите число: "))
for i in range(len(num_list)):
    if num_list[i] == user_num:
        print(num_list,"  -  ", user_num, "  -  Поздравляю, Вы угадали число!")
        break
if not num_list[i] == user_num: print(num_list,"  -  ", user_num, " -   Нет такого числа!")