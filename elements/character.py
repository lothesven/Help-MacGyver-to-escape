"""class for played character behaviour """
# instanciation method in the maze
# moving method
# status (position, objects collected)

import pygame as pg
from data import settings as st

class Character:
    def __init__(self, screen):
        self.xtile = 0
        self.ytile = 0
        self.items = []
        self.image = pg.transform.smoothscale(pg.image.load(st.MACGYVER).convert_alpha(), (st.TILESIZE, st.TILESIZE))
        self.rect = self.image.get_rect()
        screen.blit(self.image, (self.xtile * st.TILESIZE, self.ytile * st.TILESIZE))

    def move(self, level_structure, direction, screen): # perform MacGyver moves on user command
        if direction == "right" and self.xtile < 14:
            if level_structure[self.ytile][self.xtile+1] != 'W':
                self.xtile += 1
                self.rect.move_ip(st.TILESIZE, 0)
        elif direction == "gauche" and self.xtile > 0:
            if level_structure[self.ytile][self.xtile-1] != 'W':
                self.xtile -= 1
                self.rect.move_ip(-st.TILESIZE, 0)
        elif direction == "haut" and self.ytile > 0:
            if level_structure[self.ytilee-1][self.xtile] != 'W':
                self.ytile -= 1
                self.rect.move_ip(0, -st.TILESIZE)
        elif direction == "bas" and self.ytile < 14:
            if level_structure[self.ytile+1][self.xtile] != 'W':
                self.ytile += 1
                self.rect.move_ip(0, st.TILESIZE)
        else:
            pass # faire un son d'erreur
        print(direction)
        print(self.xtile, self.ytile)
        screen.blit(self.image, (self.xtile * st.TILESIZE, self.ytile * st.TILESIZE))



    def escape(self): # what happens if MacGyver escapes successfully.
        pass

    def failure(self): # what happens if MacGyver do not pass the guard.
        pass