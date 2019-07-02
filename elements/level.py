"""Class for level creation, display and update."""

import pygame as pg
from data import settings as st

class Level:
    """Level creation here uses a single file "maze".\n
    It could be used as a canvas for more..."""

    def __init__(self):
        """Reads the file "maze" and builds a list of rows. Each row is a list of tiles.\n
        Each tile is either a floor or a wall. Top left and bottom right tiles must be floor.\n
        When a tile is a floor, adds its position consisting of a tuple to a list.\n
        That list is then used for items random instanciations"""

        self.structure = []
        self.floor_locations = []

        with open(st.MAZE, "r") as file:
            for ligne in file:
                ligne = list(ligne)
                if '\n' in ligne:
                    ligne.remove('\n')
                self.structure.append(ligne)
        image = pg.image.load(st.WALLSNFLOORS).convert_alpha()
        self.wallnfloor = pg.transform.smoothscale(image, (800, 520))
        self.wall = self.wallnfloor.get_rect(topleft=(640, 0), height=40, width=40)
        self.floor = self.wallnfloor.get_rect(topleft=(720, 120), height=40, width=40)
        image = pg.image.load(st.GUARD).convert_alpha()
        self.guard = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))

    def screening(self, screen):
        """Loads level images on screen."""

        for i in range(len(self.structure)):
            for j in range(len(self.structure[i])):
                if self.structure[i][j] == 'W':
                    x_position = j * st.TILESIZE + st.MARGIN
                    y_position = i * st.TILESIZE
                    screen.blit(self.wallnfloor, (x_position, y_position), self.wall)
                elif self.structure[i][j] == '0':
                    x_position = j * st.TILESIZE + st.MARGIN
                    y_position = i * st.TILESIZE
                    self.floor_locations.append((x_position, y_position))
                    # stores possible item locations
                    screen.blit(self.wallnfloor, (x_position, y_position), self.floor)
        screen.blit(self.guard, (600, 560))

    def update(self, screen, x_position, y_position):
        """Blits back former character tile to floor tile when character moves."""

        screen.blit(self.wallnfloor, (x_position, y_position), self.floor)
