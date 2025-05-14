# normal imports
import pygame

# variables used in other files

# imports from other files
from setup import config

# variables used in this file
tiles = [pygame.image.load("sprites/misingTexture.png"),
         pygame.image.load("sprites/tile11.png"),
         pygame.image.load("sprites/tile12.png"),
         pygame.image.load("sprites/tile13.png"),
         pygame.image.load("sprites/tile14.png"),
         pygame.image.load("sprites/tile15.png"),
         pygame.image.load("sprites/tile16.png"),
         pygame.image.load("sprites/tile17.png"),
         pygame.image.load("sprites/tile18.png"),
         pygame.image.load("sprites/tile19.png"),
         pygame.image.load("sprites/tile20.png"),
         pygame.image.load("sprites/tile21.png"),
         pygame.image.load("sprites/tile22.png"),
         pygame.image.load("sprites/tile23.png"),
         pygame.image.load("sprites/tile24.png"),
         pygame.image.load("sprites/selected.png"),]
playerSprite = pygame.image.load("sprites/player.png")
screen = pygame.display.set_mode((config['native width'] * config['scale'], config['native hight'] * config['scale']))

for tileID in range(len(tiles)): # sceling tiles
    tiles[tileID] = pygame.transform.scale(tiles[tileID], (20 * config['scale'], 20 * config['scale']))
playerSprite = pygame.transform.scale(playerSprite, (config['player size'] * config['scale'], (config['player size'] * config['scale'])))

def realY(y):
    return config['native hight'] - y

def backround():
    screen.fill((84, 219, 239))

def tile(x, y, tileID: int):
    try:
        screen.blit(tiles[tileID], (x * config['scale'], (realY(y) - config['tile size']) * config['scale'] ))
    except:
        screen.blit(tiles[0], (x * config['scale'], (realY(y) - config['tile size']) * config['scale']))

def player(x, y):
    screen.blit(playerSprite, (x  * config['scale'], (realY(y) - config['player size']) * config['scale']))