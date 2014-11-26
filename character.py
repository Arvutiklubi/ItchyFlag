import pygame,sys

class Character(pygame.sprite.Sprite):

    def __init__(self,imgFile,runFile = None):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgFile)
        self.rect = self.image.get_rect()
        
        self.waitTime = 100
        self.curAnim = 0

        self.speed = [0,0]

        if runFile == None:
            self.mainSurface = pygame.image.load(imgFile)
            
        else:
            self.mainSurface = pygame.image.load(runFile)
            
        self.animations = []
        self.animLen = int(self.mainSurface.get_rect().width / 200)

        if self.animLen == 1:
            self.animations.append(self.image)
        else:
            for a in range(0,self.animLen):
                self.animations.append(self.mainSurface.subsurface(a * 200,0, 200,200))

    def update(self,ms):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        self.waitTime -= ms

        if self.waitTime <= 0:
            if self.curAnim == self.animLen - 1:
                self.curAnim = 0
            else:
                self.curAnim += 1
                
            self.waitTime = 100
        
    def runningAnimation(self,face):
        
        self.prevAnim = self.curAnim

        print(self.curAnim)

        if face == "W":
            return pygame.transform.flip(self.animations[self.curAnim],1,0)
        else:
            return self.animations[self.curAnim]
        
class Player(Character):
    
    def __init__(self,imgFile,runFile):
        Character.__init__(self,imgFile,runFile)
        self.health = 100


class Zombie(Character):
    
    def __init__(self,imgFile,runFile):
        Character.__init__(self,imgFile,runFile)
        self.health = 50
        self.range = 50
        self.time_waited = 0
        self.to_move,self.to_attack = False,False
        self.hasBeenSeen = False

    def updateAI(self,playerX,difficulty,ms,diff,width):
        
        self.to_move = True
        self.to_attack = False

        if self.rect.x < diff + width:
            self.hasBeenSeen = True
        
        if abs(self.rect.x - playerX) <= self.range:
            self.to_move = False
            self.speed[0] = 0
            
            self.time_waited += ms

            if self.time_waited > difficulty:
                self.to_attack = True
        
        elif self.to_move and self.hasBeenSeen:
            if self.rect.x - playerX > 0:
                self.speed[0] = -2
            elif self.rect.x - playerX < 0:
                self.speed[0] = 2

        
        
