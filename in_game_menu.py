import pygame
def init(screen):
    global fontobject
    fontobject = pygame.font.SysFont('Arial', 24)
def onEvent(event):
    pass
def draw(screen,ms):
    screen.blit(fontobject.render("Back to game", 1, (255, 255, 255)),(600, 300))
