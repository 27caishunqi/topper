import pygame
import os
from heart import Heart

# Paths to animations (ensure these paths are correct for your project)
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
        self.rect = self.image.get_rect()
        self.isPlayer2 = isPlayer2

        self.is_facing_right = True

        # Positioning
        if not isPlayer2:
            self.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        else:
            self.rect.center = (screen.get_width() / 2 + 60, screen.get_height() / 2)

        # Health sprites
        self.health_sprites = [
            Heart(self.rect.centerx - 20, self.rect.top - 20, 20),
            Heart(self.rect.centerx, self.rect.top - 20, 20),
            Heart(self.rect.centerx + 20, self.rect.top - 20, 20)
        ]
        # Flag to ensure one hit per attack swing
        self.has_attacked = False

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

    def state_manager(self, new_state):
        if new_state != self.state:
            print(f"State changing from {self.state} to {new_state}")
            self.state = new_state
            self.images = self.load_images(self.state)
            self.frame_index = 0
            # Reset the attack flag when leaving the attack state
            if new_state != "attack":
                self.has_attacked = False

    def attack(self):
        self.state_manager("attack")

    def update(self):
        keys = pygame.key.get_pressed()
        new_state = self.state  # Track the desired state

        # Player 2 Controls
        if self.isPlayer2:
            if keys[pygame.K_a]:
                self.rect.x -= 5
                new_state = "run"
                self.is_facing_right = False
            if keys[pygame.K_d]:
                self.rect.x += 5
                new_state = "run"
                self.is_facing_right = True
            if keys[pygame.K_w]:
                self.rect.y -= 5
                new_state = "jump"
            if keys[pygame.K_s]:
                self.rect.y += 5
                new_state = "falling"
            if keys[pygame.K_SPACE]:  # Attack key
                new_state = "attack"
        else:  # Player 1 Controls
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
                new_state = "run"
                self.is_facing_right = False
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
                new_state = "run"
                self.is_facing_right = True
            if keys[pygame.K_UP]:
                self.rect.y -= 5
                new_state = "jump"
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
                new_state = "falling"
            if keys[pygame.K_RETURN]:  # Attack key
                new_state = "attack"

        # Default back to idle if no key is pressed (adjust as needed)
        if new_state == self.state and not any(keys):
            new_state = "idle"

        self.state_manager(new_state)

        # Update animation frame
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.images):
            # If the attack animation finishes, allow a new attack next swing
            if self.state == "attack":
                self.has_attacked = False
            self.frame_index = 0

        current_image = self.images[int(self.frame_index)]
        if not self.is_facing_right:
            current_image = pygame.transform.flip(current_image, True, False)
        self.image = current_image

        # Screen wrapping
        if self.rect.x < 0:
            self.rect.x = 800
        if self.rect.x > 800:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 600
        if self.rect.y > 600:
            self.rect.y = 0

        # Update health sprite positions
        for i in range(len(self.health_sprites)):
            pos = -22 + 22 * i
            self.health_sprites[i].rect.center = (self.rect.centerx + pos, self.rect.top - 20)

    def draw_health(self, screen):
        for heart in self.health_sprites:
            screen.blit(heart.image, heart.rect)

    def hurt(self, other_player):
        print(f"Hurting {other_player}. Current health: {other_player.health}")
        other_player.health -= 1
        # Always remove one heart if available—even the last one.
        if other_player.health_sprites:
            other_player.health_sprites.pop()
        if other_player.health > 0:
            print(f"{other_player} health now: {other_player.health}")
        else:
            print(f"{other_player} is out of health!")
