import pygame
import main
def init(screen):
    global fontobject
    global choice
    #menus oleva pildi number
    global menuscreen
    #maksimum valikute arv lehel
    global n
    choice = 0
    n = 2
    menuscreen = 0
    fontobject = pygame.font.SysFont('Arial', 24)
def onEvent(event):
    global choice
    global menuscreen
    global n
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_s or event.key == pygame.K_DOWN) and choice < n:
        choice +=1
    elif event.type == pygame.KEYDOWN and (event.key == pygame.K_w or event.key == pygame.K_UP)and choice > 0:
        choice -=1
    #valikud main menu juures
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and menuscreen == 0:
        if choice == 0:
            #Start game
            main.setState(main.ingame)
        elif choice == 1:
            #Options
            menuscreen = 1
            n = 0
            choice = 0
        elif choice == 2:
            #Quit game
            main.setState(main.mainmenu)
    #valikud optionsi juures
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and menuscreen == 1:
        if choice == 0:
            menuscreen = 0
            n = 2
def draw(screen,ms):
    #mainmenu
    if menuscreen == 0:
        screen.fill( (0,0,0) )
        screen.blit(fontobject.render("Start game", 1, (255, 255, 255)),(600, 300))
        screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
        screen.blit(fontobject.render("Quit game", 1, (255, 255, 255)),(600, 400))
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
    #options
    elif menuscreen == 1:
        screen.fill( (0,0,0) )
        pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50,10,10))
        screen.blit(fontobject.render("Back", 1, (255, 255, 255)),(600, 300))
