import pygame

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
    pygame.time.wait(20)

fade = 0
fadeIn = True
