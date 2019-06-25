""" Client code for the MacGiver Maze Escape Game """

#! /usr/bin/env python3
# coding: utf-8

import pygame as pg

import data.settings as st
import elements.character as ch
import elements.item as it
import elements.level as lv


class Game:
    def __init__(self): # Game definition and settings. All elements instanciation.

        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((st.WIDTH, st.HEIGHT))
        self.screen.fill(st.GREY)
        pg.display.set_caption("MazeGyver")

        self.menu = False
        self.running = False # Boolean that indicates whether game is running or not

        self.labyrinth = lv.Level(self.screen) # level instanciation
        self.labyrinth.screening(self.screen)
        self.macgyver = ch.Character(self.screen) # character instanciation
        self.locations = [(600, 560)] # for item collection in game loop
        self.at_locations = ["guard"]

        possible_locations = self.labyrinth.floor_locations.copy() # for random item positionning

        needle = it.Item("needle", possible_locations) # item instanciation
        needle.render(self.screen)
        
        self.locations.append((needle.x, needle.y))
        self.at_locations.append(needle)
        possible_locations.remove((needle.x, needle.y)) # to avoid possible item same location

        plastic_tube = it.Item("plastic tube", possible_locations)
        plastic_tube.render(self.screen)

        self.locations.append((plastic_tube.x, plastic_tube.y))
        self.at_locations.append(plastic_tube)
        possible_locations.remove((plastic_tube.x, plastic_tube.y)) # to avoid possible item same location

        ether = it.Item("ether", possible_locations)
        ether.render(self.screen)

        self.locations.append((ether.x, ether.y))
        self.at_locations.append(ether)

        pg.key.set_repeat(400, 30) # Enables keyboard holding key

        pg.display.update() # screen update


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
                        x_pos = self.macgyver.past_xtile * st.TILESIZE + 40
                        y_pos = self.macgyver.past_ytile * st.TILESIZE
                        self.labyrinth.update(self.screen, x_pos, y_pos)
            
                        if (self.macgyver.x , self.macgyver.y) in self.locations: 
                            # when macgyver is on the same tile is on the same tile, collect object
                            index = self.locations.index((self.macgyver.x, self.macgyver.y))
                            if index:
                                item = self.at_locations[index] # identification of concerned item
                                item.take() # macgyver collect the item
                                self.locations[index] = (item.x, item.y) # prevent macgyver from taking same item twice
                                self.macgyver.items.append(self.at_locations[index].kind)
                            else:
                                print("GUARD !", "MacGyver has", self.macgyver.items, "collected")


            pg.display.update()
        
    def welcome(self): # menu screen with options, scores and intro to the game
        self.menu = True

        while self.menu:
            for event in pg.event.get():
                if event.type == pg.QUIT: # Event to break off game loop
                    self.menu = False



def main(): 
    game = Game() # Game instanciation
    game.start() # Game launch at main() call

if __name__ == "__main__":
    main()