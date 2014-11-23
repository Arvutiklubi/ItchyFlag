import pygame, map_load
def init():
    global heart_full
    global heart_empty
    heart_full = pygame.image.load('light_effects/syda1.png').convert_alpha()
    heart_empty = pygame.image.load('light_effects/syda2.png').convert_alpha()

def draw_ui(screen):
    counter = 0
    nr_hearts = int(round((map_load.player.health / 10), 0))
    for i in range(1, nr_hearts):
        screen.blit(heart_full, ((10+i*25), 10))
        counter += 1
    for i in range(counter, 9):
        screen.blit(heart_empty, ((10+i*25), 10))
