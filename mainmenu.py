import pygame
import main

def playsound(sound):
    global mute
    if mute == False:
        pygame.mixer.Sound.play(sound)

def init(screen):
    
    global fontobject
    global choice
    global choice1
    #menus oleva pildi number
    global menuscreen
    #maksimum valikute arv lehel
    global n
    global menupic
    global changeSound
    global yellowBox
    global mute
    pygame.mixer.init()
    menupic = pygame.image.load("image_data/background/menuBackground.png").convert()
    changeSound = pygame.mixer.Sound("sounds/menuButtonChange.wav")
    choice = 0
    choice1 = 0
    n = 3
    menuscreen = 0
    yellowBox = False
    mute = False
    fontobject = pygame.font.SysFont('Arial', 24)
    
def onEvent(event):
    
    global choice
    global menuscreen
    global n
    global yellowBox
    global mute
    if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and n >= 0:
        choice = 0
    elif pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 400 and n >=1:
        choice = 1
    elif pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450 and n >=2:
        choice = 2
    if pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500 and n >=3:
        choice = 3
    else:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and choice < n:
            choice +=1
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP)and choice > 0:
            choice -=1
    
    #valikud main menu juures
    if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and menuscreen == 0:
        playsound(changeSound)
        if choice == 0:
            #Start game
            main.setState(main.map_load)
        elif choice == 1:
            #Options
            menuscreen = 1
            n = 0
            choice = 0
        elif choice == 2:
            menuscreen = 2
            n = 0
            choice = 0
        elif choice == 3:
            #Quit game
            main.quit()
            
    #valikud optionsi juures
    elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and (menuscreen == 1 or menuscreen == 2):
        playsound(changeSound)
        if choice == 0:
            menuscreen = 0
            n = 3
            
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and menuscreen != 0:
        playsound(changeSound)
        menuscreen = 0
        choice = 0
        n = 3
        
    #optionsi kraam
    if pygame.mouse.get_pos()[0] > 577 and pygame.mouse.get_pos()[0] < 595 and pygame.mouse.get_pos()[1] > 362 and pygame.mouse.get_pos()[1] < 380 and menuscreen == 1:
        yellowBox = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and mute == False:
            mute = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN and mute == True:
            mute = False
            
    else:
        yellowBox = False
def draw(screen,ms):
    global menupic
    global choice1
    global yellowBox
    screen.fill( (0,0,0) )
    menupic.set_alpha(100)
    screen.blit(menupic, (0,0))
    #mainmenu
    if menuscreen == 0:
        screen.blit(fontobject.render("Start game", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
        screen.blit(fontobject.render("Credits", 1, (255, 255, 255)),(600, 400))
        screen.blit(fontobject.render("Quit game", 1, (255, 255, 255)),(600, 450))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))

    #options
    elif menuscreen == 1:
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50,10,10))
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
        pygame.draw.rect(screen, (255,255,255),(570,355,20,20),2)
        screen.blit(fontobject.render("Mute", 1, (255, 255, 255)),(600, 350))
        if mute == True:
            pygame.draw.rect(screen, (255,255,255),(574,359,13,13))
        if yellowBox == True:
            pygame.draw.rect(screen, (255,255,0),(572,357,17,17),2)
            
    #credits
    elif menuscreen == 2:
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("here should be some text", 1, (255, 255, 255)),(500, 340))
        screen.blit(fontobject.render("Credits", 1, (255, 255, 255)),(580, 200))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
        
    #sounds
    if choice != choice1:
        playsound(changeSound)
        choice1 = choice
