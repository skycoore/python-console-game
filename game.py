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

        self.refresh() # execute the refresh module
        self.loop() # execute the loop module

    def loop(self):
        while True:
            # general
            if keyboard.is_pressed("esc"): # if user press escape key, 
                exit() # stop the process
            
            # player movements
            for y in range(len(self.map)): # get player y in self.map list
                try:
                    x = self.map[y].index("player") # get player x with y in self.map
                    
                    if keyboard.is_pressed("z"): # if user press s,
                        if self.map[y-1][x] == "void": # if there isn't collision,
                            self.map[y][x] = "void" # set the current player position to "void",
                            self.map[y-1][x] = "player" # set the new player position
                            self.refresh() # to refresh the window

                    if keyboard.is_pressed("s"): # if user press z,
                        if self.map[y+1][x] == "void": # if there isn't collision,
                            self.map[y][x] = "void" # set the current player position to "void",
                            self.map[y+1][x] = "player" # set the new player position
                            self.refresh() # to refresh the window

                    if keyboard.is_pressed("q"): # if user press q,
                        if self.map[y][x-1] == "void": # if there isn't collision,
                            self.map[y][x] = "void" # set the current player position to "void",
                            self.map[y][x-1] = "player" # set the new player position
                            self.refresh() # to refresh the window

                    if keyboard.is_pressed("d"): # if user press d,
                        if self.map[y][x+1] == "void": # if there isn't collision,
                            self.map[y][x] = "void" # set the current player position to "void",
                            self.map[y][x+1] = "player" # set the new player position
                            self.refresh() # to refresh the window

                except: pass # if player isn't have the current y ("player_y")

    def refresh(self): # define refresh module and set Y to 0
        os.system("clear" if os.name != "nt" else "cls") # clear the current window
        print("linktr.ee/skycore") # ad :)
        for y in range(len(self.map)): # get y in self.map list
            line = ""
            for x in range(len(self.map[y])): # get x from y in self.map list
                type = self.map[y][x] # get the type of the current zone
                line += self.textures[type] # add the texture to the line

                if len(line) == len(self.map[y]): # if "y" isn't as last "y" named "Y" 
                    print(line) # show the line
                    line = "" # reset the line

Game() # execute Game