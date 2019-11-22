# Домашнее задание №1

from time import sleep, perf_counter
from itertools import cycle

class TrafficLight:
    _color = [["КРАСНЫЙ", 7], ["ЖЕЛТЫЙ", 2], ["ЗЕЛЕНЫЙ", 7], ["ЖЕЛТЫЙ", 2]]

    def running(self):
        for n in cycle(self._color):
            for	a, val	in	enumerate(self._color):
                print(self._color[a][0])
                sleep(self._color[a][1])

light_l = TrafficLight()
light_l.running()

# Домашнее задание №2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self):
        return F"Масса асфальта = {(self._length * self._width * 25 * 5) / 1000} тонн"

road_1 = Road(int(input("Введите длину дороги ")), int(input("Введите ширину дороги ")))
print(road_1.get_full_profit())

# Домашнее задание №3

class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Доход": profit, "Бонус": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__ (name, surname, position, profit, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


manager = Position("Иван", "Иванов", "менеджер", 30000, 7000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

# Домашнее задание №4 - ТЯГОМОТНОЕ

class Car:
    _speed = None
    _color = None
    _name = None
    _is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'Новая машина: {self.name} цвет {self.color} {type(self)}')

    def go(self):
        print(f'{self.name}: Машина поехала')

    def stop(self):
        print(f'{self.name} Машина остановилась')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self, speed):
        print(f'{self.name} Скорость автомобиля: {speed}')

class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: Скорость автомобиля: {speed}! Превышение скорости!!!')
        else:
            super().show_speed(speed)

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: Скорость автомобиля: {speed}! Превышение скорости!!!')
        else:
            super().show_speed(speed)

class SportCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'{self.name}: Скорость автомобиля: {speed}! Но это гоночный автомобиль и ему можно)))')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True

police_car = PoliceCar('ГАИ', 'синий')
police_car.go()
police_car.show_speed(90)
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('КАМАЗ', 'красный')
work_car.go()
work_car.turn(1)
work_car.show_speed(40)
work_car.turn(0)
work_car.show_speed(25)
work_car.stop()
print()

sport_car = SportCar('Гоночный автомобиль', 'белый')
sport_car.go()
sport_car.turn(0)
sport_car.show_speed(200)
sport_car.stop()
print()

town_car = TownCar('ФОРД_КА', 'зеленый')
town_car.go()
town_car.show_speed(45)
town_car.turn(1)
town_car.turn(0)

print(f'\nМашина {town_car .name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')

# Домашнее задание №5

class Stationery:
    def __init__(self, title="это то чем можно рисовать:"):
        self.title = title

    def draw(self):
        print(f"Начинаем рисовать {self.title}")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем с помощью {self.title} ручки")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем с помощью {self.title} каандаша")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем с помощью {self.title} маркера")

stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Erich Krause")
pencil.draw()
handle = Handle("Marker")
handle.draw()