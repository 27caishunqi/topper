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
        

    obstacle_collison = pygame.sprite.spritecollide(player, obstacle_group, False)
    
    for obstacle in obstacle_collison:
        dx = player.rect.centerx - obstacle.rect.centerx
        dy = player.rect.centery - obstacle.rect.centery
        if abs(dx) > abs(dy):
            if dx > 0:
                player.rect.left = obstacle.rect.right
            else:
                player.rect.right = obstacle.rect.left
        else:    
            if dy > 0:
                player.rect.top = obstacle.rect.bottom
            else:
                player.rect.bottom = obstacle.rect.top
    player_collision = pygame.sprite.spritecollide(player, player2_group, False)
    for playerCol in player_collision:
        dx = player.rect.centerx - playerCol.rect.centerx
        dy = player.rect.centery - playerCol.rect.centery
        if abs(dx) > abs(dy):
            if dx > 0:
                player.rect.left = playerCol.rect.right
            else:
                player.rect.right = playerCol.rect.left
        else:    
            if dy > 0:
                player.rect.top = playerCol.rect.bottom
            else:
                player.rect.bottom = playerCol.rect.top



