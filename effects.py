import pygame map_load

class knife(pygame.sprite.Sprite, knife_pos, suund, char_koord):

    def __init__(self, imgFile):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgFile)
        self.rect = (knife_pos[0], knife_pos[1], 50, 20)

    def update(self):
        if suund == 1:
            self.rect.x += 10
        if suund == -1:
            self.rect.x -= 10
