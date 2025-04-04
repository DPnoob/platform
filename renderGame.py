# normal imports
import pygame

# variables used in other files

# imports from other files
from setup import config

# variables used in this file
tiles = [pygame.image.load("tile0.png"),
         pygame.image.load("tile11.png")]
playerSprite = pygame.image.load("player.png")
screen = pygame.display.set_mode((config['native width'] * config['scale'], config['native hight'] * config['scale']))

for tileID in range(len(tiles)): # sceling tiles
    tiles[tileID] = pygame.transform.scale(tiles[tileID], (20 * config['scale'], 20 * config['scale']))
playerSprite = pygame.transform.scale(playerSprite, (config['player size'] * config['scale'], (config['player size'] * config['scale'])))

def realY(y):
    return config['native hight'] - y

def backround():
    screen.fill((84, 219, 239))

def tile(x, y, tileID: int):
    screen.blit(tiles[tileID], (x * config['scale'], (realY(y) - config['tile size']) * config['scale'] ))

def player(x, y):
    screen.blit(playerSprite, (x  * config['scale'], (realY(y) - config['player size']) * config['scale']))