import pygame
from settings import Settiongs

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settiongs()

        self.image = pygame.image.load('D:\\pyworkspace\\py202603\\alien_invasion\\images\\tiny_ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def bliteme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x