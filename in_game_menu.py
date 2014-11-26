import pygame, main, mainmenu

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
    global menuscreen
    menuscreen = 0
    mute = False
    backgroundSurface = None
    changeSound = pygame.mixer.Sound("sounds/menuButtonChange.wav")
    choice = 0
    choice1 = 0
    menuscreen = 0
    n = 2
    fontobject = pygame.font.SysFont('Arial', 24)

def leave(screen):
    pass

def onEvent(event):
    global choice
    global n
    global menuscreen
    if pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and n >= 0:
        choice = 0
    elif pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 400 and n >=1:
        choice = 1
    elif pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450 and n >=2:
        choice = 2
    elif pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500 and n >=3:
        choice = 3
    else:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and choice < n:
            choice +=1
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP)and choice > 0:
            choice -=1
    if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and menuscreen == 0:
        playsound(changeSound)
        if choice == 0:
            backgroundSurface == None
            main.setState(main.map_load)
        elif choice == 1:
            menuscreen = 1
            n = 2
        elif choice == 2:
            backgroundSurface == None
            main.setState(main.mainmenu)
    if menuscreen == 1 and(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and choice == 0):
        menuscreen = 0
        n = 2
        choice = 0
        
    elif choice == 1 and menuscreen == 1:
        mainmenu.yellowBox = True
        
        if((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or  event.type == pygame.MOUSEBUTTONDOWN) and mainmenu.mute == "False":
            mainmenu.mute = "True"
            
        elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and mainmenu.mute == "True":
            mainmenu.mute = "False"
            
    elif choice == 2 and menuscreen == 1:        
        mainmenu.redBox = True

        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and mainmenu.fullscreen == "True":
            mainmenu.fullscreen = "False"
            main.screen = pygame.display.set_mode((1280, 720)) 
        elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and mainmenu.fullscreen == "False":
            mainmenu.fullscreen = "True"
            main.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    else:
        mainmenu.yellowBox = False
        mainmenu.redBox = False
def draw(screen,ms):
    global choice1
    global backgroundSurface
    if backgroundSurface == None:
        backgroundSurface = screen.copy()
    screen.blit(backgroundSurface,(0,0))
    
    if menuscreen == 0:
        screen.blit(fontobject.render("Back to game", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
        screen.blit(fontobject.render("Main menu", 1, (255, 255, 255)),(600, 400))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
    
    elif menuscreen == 1:
        if choice == 0:
            pygame.draw.rect(screen, (255,255,255),(575,310,10,10))
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
        pygame.draw.rect(screen, (255,255,255),(570,355,20,20),2)
        screen.blit(fontobject.render("Mute", 1, (255, 255, 255)),(600, 350))
        pygame.draw.rect(screen, (255,255,255),(570,390,20,20),2)
        screen.blit(fontobject.render("Fullscreen", 1, (255, 255, 255)),(600, 385))
        if mainmenu.mute == "True":
            pygame.draw.rect(screen, (255,255,255),(574,359,13,13))
        if mainmenu.yellowBox == True and choice == 1:
            pygame.draw.rect(screen, (255,255,0),(572,357,17,17),2)
        if mainmenu.fullscreen == "True":
            pygame.draw.rect(screen, (255, 255, 255), (574, 394, 13, 13))
        if mainmenu.redBox == True and choice == 2:
            pygame.draw.rect(screen, (255, 0, 0), (572, 392, 17, 17),2)
            
    if choice != choice1:
        playsound(changeSound)
        choice1 = choice
