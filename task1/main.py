"""Создать класс Circle (круг). Поле класса хранит радиус окружности. Методы
класса возвращают площадь и длину окружности. Выполнить проверку на то,
что радиус-величина положительная."""
from math import pi
class Circle:
    def __init__(self, r):
        self.r = r

    def square(self):
        return f"S = Pi * r^2 = {pi * self.r**2}"

    def length(self):
        return f"C = 2 * Pi * r = {2 * pi * self.r}"

    def check(self):
        if self.r > 0:
            return self.r
        else:
            print("Радиус не может быть отрицательным")
            return exit()

try:
    radius = int(input("Введите радиус: "))
except ValueError:
    print("Вы ввели некорректные данные")

r = Circle(radius)
radius = r.check()
print(r.square())
print(r.length())

