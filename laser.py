import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x,y, speed= -8):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
