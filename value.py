"""Stores Values Required For Game"""

screen_size = screen_x, screen_y = 700, 500
game_screen_size: tuple = screen_size


# color     R    G    B
BLACK=       0,   0,   0
WHITE=     255, 255, 255
BORDERCOLOR = 22, 217, 247

FPS = 350

game_screen_start = [int(max(0, (screen_x - game_screen_size[0]) / 2)),
                     int(max(0, (screen_y - game_screen_size[1]) / 2))]

game_screen_end = [int(min(screen_x, (screen_x + game_screen_size[0]) / 2)) - 2,
                   int(min(screen_y, (screen_y + game_screen_size[1]) / 2))]

# image files

