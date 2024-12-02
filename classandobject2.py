# Атрибуты и методы объекта. Указатель на свой объект в методах
# self указатель на объект( указатель на самого себя)
class Human:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения, мне теперь {self.age}')


    def full_info(self):
        self.city
        print(f'Привет меня зовут {self.name} , мне {self.age}, я родом из города {self.city}')


den = Human('Денис', 22, 'Томбов')
max = Human('Макс', 22, 'Иркутск')
den.full_info()
max.birthday()
max.full_info()
