import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y ):
        super().__init__()
        file_path = 'Assets/Aliens/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75,75)), 180)
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, direction):
        self.rect.x += direction

class Run_Alien:
    def __init__(self):
        # Alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_direction = 1


    def alien_setup(self, rows, cols, x_distance = 80, y_distance = 64, x_offset = 50, y_offset= 50):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                ######################################
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
            if alien.rect.right >= 800: # Flexibility Check
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
                
