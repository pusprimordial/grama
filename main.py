import pygame
from pygame.locals import *
import sys
from map import map_data
from config import *
from texture import *


pygame.init()
pygame.display.set_caption('Grama')


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
