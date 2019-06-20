""" level creation reading the file "maze" """
# while doing so, create an array of free space tiles list of tuples.
# Each tuple in that list can be a location for collectable object's random instanciations

import pygame as pg
from data import settings as st

class Level:
    def __init__(self, screen): # read "maze" file and store it in a list
        self.structure = []
        self.floor_locations = []

        with open(st.MAZE, "r") as file:
            for ligne in file:
                ligne = list(ligne)
                if '\n' in ligne:
                    ligne.remove('\n')
                self.structure.append(ligne)

        self.wallnfloor = pg.transform.smoothscale(pg.image.load(st.WALLSNFLOORS).convert_alpha(), (800, 520))
        self.wall = self.wallnfloor.get_rect(topleft = (640, 0), height = st.TILESIZE, width = st.TILESIZE)
        self.floor = self.wallnfloor.get_rect(topleft = (720, 120), height = st.TILESIZE, width = st.TILESIZE)
        self.guard = pg.transform.smoothscale(pg.image.load(st.GUARD).convert_alpha(), (st.TILESIZE, st.TILESIZE))

    def screening(self, screen): # method to load level images on screen
        for i in range(len(self.structure)):
                for j in range(len(self.structure[i])):
                    if self.structure[i][j] == 'W':
                        x_position = j * st.TILESIZE
                        y_position = i * st.TILESIZE
                        screen.blit(self.wallnfloor, (x_position, y_position), self.wall)
                    elif self.structure[i][j] == '0':
                        x_position = j * st.TILESIZE
                        y_position = i * st.TILESIZE
                        self.floor_locations.append((x_position, y_position)) # stores possible item locations
                        screen.blit(self.wallnfloor, (x_position, y_position), self.floor)
                    elif self.structure[i][j] == 'G':
                        x_position = j * st.TILESIZE
                        y_position = i * st.TILESIZE
                        screen.blit(self.guard, (x_position, y_position))

    def update(self, screen, x_position, y_position): # method to call when character move to blit back former character tile
        screen.blit(self.wallnfloor, (x_position, y_position), self.floor)