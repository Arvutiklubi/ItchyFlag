import pygame, map_load

class Knife(pygame.sprite.Sprite):

    def __init__(self, knife_pos, suund, char_koord):
        pygame.sprite.Sprite.__init__(self)
        self.knife_pos = knife_pos
        self.suund = suund
        self.image = pygame.image.load('light_effects/nuga.png').convert_alpha()
        self.rect = pygame.Rect(knife_pos, 540, 50, 20)

        self.waitTime = 20 

    def update(self, ms, diff):
        if self.rect.left >= 1280 or self.rect.right <= 0:
            self.kill()
        self.waitTime -= ms
        if self.waitTime <= 0:
            if self.suund == 1:
                self.knife_pos += 10
                self.rect.x = self.knife_pos-diff
            if self.suund == -1:
                self.knife_pos -= 10
                self.rect.x = self.knife_pos-diff
        
