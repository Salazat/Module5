class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)

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


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(self.name,'- снесен, но он останется в истории')

House_1 = House('Жк 5 звезд', 22)
House_2 = House('Жк Арт Сити', 8)

print(len(House_1))
print(len(House_2))

print(str(House_1))
print(str(House_2))

print(House_1 == House_2)
print(House_1 > House_2)
print(House_1 < House_2)
print(House_1 != House_2)

House_1 += 3
print(House_1)

House_1 = House_1 + 4
print(House_1)

del House_1
print(House.houses_history[0], '- первое здание')
print(House.houses_history[-1], '- последнее здание')
del House_2
print(House.houses_history, '- список зданий')

