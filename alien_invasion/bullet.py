import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def drawBullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y



