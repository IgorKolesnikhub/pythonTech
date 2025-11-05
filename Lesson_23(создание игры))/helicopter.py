import os
from utils import randcell
from utils import clear
#🎄🌊🚁🟩🔥🏥💛🪣🏠☁️⚡🏆⬛
# tank - запас воды
# mxtank - максимальный запас воды

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x, self.y = rx, ry
        self.w = w
        self.h = h
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        #Перемещение вертолета"""
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.h and 0 <= ny < self.w:
            self.x, self.y = nx, ny

    def print_status(self, ssl):
        #Вывод статуса игры"""
        if ssl[0]:
            status = "💾 Сохранено..."
        elif ssl[1]:
            status = "📤 Игра загружена..."
        else:
            status = ""

        print(f"💧{self.tank}/{self.mxtank}   "
              f"🏆{self.score}   "
              f"💛{self.lives}   "
              f"{status}")

    def first_screen(self):


        print("=" * 40)
        print("|" + " " * 38 + "|")

        print(f"| Управление игрой:     Легенда:       |")
        print(f"| 'a' - влево           🟩 - земля     |")
        print(f"| 'd' - вправо          🌊 - вода      |")
        print(f"| 'w' - вверх           🎄 - дерево    |")
        print(f"| 's' - вниз            🔥 - огонь     |")
        print(f"| 'f' - сохранить игру  🏠 - апгрейд   |")
        print(f"| 'g' - загрузить игру  🏥 - госпиталь |")

        print("|" + " " * 38 + "|")
        print("=" * 40)

    def game_over(self):
        #KОНЕЦ ИГРЫ"""
        global helico

        text = f"GAME OVER, YOUR SCORE IS {self.score}"

        clear()

        print("=" * (len(text) + 4))
        print("|" + " " * (len(text) + 2) + "|")
        print(f"| {text} |")
        print("|" + " " * (len(text) + 2) + "|")
        print("=" * (len(text) + 4))

        exit(0)

    def export_data(self):
        #Экспорт данных вертолета"""
        return {
            "score": self.score,
            "lives": self.lives,
            "x": self.x, "y": self.y,
            "tank": self.tank, "mxtank": self.mxtank,
        }

    def import_data(self, data):
        #Импорт данных вертолета"""
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.score = data["score"] or 0
        self.lives = data["lives"] or 3
