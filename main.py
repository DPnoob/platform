# normal imports
import pygame

# variables used in other files

# imports from other files
from setup import config
import renderGame

# variables used in this file
pygame.init()
clock = pygame.time.Clock()
running = True

# main game loop
def startGame():
    global running, clock
    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # rendering
        renderGame.backround()
        for s in range(10):
            for v in range(6):
                renderGame.tile(32 * s, 32 * v, 0)

        # other
        pygame.display.flip()

        clock.tick(config['maxFPS'])
        timeDelay = clock.get_time() / 1000 # multiply to get ecurate timing (my_time * timeDelay)

    pygame.quit()
