import pygame
import renderGame


#renderGame.setscale(config['scale'])
# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True

def startGame():
    global running, clock
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE
        renderGame.backround()
        for s in range(10):
            for v in range(6):
                renderGame.tile(32 * s, 32 * v, 0)


        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60
    pygame.quit()