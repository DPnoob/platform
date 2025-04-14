# normal imports

# variables used in other files

# imports from other files
import vector
from setup import config, level
import renderGame

# variables used in this file

#main class that defines the pleyer
class Player:
    def __init__(self, x, y, mass = 1):
        self.x = x
        self.y = y
        self.mass = mass
        self.force = vector.Vector()
        self.acceleration = vector.Vector()
        #self.speed = vector.Vector()
        self.speedX = 0
        self.speedY = 0
        self.acceleration.addY('gravity', -config['gravity'])

    def update(self, timeDelay):
        #calculating acceleratin
        for i in self.force.vektor:
            if self.acceleration.getSpecific(i) is None:
                self.acceleration.add(i, self.force.getSpecific(i)[0] / self.mass, self.force.getSpecific(i)[1])
            else:
                self.acceleration.change(i, self.force.getSpecific(i)[0] / self.mass, self.force.getSpecific(i)[1])

        for i in self.force.vektorX:
            if self.acceleration.getSpecificX(i) is None:
                self.acceleration.addX(i, self.force.getSpecificX(i) / self.mass)
            else:
                self.acceleration.sizeX(i, self.force.getSpecificX(i) / self.mass)

        for i in self.force.vektorY:
            if self.acceleration.getSpecificY(i) is None:
                self.acceleration.addY(i, self.force.getSpecificY(i) / self.mass)
            else:
                self.acceleration.sizeY(i, self.force.getSpecificY(i) / self.mass)

        #calculating speed

        """
        for i in self.acceleration.vektor:
            if self.speed.getSpecific(i) is None:
                self.speed.add(i, self.acceleration.getSpecific(i)[0] * timeDelay ** 2, self.acceleration.getSpecific(i)[1])
            else:
                self.speed.change(i, self.speed.getSpecific(i)[0] + self.acceleration.getSpecific(i)[0] * timeDelay ** 2, self.acceleration.getSpecific(i)[1])

        for i in self.acceleration.vektorX:
            if self.speed.getSpecificX(i) is None:
                self.speed.addX(i, self.acceleration.getSpecificX(i) * timeDelay ** 2)
            else:
                self.speed.sizeX(i, self.speed.getSpecificX(i) + self.acceleration.getSpecificX(i) * timeDelay ** 2)

        for i in self.acceleration.vektorY:
            if self.speed.getSpecificY(i) is None:
                self.speed.addY(i, self.acceleration.getSpecificY(i) * timeDelay ** 2)
            else:
                self.speed.sizeY(i, self.speed.getSpecificY(i) + self.acceleration.getSpecificY(i) * timeDelay ** 2)
        """
        self.speedX += self.acceleration.getX() * timeDelay ** 2
        self.speedY += self.acceleration.getY() * timeDelay ** 2

    def move(self, timeDelay):
        #self.x += self.speed.getX() * timeDelay
        #self.y += self.speed.getY() * timeDelay
        self.x += self.speedX * timeDelay
        self.y += self.speedY * timeDelay

    def collision(self):
        for i in level:
            if (i['x1'] * config['tile size'] < self.x + config['player size'] and
                (i['x2'] + 1) * config['tile size'] > self.x):

                if ((i['y2'] + 1) * config['tile size'] > self.y and
                    (i['y2'] + 1) * config['tile size'] + self.speedY < self.y):
                    self.speedY = 0
                    self.y = (i['y2'] + 1) * config['tile size']

                elif (i['y1'] * config['tile size'] < self.y + config['player size'] and
                    i['y1'] * config['tile size'] + self.speedY > self.y + config['player size']):
                    self.speedY = 0
                    self.y = i['y1'] * config['tile size'] - config['player size']

            if (i['y1'] * config['tile size'] < self.y + config['player size'] and
                (i['y2'] + 1) * config['tile size'] > self.y):

                if ((i['x2'] + 1) * config['tile size'] > self.x and
                    (i['x2'] + 1) * config['tile size'] + self.speedX < self.x):
                    self.speedX = 0
                    self.x = (i['x2'] + 1) * config['tile size']

                elif (i['x1'] * config['tile size'] < self.x + config['player size'] and
                    i['x1'] * config['tile size'] + self.speedX > self.x + config['player size']):
                    self.speedX = 0
                    self.x = i['x1'] * config['tile size'] - config['player size']

    def render(self):
        renderGame.player(self.x, self.y)
