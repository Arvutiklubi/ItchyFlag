import pygame
import main
def init(screen):
    global fontobject
    global choice
    choice = 0
    fontobject = pygame.font.SysFont('Arial', 24)
def onEvent(event):
    global choice
    if event.type == pygame.KEYDOWN and event.key == pygame.K_s and choice < 2:
        choice +=1
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and choice > 0:
        choice -=1
    
def draw(screen,ms):
    screen.fill( (0,0,0) )
    screen.blit(fontobject.render("Start game", 1, (255, 255, 255)),(600, 300))
    screen.blit(fontobject.render("Options", 1, (255, 255, 255)),(600, 350))
    screen.blit(fontobject.render("Quit game", 1, (255, 255, 255)),(600, 400))
    pygame.draw.rect(screen, (255,255,255),(575,310 + choice*50 ,10,10))
    
