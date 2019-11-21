# Домашнее задание №1

my_list = [888, True, {"one": "один", "two": "два"}, "привет", 7.4, [5, 4, 3, 2, 1], (333, 444)]
for n in range(len(my_list)):
    print(my_list[n], type(my_list[n]))

# Домашнее задание №2

my_list = input("Введите цифры через пробел").split()
print("Вы ввели - ", my_list)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print("Задание выполнено", my_list)

# Домашнее задание №3.1 список.

seasons_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
                "ноябрь", "декабрь"]
month = int(input("Введите с помощью цифры месяц в календаре "))
for i in range(len(seasons_list)):
    if month == i+1:
        if 3 <= month <= 5:
            print("Это весна, месяц - ", seasons_list[i])
        elif 6 <= month <= 8:
            print("Это лето, месяц - ", seasons_list[i])
        elif 9 <= month <= 11:
            print("Это осень, месяц - ",  seasons_list[i])
        else:
            print("Это зима, месяц - ", seasons_list[i])

# Домашнее задание №3.2 словарь

seasons_dict = {0: "январь", 1: "февраль", 2: "март", 3: "апрель", 4: "май", 5: "июнь", 6: "июль", 7: "август",
                8: "сентябрь", 9: "октябрь", 10: "ноябрь", 11: "декабрь"}
month = int(input("Введите с помощью цифры месяц в календаре "))
for i in range(len(seasons_dict)):
    if month == i+1:
        if 3 <= month <= 5:
            print("Это весна, месяц - ", seasons_dict.get(i))
        elif 6 <= month <= 8:
            print("Это лето, месяц - ", seasons_dict.get(i))
        elif 9 <= month <= 11:
            print("Это осень, месяц - ",  seasons_dict.get(i))
        else:
            print("Это зима, месяц - ", seasons_dict.get(i))

# Домашнее задание №4

my_lyst = (input("Введите несколько слов, разделенных пробелами ")).split()
for i in range(len(my_lyst)):
    if len(my_lyst[i]) <= 10:
        print(i+1, my_lyst[i])
    else:
        print(i+1, (my_lyst[i])[:11], "...")

# Домашнее задание №5

rating = [7, 5, 3, 3, 2]
print(f"Рейтинг: {rating}")
print("Введите целое положительное число, либо просто нажмите enter для выхода из программы")
while True:
    n = input(" - ")
    if n == "":
        print("Вы завершили выполнение программы")
        break
    try:
        n = int(n)
    except ValueError:
        print("Некоретное значение, введите пожалуйста целое положительное число")
        continue
    if n < 0:
        print("Больше нуля")
        continue
    for i, val in enumerate(rating):
        if n > val:
            rating.insert(i, n)
            break
    else:
        rating.append(n)
    print(f"{rating}")

# Домашнее задание №6

goods = []
features = {"название": "", "цена": "",	"количество": "", "единица измерения": ""}
analytics = {"название": [], "цена": [], "количество": [], "единица измерения": []}
num = 0
while True:
    if input("Для выхода из программы нажмите q, для продолжения Enter").upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        _ = input(f"ведите значение свойства '{f}': ")
        features[f] = int(_) if( f == "цена" or f == "количество" ) else _
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f"\n Текущая аналитика по товарам: \n {'*'*30}")
    for key, value in analytics.items():
        print(f"{key[:25]:>30}: {value}")
    print('*'*30)
