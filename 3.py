wknds_list = int(input("Укажите количество выходных дней? "))
weekdays = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
print("Ваши выходные дни: ", weekdays[:-wknds_list-1:-1])
print("Ваши рабочие дни: ", weekdays[:-wknds_list])
