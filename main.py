# normal imports
import pygame

# variables used in other files

# imports from other files

# variables used in this file

# main game loop
def startGame():
    from setup import config, level
    import renderGame
    import player

    running = True
    timeDelay = 0
    pygame.init()
    clock = pygame.time.Clock()
    player = player.Player(config['tile size'], config['tile size'])

    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #moving
        player.update(timeDelay)
        player.move(timeDelay)
        player.collision()

        # rendering
        renderGame.backround()
        """
        for s in range(16):
            for v in range(9):
                renderGame.tile(config['tile size'] * s, config['tile size'] * v, 0)
        """
        for block in level:
            for x in range(block['x1'], block['x2'] + 1):
                for y in range(block['y1'], block['y2'] + 1):
                    renderGame.tile(config['tile size'] * x, config['tile size'] * y, block['tileID'])
        player.render()

        # other
        pygame.display.flip()

        clock.tick(config['maxFPS'])
        print(player.x, player.y)
        timeDelay = clock.get_time() / 50 # multiply to get ecurate timing (my_time * timeDelay)

    pygame.quit()
