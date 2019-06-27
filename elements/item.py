""" Class for different items to collect in the maze """
# each objet is an instance of this class
# have an item kind and position on the level

import pygame as pg
import random as rd

from data import settings as st

class Item:
    def __init__(self, kind, locations):
        self.locations = locations
        self.kind = kind
        random_location = rd.sample(self.locations, 1)
        self.x = random_location[0][0]
        self.y = random_location[0][1]
        self.collected = False

        if self.kind == "needle":
            image = pg.image.load(st.NEEDLE).convert()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "plastic tube":
            image = pg.image.load(st.PLASTUBE).convert()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "ether":
            image = pg.image.load(st.ETHER).convert_alpha()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "siringe":
            image = pg.image.load(st.SIRINGE).convert_alpha()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))

    def render(self, screen): # is called to print object on game screen
        screen.blit(self.image, (self.x, self.y))