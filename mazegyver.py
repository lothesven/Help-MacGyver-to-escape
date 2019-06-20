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
        self.running = False # Boolean that indicates whether game is running or not

        self.labyrinth = lv.Level(self.screen) # level instanciation
        self.labyrinth.screening(self.screen)
        self.macgyver = ch.Character(self.screen) # character instanciation

        possible_locations = self.labyrinth.floor_locations.copy() # for random item positionning
        needle = it.Item("needle", possible_locations) # item instanciation
        needle.render(self.screen)

        possible_locations.remove((needle.x, needle.y)) # to avoid possible item same position
        plastic_tube = it.Item("plastic_tube", possible_locations)
        plastic_tube.render(self.screen)

        possible_locations.remove((plastic_tube.x, plastic_tube.y)) # to avoid possible item same position
        ether = it.Item("ether", possible_locations)
        ether.render(self.screen)


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
                        x_pos = self.macgyver.past_xtile * st.TILESIZE
                        y_pos = self.macgyver.past_ytile * st.TILESIZE
                        self.labyrinth.update(self.screen, x_pos, y_pos)
            
            pg.display.update()
        

def main(): 
    game = Game() # Game instanciation
    game.start() # Game launch at main() call

if __name__ == "__main__":
    main()