import pygame, math, character, user_interface, main, effects

transitionPercent = 0.0
transitionSurf1 = transitionSurf2 = None

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
    global group_knives,enemies
    global transitionShadow1, transitionShadow2
    
    sky_surfaces = {
            1 : pygame.image.load("image_data/sky/taevas1.png").convert_alpha(),
            2 : pygame.image.load("image_data/sky/taevas2.png").convert_alpha(),
        }
    background_surfaces = {
            1 : pygame.image.load("image_data/background/taust1.png").convert_alpha(),
            2 : pygame.image.load("image_data/background/taust2.png").convert_alpha(),
            3 : pygame.image.load("image_data/background/taust3.png").convert_alpha(),
            4 : pygame.image.load("image_data/background/taust4.png").convert_alpha(),
        }
    close_objects_surfaces = {
            1 : pygame.image.load("image_data/close_objects/tree1.png").convert_alpha(),
            2 : pygame.image.load("image_data/close_objects/tree2.png").convert_alpha(),
            3 : pygame.image.load("image_data/close_objects/tree3.png").convert_alpha(),
        }
    ground_surfaces = {
            1 : pygame.image.load("image_data/ground/maapind1.png").convert_alpha(),
            2 : pygame.image.load("image_data/ground/maapind2.png").convert_alpha(),
        }

    player = character.Player("char_data/mainchar_idle.png","char_data/mainchar_run.png")

    player.rect.y = screen.get_height() * (5/8)
    player.rect.x = 50
    player.image = pygame.transform.flip(player.image,1,0)

    group = pygame.sprite.Group()
    group_knives = pygame.sprite.Group()
    
    enemies = pygame.sprite.Group()

    group.add(player)

    f = open("map.txt")
    sky_line = f.readline().strip()
    background_line = f.readline().strip()
    close_objects_line = f.readline().strip()
    ground_line = f.readline().strip()
    enemy_line = f.readline().strip().split()
    f.close()

    for distance in enemy_line:
        enemy = character.Zombie("mob_data/creep_ranged.png","mob_data/creep_ranged_run.png")
        enemy.rect.x = int(distance)
        enemy.rect.y = screen.get_height() * (5/8)
        enemies.add(enemy)
        

    diff = 0
    endHasBeenReached = False
    maxX = len(sky_line) * 500
    face = "W"

    user_interface.init()

    transitionShadow1 = pygame.image.load("intro/shadow.png")
    transitionShadow2 = pygame.transform.flip(transitionShadow1, False, True)

def leave(screen):
    global transitionPercent, transitionSurf1, transitionSurf2
    transitionPercent = 0.0
    transitionSurf1 = transitionSurf2 = None

def onEvent(e):
    global face
    global group_knives

    if e.type == pygame.KEYDOWN:
        #if e.key == pygame.K_w:
                #player.speed[1] = -10
        #elif e.key == pygame.K_s:
                #player.speed[1] = 10
        if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
            if face == "E":
                player.image = flip(player.image)
            player.speed[0] = 10
            face = "W"
        elif e.key == pygame.K_a or e.key == pygame.K_LEFT:
            if face == "W":
                player.image = flip(player.image)
            player.speed[0] = -10
            face = "E"
        elif e.key == pygame.K_SPACE:
            if face == "W":
                player.image = flip(pygame.image.load("char_data/mainchar_attack.png"))
            else:
                player.image = pygame.image.load("char_data/mainchar_attack.png")

        elif e.key == pygame.K_ESCAPE or e.key == pygame.K_p:
            main.setState(main.in_game_menu)

        elif e.key == pygame.K_h:
            group_knives.add(effects.Knife(1000, -1))
            
    elif e.type == pygame.KEYUP:
        if e.key == pygame.K_a and face =="E":
            player.speed[0] = 0
        elif e.key == pygame.K_d and face == "W":
            player.speed[0] = 0
        elif e.key == pygame.K_SPACE:
            if face == "W":
                player.image = flip(pygame.image.load("char_data/mainchar_idle.png"))
            else:
                player.image = pygame.image.load("char_data/mainchar_idle.png")

def draw(screen,millis):
    global diff, endHasBeenReached, enemies
    global transitionPercent, transitionSurf1, transitionSurf2

    if not transitionSurf1 or not transitionSurf2:
        scopy = screen.copy()
        transitionSurf1 = scopy.subsurface((0, 0,
                                            screen.get_width(),
                                            screen.get_height()//2))
        transitionSurf2 = scopy.subsurface((0, screen.get_height()//2,
                                            screen.get_width(),
                                            screen.get_height()//2))

    if diff + screen.get_width() >= maxX:
        endHasBeenReached = True

    if player.speed[0] > 0:
        player.image = player.runningAnimation("W")

    if player.speed[0] < 0:
        player.image = player.runningAnimation("E")
    
    #screen.blit(sky_surfaces[1],(0,0))

    for i in range(len(sky_line)):
        screen.blit(sky_surfaces[int(sky_line[i])],(i*1280,0))
        screen.blit(background_surfaces[int(background_line[i])],(i*500 - diff,(130)))
        screen.blit(close_objects_surfaces[int(close_objects_line[i])],(i*500 - diff,screen.get_height()*1/4))
        screen.blit(ground_surfaces[int(ground_line[i])], (i * 500 - diff, (screen.get_height()) * 3/4))
    
    if player.rect.x > screen.get_width()/2 and not endHasBeenReached:
        diff += 10
        player.rect.x -= 10
        for enemy in enemies:
            enemy.rect.x -= 10

    if player.rect.x > screen.get_width() - 150:
        player.rect.x = screen.get_width() - 150
    elif player.rect.x < -50:
        player.rect.x = -50

    group.update(millis)
    group.draw(screen)

    #joonistame vastased ekraanile
   
    for enemy in enemies:
        enemy.updateAI(player.rect.x, 2000 ,millis,diff,screen.get_width())
        if enemy.speed[0] > 0:
            enemy.image = enemy.runningAnimation("W")
        if enemy.speed[0] < 0:
            enemy.image = enemy.runningAnimation("E")
    enemies.update(millis)       
    enemies.draw(screen)
    
    group_knives.update(millis, diff)
    group_knives.draw(screen)
    
    user_interface.draw_ui(screen)
    
    if transitionPercent < 100.0:
        transitionPercent += millis / 10
        
        h = screen.get_height() / 2
        addY = h * transitionPercent // 100
        screen.blit(transitionShadow1, (0, h - addY))
        screen.blit(transitionShadow2, (0, h + addY - transitionShadow2.get_height()))
        screen.blit(transitionSurf1, (0, 0), (0, addY, screen.get_width(), h))
        screen.blit(transitionSurf2, (0, h + addY), (0, addY, screen.get_width(), h))
