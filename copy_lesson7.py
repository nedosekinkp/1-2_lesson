# Домашнее задание №1

class Matrix:
    def __init__ (self, args):
        self.args = args

    def __str__(self):
        return str('\n'. join(['\t'.join([str(j) for j in i]) for i in self.args]))

    def __add__	(self, other):
        result = []
        num = []
        for i in range(len(self.args)):
            for j in range(len(self.args[i])):
                num.append(self.args[i][j] + other.args[i][j])
                if len(num) == len(self.args[i]):
                    result.append(num)
                    num = []
        return result

stroki = int(input("Введите количество строк/столбцов матрицы  - "))
m_new_1 = Matrix([[i * j for j in range(stroki)] for i in range(stroki)])
m_new_2 = Matrix([[i + j for j in range(stroki)] for i in range(stroki)])

print("Матрица 1\n\n", m_new_1,'\n')
print("Матрица 2\n\n", m_new_2,'\n')
print(m_new_1 + m_new_2)

# Домашнее задание №2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return f' Coat	- {round(self.param / 6.5) + 0.5}'
class Costume(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return f' Costume - {2 * self.param + 0.3}'

coat = Coat(int(input("Size coat ")))
costume = Costume(int(input("Size costume ")))
print(coat.consumption)
print(costume.consumption)

#Домашнее задание №3

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n' .join(['*' * rows for _ in range(self.nums // rows)]) + '\n' +'*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return f'Сумма клеток = {self.nums + other.nums}'

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше равно второй. Вычитание невозможно"

    def __mul__(self, other):
        return f"Умнжение клеток равно- {self.nums * other.nums}"

    def __truediv__(self, other):
        return f"Деление клеток = {round(self.nums / other.nums)}"

cell_l = Cell(15)
cell_2 = Cell(24)
print(cell_l + cell_2)
print(cell_l - cell_2)
print(cell_l * cell_2)
print(cell_l / cell_2)
print(cell_2.make_order(7))