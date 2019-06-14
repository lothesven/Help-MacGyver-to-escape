"""class for played character behaviour """
# instanciation method in the maze
# moving method
# status (alive, position, objects collected)

from data import settings as st

class Character:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.alive = True
        self.items = []
        self.name = "MacGyver"
        # self.image = constants.macgyver
        pass

    def move(self, direction): # perform MacGyver moves on user command
        pass
    
    def update(self): # screen update of MacGyver. Method to call after a move.
        pass

    def escape(self): # what happens if MacGyver escapes successfully.
        pass

    def failure(self): # what happens if MacGyver do not pass the guard.
        pass