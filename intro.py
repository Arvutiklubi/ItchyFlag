import pygame
import main

def init(screen):
    global intropic
    intropic = pygame.image.load("intro/algintro.png").convert()

def onEvent(event):
    pass

def draw(screen, ms):
    global fade
    global fadeIn
    global intropic
    if fadeIn:
        fade += 1
    else:
        fade -= 1
    screen.fill((0,0,0))
    intropic.set_alpha(fade)
    screen.blit(intropic, (0,0))
    pygame.display.flip()
    if fade == 255:
        fadeIn = False
    if fade == 0 and not fadeIn:
        main.setState(main.mainmenu)

fade = 0
fadeIn = True
