import pygame
import os
from heart import Heart

IDLE_PATH = "blackwhiteChar/idle/PNG file/"
ATTACK_PATH = "blackwhiteChar/Attack/png file/"
JUMP_PATH = "blackwhiteChar/jump/jump.png"
RUN_PATH = "blackwhiteChar/run/Png/"
FALLING_PATH = "blackwhiteChar/falling/"
class Player(pygame.sprite.Sprite):
    def __init__(self, screen, isPlayer2=False):
        pygame.sprite.Sprite.__init__(self)
        self.state = "idle"
        self.frame_index = 0
        self.animation_speed = 0.1
        self.health = 3
        self.images = self.load_images(self.state)
        self.image = self.images[self.frame_index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.health_sprite = Heart(self.rect.x, self.rect.y, 20)
        if not isPlayer2:
            self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
            self.rect 
        else:
            self.rect.center = (screen.get_width() / 2 + 60, screen.get_height() / 2)
        self.isPlayer2 = isPlayer2

    def load_images(self, state):
        images = []
        if state == "idle":
            for file_name in sorted(os.listdir(IDLE_PATH)):
                if file_name.endswith(".png"):
                    images.append(pygame.image.load(os.path.join(IDLE_PATH, file_name)))
        elif state == "attack":
            for file_name in sorted(os.listdir(ATTACK_PATH)):
                if file_name.endswith(".png"):
                    images.append(pygame.image.load(os.path.join(ATTACK_PATH, file_name)))
        elif state == "falling":
            for file_name in sorted(os.listdir(FALLING_PATH)):
                if file_name.endswith(".png"):
                    images.append(pygame.image.load(os.path.join(FALLING_PATH, file_name)))
        elif state == "jump":
            images.append(pygame.image.load(JUMP_PATH))
        elif state == "run":
            for file_name in sorted(os.listdir(RUN_PATH)):
                if file_name.endswith(".png"):
                    images.append(pygame.image.load(os.path.join(RUN_PATH, file_name)))
        return images

    def state_manager(self):
        self.images = self.load_images(self.state)
        self.frame_index = 0

    def attack(self):
        self.state = "attack"
        self.state_manager()

    def update(self):
        previous_state = self.state
        
        keys = pygame.key.get_pressed()
        if self.isPlayer2:
            if keys[pygame.K_a]:
                self.rect.x -= 5
                self.state = "run"
            if keys[pygame.K_d]:
                self.rect.x += 5
                self.state = "run"
            if keys[pygame.K_w]:
                self.rect.y -= 5
                self.state = "jump"
            if keys[pygame.K_s]:
                self.rect.y += 5
                self.state = "falling"
            if keys[pygame.K_SPACE]:
                self.attack()
        else:
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                self.state = "run"
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                self.state = "run"
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                self.state = "jump"
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                self.state = "falling"
            if keys[pygame.K_RETURN]:
                self.attack()

        if self.isPlayer2 and not any([keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_SPACE], keys[pygame.K_RETURN]]):
            self.state = "idle"
        if not self.isPlayer2 and not any([keys[pygame.K_LEFT], keys[pygame.K_RIGHT], keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_RETURN]]):
            self.state = "idle"

        if self.state != previous_state:
            self.state_manager()

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            self.frame_index = 0
        self.image = self.images[int(self.frame_index)]

        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 600
        if self.rect.y > 600:
            self.rect.y = 0
