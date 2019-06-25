""" Client code for the MacGiver Maze Escape Game """

#! /usr/bin/env python3
# coding: utf-8

import pygame as pg

import data.settings as st
import elements.character as ch
import elements.item as it
import elements.level as lv


class Game:
    def __init__(self): # Game definition and settings. 

        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((st.WIDTH + st.MARGIN * 2, st.HEIGHT + st.FOOTLOGS))
        pg.display.set_caption("MazeGyver")

        self.font = st.GAMEFONT
        # self.font = pg.font.SysFont("arial", 25)

        self.menu = False # Boolean that indicates whether menu is on screen or not
        self.running = False # Boolean that indicates whether game is running or not

    def elements_creation(self): # All elements instanciation that happens after welcoming screen

        self.screen.fill(st.BLACK) # Get rid of menu texts and image

        self.labyrinth = lv.Level(self.screen) # level instanciation
        self.labyrinth.screening(self.screen) # level rending on screen
        self.macgyver = ch.Character(self.screen) # character instanciation

        self.special_locations = [(600, 560)] # for special behaviour in game loop 
        self.at_locations = ["guard"] # (600, 560) is Guard position

        possible_locations = self.labyrinth.floor_locations.copy() # for random item positionning

        needle = it.Item("needle", possible_locations) # item instanciation
        needle.render(self.screen)
        
        self.special_locations.append((needle.x, needle.y))
        self.at_locations.append(needle)
        possible_locations.remove((needle.x, needle.y)) # to avoid possible item same location

        plastic_tube = it.Item("plastic tube", possible_locations)
        plastic_tube.render(self.screen)

        self.special_locations.append((plastic_tube.x, plastic_tube.y))
        self.at_locations.append(plastic_tube)
        possible_locations.remove((plastic_tube.x, plastic_tube.y)) # to avoid possible item same location

        ether = it.Item("ether", possible_locations)
        ether.render(self.screen)

        self.special_locations.append((ether.x, ether.y))
        self.at_locations.append(ether)

        pg.key.set_repeat(400, 30) # Enables keyboard holding key

        pg.display.update() # screen update

    def blit_text(self, surface, text, position, font, color):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width = surface.get_width()
        x, y = position
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0]  # Reset the x.
            y += word_height  # Start on new row.


    def start(self): # Initialization of game loop
        self.running = True

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

                    if self.macgyver.has_moved: # blit back floor tile on previous position only if macgyver has moved
                        x_pos = self.macgyver.past_xtile * st.TILESIZE + st.MARGIN
                        y_pos = self.macgyver.past_ytile * st.TILESIZE
                        self.labyrinth.update(self.screen, x_pos, y_pos)
            
                        if (self.macgyver.x , self.macgyver.y) in self.special_locations: 
                            # when macgyver is on the same tile is on the same tile, collect object
                            index = self.special_locations.index((self.macgyver.x, self.macgyver.y))
                            if index:
                                item = self.at_locations[index] # identification of concerned item
                                item.take() # macgyver collect the item
                                self.special_locations[index] = (item.x, item.y) # prevent macgyver from taking same item twice
                                self.macgyver.items.append(self.at_locations[index].kind)
                            else:
                                print("GUARD !", "MacGyver has", self.macgyver.items, "collected")


            pg.display.update()
        
    def welcome(self): # introduction to the game // welcome() can call start()
        self.menu = True

        title = pg.transform.smoothscale(pg.image.load(st.MENU).convert(), (st.WIDTH, int(st.HEIGHT/2)))
        pg.font.init()
        intro = "Help MacGyver to escape from a maze.\n\n" \
                "Use arrows on your keyboard to move in according directions.\n\n" \
                "MacGyver must collect objects to craft a siringe before trying to pass the guard at exit."
        instruction = "Press any button to begin the game."

        self.screen.fill(st.BLACK)
        self.screen.blit(title, (st.MARGIN, 0))
        self.blit_text(self.screen, intro, (st.MARGIN, int(st.HEIGHT/2)), self.font, st.WHITE)
        self.blit_text(self.screen, instruction, (st.MARGIN, st.HEIGHT), self.font, st.RED)

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
    game = Game() # Game instanciation
    game.welcome() # Loading menu wait for input to actually start the game

if __name__ == "__main__":
    main()