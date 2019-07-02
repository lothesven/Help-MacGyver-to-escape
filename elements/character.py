"""class for played character behaviour """
# instanciation method in the maze
# moving method
# status (position, objects collected)

import pygame as pg

from data import settings as st

class Character:
    """ To fill """
    def __init__(self, screen):
        self.past_xtile = 0 # used for screen update
        self.past_ytile = 0 # used for screen update
        self.has_moved = False # used for screen update
        self.xtile = 0
        self.ytile = 0
        self.x_pos = 0
        self.y_pos = 0
        self.items = []

        image = pg.image.load(st.MACGYVER).convert_alpha()
        tile = pg.transform.smoothscale(image, (st.TILESIZE, st.TILESIZE))
        image = pg.image.load(st.WIN).convert()
        escape = pg.transform.smoothscale(image, (st.HEIGHT, st.WIDTH))
        image = pg.image.load(st.LOSE).convert()
        failure = pg.transform.smoothscale(image, (st.HEIGHT, st.WIDTH))

        self.images = [tile, escape, failure]
        screen.blit(self.images[0], (self.xtile * 40 + st.MARGIN, self.ytile * 40))

    def move(self, level_structure, direction, screen):
        """Performs MacGyver moves on user command."""
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

        self.x_pos = self.xtile * st.TILESIZE + st.MARGIN
        self.y_pos = self.ytile * st.TILESIZE
        screen.blit(self.images[0], (self.x_pos, self.y_pos))

    def escape(self, screen, sound):
        """Instructions if MacGyver escapes successfully."""
        pg.mixer.init()
        pg.mixer.stop()
        pg.mixer.Sound.play(sound)
        screen.blit(self.images[1], (st.MARGIN, 0))

    def failure(self, screen, sound):
        """Instructions if MacGyver do not pass the guard."""
        pg.mixer.init()
        pg.mixer.stop()
        pg.mixer.Sound.play(sound)
        screen.blit(self.images[2], (st.MARGIN, 0))
