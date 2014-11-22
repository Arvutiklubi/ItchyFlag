import pygame
import main
def init(screen):
    
    global fontobject
    global choice
    #menus oleva pildi number
    global menuscreen
    #maksimum valikute arv lehel
    global n
    global menupic
    menupic = pygame.image.load("image_data/background/menuBackground.png").convert()
    choice = 0
    n = 3
    menuscreen = 0
    fontobject = pygame.font.SysFont('Arial', 24)
    
def onEvent(event):
    
    global choice
    global menuscreen
    global n
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
    if (event.type == pygame.K_RETURN or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and menuscreen == 0:
        if choice == 0:
            #Start game
            main.setState(main.map_load)
        elif choice == 1:
            #Options
            menuscreen = 1
            n = 0
            choice = 0
        elif choice == 3:
            #Quit game
            main.quit()
            
    #valikud optionsi juures
    elif (event.type == pygame.K_RETURN or (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] > 600 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 500)) and menuscreen == 1:
        if choice == 0:
            menuscreen = 0
            n = 3
            
def draw(screen,ms):
    global menupic
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
