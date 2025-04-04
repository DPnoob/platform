# normal imports

# variables used in other files

# imports from other files
import vector
from setup import config
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
        self.speed = vector.Vector()
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

    def move(self, timeDelay):
        self.x += self.speed.getX() * timeDelay
        self.y += self.speed.getY() * timeDelay

    def render(self):
        renderGame.player(self.x, self.y)
