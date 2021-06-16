import sys

import pygame as py
from pygame.locals import *

from size import *

py.init()

fpstimer = py.time.Clock()

screen = py.display.set_mode(screen_size)
py.display.set_caption("Save The Ball!")


# TODO: CREATE BALL AND ITS MOTION


class Ball:

    # ball = None

    def __init__(self):
        self.centerx = 100
        self.centery = 4
        self.radius = 10
        self.speedx = self.speedy = 1
        py.draw.circle(screen, WHITE, (self.centerx, self.centery), self.radius)

    def move(self, x, y):
        self.centerx += self.speedx
        self.centery += self.speedy
        py.draw.circle(screen, WHITE, (self.centerx, self.centery), self.radius)


ball = Ball()


# Blocker details

class Blocker:
    def __init__(self):
        self.length = 100
        self.startx = (game_screen_end[0] - self.length) / 2
        self.starty = 400
        self.endx = self.startx + self.length
        self.endy = self.starty
        py.draw.line(screen, WHITE, (self.startx, self.starty), (self.endx, self.endy))

    def move(self, x):
        self.startx += x
        self.endx = self.startx + self.length
        py.draw.line(screen, WHITE, (self.startx, self.starty), (self.endx, self.endy))


blocker = Blocker()

screen_size = py.display.get_window_size()

score = 0
level = 1
increase_in_score = 0
high_score: int = 0
# Has shown high score
shown: bool = False
font = py.font.Font('freesansbold.ttf', 20)


def restart_game():
    global score, level, ball_speed_in_y, ball_speed_in_x, ball, blocker_rect
    score = 0
    level = 1
    ball_speed_in_y = ball_speed_in_x = 1
    ball.center = 200, 10
    blocker_rect.center = game_screen_end[0] / 2, game_screen_end[1] - 2
    for i in range(3):
        screen.fill(BLACK)
        restart_text2 = font.render("Restart in : " + str(3 - i) + " sec", True, WHITE)
        restart_text1 = font.render("Oops! You lost the Gam", True, WHITE)
        screen.blit(restart_text1, (screen_x / 2 - 20 - restart_text1.get_rect().centerx / 2, screen_y / 2 - 40))
        screen.blit(restart_text2, (screen_x / 2 - 20 - restart_text2.get_rect().centerx / 2, screen_y / 2))
        py.display.update()
        py.time.delay(1000)


def high_score_check(show=shown):
    global high_score
    if score > high_score and (not show):
        show = True
        high_score = score
        show_high_score = font.render("High Score Achieved", True, WHITE)
        screen.blit(show_high_score, (200, 4))


def show_score_and_level():
    score_text = font.render("Score: " + str(int(score)), True, WHITE)
    screen.blit(score_text, (4, 4))
    level_text = font.render("Level: " + str(level), True, WHITE)
    level_text_rect = level_text.get_rect()
    print(level_text_rect)
    screen.blit(level_text, (game_screen_end[0] - level_text_rect.width - 10, 4))


while True:
    screen.fill(BLACK)
    blocker.move(0)
    increase_in_score += (0.001) * level
    score += increase_in_score
    if increase_in_score > 10000 * level:
        level += 1
        increase_in_score = 0
    #  Screen Size and updating according to size

    # print(level, " ", score, " ", ball_speed_in_x, " ", ball_speed_in_y)
    # print(screen_size, " ", game_screen_start, " ", game_screen_end)
    keys = py.key.get_pressed()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
            sys.exit()
        if events.type == KEYDOWN:
            if events.key == K_a:
                if blocker.startx >= game_screen_start[0] + blocker_speed:
                    blocker.move(-blocker_speed)
            if events.key == K_d:
                if blocker.endx <= game_screen_end[0] - blocker_speed:
                    blocker.move(blocker_speed)
    if keys[K_a] or keys[K_LEFT]:
        if blocker.startx >= game_screen_start[0] + blocker_speed:
            blocker.move(-blocker_speed)
    if keys[K_d] or keys[K_RIGHT]:
        if blocker.endx <= game_screen_end[0] - blocker_speed:
            blocker.move(blocker_speed)

    # Check game status

    # ball = ball.move_ip((ball_speed_in_x, ball_speed_in_y))
    # py.draw.circle(screen,WHITE,ball.center,ball_radius)
    ball.move(ball.centerx, ball.centery)
    show_score_and_level()
    high_score_check()
    # game_border=py.draw.rect(screen,BLACK,(game_screen_start,game_screen_end))

    h1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_end[0], game_screen_start[1]), width=2)
    v1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_start[0], game_screen_end[1]), width=2)
    h2 = py.draw.line(screen, BORDERCOLOR, (game_screen_start[0], game_screen_end[1]), game_screen_end, width=2)
    v2 = py.draw.line(screen, BORDERCOLOR, (game_screen_end[0], game_screen_start[1]), game_screen_end, width=2)

    py.display.update()
    fpstimer.tick(FPS)
