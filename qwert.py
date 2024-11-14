import pygame, sys
from player import Player
from alien import Alien
from laser import Laser

# Clases And Functions
class Menu():
    def __init__(self):
        # BackGround
        self.BG = pygame.transform.scale(pygame.image.load('Assets/space.png'), (screen_width, screen_height))

        # Loading images
        self.START_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Start_BTN.png'), (250,60)) 
        self.MAP_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Map_BTN.png'), (250,60))
        self.EXIT_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Exit_BTN.png'),(250,60))

        self.SETTINGS = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Settings_BTN.png'), (76,76))
        self.SHOP_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Shop_BTN.png'), (76,76)) 
        self.INFO_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Info_BTN.png'), (76,76)) 

        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1

        # Lasers
        self.lasers = pygame.sprite.Group()

    def shoot_lasers(self):
        self.lasers.add(Laser(self.rect.center))
        pass


    def alien_setup(self, rows, cols, x_distance = 80, y_distance = 64, x_offset = 50, y_offset= 50):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0 :alien_sprite = Alien('yellow', x, y)
                if row_index == 1 :alien_sprite = Alien('blue', x, y)
                if row_index == 2 :alien_sprite = Alien('green', x, y)
                if row_index == 3 :alien_sprite = Alien('pink', x, y)
                if row_index == 4 :alien_sprite = Alien('9', x, y)
                if row_index == 5 :alien_sprite = Alien('15', x, y)

                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            if alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)
        return self.alien_direction



    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance
                

    def draw_screen(self):
        screen.blit(self.BG, (0,0))
        screen.blit(self.START_BTN, (275, 300))
        screen.blit(self.MAP_BTN, (275, 400))
        screen.blit(self.EXIT_BTN, (275, 500))
        screen.blit(self.SETTINGS, (663, 50))
        screen.blit(self.SHOP_BTN, (663, 150))
        screen.blit(self.INFO_BTN, (663, 250))

    def press_mechanism(self, Img, X, Y):
        self.Img = Img
        self.rect = self.Img.get_rect(center= (X, Y))
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            self.Img = pygame.transform.scale(self.Img, (self.rect[2]+10, self.rect[3]+10))
            self.rect = self.Img.get_rect(center= (X, Y))
            screen.blit(self.Img, (self.rect.x, self.rect.y))

            if pygame.mouse.get_pressed()[0]:
                game_state.state = 'main_game'
        else:
            self.topleft = X, Y


    def update(self):
        self.draw_screen()
        self.press_mechanism(self.START_BTN, 400, 330 )
        self.press_mechanism(self.MAP_BTN,400, 430)
        self.press_mechanism(self.EXIT_BTN,400, 530)
        self.press_mechanism(self.SETTINGS,700, 88)
        self.press_mechanism(self.SHOP_BTN,700, 188)
        self.press_mechanism(self.INFO_BTN,700, 288)


class Game_State:
    def __init__(self):
        self.state = 'Menu'

    def menu_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        menu.update()
        pygame.display.update()
        clock.tick(60)

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys_pressed = pygame.key.get_pressed()
        #player.movement(keys_pressed)
        menu.aliens.draw(screen)
        direction = menu.alien_position_checker()
        menu.aliens.update(direction)
        #player.shoot(keys_pressed)
        pygame.display.update()
        clock.tick(60)
    
    def state_manager(self):
        if self.state == 'Menu':
            self.menu_start()
        if self.state == 'main_game':
            self.main_game()


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 800
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Objects
menu = Menu()
game_state = Game_State()

#Main Loop
while True:
    game_state.state_manager()
