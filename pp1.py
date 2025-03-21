import pygame
import os


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.mixer.init()
pygame.init()

background = pygame.image.load("images/boombox.png")
Music = "/Users/alizhantulep/Desktop/Pygame/music"

tracks = [(f) for f in os.listdir(Music) if f.lower().endswith("mp3") ]

width,height = background.get_size()
screen = pygame.display.set_mode((width,height+50))
pygame.display.set_caption("Music player")
print("detected :", tracks)

current_index = 0 
is_Paused = False

pygame.mixer.music.load(os.path.join(Music, tracks[current_index]))
pygame.mixer.music.play()

def play_music():
    global is_Paused
    if is_Paused:
        pygame.mixer.music_unpause()
        is_Paused = False
    else:
        pygame.mixer.music_pause()

def stop_music():
    global is_Paused
    pygame.mixer.music.stop()
    is_Paused = True

def next_track():
    global is_Paused, current_index
    current_index = (current_index + 1) % len(tracks)
    pygame.mixer.music.load(os.path.join(Music, tracks[current_index]))
    pygame.mixer.music.play()
    is_Paused = False    


def previous_track():
    global is_Paused, current_index
    current_index = (current_index - 1) % len(tracks)
    pygame.mixer.music.load(os.path.join(Music, tracks[current_index]))
    pygame.mixer.music.play()
    paused = False

run = True
while run:
    screen.blit(background, (0, 0))


    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_music()
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
            elif event.key == pygame.K_q:
                stop_music()
                run = False
pygame.quit()
        