import pygame
from player import Player
from obstacle import Obstacle

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(screen)
player_group = pygame.sprite.Group()
player_group.add(player)
obstacle = Obstacle(screen)
obstacle_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,0,0))
    player.update()
    player_group.draw(screen)
    obstacle.update()
    obstacle_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
    

#Make an obstacle as a sprite



