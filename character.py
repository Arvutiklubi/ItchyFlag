import pygame,sys

class Character(pygame.sprite.Sprite):

    def __init__(self,imgFile):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgFile)
        self.rect = self.image.get_rect()

        self.speed = [0,0]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        #print(ms / 1000)


class Player(Character):
    
    def __init__(self,imgFile):
        Character.__init__(self,imgFile)


class Zombie(Character):
    
    def __init__(self,imgFile):
        Character.__init__(self,imgFile)


if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()
    
    pygame.display.set_caption("Player test")
    
    screen = pygame.display.set_mode((600,600))

    group = pygame.sprite.Group()
    eg = pygame.sprite.Group()
    
    player = Player("player.png")
    enemy = Zombie("player.png")

    group.add(player)
    eg.add(enemy)

    player.rect.x = 300
    player.rect.y = 300
    
    enemy.rect.x = 500
    enemy.rect.y = 500
    
    while 1:
        ms = clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
               pygame.quit()
               sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    enemy.speed[1] = -2
                elif e.key == pygame.K_s:
                    enemy.speed[1] = 2
                elif e.key == pygame.K_d:
                    enemy.speed[0] = 2
                elif e.key == pygame.K_a:
                    enemy.speed[0] = -2
            elif e.type == pygame.KEYUP:
                enemy.speed[0] = 0
                enemy.speed[1] = 0

        if pygame.sprite.spritecollide(enemy,group,0):
            print("yes")
        screen.fill((0,0,0))

        group.update()
        eg.update()
        
        group.draw(screen)
        eg.draw(screen)
        
        pygame.display.flip()
    
    
