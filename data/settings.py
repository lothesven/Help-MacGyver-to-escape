"""contains all settings constants such as:
colors, fonts, sounds, images, positions, structures and sizes"""

import os.path

from pygame import font

DIRECTORY = os.path.abspath(os.path.dirname(__file__))
HEIGHT, WIDTH = 600, 600
MARGIN = 40
FOOTLOGS = 80
TILESIZE = 40

MENU = os.path.join(DIRECTORY, "images", "macgyver_t.jpg")
WIN = os.path.join(DIRECTORY, "images", "macgyver_victory.jpg")
LOSE = os.path.join(DIRECTORY, "images", "macgyver_failure.jpg")
MACGYVER = os.path.join(DIRECTORY, "images", "macgyver.png")
GUARD = os.path.join(DIRECTORY, "images", "guard.png")
WALLSNFLOORS = os.path.join(DIRECTORY, "images", "wallsnfloors.png")
NEEDLE = os.path.join(DIRECTORY, "images", "needle.png")
PLASTUBE = os.path.join(DIRECTORY, "images", "plastic_tube.png")
ETHER = os.path.join(DIRECTORY, "images", "ether.png")
SIRINGE = os.path.join(DIRECTORY, "images", "siringe.png")

FOOTSTEPS = os.path.join(DIRECTORY, "sounds", "38874__swuing__footstep-grass.ogg")
ERROR = os.path.join(DIRECTORY, "sounds", "450616__breviceps__8-bit-error.ogg")
AMBIANT = os.path.join(DIRECTORY, "sounds", "MacGyver-Theme-Song-Intro.ogg")
WINNING = os.path.join(DIRECTORY, "sounds", "MacGyver-Theme-Song-Middle.ogg")
VICTORY = os.path.join(DIRECTORY, "sounds", "MacGyver-Theme-Song.ogg")
FAILURE = os.path.join(DIRECTORY, "sounds", "game-fail-sound-effect.ogg")

font.init()
FONT = font.Font(os.path.join(DIRECTORY, "fonts", "Niew CroMagnon.TTF"), 30)

MAZE = os.path.join(DIRECTORY, "maze")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
