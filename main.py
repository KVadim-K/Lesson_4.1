class warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 10
        self.power += 5
    def eat(self):
        print(f"{self.name} сел поесть")
    def hit(self):
        print(f"{self.name} нанес удар")
        self.endurance -= 6
    def wolk(self):
        print(f"{self.name} идет")
    def info(self):
        print(f"Имя война: {self.name}")
        print(f"Сила война: {self.power}")
        print(f"Выносливость война: {self.endurance}")
        print(f"Цвет волос война: {self.hair_color}")



