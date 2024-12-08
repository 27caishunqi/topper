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

obstacle = Obstacle(screen)
obstacle_group = pygame.sprite.Group()
obstacle_group.add(obstacle)

timer = time.time() + 5
while time.time() < timer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0))
    player.update()
    player_group.draw(screen)
    player2.update()
    player2_group.draw(screen)
    obstacle.update()
    obstacle_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
    

#Make an obstacle as a sprite



