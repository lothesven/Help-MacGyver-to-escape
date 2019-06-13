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

        self.screen = pg.display.set_mode((st.WIDTH, st.HEIGHT))
        self.running = False # Boolean that indicates whether game is running or not

        pg.key.set_repeat(400, 30) # Enables keyboard holding key

        pg.display.update()

    def start(self): # Initialization of game loop
        self.running = True

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT: # Event to break off game loop
                    self.running = False

        

def main(): 
    game = Game() # Game instanciation
    game.start() # Game launch at main() call

if __name__ == "__main__":
    main()