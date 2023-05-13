import pygame
from pygame.locals import *
import sys

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Grama')
FPSCLOCK = pygame.time.Clock()

#player_x = SCREEN.get_width() / 2
#player_y = SCREEN.get_height() / 2

map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

wall = pygame.image.load('./assets/wall.png').convert_alpha()
grass = pygame.image.load('./assets/grass.png').convert_alpha()
#player_image = pygame.image.load('./assets/player.png').convert_alpha()

TILEWIDTH = 64
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

for row_nb, row in enumerate(map_data):
    for col_nb, tile in enumerate(row):
        if tile == 1:
            tileImage = wall
        else:
            tileImage = grass
        cart_x = row_nb * TILEWIDTH_HALF
        cart_y = col_nb * TILEHEIGHT_HALF
        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y) / 2
        centered_x = SCREEN.get_rect().centerx + iso_x
        centered_y = SCREEN.get_rect().centery / 2 + iso_y
        SCREEN.blit(tileImage, (centered_x, centered_y))

#iso_x = player_x - player_y
#iso_y = (player_x + player_y) / 2

#centered_x = SCREEN.get_rect().centerx + iso_x
#centered_y = SCREEN.get_rect().centery / 2 + iso_y

#SCREEN.blit(player_image, (centered_x, centered_y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    FPSCLOCK.tick(30)