import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((57, 147))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/4, screen.get_height()/3)
        self.image2 = pygame.Surface((57, 147))
        self.image2.fill((0, 255, 255))
        self.rect2 = self.image2.get_rect()
        self.rect2.center = (screen.get_width()/1.3, screen.get_height()/2.5)
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x -= 0
        self.rect.y -= 0
        self.rect2.x -= 0
        self.rect2.y -= 0
