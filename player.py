from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        # Задаем начальное положение игрока
        self.x, self.y = PLATES_POS
        # Задаем начальный угол поворота игрока
        self.angle = PLAYES_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        # Начальное измнение положения игрока
        dx, dy = 0, 0
        # Скорость определяется с учетом задержки времени между кадрами.
        # Так она не будет зависеть от частоты кадров
        speed = PLAYES_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Получаем кнопки нажатые игроком
        keys = pg.key.get_pressed()
        # В зависимости от нажатых кнопок изеняем изменение положения игрока
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # Изменяем положение игрока
        self.check_wall_collision(dx, dy)

        # Определяем измнение угла поворота игрока
        if keys[pg.K_LEFT]:
            self.angle -= PLAYES_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYES_ROT_SPEED * self.game.delta_time
        # Определяем остаток от деления на 2пи для сохранения угла в диапазоне 2пи
        self.angle %= math.tau

    def check_wall(self, x, y):
        # Проверяет попадают ли координаты игрока в стену
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        # Проверям и разрешаем дальнейшее перемещение игрока
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    # Проверка попадания игрока в определенную ячейку карты
    # def check_win(self, x, y):
    #     return (x, y) == (1, 1)

    def draw(self):
        # Линия отрисовки центра видимости игрока
        # pg.draw.line(self.game.screen, "yellow", (self.x * 100, self.y * 100),
        #              (self.x * 100 + WIDTH * math.cos(self.angle),
        #               self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        # Круг позиции игрока
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), 15)
        # if self.check_win(int(self.x), int(self.y)):
        #     pg.draw.rect(self.game.screen, "darkgray", (0, 0, WIDTH, HEIGHT))

    def update(self):
        self.movement()

    @property
    def pos(self):
        # Возвращаем абсолютную позицию игрока
        return self.x, self.y

    @property
    def map_pos(self):
        # Возвращаем позицию игрока относительно карты
        return int(self.x), int(self.y)
