import pygame,sys

class Character(pygame.sprite.Sprite):

    def __init__(self,imgFile):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgFile)
        self.rect = self.image.get_rect()
        
        self.waitTime = 100
        self.prevAnim = 1
        self.curAnim = 0

        self.speed = [0,0]

    def update(self,ms):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        self.waitTime -= ms

        if self.waitTime <= 0:
            if self.prevAnim == 0:
                self.curAnim = 1
                self.prevAnim = 1
            elif self.prevAnim == 1:
                self.curAnim = 2
                self.prevAnim = 2
            elif self.prevAnim == 2:
                self.curAnim = 0
                self.prevAnim = 0
                
            self.waitTime = 100     

class Player(Character):
    
    def __init__(self,imgFile):
        Character.__init__(self,imgFile)
        self.health = 100

        self.prevAnim = 1
        self.curAnim = 0
        
        self.animations = []
        self.animations.append(pygame.image.load("char_data/mainchar_run1.png"))
        self.animations.append(pygame.image.load("char_data/mainchar_run2.png"))
        self.animations.append(pygame.image.load("char_data/mainchar_run3.png"))

    def runningAnimation(self,face):
        self.prevAnim = self.curAnim
        if face == "W":
            return pygame.transform.flip(self.animations[self.curAnim],1,0)
        else:
            return self.animations[self.curAnim]

class Zombie(Character):
    
    def __init__(self,imgFile):
        Character.__init__(self,imgFile)
        self.health = 50
