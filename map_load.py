import sys, pygame, math

pygame.init()

size = width, height = 800,600

screen = pygame.display.set_mode(size)

sky_surfaces = {
        1 : pygame.image.load("image_data/sky/taevas1.png")
    }
background = {
        1 : pygame.image.load("image_data/background/taust1.png"),
        2 : pygame.image.load("image_data/background/tree1.png")
    }
ground_surfaces = {
        1 : pygame.image.load("image_data/ground/maapind1.png")
    }

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    screen.blit(sky_surfaces[1],(0,0))

    for i in range(3):
        screen.blit(background[1],(i*540,(height-500)*3/4))
        screen.blit(background[2],(i*540+20,(height-500)*3/4))

    pygame.display.flip()
