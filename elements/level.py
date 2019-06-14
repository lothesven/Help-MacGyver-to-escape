""" level creation reading the file "maze" """
# while doing so, create an array of free space tiles list of tuples.
# Each tuple in that list can be a location for collectable object's random instanciations

import pygame as pg
from data import settings as st

class Level:
    def __init__(self): # read "maze" file and store it in a list
        self.structure = []
        self.floor_locations = []

        with open(st.MAZE, "r") as file:
            for ligne in file:
                ligne = list(ligne)
                if '\n' in ligne:
                    ligne.remove('\n')
                self.structure.append(ligne)

        self.wallnfloor = pg.transform.smoothscale(pg.image.load(st.WALLSNFLOORS).convert_alpha(), (800, 520))
        self.wall = self.wallnfloor.get_rect(topleft = (640, 0), height = 40, width = 40)
        self.floor = self.wallnfloor.get_rect(topleft = (720, 120), height = 40, width = 40)
        self.guard = pg.transform.smoothscale(pg.image.load(st.GUARD).convert_alpha(), (40, 40))

    def screening(self, screen): # method to load level images on screen
        for i in range(len(self.structure)):
                for j in range(len(self.structure[i])):
                    if self.structure[i][j] == 'W':
                        position_x = j * 40
                        position_y = i * 40
                        screen.blit(self.wallnfloor, (position_x, position_y), self.wall)
                    elif self.structure[i][j] == '0':
                        position_x = j * 40
                        position_y = i * 40
                        self.floor_locations.append((position_x, position_y)) # stores possible item locations
                        screen.blit(self.wallnfloor, (position_x, position_y), self.floor)
                    elif self.structure[i][j] == 'G':
                        position_x = j * 40
                        position_y = i * 40
                        screen.blit(self.guard, (position_x, position_y))

    def update(self, screen, position_x, position_y): # method to call when character move to blit back former character tile
        screen.blit(self.wallnfloor, (position_x, position_y), self.floor)