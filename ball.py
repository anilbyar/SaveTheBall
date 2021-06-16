from random import randint
import pygame as py
from value import *

class Ball:
    # ball = None
    def __init__(self, screen):
        self.screen=screen
        self.center_x = 100
        self.center_y = 10
        self.radius = 6
        self.speed_x = self.speed_y = 2
        self.color=WHITE
        py.draw.circle(self.screen, self.color, (self.center_x, self.center_y), self.radius)

    def move(self, x, y):
        self.center_x += self.speed_x
        self.center_y += self.speed_y
        py.draw.circle(self.screen, self.color, (self.center_x, self.center_y), self.radius)

    def start_x(self):
        return self.center_x - self.radius

    def end_x(self):
        return self.center_x + self.radius

    def top(self):
        return self.center_y - self.radius

    def bottom(self):
        return self.center_y+self.radius

    def change_color(self):
        color_id=randint(50,255),randint(50,255),randint(50,255)
        self.color=color_id

    def is_in_blocker(self,blocker):
        return self.start_x() > blocker.end_x or self.end_x() < blocker.start_x
