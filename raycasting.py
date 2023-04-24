import pygame as pg
import math
from settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            # Вычисляем синус и косинус угла игрока
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            # вычисление горизонтального пересечения
            # Определяем основные параметры линии зрения
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            #
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            # Вычисляем длину луча отрисовки при пересечении стены
            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                # Проверяем пересечение со стеной
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # вычисление вертикального пересечения
            # Определяем основные параметры линии зрения
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            # Вычисляем длину луча отрисовки при пересечении стены
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                # Проверяем пересечение со стеной
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # Выбираем меньшую длину пересечения, для определения ближней грани ячейки стены
            if depth_hor > depth_vert:
                depth = depth_vert
            else:
                depth = depth_hor

            # Отрисовываем луч рэйкастинга для отладки
            # pg.draw.line(self.game.screen, "yellow", (100 * ox, 100 * oy),
            #              (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

            # Убираем эффект аквариума
            depth *= math.cos(self.game.player.angle - ray_angle)
            # Высота проекции стены
            # Если дистанция до стены будет 0, добавляем небольшое значение, чтобы
            # избежать ошибки деления на 0
            proj_height = SCREEN_DIST / (depth + 0.0001)

            # Отрисовываем стены
            # color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            # pg.draw.rect(self.game.screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2,
            #                                          SCALE, proj_height))
            pg.draw.line(self.game.screen, "green", (ray * SCALE, HALF_HEIGHT - proj_height // 2), (ray * SCALE, HALF_HEIGHT + proj_height // 2))
            pg.draw.line(self.game.screen, "green", (ray * SCALE + SCALE, HALF_HEIGHT - proj_height // 2), (ray * SCALE + SCALE, HALF_HEIGHT + proj_height // 2))
            pg.draw.line(self.game.screen, "green", (ray * SCALE, HALF_HEIGHT - proj_height // 2), (ray * SCALE + SCALE, HALF_HEIGHT - proj_height // 2))
            pg.draw.line(self.game.screen, "green", (ray * SCALE, HALF_HEIGHT + proj_height // 2), (ray * SCALE + SCALE, HALF_HEIGHT + proj_height // 2))
            ray_angle += DELTA_ANGLE

    def update(self):
        """Метод интерфейса запуска рейкастинга"""
        self.ray_cast()
