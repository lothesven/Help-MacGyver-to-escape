"""class for played character behaviour """
# instanciation method in the maze
# moving method
# status (position, objects collected)

import pygame as pg
from data import settings as st

class Character:
    def __init__(self, screen):
        self.past_xtile = 0 # used for screen update
        self.past_ytile = 0 # used for screen update
        self.has_moved = False # used for screen update
        self.xtile = 0
        self.ytile = 0
        self.x = 0
        self.y = 0
        self.items = []
        image = pg.image.load(st.MACGYVER).convert_alpha()
        self.image = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        self.rect = self.image.get_rect()
        screen.blit(self.image, (self.xtile * st.TILESIZE + st.MARGIN, self.ytile * st.TILESIZE))

    def move(self, level_structure, direction, screen): # perform MacGyver moves on user command
        self.has_moved = False
        if direction == "right" and self.xtile < 14:
            if level_structure[self.ytile][self.xtile+1] != 'W':
                self.past_xtile, self.past_ytile = self.xtile, self.ytile
                self.xtile += 1
                self.has_moved = True
        elif direction == "left" and self.xtile > 0:
            if level_structure[self.ytile][self.xtile-1] != 'W':
                self.past_xtile, self.past_ytile = self.xtile, self.ytile
                self.xtile -= 1
                self.has_moved = True
        elif direction == "up" and self.ytile > 0:
            if level_structure[self.ytile-1][self.xtile] != 'W':
                self.past_xtile, self.past_ytile = self.xtile, self.ytile
                self.ytile -= 1
                self.has_moved = True
        elif direction == "down" and self.ytile < 14:
            if level_structure[self.ytile+1][self.xtile] != 'W':
                self.past_xtile, self.past_ytile = self.xtile, self.ytile
                self.ytile += 1
                self.has_moved = True
        else:
            pass # faire un son d'erreur
        
        self.x = self.xtile * st.TILESIZE + st.MARGIN
        self.y = self.ytile * st.TILESIZE
        screen.blit(self.image, (self.x, self.y))

    def escape(self, sound): # what happens if MacGyver escapes successfully.
        pg.mixer.init()
        pg.mixer.stop()
        pg.mixer.Sound.play(sound)
        print("MacGyver escapes ! :D")

    def failure(self, sound): # what happens if MacGyver do not pass the guard.
        pg.mixer.init()
        pg.mixer.stop()
        pg.mixer.Sound.play(sound)
        print("MacGyver dies :'(")