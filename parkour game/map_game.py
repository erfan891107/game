from pygame.locals import Rect
import pygame

BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH, HEIGHT = 1200, 600

class Map:
    def __init__(self):
        self.levels = {}

    def add_level(self, level_name):
        self.levels[level_name] = {}

    def draw_rects(self, display, level_number, name):

        for mane in self.levels[level_number][name]:
            pygame.draw.rect(display, RED, [mane.x, mane.y, mane.width, mane.height])    

class Map:
    def __init__(self):
        self.levels = {}

    def add_level(self, level_name):
        self.levels[level_name] = {}

    def draw_rects(self, display, level_number, name):

        for mane in self.levels[level_number][name]:
            pygame.draw.rect(display, RED, [mane.x, mane.y, mane.width, mane.height]) 

map = Map()
map.add_level(1)
map.levels[1]["wall"] = [Rect ([0, 0, 1200, 50]),
                    Rect ([0, 550, 1200, 50]),
                    Rect ([1150, 50, 50, 550]),
                    Rect ([0, 0, 50, 550]),
                    Rect ([0, 100, 950, 50]),
                    Rect ([1050, 100, 50, 200]),
                    Rect ([900, 250, 200, 50]),
                    Rect ([900, 150, 50, 150]),
                    Rect ([750, 350, 400, 50]),
                    Rect ([500, 300, 250, 100]),
                    Rect ([50, 300, 350, 150]),
                    Rect ([500, 400, 200, 50]),
                    Rect ([175, 200, 725, 50]),
                    Rect ([800, 450, 350, 100]),
                    Rect ([750, 500, 50, 50]),
                    Rect ([775, 475, 25, 25]),
                    Rect ([725, 525, 25, 25]),
                    Rect ([750, 325, 25, 25])]


map.levels[1]["mane_1"] =  [Rect ([950, 200, 150, 50])]

map.levels[1]["mane_2"] =  [Rect ([50, 250, 50, 50]),
                            Rect ([100, 275, 25, 25])]

map.levels[1]["bridge_1"] = [Rect ([950, 100, 100, 25])]

map.levels[1]["bridge_2"] = [Rect ([150, 225, 25, 25])]

map.levels[1]["score"] = [Rect ([850, 165, 25, 25])]

map.levels[1]["finish"] = [Rect ([1075, 400, 50, 50])]

map.levels[1]["trap"] = [Rect ([55, 450, 100, 100])]
