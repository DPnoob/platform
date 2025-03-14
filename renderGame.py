import pygame
from setup import config

tiles = [pygame.image.load("tile.png")]
screen = pygame.display.set_mode((config['native sirina'] * config['scale'], config['native visina'] * config['scale']))

for tileID in range(len(tiles)):
    tiles[tileID] = pygame.transform.scale(tiles[tileID], (32 * config['scale'], 32 * config['scale']))


def backround():
    screen.fill((255, 255, 255))


def tile(x, y, tileID: int):
    screen.blit(tiles[tileID], (x * config['scale'], y * config['scale']))
