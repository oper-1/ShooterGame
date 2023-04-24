import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *


class Game:
    def __init__(self):
        pg.init()
        # Устанавливаем размер окна игры
        self.screen = pg.display.set_mode(RES)
        # Создаем объект для отслежтвания времени игры
        self.clock = pg.time.Clock()
        # Переменная для отслеживания врмени прошедшего с последнего обновления кадра
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        # Проводим расчет движения игрока
        self.player.update()
        # Проводим рейкастинг
        self.raycasting.update()
        # Обновляем изображение экрана
        pg.display.flip()
        # Обновление счетчика времени
        self.delta_time = self.clock.tick(FPS)
        # Отражаем текущее FPS в заголовке окна (округляем число до 1 знка после
        # запятой
        pg.display.set_caption(f"{self.clock.get_fps() :.1f}")

    def draw(self):
        # Заполняем экран черным цветом
        self.screen.fill("black")
        # Отрисовываем карту
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        # Отслеживаем события
        for event in pg.event.get():
            # Если нажат выход или клавиша ESCAPE, то выходим из программы
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        # Запускаем основной цикл игры
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()