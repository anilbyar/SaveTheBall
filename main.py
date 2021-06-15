import sys

import pygame as py
from pygame.locals import *

py.init()




screen_size = screen_x, screen_y = 700, 500
game_screen_size: tuple = screen_size
BLACK = 0, 0, 0
WHITE: tuple = 255, 255, 255
BORDERCOLOR = 22, 217, 247





FPS = 300
fpstimer = py.time.Clock()
ball_speed = ball_speed_in_x, ball_speed_in_y = 1, 1
blocker_speed = 2

screen = py.display.set_mode(screen_size)
py.display.set_caption("Save The Ball!")

blocker = py.image.load("blocker.png")
ball = py.image.load("ball.png")

ball_rect = ball.get_rect()
ball_radius=50
blocker_rect = blocker.get_rect()

screen_size = py.display.get_window_size()

game_screen_start = [int(max(0, (screen_x - game_screen_size[0]) / 2)),
                     int(max(0, (screen_y - game_screen_size[1]) / 2))]

game_screen_end = [int(min(screen_x, (screen_x + game_screen_size[0]) / 2)) - 2,
                   int(min(screen_y, (screen_y + game_screen_size[1]) / 2))]

ball_rect.center = 200, 10
blocker_rect.center = game_screen_end[0] / 2, game_screen_end[1] - 2
score = 0
level = 1
increase_in_score = 0
high_score: int=0
# Has shown high score
shown: bool = False
font = py.font.Font('freesansbold.ttf', 20)


py.display.update()




def restart_game():

    global score, level, ball_speed_in_y, ball_speed_in_x, ball_rect, blocker_rect
    score = 0
    level = 1
    ball_speed_in_y = ball_speed_in_x = 1
    ball_rect.center = 200, 10
    blocker_rect.center = game_screen_end[0] / 2, game_screen_end[1] - 2
    for i in range(3):
        screen.fill(BLACK)
        restart_text = font.render("Restart in : " + str(3 - i) + " sec", True, WHITE)
        screen.blit(restart_text, (screen_x / 2 - 80, screen_y / 2 - 40))
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
    increase_in_score += (0.001) * level
    score += increase_in_score
    if increase_in_score > 10000 * level:
        level += 1
        increase_in_score = 0
    #  Screen Size and updating according to size

    blocker_rect.centery = game_screen_end[1] - 2
    # print(level, " ", score, " ", ball_speed_in_x, " ", ball_speed_in_y)
    # print(screen_size, " ", game_screen_start, " ", game_screen_end)
    keys = py.key.get_pressed()
    for events in py.event.get():
        if events.type == py.QUIT:
            py.quit()
            sys.exit()
        if events.type == KEYDOWN:
            if events.key == K_a:
                if blocker_rect.left >= game_screen_start[0] + blocker_speed:
                    blocker_rect = blocker_rect.move(-blocker_speed, 0)
            if events.key == K_d:
                if blocker_rect.right <= game_screen_end[0] - blocker_speed:
                    blocker_rect = blocker_rect.move(blocker_speed, 0)
    if keys[K_a] or keys[K_LEFT]:
        if blocker_rect.left >= game_screen_start[0] + blocker_speed:
            blocker_rect = blocker_rect.move(-blocker_speed, 0)
    if keys[K_d] or keys[K_RIGHT]:
        if blocker_rect.right <= game_screen_end[0] - blocker_speed:
            blocker_rect = blocker_rect.move(blocker_speed, 0)

    # Check game status
    if ball_rect.centery >= blocker_rect.centery:
        if ball_rect.right >= blocker_rect.left and ball_rect.left <= blocker_rect.right:
            ball_speed_in_y = -ball_speed_in_y
        else:
            print("You lost the Game!")
            restart_game()
    elif ball_rect.top < game_screen_start[1]:
        ball_speed_in_y = -ball_speed_in_y
    if ball_rect.left < game_screen_start[0] or ball_rect.right > game_screen_end[0]:
        ball_speed_in_x = -ball_speed_in_x

    ball_rect = ball_rect.move((ball_speed_in_x, ball_speed_in_y))
    screen.fill(BLACK)
    screen.blit(ball, ball_rect)
    screen.blit(blocker, blocker_rect)
    show_score_and_level()
    high_score_check()
    # game_border=py.draw.rect(screen,BLACK,(game_screen_start,game_screen_end))

    h1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_end[0], game_screen_start[1]), width=2)
    v1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_start[0], game_screen_end[1]), width=2)
    h2 = py.draw.line(screen, BORDERCOLOR, (game_screen_start[0], game_screen_end[1]), game_screen_end, width=2)
    v2 = py.draw.line(screen, BORDERCOLOR, (game_screen_end[0], game_screen_start[1]), game_screen_end, width=2)

    py.display.update()
    fpstimer.tick(FPS)
