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

obstacle = Obstacle(screen, (150,100), (31, 137), (193, 198, 36))
obstacle2 = Obstacle(screen, (700, 370), (140, 145), (127, 27, 163))
obstacle3 = Obstacle(screen, (284, 528), (12, 94), (138, 49, 27))
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)
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
screen.fill((0,0,0))
player.update()
player_group.draw(screen)
player2.update()
player2_group.draw(screen)
obstacle.update()
obstacle_group.draw(screen)
pygame.display.update()
clock.tick(60)
    

obstacle_collison = pygame.sprite.spritecollide(player, obstacle, False)
if obstacle_collison:
    if player.rect.right >= obstacle.rect.left:
        player.rect.right = obstacle.rect.left
    if player.rect.left <= obstacle.rect.right:
        player.rect.left = obstacle.rect.right
    if player.rect.top >= obstacle.rect.bottom:
        player.rect.top = obstacle.rect.bottom
    if player.rect.bottom <= obstacle.rect.top:
        player.rect.bottom = obstacle.rect.top
    if player1.rect.right >= player2.rect.left:
        player1.rect.right = player2.rect.left
    if player1.rect.left <= player2.rect.right:
        player1.rect.left = player2.rect.right
    if player1.rect.top >= player2.rect.bottom:
        player1.rect.top = player2.rect.bottom
    if player1.rect.bottom <= player2.rect.top:
        player1.rect.bottom = player2.rect.top
#Make an obstacle as a sprite



