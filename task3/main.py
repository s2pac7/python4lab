class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск зарисовки")

class Pen(Stationery):
    def draw(self):
        print(f"{self.title} истратила чернилы")

class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} истратил грифель")

class Handle(Stationery):
    def draw(self):
        print(f"{self.title} истратил краску")

pen = Pen("Ручка")
pen.draw()
pencil = Pencil("Карандаш")
pencil.draw()
handle = Handle("Маркер")
handle.draw()