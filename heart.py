import pygame 
HEALTH_SPRITE_PATH = "Sprite-heart-real.png"

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        #initialize needed values for it to spawn and show the image at a specific place
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(HEALTH_SPRITE_PATH)
        self.rect = self.image.get_rect()
        self.size = size
        self.rect.center = (x, y - 100)
        


