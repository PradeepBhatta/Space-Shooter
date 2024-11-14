import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.PLAYER_WIDTH = int(107/1.4)
        self.PLAYER_HEIGHT = int(138/1.4)
        self.image = pygame.image.load('Assets/player.png')
        self.image = pygame.transform.scale(self.image, (self.PLAYER_WIDTH,self.PLAYER_HEIGHT))
        self.rect = self.image.get_rect(center= (400, 600))
        
        self.laser_cooldown = 500
        self.laser_time = 0
        self.ready = True

        self.lasers = pygame.sprite.Group()

    def movement(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.x > 0:  # LEFT
            self.rect.x -= 5
        if key[pygame.K_RIGHT] and self.rect.x < 800 - self.PLAYER_WIDTH:  # RIGHT
            self.rect.x += 5
        if key[pygame.K_UP] and self.rect.y > 0:  # UP
            self.rect.y -= 5
        if key[pygame.K_DOWN] and self.rect.y < 680 - self.PLAYER_HEIGHT:  # DOWN
            self.rect.y += 5  

        if key[pygame.K_SPACE] and self.ready :
            self.ready = False
            self.shoot_laser()
            self.laser_time = pygame.time.get_ticks()

    def shoot_laser(self):
        space = 0
        for i in range(1):
            self.lasers.add(Laser(self.rect.x + 38 , self.rect.y+ space))
            space += 50 

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def update(self):
        self.movement()
        self.recharge()
        self.lasers.update()
