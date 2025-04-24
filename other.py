# normal imports

# variables used in other files

# imports from other files
from setup import config

# variables used in this file
def getRealMouse(mousePosition):
    return mousePosition[0] / config['scale'], realY(mousePosition[1] / config['scale'])

def realY(y):
    return config['native hight'] - y

def blockPosition(x,y):
    return int(x // config['tile size']), int(y // config['tile size'])