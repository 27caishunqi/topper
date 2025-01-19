import pygame

HEALTH_SPRITE_PATH = "Sprite-heart-real.png"

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(HEALTH_SPRITE_PATH).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
