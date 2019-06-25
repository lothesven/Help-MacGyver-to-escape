""" Class for different items to collect in the maze """
# each objet is an instance of this class
# have an item kind and position on the level

import pygame as pg
import random as rd

from data import settings as st

class Item:
    def __init__(self, kind, locations): # instanciation providing possible locations from level
        self.locations = locations
        self.kind = kind
        random_location = rd.sample(self.locations, 1)
        self.x = random_location[0][0]
        self.y = random_location[0][1]
        self.collected = False

        if self.kind == "needle":
            self.image = pg.transform.smoothscale(pg.image.load(st.NEEDLE).convert(), (st.TILESIZE, st.TILESIZE))
        elif self.kind == "plastic tube":
            self.image = pg.transform.smoothscale(pg.image.load(st.PLASTUBE).convert(), (st.TILESIZE, st.TILESIZE))
        elif self.kind == "ether":
            self.image = pg.transform.smoothscale(pg.image.load(st.ETHER).convert_alpha(), (st.TILESIZE, st.TILESIZE))
        elif self.kind == "siringe":
            self.image = pg.transform.smoothscale(pg.image.load(st.SIRINGE).convert_alpha(), (st.TILESIZE, st.TILESIZE))

    def render(self, screen): # is called to print object on game screen
        screen.blit(self.image, (self.x, self.y))