import pygame
from player import Player
from obstacle import Obstacle

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Health Sprite")
clock = pygame.time.Clock()

# Create player objects
player = Player(screen)
player2 = Player(screen, True)

# Create sprite groups
player_group = pygame.sprite.Group(player)
player2_group = pygame.sprite.Group(player2)

# Create obstacle objects
obstacle1 = Obstacle(screen, (150, 100), (31, 137), (193, 198, 36))
obstacle2 = Obstacle(screen, (700, 370), (140, 145), (127, 27, 163))
obstacle3 = Obstacle(screen, (284, 528), (12, 94), (138, 49, 27))
obstacle_group = pygame.sprite.Group(obstacle1, obstacle2, obstacle3)

# Collision handling
def collision(sprite, sprite_group):
    collided = pygame.sprite.spritecollide(sprite, sprite_group, False)
    for obj in collided:
        dx = sprite.rect.centerx - obj.rect.centerx
        dy = sprite.rect.centery - obj.rect.centery
        if abs(dx) > abs(dy):
            if dx > 0:
                sprite.rect.left = obj.rect.right
            else:
                sprite.rect.right = obj.rect.left
        else:
            if dy > 0:
                sprite.rect.top = obj.rect.bottom
            else:
                sprite.rect.bottom = obj.rect.top

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((100, 100, 100))

    # Update and draw player 1
    player.update()
    player_group.draw(screen)
    player.draw_health(screen)

    # Update and draw player 2
    player2.update()
    player2_group.draw(screen)
    player2.draw_health(screen)

    # Update and draw obstacles
    obstacle_group.draw(screen)

    # Handle collisions
    collision(player, obstacle_group)
    collision(player2, obstacle_group)
    collision(player, player2_group)
    collision(player2, player_group)

    # Update the display
    pygame.display.update()
    clock.tick(70)