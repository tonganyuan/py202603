import sys
import pygame
from settings import Settiongs
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settiongs()
        self.screen = pygame.display.set_mode((self.settings.screen_x,self.settings.screen_y))
        self.clock = pygame.time.Clock()
        self.bg_cloor = self.settings.bg_cloor
        pygame.display.set_caption("Alien Invasion")
        self.bullet_group = pygame.sprite.Group()
        self.ship = Ship(self)
    

    def run_game(self):
        while True:
            self._check_events()
            self.bullet_group.update()
            for bullet in self.bullet_group.copy():
                if bullet.rect.bottom <=0:
                    self.bullet_group.remove(bullet)
            print(len(self.bullet_group))
            self._update_screen()
            self.clock.tick(self.settings.tick)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    if len(self.bullet_group) < self.settings.bullet_allowed:
                        bullet = Bullet(self)
                        self.bullet_group.add(bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.move_left = False
            
            

    def _update_screen(self):
        self.screen.fill(self.bg_cloor)
        self.ship.update()
        self.ship.bliteme()
        for bullet in self.bullet_group.sprites():
            bullet.drawBullet()
        pygame.display.flip()
    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()