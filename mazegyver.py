""" Client code for the MacGiver Maze Escape Game """

#! /usr/bin/env python3
# coding: utf-8

import pygame as pg

import data.settings as st
import data.functions.blit_text as bt

import elements.character as ch
import elements.item as it
import elements.level as lv


class Game:
    """Game settings, menu screen and maze game loop."""
    def __init__(self):
        """Game definition and settings"""

        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((st.WIDTH + st.MARGIN * 2, st.HEIGHT + st.FOOTLOGS))
        pg.display.set_caption("MazeGyver")

        self.font = st.GAMEFONT

        footsteps = pg.mixer.Sound(st.FOOTSTEPS)
        footsteps.set_volume(0.3)
        error = pg.mixer.Sound(st.ERROR)
        error.set_volume(0.3)
        ambiant = pg.mixer.Sound(st.AMBIANT)
        ambiant.set_volume(0.5)
        winning = pg.mixer.Sound(st.WINNING)
        winning.set_volume(0.8)
        victory = pg.mixer.Sound(st.VICTORY)
        failure = pg.mixer.Sound(st.FAILURE)
        self.sounds = [footsteps, error, ambiant, winning, victory, failure]

        self.menu = False # Boolean that indicates whether menu is on screen or not
        self.running = False # Boolean that indicates whether game is running or not

        self.labyrinth = None
        self.macgyver = None
        self.special_locations = None
        self.at_locations = None

    def elements_creation(self):
        """Instantiate objects inside the game using modules in elements subdirectory"""

        self.screen.fill(st.BLACK) # Gets rid of menu texts and image

        self.labyrinth = lv.Level(self.screen)
        self.labyrinth.screening(self.screen)
        self.macgyver = ch.Character(self.screen)

        self.special_locations = [(600, 560)] # Locations with special behaviour in game loop
        self.at_locations = ["guard"] # (600, 560) refers to Guard location

        possible_locations = self.labyrinth.floor_locations.copy()
        # Locations from level instance for random item positionning

        possible_locations.remove((st.MARGIN, 0))
        possible_locations.remove((600, 560))
        # Removes MacGyver starting location and guard location

        needle = it.Item("needle", possible_locations)
        needle.render(self.screen)

        self.special_locations.append((needle.x, needle.y))
        self.at_locations.append(needle)

        possible_locations.remove((needle.x, needle.y))
        # Prevents next item to be on same location

        plastic_tube = it.Item("plastic tube", possible_locations)
        plastic_tube.render(self.screen)

        self.special_locations.append((plastic_tube.x, plastic_tube.y))
        self.at_locations.append(plastic_tube)

        possible_locations.remove((plastic_tube.x, plastic_tube.y))
        # Prevents next item to be on same location

        ether = it.Item("ether", possible_locations)
        ether.render(self.screen)

        self.special_locations.append((ether.x, ether.y))
        self.at_locations.append(ether)

        pg.key.set_repeat(400, 30) # Enables keyboard holding key

        pg.display.update()

    def start(self):
        """Initialization of game loop"""
        self.running = True
        pg.mixer.stop() # stops music from potential previous game
        pg.mixer.Sound.play(self.sounds[2], -1)

        while self.running:

            self.clock.tick(30)

            for event in pg.event.get():
                if event.type == pg.QUIT: # Event to break off game loop
                    self.running = False

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.macgyver.move(self.labyrinth.structure, "right", self.screen)
                    elif event.key == pg.K_LEFT:
                        self.macgyver.move(self.labyrinth.structure, "left", self.screen)
                    elif event.key == pg.K_UP:
                        self.macgyver.move(self.labyrinth.structure, "up", self.screen)
                    elif event.key == pg.K_DOWN:
                        self.macgyver.move(self.labyrinth.structure, "down", self.screen)

                    if self.macgyver.has_moved:
                        # blit back floor tile on previous position only if macgyver has moved
                        x_pos = self.macgyver.past_xtile * st.TILESIZE + st.MARGIN
                        y_pos = self.macgyver.past_ytile * st.TILESIZE
                        self.labyrinth.update(self.screen, x_pos, y_pos)
                        pg.mixer.Sound.play(self.sounds[0])
                    else:
                        pg.mixer.Sound.play(self.sounds[1])

            if (self.macgyver.x, self.macgyver.y) in self.special_locations:
                # when macgyver is on the same tile is on the same tile, collect object
                index = self.special_locations.index((self.macgyver.x, self.macgyver.y))
                if index: # index is positive if not on Guard location
                    item = self.at_locations[index] # identification of concerned item
                    self.macgyver.items.append(self.at_locations[index].kind)
                    item.x, item.y = -40, -40 # puts item out of screen ...
                    self.special_locations[index] = (item.x, item.y)
                    # ... and prevents macgyver from taking same item twice
                    logs_pos = (st.MARGIN, st.HEIGHT)
                    bt.blit_text(self.screen, "Inventory:", logs_pos, self.font, st.GREEN)
                    item_x_pos = 2 * (st.MARGIN * len(self.macgyver.items)) - st.MARGIN
                    item_y_pos = st.HEIGHT + 30
                    item_inventory_position = (item_x_pos, item_y_pos)
                    self.screen.blit(item.image, item_inventory_position)
                    if len(self.macgyver.items) > 2: # if all objects are collected
                        pg.mixer.Sound.stop(self.sounds[2])
                        pg.mixer.Sound.play(self.sounds[3], -1) # victory is at hand
                        rect_pos = st.MARGIN, st.HEIGHT, st.WIDTH, st.FOOTLOGS
                        pg.draw.rect(self.screen, st.BLACK, rect_pos)
                        long_text = "MacGyver has collected all items and stops to craft ..."
                        bt.blit_text(self.screen, long_text, logs_pos, self.font, st.GREEN)
                        pg.display.update()
                        pg.time.wait(2000)
                        pg.draw.rect(self.screen, st.BLACK, rect_pos)
                        bt.blit_text(self.screen, "Inventory:", logs_pos, self.font, st.GREEN)
                        siringe = it.Item("siringe", [(-40, -40)])
                        self.macgyver.items = [siringe.kind]
                        self.screen.blit(siringe.image, (st.MARGIN, st.HEIGHT + 30))

                else:
                    print("GUARD !", "MacGyver has", self.macgyver.items, "collected")
                    if "siringe" in self.macgyver.items:
                        self.macgyver.escape(self.sounds[4])
                        self.running = False
                        self.welcome()
                    else:
                        self.macgyver.failure(self.sounds[5])
                        self.running = False
                        self.welcome()


            pg.display.update()

    def welcome(self):
        """Introduction to the game.
        Explains controlls and wait for user input to begin the game."""
        self.menu = True

        image = pg.image.load(st.MENU).convert()
        title = pg.transform.smoothscale(image, (st.WIDTH, int(st.HEIGHT/2)))
        pg.font.init()
        intro = "Help MacGyver to escape from a maze.\n\n" \
                "Use arrows on your keyboard to move in according directions.\n\n" \
                "MacGyver must collect objects to craft a siringe before trying to pass " \
                "the guard at exit."
        instruction = "Press any button to begin the game."

        self.screen.fill(st.BLACK)
        self.screen.blit(title, (st.MARGIN, 0))
        bt.blit_text(self.screen, intro, (st.MARGIN, int(st.HEIGHT/2)), self.font, st.WHITE)
        bt.blit_text(self.screen, instruction, (st.MARGIN, st.HEIGHT), self.font, st.RED)

        pg.display.update()

        while self.menu:
            for event in pg.event.get():
                if event.type == pg.QUIT: # Event to break off game loop
                    self.menu = False
                elif event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                    self.menu = False
                    self.elements_creation()
                    self.start()


def main():
    """Defines launching steps"""
    game = Game() # Game instanciation
    game.welcome() # Loading menu wait for input to actually start the game

if __name__ == "__main__":
    main()
