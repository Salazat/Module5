# Необходимо дополнить класс House следующими специальными методами:
# 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# 5. Остальные методы арифметических операторов, где self - x, other - y:
#
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.

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

House_2 = 10 + House_2
House_1.go_to(3)
House_2.go_to(0)