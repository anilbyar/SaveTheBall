import pygame as py
from value import *

class Blocker:
    def __init__(self,screen):
        self.speed=2
        self.screen=screen
        self.length = 200
        self.start_x = (game_screen_end[0] - self.length) / 2
        self.start_y = game_screen_end[1] - 2
        self.end_x = self.start_x + self.length
        self.end_y = self.start_y
        self.center=self.start_x+self.length/2
        py.draw.line(screen, WHITE, (self.start_x, self.start_y), (self.end_x, self.end_y), 7)

    def move(self, x):
        self.start_x += x
        self.end_x = self.start_x + self.length
        self.center=self.start_x+self.length/2
        py.draw.line(self.screen, WHITE, (self.start_x, self.start_y), (self.end_x, self.end_y), 7)
