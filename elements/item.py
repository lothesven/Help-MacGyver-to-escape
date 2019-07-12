"""Class for different items in the maze."""

import random as rd
import pygame as pg

from data import settings as st

class Item:
    """Each item have kind and position in the maze.\n
    Position is random.\n
    Each kind has a specific related image."""

    def __init__(self, kind, locations):
        self.locations = locations
        self.kind = kind
        random_location = rd.sample(self.locations, 1)
        self.x_pos = random_location[0][0]
        self.y_pos = random_location[0][1]

        if self.kind == "needle":
            image = pg.image.load(st.NEEDLE).convert()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "plastic tube":
            image = pg.image.load(st.PLASTUBE).convert()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "ether":
            image = pg.image.load(st.ETHER).convert_alpha()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        elif self.kind == "syringe":
            image = pg.image.load(st.SYRINGE).convert_alpha()
            self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))

    def render(self, screen):
        """Prints object in the maze on game screen."""
        screen.blit(self.image, (self.x_pos, self.y_pos))
