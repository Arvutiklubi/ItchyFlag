import pygame, math, character, user_interface, main

def flip(img):
    aimg = pygame.transform.flip(img,1,0)
    return aimg

def init(screen):
    
    global sky_surfaces, background_surfaces
    global close_objects_surfaces, ground_surfaces
    global player, group
    global sky_line, background_line,enemy_line,enemy_ranged
    global close_objects_line, ground_line
    global diff, maxX, face, endHasBeenReached
    
    sky_surfaces = {
            1 : pygame.image.load("image_data/sky/taevas1.png").convert_alpha(),
        }
    background_surfaces = {
            1 : pygame.image.load("image_data/background/taust1.png").convert_alpha(),
            2 : pygame.image.load("image_data/background/taust2.png").convert_alpha(),
        }
    close_objects_surfaces = {
            1 : pygame.image.load("image_data/close_objects/tree1.png").convert_alpha(),
            2 : pygame.image.load("image_data/close_objects/tree2.png").convert_alpha(),
        }
    ground_surfaces = {
            1 : pygame.image.load("image_data/ground/maapind1.png").convert_alpha(),
        }

    player = character.Player("char_data/mainchar_idle.png")
    enemy_ranged = pygame.image.load("mob_data/creep_ranged.png")

    player.rect.y = screen.get_height() * (5/8)
    player.rect.x = 50
    player.image = pygame.transform.flip(player.image,1,0)

    group = pygame.sprite.Group()

    group.add(player)

    f = open("map.txt")
    sky_line = f.readline().strip()
    background_line = f.readline().strip()
    close_objects_line = f.readline().strip()
    ground_line = f.readline().strip()
    enemy_line = f.readline().strip().split()
    f.close()

    diff = 0
    endHasBeenReached = False
    maxX = len(sky_line) * 500
    face = "W"

def onEvent(e):
    global face

    if e.type == pygame.KEYDOWN:
        #if e.key == pygame.K_w:
                #player.speed[1] = -10
        #elif e.key == pygame.K_s:
                #player.speed[1] = 10
        if e.key == pygame.K_d:
            if face == "E":
                player.image = flip(player.image)
            player.speed[0] = 10
            face = "W"
        elif e.key == pygame.K_a:
            if face == "W":
                player.image = flip(player.image)
            player.speed[0] = -10
            face = "E"
        elif e.key == pygame.K_SPACE:
            if face == "W":
                player.image = flip(pygame.image.load("char_data/mainchar_attack.png"))
            else:
                player.image = pygame.image.load("char_data/mainchar_attack.png")

        if e.key == pygame.K_ESCAPE or e.key == pygame.K_p:
            main.setState(main.in_game_menu)
    elif e.type == pygame.KEYUP:
        player.speed[0] = 0
        player.speed[1] = 0

        if e.key == pygame.K_SPACE:
            if face == "W":
                player.image = flip(pygame.image.load("char_data/mainchar_idle.png"))
            else:
                player.image = pygame.image.load("char_data/mainchar_idle.png")

def draw(screen,millis):
    global diff, endHasBeenReached

    if diff + screen.get_width() >= maxX:
        endHasBeenReached = True

    if player.speed[0] > 0:
        player.image = player.runningAnimation("W")

    if player.speed[0] < 0:
        player.image = player.runningAnimation("E")
    
    screen.blit(sky_surfaces[1],(0,0))

    for i in range(len(sky_line)):
        screen.blit(background_surfaces[int(background_line[i])],(i*500 - diff,(130)))
        screen.blit(close_objects_surfaces[int(close_objects_line[i])],(i*500 - diff,screen.get_height()*1/4))
        screen.blit(ground_surfaces[int(ground_line[i])], (i * 500 - diff, (screen.get_height()) * 3/4))


    for i in range(len(enemy_line)):
        if diff>int(enemy_line[i]):
            screen.blit(enemy_ranged,(screen.get_width()-200,screen.get_height() * (5/8)))
    
    if player.rect.x > screen.get_width()/2 and not endHasBeenReached:
        diff += 10
        player.rect.x -= 10

    group.update(millis)
    group.draw(screen)
