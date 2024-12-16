import time

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Добро пожаловать, {nickname}!')
                return
        print('Неверный логин или пароль.')

    def log_out(self):
        if self.current_user:
            print(f'До свидания, {self.current_user.nickname}!')
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video in self.videos:
                print(f'Видео с названием {video.title} уже есть.')
            else:
                self.videos.append(video)
                print(f'Видео {video.title} добавлено.')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f'Пользователь {nickname} успешно зарегистрирован.')
        self.log_in(nickname, password)

    def get_videos(self, word):
        video_list = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                video_list.append(video.title)
        return video_list

    def watch_video(self, film_name):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return

        for video in self.videos:
            if film_name == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                    return
                print(f'Проигрывание видео: {video.title}')
                for current_time in range(1, video.duration + 1):
                    print(f'Секунда {current_time} из {video.duration}')
                    time.sleep(1)
                print('Конец видео')
                return
        print(f'Видео {film_name} не найден.')


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}, Возраст: {self.age}'


# Тестирование
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
