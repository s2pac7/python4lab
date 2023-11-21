"""Базовый класс Worker (работник).
1. Определить атрибуты: name, surname, position (должность), income
(доход);
2. Последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus":
bonus};
3. Создать класс Position (должность) на базе класса Worker;
4. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
5. Проверить работу примера на реальных данных: создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать
методы экземпляров"""

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{self._income["wage"] + self._income["bonus"]}"

income_dict = {"wage": 2000, "bonus": 1000 }

rab_1 = Position("Володя", "Некрасов", "Дворник", income_dict)
rab_2 = Position("Петр", "Достоевкий", "Садовод", income_dict)

print(rab_1.get_full_name())
print(rab_1.get_total_income())

print(rab_2.get_full_name())
print(rab_2.get_total_income())