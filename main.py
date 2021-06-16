import sys
from blocker import Blocker
from ball import Ball
import pygame as py
from pygame.locals import *
from value import *

py.init()
fpstimer = py.time.Clock()

screen = py.display.set_mode(screen_size)
py.display.set_caption("Save The Ball!")


# TODO: CREATE BALL AND ITS MOTION

ball = Ball(screen)


# Blocker details

blocker = Blocker(screen)

screen_size = py.display.get_window_size()

score = 0
level = 1
increase_in_score = 0
high_score: int = 0
# Has shown high score

# Image resources
size_of_resume=25
pause_img=pygame.image.load("pause.bmp").convert_alpha()
pause_img=pygame.transform.smoothscale(pause_img,(size_of_resume,size_of_resume))
resume_img=pygame.image.load("resume.bmp").convert_alpha()
resume_img=pygame.transform.smoothscale(resume_img,(size_of_resume,size_of_resume))
pause_resume_rect=Rect(600,5,25,25)
isPlaying=True


font = py.font.Font('freesansbold.ttf', 15)
def check_exit_event():
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()


def restart_game():
    py.time.delay(500)
    global score, level, ball_speed_in_y, ball_speed_in_x, ball, blocker_rect
    global ball,blocker
    ball=Ball(screen)
    blocker=Blocker(screen)
    for i in range(3):
        check_exit_event()
        screen.fill(BLACK)
        textscore=str(int(score))
        score_text_afterGameover=font.render("Your Score: "+textscore,True,WHITE)
        restart_text2 = font.render("Restart in : " + str(3 - i) + " sec", True, WHITE)
        restart_text1 = font.render("Oops! You lost the Game", True, WHITE)
        width=restart_text1.get_rect().height
        screen.blit(score_text_afterGameover,((game_screen_end[0] - score_text_afterGameover.get_rect().centerx) / 2, game_screen_end[1] / 2 ))
        screen.blit(restart_text1, ((game_screen_end[0] - restart_text1.get_rect().centerx) / 2, game_screen_end[1] / 2 - width))
        screen.blit(restart_text2, ((game_screen_end[0] - restart_text2.get_rect().centerx) / 2, game_screen_end[1] / 2+width))
        py.display.update()
        py.time.delay(1000)
    score = 0
    level = 1


def high_score_check():
    global high_score
    high_score_location=200,4
    if score > high_score:
        high_score = int(score)
        show_high_score = font.render("High Score Achieved  High Score: "+str(high_score), True, WHITE)
        screen.blit(show_high_score, high_score_location)
    else:
        show_high_score=font.render("High Score: "+str(high_score),True,WHITE)
        screen.blit(show_high_score,high_score_location)


def show_score_and_level():
    score_text = font.render("Score: " + str(int(score)), True, WHITE)
    screen.blit(score_text, (4, 4))
    global level
    level_text = font.render("Level: " + str(level), True, WHITE)
    level_text_rect = level_text.get_rect()
    screen.blit(level_text, (game_screen_end[0] - level_text_rect.width - 10, 4))

def update_score__level():
    global increase_in_score,score,level,ball
    increase_in_score += (0.1) * level*abs(ball.speed_y)
    score += (0.1) * level
    if increase_in_score > 100*level:
        level += 1
        increase_in_score=0

def change_ball_x_velocity():
    global ball
    sign=ball.speed_x/abs(ball.speed_x)
    ball.speed_x=sign*abs(((blocker.center-ball.center_x)*3)/(blocker.length/2))
    print(blocker.center," ",ball.center_x," ",ball.speed_x)


# TODO: Check mouse action


def check_pause():
    mouse_pos=py.mouse.get_pos()
    global isPlaying
    if isPlaying:
        screen.blit(pause_img,pause_resume_rect)
        if mouse_pos[0]>pause_resume_rect.left and mouse_pos[0]>pause_resume_rect.left:  #check x position
            if mouse_pos[1]>pause_resume_rect.top and mouse_pos[1]<pause_resume_rect.bottom:
                isPlaying=False
                screen.blit(resume_img,pause_resume_rect)
    else:
        screen.blit()

while True:
    screen.fill(BLACK)
    blocker.move(0)
    update_score__level()

    #  Screen Size and updating according to size

    # print(level, " ", score, " ", ball_speed_in_x, " ", ball_speed_in_y)
    # print(screen_size, " ", game_screen_start, " ", game_screen_end)
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
        if ball.is_in_blocker(blocker):
            restart_game()
        else:
            ball.change_color()
            change_ball_x_velocity()
            ball.speed_y = -ball.speed_y
    else:
        if ball.start_x() < game_screen_start[0] or ball.end_x() > game_screen_end[0]:
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
    fpstimer.tick(FPS)
