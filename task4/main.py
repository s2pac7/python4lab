"""Придумать класс самостоятельно, реализовать в нем методы экземпляра
класса, статические, методы, методы класса"""

class Auto:
    count_car = 500

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show_car(self):
        print(f"Модель: {self.model}\nЦвет: {self.color}") # Метод экземпляра класса

    @classmethod
    def show_count_car(cls):
        print(cls.count_car)

    @staticmethod
    def description():
        print("Машины хорошие\nКрасивые")

a = Auto("Жигуль", "Оранжевый")
a.show_car()
print("______________________________________________________________")
Auto.show_count_car()
print("______________________________________________________________")
Auto.description()