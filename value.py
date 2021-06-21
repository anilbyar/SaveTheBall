import pygame

screen_size = screen_x, screen_y = 700, 500
game_screen_size: tuple = screen_size


# color     R    G    B
BLACK=       0,   0,   0
WHITE=     255, 255, 255
GREEN=      61, 242, 109
RED=       255,  45,  38
YELLOW=    255, 201,  38
CYAN=       38, 255, 248
BLUE=       38,  99, 255
PURPLE=    163,  68, 252
PINK=      244,  38, 255
BORDERCOLOR = 22, 217, 247
COLORS=(WHITE, GREEN, RED, YELLOW, CYAN, BLUE, PURPLE, PINK)

FPS = 250

game_screen_start = [int(max(0, (screen_x - game_screen_size[0]) / 2)),
                     int(max(0, (screen_y - game_screen_size[1]) / 2))]

game_screen_end = [int(min(screen_x, (screen_x + game_screen_size[0]) / 2)) - 2,
                   int(min(screen_y, (screen_y + game_screen_size[1]) / 2))]

# image files

