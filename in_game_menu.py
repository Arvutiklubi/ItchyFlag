import pygame, main

def playsound(sound):
    global mute
    if mute == False:
        pygame.mixer.Sound.play(sound)

def init(screen):
    global fontobject
    global choice
    global n
    global menuscreen
    global choice1
    global changeSound
    global mute
    global backgroundSurface
    mute = False
    backgroundSurface = None
    changeSound = pygame.mixer.Sound("sounds/menuButtonChange.wav")
    choice = 0
    choice1 = 0
    menuscreen = 0
    n = 2
    fontobject = pygame.font.SysFont('Arial', 24)
def onEvent(event):
    global choice
    global n
    global menuscreen
    if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and n >= 0:
        choice = 0
    elif pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 400 and n >=1:
        choice = 1
    elif pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450 and n >=2:
        choice = 2
    elif pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500 and n >=3:
        choice = 3
    else:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and choice < n:
            choice +=1
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP)and choice > 0:
            choice -=1
    if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and menuscreen == 0:
        playsound(changeSound)
        if choice == 0:
            backgroundSurface == None
            main.setState(main.map_load)
        elif choice == 2:
            backgroundSurface == None
            main.setState(main.mainmenu)
            
def draw(screen,ms):
    global choice1
    global backgroundSurface
    if backgroundSurface == None:
        backgroundSurface = screen.copy()
    screen.blit(backgroundSurface,(0,0))
    screen.blit(fontobject.render("Back to game", 1, (255, 255, 255)),(600, 300))
    screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
    screen.blit(fontobject.render("Main menu", 1, (255, 255, 255)),(600, 400))
    pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
    
    if choice != choice1:
        playsound(changeSound)
        choice1 = choice
