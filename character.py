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
        self.health = 100


class Zombie(Character):
    
    def __init__(self,imgFile):
        Character.__init__(self,imgFile)
        self.health = 50
