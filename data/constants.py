# will contains all colors, fonts, sounds and sprites

from pygame import font
import os.path

directory = os.path.abspath(os.path.dirname(__file__))

macgyver = os.path.join(directory, "images", "macgyver.png")
guard = os.path.join(directory, "images", "guard.png")
floor = os.path.join(directory, "images", "wallsnfloors.png")
wall = os.path.join(directory, "images", "wallsnfloors.png")
needle = os.path.join(directory, "images", "needle.png")
plastic_tube = os.path.join(directory, "images", "plastic_tube.png")
ether = os.path.join(directory, "images", "ether.png")
siringe = os.path.join(directory, "images", "siringe.png")

footsteps = os.path.join(directory, "sounds", "footsteps.ogg")
error = os.path.join(directory, "sounds", "error.ogg")
victory = os.path.join(directory, "sounds", "victory.ogg")
failure = os.path.join(directory, "sounds", "failure.ogg")

gamefont = font.SysFont("arial", 40)

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)