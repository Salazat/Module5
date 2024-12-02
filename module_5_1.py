# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.

# Примечание:
# self - это переменная указывающая на объект. Используйте её для обращения к атрибутам или методам объекта.
# Обращение к атрибутам или методам объекта/класса происходит при помощи "."
# Метод __init__ вызывается в момент создания объекта.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

House_1.go_to(3)
House_2.go_to(0)

