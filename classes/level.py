# level creation reading the file "maze"
# while doing so, create an array of free space tiles list of tuples.
# Each tuple in that list can be a location for collectable object's random instanciations

class Level:
    def __init__(self): # read "maze" file and store it in a list
        self.structure = []
        # self.image = [constants.floor, constants.wall]
        pass

    def update(self): # method to call after character move to blit back former character tile
        pass