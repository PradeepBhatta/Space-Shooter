import pygame, sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

class bar:
    def __init__(self):
        self.current = 0 
        self.BORDER = pygame.transform.scale(pygame.image.load('Assets/Menu/Loading_Bar/Table.png'),(504,30))
        self.BORDER_rect = self.BORDER.get_rect() 

    def loading_bar(self):
        screen.blit(self.BORDER, (7,42))
        load_bar_rect = pygame.Rect(10,45,self.current, 25)
        pygame.draw.rect(screen, (255,0,0), load_bar_rect, border_radius = 3)
        if load_bar_rect.right <= self.BORDER_rect.right:
            self.current += 10

    
l = bar()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 150, 200))
    l.loading_bar()
    pygame.display.update()
    clock.tick(30)