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
player2 = Player(screen, isPlayer2=True)

# Create obstacle objects (adjust positions, sizes, and colors as needed)
obstacle1 = Obstacle(screen, (150, 100), (31, 137), (193, 198, 36))
obstacle2 = Obstacle(screen, (700, 370), (140, 145), (127, 27, 163))
obstacle3 = Obstacle(screen, (284, 528), (12, 94), (138, 49, 27))
obstacle_group = pygame.sprite.Group(obstacle1, obstacle2, obstacle3)

# Function to handle collisions with obstacles (physical collisions)
def handle_obstacle_collision(sprite, sprite_group):
    collided = pygame.sprite.spritecollide(sprite, sprite_group, False)
    for obj in collided:
        # Basic collision response: push the sprite out of the object
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

# Function to handle player-vs-player attacks with extended range
def player_attack_collision(attacker, defender, attack_range=40):
    if attacker.state == "attack" and not attacker.has_attacked:
        dx = attacker.rect.centerx - defender.rect.centerx
        dy = attacker.rect.centery - defender.rect.centery
        distance = (dx**2 + dy**2)**0.5
        if distance <= attack_range:
            print(f"{attacker} is attacking {defender} from {distance:.2f} pixels away")
            attacker.hurt(defender)
            attacker.has_attacked = True

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((100, 100, 100))

    # Update players
    player.update()
    player2.update()

    # Draw players
    screen.blit(player.image, player.rect)
    screen.blit(player2.image, player2.rect)

    # Draw health sprites
    player.draw_health(screen)
    player2.draw_health(screen)

    # Draw obstacles
    obstacle_group.draw(screen)

    # Handle obstacle collisions (physical movement constraints)
    handle_obstacle_collision(player, obstacle_group)
    handle_obstacle_collision(player2, obstacle_group)

    # Handle player vs. player attacks (allows attack from 20 pixels away)
    player_attack_collision(player, player2, attack_range=20)
    player_attack_collision(player2, player, attack_range=20)

    # Update display and tick clock
    pygame.display.update()
    clock.tick(70)
    if player.health == 0 or player2.health == 0:
        break

if player.health > 0:
    print("Player 1 WINS")
elif player2.health > 0:
    print("Player 2 Wins")
