import pygame,sys
from alien import Run_Alien
from player import  Player
from menu import Menu

class Game_State:
    def __init__(self):
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def main_game(self):
        screen.blit(BG, (0,0))
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.player.update()
        run.aliens.draw(screen)
        self.collisons_check()
        direction = run.alien_position_checker()
        run.aliens.update(direction)


    def collisons_check(self):
        # player lasers
        for laser in self.player.sprite.lasers:
            if pygame.sprite.spritecollide(laser,run.aliens,True):
                laser.kill()

    
    def state_manager(self):
        state = menu.game_state
        if state == 'Loading':
            menu.loading_bar()
        elif state == 'Menu':
            menu.menu_update()
        elif state == 'main_game':
            self.main_game()
        elif state == 'settings':
            menu.draw_setting()


# General Setup
pygame.init()
clock = pygame.time.Clock()

# Screen
screen_width = 800
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
BG = pygame.transform.scale(pygame.image.load('Assets/space.png'), (screen_width,screen_height))

# Objects
player_sprite = Player()
game_state = Game_State()
menu = Menu(screen, screen_width, screen_height)
run = Run_Alien()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_state.state_manager()
    pygame.display.update()
    clock.tick(60)
