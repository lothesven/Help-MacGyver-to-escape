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

        pg.key.set_repeat(400, 30) # Enables keyboard holding key

        self.labyrinth = lv.Level(self.screen) # level instanciation
        self.labyrinth.screening(self.screen)
        self.macgyver = ch.Character(self.screen) # character instanciation

        possible_locations = self.labyrinth.floor_locations.copy() # for random item positionning
        tube = it.Item("tube", possible_locations) # item instanciation

        possible_locations.remove((tube.x, tube.y)) # to avoid possible item same position
        siringe = it.Item("siringe", possible_locations)

        possible_locations.remove((siringe.x, siringe.y))
        needle = it.Item("needle", possible_locations)

        pg.display.flip() # screen update


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
        

def main(): 
    game = Game() # Game instanciation
    game.start() # Game launch at main() call

if __name__ == "__main__":
    main()