import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, isPlayer2 = False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        if not isPlayer2:
            self.image.fill((255, 0, 0))
        else:
            self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()/2, screen.get_height()/2)
        self.isPlayer2 = isPlayer2
    
    def update(self):
        keys = pygame.key.get_pressed()
        if self.isPlayer2:
            if keys[pygame.K_a]:
                self.rect.x -= 5
            if keys[pygame.K_d]:
                self.rect.x += 5
            if keys[pygame.K_w]:
                self.rect.y -= 5
            if keys[pygame.K_s]:
                self.rect.y += 5
        else:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5

        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 600
        if self.rect.y > 600:
            self.rect.y = 0


