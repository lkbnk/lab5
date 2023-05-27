from random import randint

num_list = []
for i in range(10):
    num_list.append(randint(0, 100))
print(num_list)
duplicate = {str(num) for num in num_list if num_list.count(num) > 1}
print("Повторяющиеся элементы отсутствуют") if len(duplicate) < 1 else print("Повторяется ", " ".join(duplicate))