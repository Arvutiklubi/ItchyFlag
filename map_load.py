import sys, pygame, math,character

def imageDim(image):
    return pygame.image.load(image).get_rect().size
    
pygame.init()

size = width, height = 1280,720

screen = pygame.display.set_mode(size)

sky_surfaces = {
        1 : pygame.image.load("image_data/sky/taevas1.png")
    }
background_surfaces = {
        1 : pygame.image.load("image_data/background/taust1.png"),
        2 : pygame.image.load("image_data/background/taust2.png")
    }
close_objects_surfaces = {
        1 : pygame.image.load("image_data/close_objects/tree1.png"),
        2 : pygame.image.load("image_data/close_objects/tree2.png")
    }
ground_surfaces = {
        1 : pygame.image.load("image_data/ground/maapind1.png")
    }

player = character.Player("char_data/mainchar_idle.png")

player.rect.y = height * (5/8)
player.rect.x = 50


group = pygame.sprite.Group()

group.add(player)

f = open("map.txt")
sky_line = f.readline().strip()
background_line = f.readline().strip()
close_objects_line = f.readline().strip()
ground_line = f.readline().strip()
f.close()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit()
        
        elif e.type == pygame.KEYDOWN:
            #if e.key == pygame.K_w:
                    #player.speed[1] = -10
            #elif e.key == pygame.K_s:
                    #player.speed[1] = 10
            if e.key == pygame.K_d:
                    player.speed[0] = 10
            elif e.key == pygame.K_a:
                    player.speed[0] = -10
        elif e.type == pygame.KEYUP:
                player.speed[0] = 0
                player.speed[1] = 0
                
    screen.blit(sky_surfaces[1],(0,0))

    for i in range(len(sky_line)):
        screen.blit(sky_surfaces[int(sky_line[i])],(i*500,(height*0)))
        screen.blit(background_surfaces[int(background_line[i])],(i*500,(height*1/4)))
        screen.blit(close_objects_surfaces[int(close_objects_line[i])],(i*500,height*1/4))
        screen.blit(ground_surfaces[int(ground_line[i])], (i * 500, (height) * 3/4))

    group.update()
    group.draw(screen)

    pygame.display.flip()
