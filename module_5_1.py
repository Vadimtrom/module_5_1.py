class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.info()

    def info(self):
        print(f'Название комплекса: {self.name}, количество этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for f in range(1, new_floor + 1):
                print(f)
        else:
            print('Такого этажа не существует')
h1 = House('ЖК Горский', 18)

h2 = House('Элитные кварталы', 3)

h1.go_to(5)

h2.go_to(10)