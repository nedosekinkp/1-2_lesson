# домашнее задание №1

a = "Я начал изучение языка программирования"
b = "Python"
c = "Меня зовут Константин Недосекин, мне 41 год."
print(f"{a} {b}. {c}")
numbr = int(input("введите любое число: "))
word = input("Введите любой текст: ")
print(f"Вы ввели число: {numbr} и текст: {word}")

# домашнее задание №2.

time = int(input("Введите время в секундах: "))
h = time // 3600
min = (time // 60) - (h * 60)
sec = time % 60
print(f"Время {h:02}:{min:02}:{sec:02}")

# домашнее задание №3

n = input("Введите число - ")
print(f"Расчет: {n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}") # используем объединение строк и перевод строк в число

# домашнее задание №4

num_polzovatel = int(input("ведите целое положительное число - " ))
max = 0
num = num_polzovatel
while num > 0:
    digit = num % 10
    if digit > max:
        max = digit
    num = num // 10
print(f"Наибольшая цифра в числе {num_polzovatel} равна {max}")

# домашнее задание №5

revenue = float(input("Укажите Вашу выручку -"))
costs = float(input("вУкажите Ваши издержки - "))
result = revenue - costs
if result > 0:
    print(f"Компания прибыль {result} рублей")
    print(f"Рентабельность бизнеса {100 * result / revenue:.1f}%")
    personal_n = float(input("\nУкажите количество сотрудников в Вашей компании? - "))
    print(f"Прибыль на одного сотрудника составляет {result / personal_n:.1f} рублей.")
elif result <= 0:
    print(f"У Вас нет прибыли, финансовый результат работы Вашей компании {result} рублей")

# домашнее задание №6

while True:
    days = 1
    start_km = int(input("Результат первого дня: "))
    itog_km = int(input("Необходимый спортсмену результат: "))
    if start_km > itog_km:
        print("Необходимый спортсмену результат  должен быть больше результата первого дня")
    else:
        while start_km < itog_km:
            start_km += start_km * 0.1
            days += 1
        print(f"Спортсмен добьется результат за {days} дней")
        break