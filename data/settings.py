"""Contains all settings constants such as:\n
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

FOOTSTEPS = os.path.join(DIRECTORY, "sounds", "footsteps.ogg")
ERROR = os.path.join(DIRECTORY, "sounds", "error.ogg")
AMBIANT = os.path.join(DIRECTORY, "sounds", "ambiant.ogg")
WINNING = os.path.join(DIRECTORY, "sounds", "winning.ogg")
VICTORY = os.path.join(DIRECTORY, "sounds", "victory.ogg")
FAILURE = os.path.join(DIRECTORY, "sounds", "failure.ogg")

font.init()
FONT = font.Font(os.path.join(DIRECTORY, "fonts", "niew_cromagnon.ttf"), 30)

MAZE = os.path.join(DIRECTORY, "maze")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
