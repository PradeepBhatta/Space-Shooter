import pygame, sys, time
pygame.init()

class Menu:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.game_state = 'Loading'

        # BackGround
        self.BG = pygame.transform.scale(pygame.image.load('Assets/space.png'), (screen_width, screen_height))

        # Loading Images For Menu
        self.START_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Start_BTN.png'), (250,60)) 
        self.MAP_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Map_BTN.png'), (250,60))
        self.EXIT_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Exit_BTN.png'),(250,60))

        self.SETTINGS = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Settings_BTN.png'), (76,76))
        self.SHOP_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Shop_BTN.png'), (76,76)) 
        self.INFO_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Main_Menu/Info_BTN.png'), (76,76)) 

        # Loading Images For Settings
        self.MENU_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Menu_BTN.png'),(76,76))
        self.CLOSE_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Close_BTN.png'),(76,76))
        self.MUSIC_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Music_BTN.png'), (76,76))
        self.SOUND_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Sound_BTN.png'), (76,76))
        self.OK_BTN = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Ok_BTN.png'), (76,76) )
        self.WINDOW = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Window_2.png'), (460,670))
        self.HEADER = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Header.png'), (190,25))
        self.MUSIC = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Music.png'), (120,25))
        self.SOUND = pygame.transform.scale(pygame.image.load('Assets/Menu/Setting/Sound.png'), (130,25))

        # Loading Images For Loading Bar
        self.current = 0 
        self.BORDER = pygame.transform.scale(pygame.image.load('Assets/Menu/Loading_Bar/Table.png'),(504,30))
        self.BORDER_rect = self.BORDER.get_rect() 


    def loading_bar(self):
        self.screen.blit(self.BG, (0,0))
        self.screen.blit(self.BORDER, (148,285))
        load_bar_rect = pygame.Rect(151,288,self.current, 25)
        pygame.draw.rect(self.screen, (255,0,0), load_bar_rect, border_radius = 3)
        
        print(self.BORDER_rect.right, load_bar_rect.right)
        print(self.BORDER_rect.topright)
        if load_bar_rect.right <= self.BORDER_rect.right:
            self.current += 10
        if load_bar_rect.right > self.BORDER_rect.right:
            time.delay(100)
            self.game_state = 'Menu'   

    def draw_menu(self):
        self.screen.blit(self.BG, (0,0))
        self.screen.blit(self.START_BTN, (275, 300))
        self.screen.blit(self.MAP_BTN, (275, 400))
        self.screen.blit(self.EXIT_BTN, (275, 500))
        self.screen.blit(self.SETTINGS, (663, 50))
        self.screen.blit(self.SHOP_BTN, (663, 150))
        self.screen.blit(self.INFO_BTN, (663, 250))


    def press_mechanism(self, Img, X, Y):
        self.Img = Img
        self.rect = self.Img.get_rect(center= (X, Y))
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            self.Img = pygame.transform.scale(self.Img, (self.rect[2]+10, self.rect[3]+10))
            self.rect = self.Img.get_rect(center= (X, Y))
            self.screen.blit(self.Img, (self.rect.x, self.rect.y))

            if pygame.mouse.get_pressed()[0]:
                if Img == self.START_BTN :
                    self.game_state = 'main_game'

                elif Img == self.SETTINGS:
                    self.game_state = 'settings'
    
                elif Img == self.EXIT_BTN:
                    pygame.quit()
                    sys.exit()

    def menu_update(self):
        self.draw_menu()
        self.press_mechanism(self.START_BTN, 400, 330 )
        self.press_mechanism(self.MAP_BTN,400, 430)
        self.press_mechanism(self.EXIT_BTN,400, 530)
        self.press_mechanism(self.SETTINGS,700, 88)
        self.press_mechanism(self.SHOP_BTN,700, 188)
        self.press_mechanism(self.INFO_BTN,700, 288)

    def map_(self):
        self.screen.blit(self.BG, (0,0))

    def draw_setting(self):

        self.screen.blit(self.BG, (0,0))
        self.screen.blit(self.WINDOW, (195,5))
        self.screen.blit(self.HEADER, (302, 25))
        self.screen.blit(self.MUSIC_BTN, (225, 85))
        self.screen.blit(self.SOUND_BTN, (225, 175))
        self.screen.blit(self.MUSIC, (350, 110))
        self.screen.blit(self.SOUND, (350, 200))
        self.screen.blit(self.CLOSE_BTN, (250, 450))
        self.screen.blit(self.MENU_BTN, (350, 450))
        self.screen.blit(self.OK_BTN, (450, 450))

        self.press_mechanism(self.MUSIC_BTN, 263, 123 )
        self.press_mechanism(self.SOUND_BTN, 263, 213 )
