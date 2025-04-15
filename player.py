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
        self.speedX = 0
        self.speedY = 0
        self.acceleration.addY('gravity', -config['gravity'])

    def move(self, timeDelay):
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
        try:
            self.speedX += self.acceleration.getX() * timeDelay * 0.5
            self.speedY += self.acceleration.getY() * timeDelay * 0.5
        except: pass

        #moving
        try:
            self.x += self.speedX * timeDelay
            self.y += self.speedY * timeDelay
        except: pass

        # adding the rest of speed
        try:
            self.speedX += self.acceleration.getX() * timeDelay * 0.5
            self.speedY += self.acceleration.getY() * timeDelay * 0.5
        except: pass

    def action(self, key_positions, timeDelay):
        if self.florBelow() and (key_positions.get('w') or key_positions.get('space')):
            self.speedY += 36
        try:
            self.force.sizeX('premikanje', (key_positions.get('d') - key_positions.get('a')) * 10)
        except: pass

    def collision(self, timeDelay):
        for i in level:
            if (i['x1'] * config['tile size'] < self.x + config['player size'] and
                (i['x2'] + 1) * config['tile size'] > self.x):

                if ((i['y2'] + 1) * config['tile size'] > self.y and
                    (i['y2'] + 1) * config['tile size'] + self.speedY * timeDelay < self.y):
                    self.speedY = 0
                    self.y = (i['y2'] + 1) * config['tile size']

                elif (i['y1'] * config['tile size'] < self.y + config['player size'] and
                    i['y1'] * config['tile size'] + self.speedY * timeDelay > self.y + config['player size']):
                    self.speedY = 0
                    self.y = i['y1'] * config['tile size'] - config['player size']

            if (i['y1'] * config['tile size'] < self.y + config['player size'] and
                (i['y2'] + 1) * config['tile size'] > self.y):

                if ((i['x2'] + 1) * config['tile size'] > self.x and
                    (i['x2'] + 1) * config['tile size'] + self.speedX * timeDelay < self.x):
                    self.speedX = 0
                    self.x = (i['x2'] + 1) * config['tile size']

                elif (i['x1'] * config['tile size'] < self.x + config['player size'] and
                    i['x1'] * config['tile size'] + self.speedX * timeDelay > self.x + config['player size']):
                    self.speedX = 0
                    self.x = i['x1'] * config['tile size'] - config['player size']

    def florBelow(self):
        for i in level:
            if (i['x1'] * config['tile size'] < self.x + config['player size'] and
                (i['x2'] + 1) * config['tile size'] > self.x and
                (i['y2'] + 1) * config['tile size'] > self.y - 1 and
                i['y1'] * config['tile size'] < self.y):
                return True
        return False

    def render(self):
        renderGame.player(self.x, self.y)
