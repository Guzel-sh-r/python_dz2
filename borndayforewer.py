day = ""
while True:
    if day == 6:
        break
    year = int(input("Введите год рождения Пушкина: "))
    if year == 1799:
        while True:
            day = int(input("Введите день рождения Пушкина: "))
            if day == 6:
                year = ""
                print("Верно")
                break
