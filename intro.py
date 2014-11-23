import pygame

def init(screen):
    global main
    import main
    global intropic
    intropic = pygame.image.load("intro/intro.png").convert()

def onEvent(event):
    global fadeIn
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        fadeIn = False
        
def draw(screen, ms):
    global main
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
    if fade == 255:
        fadeIn = False
    if fade == 0 and not fadeIn:
        main.setState(main.mainmenu)

fade = 0
fadeIn = True
