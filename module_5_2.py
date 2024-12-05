# Домашняя работа по уроку "Специальные методы классов"
#
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".



class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        line = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return line

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'{new_floor} - такого этажа не существует в {self.name}!')
        else:
            print(f'Здание {self.name} имеет количество этажей {self.number_of_floors} и поднимается на {new_floor}')
            print(f'Поднимаемся на этаж {new_floor}:')
            for floor in range(1, new_floor + 1):
                print(floor + 1)

House_1 = House('Жк 5 звезд', 22)
House_2 = House('Жк Арт Сити', 8)

print(len(House_1))
print(len(House_2))

print(str(House_1))
print(str(House_2))

House_1.go_to(3)
House_2.go_to(0)