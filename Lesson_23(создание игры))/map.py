from utils import randbool
from utils import randcell
from utils import randcell2
#🎄🌊🚁🟩🔥🏥💛🪣🏠☁️⚡🏆⬛
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = "🟩🎄🌊🏥🏠🔥"
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 10000

class Map:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.generate_forest(5, 10)
        self.generate_rivers(10)
        self.generate_rivers(10)
        self.generate_upgrade_shop()
        self.generate_hospital()

    def check_bounds(self, x, y):
        #Проверка границ поля
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def print_map(self, helicopter, clouds):
        #Отрисовка карты
        print("⬛" * (self.w + 2) + " " * 4)
        for ri in range(self.h):
            print("⬛", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 1:
                    print("☁️", end="")
                elif clouds.cells[ri][ci] == 2:
                    print("⚡", end="")
                elif helicopter.x == ri and helicopter.y == ci:
                    print("🚁", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛")
        print("⬛" * (self.w + 2) + " " * 4)

    def generate_rivers(self, l):
        #Генератор реки (l - длина)
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        #Генератор леса (r - вероятность, mxr - максимальное число рандома)
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        #Генератор дерева"""
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1

    def generate_upgrade_shop(self):
        #Генератор домика апгрейда"""
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        #Генератор госпиталя"""
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()

    def add_fire(self):
        #Добавляет огонь на дерево"""
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self, helico):
        #Обновляем место пожара, если дерево сгорело, рисуем землю"""
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    if helico.score != 0:
                        helico.score -= TREE_BONUS
        for i in range(5):
            self.add_fire()

    def process_helicopter(self, helico, clouds):
        #Процесс взаимодействия вертолета с миром"""
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if c == 4 and helico.score >= UPGRADE_COST:
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if c == 3 and helico.score >= LIFE_COST:
            helico.lives += helico.lives // 2
            helico.score -= LIFE_COST
        if d == 2:
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def export_data(self):
        #Экспорт данных карты"""
        return {
            "cells": self.cells,
        }

    def import_data(self, data):
        #Импорт данных карты"""
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]
