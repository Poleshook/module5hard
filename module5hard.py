import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        else:
            user_2 = User(nickname, password, age)
            self.users.append(user_2)
            print(f"{nickname} выполнен вход")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video_clip in args:
            if not any (i.title == video_clip.title for i in self.videos):
                self.videos.append(video_clip)
            else:
                print("Видео с таким названием уже существует")

    def get_videos(self, search):
        search2 = search.upper()
        return [video_clip.title for video_clip in self.videos if search2 in video_clip.title.upper()]

    def watch_video(self, title):
        if not self.current_user:
            print("Зарегистрируйтесь или авторизуйтесь для просмотра видео")
            return

        for i in self.videos:
            if i.title == title:
                if i.adult_mode and self.current_user.age < 18:
                    print("Доступ к этому видео запрещён. Вам нет 18 лет")
                    return
                for j in range(1, i.duration + 1):
                    print(j, end=' ', flush=True)
                    time.sleep(0.1)
                print("\nКонец.")
                return

        print("Видео не найдено.")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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