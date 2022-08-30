import os
import keyboard

class Game:
    def __init__(self):
        self.map = [
            ["block", "block", "block", "block", "block"], # y = 0
            ["block", "void", "player", "void", "block"], # y = 1
            ["block", "void", "void", "void", "block"], # y = 2
            ["block", "block", "block", "block", "block"], # y = 3
        ]

        self.textures = {
            "block": "#",
            "player": "@",
            "void": "."
        }

        self.refresh()
        self.loop()

    def loop(self):
        while True:
            if keyboard.is_pressed("esc"):
                exit()

            if keyboard.is_pressed("z"):
                self.move("player", 0, -1)

            if keyboard.is_pressed("s"):
                self.move("player", 0, +1)

            if keyboard.is_pressed("q"):
                self.move("player", -1, 0)

            if keyboard.is_pressed("d"):
                self.move("player", +1, 0)

    def move(self, target, add_to_x, add_to_y):
        for y in range(len(self.map)):
            try:
                x = self.map[y].index(target)

                if self.map[y+(add_to_y)][x+(add_to_x)] == "void":
                    self.map[y][x] = "void"
                    self.map[y+(add_to_y)][x+(add_to_x)] = target
                    self.refresh()
            except: pass

    def refresh(self):
        os.system("clear" if os.name != "nt" else "cls")
        print("linktr.ee/skycore")
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                type = self.map[y][x]
                print(self.textures[type], end="")

                if x == len(self.map):
                    print("")

Game()
