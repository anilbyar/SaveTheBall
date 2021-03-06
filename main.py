import sys

import pygame as py
from pygame.locals import *

from ball import Ball
from blocker import Blocker
from value import *

py.init()
fps_timer = py.time.Clock()

# Set display screen
screen = py.display.set_mode(screen_size)
py.display.set_caption("Save The Ball!")

# Create a ball
ball = Ball(screen)

# Create horizontal blocker
blocker = Blocker(screen)

# Getting screen size
screen_size = py.display.get_window_size()

# Has shown high score
font = py.font.Font('freesansbold.ttf', 15)

# Initialize these value
score = 0
level = 1
increase_in_score = 0
high_score: int
high_score_changed = False


# Get high score if already played otherwise create file to store high score to 0
def get_high_score():
    global high_score
    try:
        with open('highscore.txt', 'r') as f:
            high_score = int(f.readline())
            f.close()
    except PermissionError:
        py.quit()
        sys.exit()
    except FileNotFoundError:
        with open('highscore.txt', 'w') as f:
            high_score = 0
            f.write('0')
            f.close()


def check_exit_event():
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()


def restart_game():
    update_high_score_infile()
    py.time.delay(500)
    global score, level, ball
    global ball, blocker
    ball = Ball(screen)
    blocker = Blocker(screen)
    for i in range(3):
        check_exit_event()
        screen.fill(BLACK)
        text_score = str(int(score))
        score_text_after_game_over = font.render("Your Score: " + text_score, True, WHITE)
        restart_text2 = font.render("Restarting Game in : " + str(3 - i) + " sec", True, WHITE)
        restart_text1 = font.render("Oops! You lost the Game", True, WHITE)
        width = restart_text1.get_rect().height
        screen.blit(score_text_after_game_over,
                    ((game_screen_end[0] - score_text_after_game_over.get_rect().centerx) / 2, game_screen_end[1] / 2))
        screen.blit(restart_text1,
                    ((game_screen_end[0] - restart_text1.get_rect().centerx) / 2, game_screen_end[1] / 2 - width))
        screen.blit(restart_text2,
                    ((game_screen_end[0] - restart_text2.get_rect().centerx) / 2, game_screen_end[1] / 2 + width))
        py.display.update()
        py.time.delay(1000)

    score = 0
    level = 1

# Update high score in file when geme ends
def update_high_score_infile():
    global high_score, high_score_changed
    if high_score_changed:
        with open('highscore.txt', 'w') as f:
            f.flush()
            f.write(str(high_score + 1))
    high_score_changed=False


def high_score_check():
    global high_score, high_score_changed
    high_score_location = 200, 4
    if score > high_score:
        high_score_changed=True
        high_score = int(score)
        show_high_score = font.render("High Score Achieved  High Score: " + str(high_score), True, WHITE)
        screen.blit(show_high_score, high_score_location)
    else:
        show_high_score = font.render("High Score: " + str(high_score), True, WHITE)
        screen.blit(show_high_score, high_score_location)


def show_score_and_level():
    score_text = font.render("Score: " + str(int(score)), True, WHITE)
    screen.blit(score_text, (4, 4))
    global level
    level_text = font.render("Level: " + str(level), True, WHITE)
    level_text_rect = level_text.get_rect()
    screen.blit(level_text, (game_screen_end[0] - level_text_rect.width - 10, 4))


def update_score_level():
    global increase_in_score, score, level, ball
    increase_in_score += 0.1 * level * abs(ball.speed_y)
    score += 0.1 * level
    if increase_in_score > 100 * level:
        level += 1
        increase_in_score = 0


def change_ball_x_velocity():
    global ball
    sign = ball.speed_x / abs(ball.speed_x)
    ball.speed_x = sign * abs(((blocker.center - ball.center_x) * 2) / (blocker.length / 2))


# TODO: Check mouse for pause, resume and restart game
def mouse_action():
    pass


# Getting high score before starting Game
get_high_score()

while True:
    screen.fill(BLACK)
    blocker.move(0)
    update_score_level()

    #  Screen Size and updating according to size

    keys = py.key.get_pressed()
    check_exit_event()
    for events in py.event.get():
        if events.type == KEYDOWN:
            if events.key == K_a:
                if blocker.start_x >= game_screen_start[0] + blocker.speed:
                    blocker.move(-blocker.speed)
            if events.key == K_d:
                if blocker.end_x <= game_screen_end[0] - blocker.speed:
                    blocker.move(blocker.speed)
    if keys[K_a] or keys[K_LEFT]:
        if blocker.start_x >= game_screen_start[0] + blocker.speed:
            blocker.move(-blocker.speed)
    if keys[K_d] or keys[K_RIGHT]:
        if blocker.end_x <= game_screen_end[0] - blocker.speed:
            blocker.move(blocker.speed)

    # Check game status
    # Update ball motion on striking wall

    if ball.bottom() > blocker.start_y:
        if ball.is_out_of_blocker(blocker):
            restart_game()
        else:
            ball.change_color()
            change_ball_x_velocity()
            ball.speed_y = -ball.speed_y
    else:
        if ball.start_x() < game_screen_start[0]-1 or ball.end_x() > game_screen_end[0]+1:
            ball.speed_x = -ball.speed_x
        if ball.top() < game_screen_start[1]:
            ball.speed_y = -ball.speed_y

    ball.move(ball.center_x, ball.center_y)
    show_score_and_level()
    high_score_check()

    # Create Game border
    h1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_end[0], game_screen_start[1]), width=2)
    v1 = py.draw.line(screen, BORDERCOLOR, game_screen_start, (game_screen_start[0], game_screen_end[1]), width=2)
    h2 = py.draw.line(screen, BORDERCOLOR, (game_screen_start[0], game_screen_end[1]), game_screen_end, width=2)
    v2 = py.draw.line(screen, BORDERCOLOR, (game_screen_end[0], game_screen_start[1]), game_screen_end, width=2)

    py.display.update()
    fps_timer.tick(FPS)
