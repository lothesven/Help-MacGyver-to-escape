""" Class for different items to collect in the maze """
# each objet is an instance of this class
# have an item kind and position on the level
# have a status collected

import random as rd

from data import settings as st

class Item:
    def __init__(self, kind, locations): # instanciation providing possible locations from level
        self.locations = locations
        self.kind = kind
        random_location = self.locations[rd.random(rd.randrange(len(self.locations)))]
        self.x = random_location[0]
        self.y = random_location[1]
        # self.image = []
        self.collected = False
        pass

    def render(self): # is called to print object on game screen
        pass

    def collect(self): # is called when macgyver is on same tile
        self.collected = True
        pass

    