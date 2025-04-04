# normal imports
from math import cos, sin, radians

# variables used in other files

# imports from other files

# variables used in this file

# class BeterMath used for easier calculations
class BeterMath:
    @staticmethod
    def cos(deg): # returns cosinus of an angle given in degrees
        return cos(radians(deg))

    @staticmethod
    def sin(deg): # returns sinus of an angle given in degrees
        return sin(radians(deg))

# Vector class that suports 2D vectors (all directions, horizontal, vertikal)
class Vector:
    def __init__(self):
        self.vektor = {}
        self.vektorX = {}
        self.vektorY = {}

    def add(self, name, size, direction):
        self.vektor[name] = [size, direction]

    def addX(self, name, size):
        self.vektorX[name] = size

    def addY(self, name, size):
        self.vektorY[name] = size

    def change(self, name, size, direction):
        self.vektor[name] = [size, direction]

    def rotate(self, name, direction):
        self.vektor[name][1] = direction

    def size(self, name, size):
        self.vektor[name][0] = size

    def sizeX(self, name, size):
        self.vektorX[name] = size

    def sizeY(self, name, size):
        self.vektorY[name] = size

    def getSpecific(self, name):
        return self.vektor.get(name)

    def getSpecificSize(self, name):
        return self.vektor.get(name)[0]

    def getSpecificDir(self, name):
        return self.vektor.get(name)[1]

    def getSpecificX(self, name):
        return self.vektorX.get(name)

    def getSpecificY(self, name):
        return self.vektorY.get(name)

    def getX(self):
        return sum(self.vektorX.values()) + sum((BeterMath.cos(i[1]) * i[0] for i in self.vektor.values()))

    def getY(self):
        return sum(self.vektorY.values()) + sum((BeterMath.sin(i[1]) * i[0] for i in self.vektor.values()))