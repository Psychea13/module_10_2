from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        num_days = 0
        for i in range(enemies):
            if enemies > 0:
                enemies -= self.power
                num_days += 1
                sleep(1)
                print(f'{self.name} сражается {num_days} день..., осталось {enemies} воинов.')
                if enemies <= 0:
                    print(f'{self.name} одержал победу спустя {num_days} дней(-я)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
