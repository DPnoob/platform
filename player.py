#not final

from setup import config
import renderGame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitrostX = 0
        self.hitrostY = 5

    def gravity(self, timeDelay):
        self.hitrostY -= config['gravity'] * timeDelay ** 2

    def move(self):
        self.y += self.hitrostY

    def render(self):
        renderGame.player(self.x, self.y)
