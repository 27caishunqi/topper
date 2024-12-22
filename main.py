import pygame
from player import Player
from obstacle import Obstacle
import time

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(player)

player2 = Player(screen, True)
player2_group = pygame.sprite.Group()
player2_group.add(player2)

obstacle1 = Obstacle(screen, (150,100), (31, 137), (193, 198, 36))
obstacle2 = Obstacle(screen, (700, 370), (140, 145), (127, 27, 163))
obstacle3 = Obstacle(screen, (284, 528), (12, 94), (138, 49, 27))
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle1)
obstacle_group.add(obstacle2)
obstacle_group.add(obstacle3)
def collision(sprite, sprite_group):
    collided = pygame.sprite.spritecollide(sprite, sprite_group, False)
    
    for object in collided:
        dx = sprite.rect.centerx - object.rect.centerx
        dy = sprite.rect.centery - object.rect.centery
        if abs(dx) > abs(dy):
            if dx > 0:
                sprite.rect.left = object.rect.right
            else:
                sprite.rect.right = object.rect.left
        else:    
            if dy > 0:
                sprite.rect.top = object.rect.bottom
            else:
                sprite.rect.bottom = object.rect.top



'''
timer = time.time() + 5
while time.time() < timer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
'''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((0,0,0))
    player.update()
    player_group.draw(screen)
    player2.update()
    player2_group.draw(screen)
    obstacle1.update()
    obstacle_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
        
    collision(player, obstacle_group)
    collision(player2, obstacle_group)
    collision(player, player2_group)
    collision(player2, player_group)
