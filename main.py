import sys
from size import *
import pygame as py
from pygame.locals import *

py.init()


fpstimer = py.time.Clock()

screen = py.display.set_mode(screen_size)
py.display.set_caption("Save The Ball!")

blocker = py.image.load("blocker.png")
#ball = py.image.load("ball.png")


ball=py.draw.circle(screen,WHITE,(100,100),ball_radius)

blocker_rect = blocker.get_rect()

screen_size = py.display.get_window_size()

blocker_rect.center = game_screen_end[0] / 2, game_screen_end[1] - 2
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
    if ball.centery >= blocker_rect.centery:
        if ball.right >= blocker_rect.left and ball.left <= blocker_rect.right:
            ball_speed_in_y = -ball_speed_in_y
        else:
            print("You lost the Game!")
            restart_game()
    elif ball.top < game_screen_start[1]:
        ball_speed_in_y = -ball_speed_in_y
    if ball.left < game_screen_start[0] or ball.right > game_screen_end[0]:
        ball_speed_in_x = -ball_speed_in_x

    ball = ball.move_ip((ball_speed_in_x, ball_speed_in_y))
    screen.fill(BLACK)
    #py.draw.circle(screen,WHITE,ball.center,ball_radius)
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
