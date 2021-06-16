import pygame as py
def draw_play_pause():
    if isPlaying:
        screen.blit(pause_img, pause_resume_rect)
    else:
        screen.blit(resume_img, pause_resume_rect)

def clicked_play_pause():
    global isPlaying

    mouse_pos = py.mouse.get_pos()
    mouse_button = py.mouse.get_pressed(3)
    event.
    if pause_resume_rect.left < mouse_pos[0] < pause_resume_rect.right:  # check x position
        if pause_resume_rect.top < mouse_pos[1] < pause_resume_rect.bottom:
            if mouse_button[0] or mouse_button[1] or mouse_button[2]:
                if isPlaying:
                    isPlaying=False
                else:
                    isPlaying=True


def check_pause():
    x:int=0
    while True:
        x+=1
        clicked_play_pause()
        draw_play_pause()
        if not isPlaying:

            screen.fill(BLACK)
            py.display.update()
        if isPlaying:
            #print(x)
            x=0
            break
