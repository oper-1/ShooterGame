import pygame as pg

# Определяем пустое пространство как False
_ = False
# Делаем миникарту
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        # enumerate позволяет вести счет используемого row (т.е. j как переменная счетчик
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                # Если в ячейке 1, то добавляем стену в карту мира
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        # Надо разобраться с этим циклом в скобках
        # Это генератор списка, он возвращает список и позволяет записать цикл for более компактно
        # Рисуются квадраты стен из карты мира
        [pg.draw.rect(self.game.screen, "darkgray", (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
        # pg.draw.rect(self.game.screen, "green", (100, 100, 100, 100))


