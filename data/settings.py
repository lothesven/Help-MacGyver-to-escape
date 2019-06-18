# will contains all colors, fonts, sounds and sprites

from pygame import font
import os.path

DIRECTORY = os.path.abspath(os.path.dirname(__file__))
HEIGHT, WIDTH = 600, 600
TILESIZE = 40

MACGYVER = os.path.join(DIRECTORY, "images", "macgyver.png")
GUARD = os.path.join(DIRECTORY, "images", "guard.png")
WALLSNFLOORS = os.path.join(DIRECTORY, "images", "wallsnfloors.png")
NEEDLE = os.path.join(DIRECTORY, "images", "needle.png")
PLASTUBE = os.path.join(DIRECTORY, "images", "plastic_tube.png")
ETHER = os.path.join(DIRECTORY, "images", "ether.png")
SIRINGE = os.path.join(DIRECTORY, "images", "siringe.png")

FOOTSTEPS = os.path.join(DIRECTORY, "sounds", "footsteps.ogg")
ERROR = os.path.join(DIRECTORY, "sounds", "error.ogg")
VICTORY = os.path.join(DIRECTORY, "sounds", "victory.ogg")
FAILURE = os.path.join(DIRECTORY, "sounds", "failure.ogg")

font.init()
GAMEFONT = font.Font(os.path.join(DIRECTORY, "fonts", "Atmosphere-Regular.TTF"), 40)

MAZE = os.path.join(DIRECTORY, "maze")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)