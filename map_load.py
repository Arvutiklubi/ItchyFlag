import sys, pygame, math,character

def imageDim(image):
    return pygame.image.load(image).get_rect().size
    
pygame.init()

size = width, height = 1280,720

screen = pygame.display.set_mode(size)

sky_surfaces = {
        1 : pygame.image.load("image_data/sky/taevas1.png").convert_alpha()
    }
background_surfaces = {
        1 : pygame.image.load("image_data/background/taust1.png").convert_alpha(),
        2 : pygame.image.load("image_data/background/tree1.png").convert_alpha()
    }
ground_surfaces = {
        1 : pygame.image.load("image_data/ground/maapind1.png").convert_alpha()
    }

player = character.Player("char_data/mainchar_idle.png")

player.rect.y = height * (5/8)
player.rect.x = 70


group = pygame.sprite.Group()

group.add(player)

f = open("map.txt")
sky_line = f.readline().strip()
background_line = f.readline().strip()
ground_line = f.readline().strip()
f.close()

diff = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
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
                diffDir = ""
                
    screen.blit(sky_surfaces[1],(0,0))
    
    for i in range(len(sky_line)):
        screen.blit(sky_surfaces[int(sky_line[i])],(i*500 - diff,(height*0)))
        screen.blit(background_surfaces[int(background_line[i])],(i*500 - diff,(height*1/4)))
        screen.blit(ground_surfaces[int(ground_line[i])], (i * 500 - diff, (height) * 3/4))

    if player.rect.x > width/2:
        diff += 10
        player.rect.x -= 10
        
    group.update()
    group.draw(screen)

    pygame.display.flip()
