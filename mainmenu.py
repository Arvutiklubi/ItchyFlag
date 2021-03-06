import pygame
import main
from random import randint

bgPosX = bgPosY = 0
bgSpeedX = bgSpeedY = 0
bgAlpha = 0

def playsound(sound):
    global mute
    if mute == "False":
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
    global radialGradPic
    global changeSound
    global yellowBox
    global mute
    global fullscreen
    global redBox
    global bgSpeedX, bgSpeedY
    global bgOverlaySurf
    global mouseMoved
    
    mouseMoved = pygame.mouse.get_pos()
    pygame.mixer.init()
    
    menupic = pygame.image.load("image_data/background/menuBackground.png").convert()
    radialGradPic = pygame.image.load("intro/shadow_inmenu.png").convert_alpha()
    changeSound = pygame.mixer.Sound("sounds/menuButtonChange.wav")
    choice = 0
    choice1 = 0
    n = 3
    menuscreen = 0
    yellowBox = False
    
    config = {}
    fail = open("config.txt")
    for line in fail:
        line = line.split("=")
        config[line[0]] = line[1].strip()
    fail.close()
    fullscreen = "fullscreen" in config and config["fullscreen"]
    mute = "mute" in config and config["mute"]
    
    redBox = False
    fontobject = pygame.font.SysFont('Arial', 24)

    bgSpeedX = randint(5, 15)
    bgSpeedY = randint(5, 15)

    bgOverlaySurf = screen.copy()
    bgOverlaySurf.fill((0, 0, 0))

def leave(screen):
    global bgAlpha
    bgAlpha = 0
    
def onEvent(event):
    
    global choice
    global menuscreen
    global n
    global yellowBox
    global mute
    global fullscreen
    global redBox
    global mouseMoved
    
    if abs(pygame.mouse.get_pos()[0] - mouseMoved[0]) > 2 or abs(pygame.mouse.get_pos()[1] - mouseMoved[1]) > 2:
        if pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350 and n >= 0:
            choice = 0
        elif pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 350 and pygame.mouse.get_pos()[1] < 400 and n >=1:
            choice = 1
        elif pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 450 and n >=2:
            choice = 2
        if pygame.mouse.get_pos()[0] > 570 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 450 and pygame.mouse.get_pos()[1] < 500 and n >=3:
            choice = 3
        mouseMoved = pygame.mouse.get_pos()
        
    else:
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and choice < n:
            choice +=1
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP)and choice > 0:
            choice -=1
        

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and menuscreen != 0:
        playsound(changeSound)
        menuscreen = 0
        choice = 0
        n = 3
        
    #valikud main menu juures
    if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and menuscreen == 0:
        playsound(changeSound)
        if choice == 0:
            #Start game
            main.setState(main.map_load)
        elif choice == 1:
            #Options
            menuscreen = 1
            n = 2
            choice = 0
        elif choice == 2:
            menuscreen = 2
            n = 0
            choice = 0
        elif choice == 3:
            #Quit game
            fail = open("config.txt", "w")
            fail.write("fullscreen="+ fullscreen+ "\n")
            fail.write("mute="+ mute)
            fail.close()
            main.quit()
            
    #valikud optionsi juures
    elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 350)) and (menuscreen == 1 or menuscreen == 2):
        playsound(changeSound)
        if choice == 0:
            menuscreen = 0
            n = 3
            
    #optionsi kraam
    if choice == 1 and menuscreen == 1:
        yellowBox = True
        
        if((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or  event.type == pygame.MOUSEBUTTONDOWN) and mute == "False":
            mute = "True"
            
        elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and mute == "True":
            mute = "False"
            
    elif choice == 2 and menuscreen == 1:        
        redBox = True

        if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and fullscreen == "True":
            fullscreen = "False"
            main.screen = pygame.display.set_mode((1280, 720)) 
        elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN) and fullscreen == "False":
            fullscreen = "True"
            main.screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    else:
        yellowBox = False
        redBox = False
        
def draw(screen,ms):
    global menupic
    global choice1
    global yellowBox
    global redBox
    global fullscreen
    global mute
    global bgPosX, bgPosY, bgSpeedX, bgSpeedY, bgAlpha
    screen.fill( (0,0,0) )
    menupic.set_alpha(100)
    bgPosX += bgSpeedX * ms / 1000
    bgPosY += bgSpeedY * ms / 1000
    if bgPosX < 0:
        bgPosX = 0
        bgSpeedX = randint(5, 15)
    elif bgPosX >= menupic.get_width()-screen.get_width():
        bgPosX = menupic.get_width()-screen.get_width()
        bgSpeedX = -randint(5, 15)
    if bgPosY < 0:
        bgPosY = 0
        bgSpeedY = randint(5, 15)
    elif bgPosY >= menupic.get_height() - screen.get_height():
        bgPosY = menupic.get_height()-screen.get_height()
        bgSpeedY = -randint(5, 15)
    screen.blit(menupic, (0,0), (bgPosX, bgPosY, screen.get_width(), screen.get_height()))
    screen.blit(radialGradPic, (0, 0))
    if bgAlpha < 255:
        bgAlpha += ms / 5
        bgOverlaySurf.set_alpha(255 - bgAlpha)
        screen.blit(bgOverlaySurf, (0, 0))
    #mainmenu
    if menuscreen == 0:
        screen.blit(fontobject.render("Start game", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
        screen.blit(fontobject.render("Credits", 1, (255, 255, 255)),(600, 400))
        screen.blit(fontobject.render("Quit game", 1, (255, 255, 255)),(600, 450))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))

    #options
    elif menuscreen == 1:
        if choice == 0:
            pygame.draw.rect(screen, (255,255,255),(575,310,10,10))
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
        pygame.draw.rect(screen, (255,255,255),(570,355,20,20),2)
        screen.blit(fontobject.render("Mute", 1, (255, 255, 255)),(600, 350))
        pygame.draw.rect(screen, (255,255,255),(570,390,20,20),2)
        screen.blit(fontobject.render("Fullscreen", 1, (255, 255, 255)),(600, 385))
        if mute == "True":
            pygame.draw.rect(screen, (255,255,255),(574,359,13,13))
        if yellowBox == True and choice == 1:
            pygame.draw.rect(screen, (255,255,0),(572,357,17,17),2)
        if fullscreen == "True":
            pygame.draw.rect(screen, (255, 255, 255), (574, 394, 13, 13))
        if redBox == True and choice == 2:
            pygame.draw.rect(screen, (255, 0, 0), (572, 392, 17, 17),2)
            
    #credits
    elif menuscreen == 2:
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("Hendrik Eerikson, Silver Juvanen, Karl Jääts, Meelis Perli, " +
                                      "Joonatan Samuel, Simo Sirel, Magnus Teekivi",
                                      1, (255, 255, 255)),(150, 360))
        screen.blit(fontobject.render("Developed as part of a 24 hour Arvutiklubi coding camp",
                                      1, (255, 255, 255)), (350, 420))
        screen.blit(fontobject.render("on 22nd to 23rd of November, 2014",
                                      1, (255, 255, 255)), (475, 450))
        screen.blit(fontobject.render("Credits", 1, (255, 255, 255)),(580, 200))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
        
    #sounds
    if choice != choice1:
        playsound(changeSound)
        choice1 = choice
