# normal imports
import pygame

import other


# variables used in other files

# imports from other files

# variables used in this file

# main game loop
def startGame():
    from setup import config, level
    import renderGame
    import player
    import inputs

    running = True
    timeDelay = 0
    pygame.init()
    clock = pygame.time.Clock()
    player = player.Player(config['tile size'], config['tile size'])
    key_positions = {}

    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key_positions = inputs.keys()

        #moving
        player.action(key_positions, timeDelay)
        player.move(timeDelay)
        player.collision(timeDelay)

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
        timeDelay = clock.get_time() / 150 # multiply to get ecurate timing (my_time * timeDelay)

    pygame.quit()

def levelEditor():
    from setup import config, level
    import renderGame
    from other import getRealMouse, blockPosition

    new_level = []
    for block in level:
        for x in range(block['x1'], block['x2'] + 1):
            for y in range(block['y1'], block['y2'] + 1):
                new_level.append({'x': x, 'y': y, 'tileID': block['tileID']})

    running = True
    pygame.init()
    clock = pygame.time.Clock()
    key_positions = {}
    desni_klik = False
    desni_klik_prej = True
    tileW = 1

    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                desni_klik = pygame.mouse.get_pressed()[0]
            if event.type == pygame.MOUSEWHEEL:
                tileW = (tileW + event.y - 1 ) % 14 + 1

        x, y = getRealMouse(pygame.mouse.get_pos())
        bX, bY= other.blockPosition(x, y)

        if desni_klik_prej and desni_klik:
            desni_klik_prej = False

            ni_tile = True
            for tile in new_level:
                if tile['x'] == bX and tile['y'] == bY:
                    new_level.remove(tile)
                    ni_tile = False
                    break

            if ni_tile:
                new_level.append({'x': bX, 'y': bY, 'tileID': tileW})


        elif not desni_klik:
            desni_klik_prej = True

        # rendering
        renderGame.backround()
        for block in new_level:
            renderGame.tile(config['tile size'] * block['x'], config['tile size'] * block['y'], block['tileID'])
        renderGame.tile(bX * config['tile size'], bY * config['tile size'],tileW)
        renderGame.tile(bX * config['tile size'], bY * config['tile size'], -1)


        # other
        pygame.display.flip()

        clock.tick(config['maxFPS'])

    pygame.quit()

    new_level.sort(key=lambda tile: tile['y'] * 1000 + tile['x'])

    new_level_united = [{'x1' : new_level[0]['x'], 'x2' : new_level[0]['x'], 'y1' : new_level[0]['y'], 'y2' : new_level[0]['y'], 'tileID' : new_level[0]['tileID']}]


    for i in range(1, len(new_level)):
        if new_level[i]['y'] == new_level_united[-1]['y1'] and new_level[i]['tileID'] == new_level_united[-1]['tileID'] and new_level[i]['x'] - 1 == new_level_united[-1]['x2']:
            new_level_united[-1]['x2'] = new_level[i]['x']
        else:
            new_level_united.append({'x1' : new_level[i]['x'], 'x2' : new_level[i]['x'], 'y1' : new_level[i]['y'], 'y2' : new_level[i]['y'], 'tileID' : new_level[i]['tileID']})

    new_level_united.sort(key=lambda block: block['x1'] * 1000 + block['y1'])

    new_level_hole = [{'x1' : new_level_united[0]['x1'], 'x2' : new_level_united[0]['x2'], 'y1' : new_level_united[0]['y1'], 'y2' : new_level_united[0]['y2'], 'tileID' : new_level_united[0]['tileID']}]

    for i in range(1, len(new_level_united)):
        if new_level_united[i]['x1'] == new_level_hole[-1]['x1'] and new_level_united[i]['x2'] == new_level_hole[-1]['x2'] and new_level_united[i]['y1'] - 1 == new_level_hole[-1]['y2'] and new_level_united[i]['tileID'] == new_level_hole[-1]['tileID']:
            new_level_hole[-1]['y2'] = new_level_united[i]['y1']
        else:
            new_level_hole.append({'x1': new_level_united[i]['x1'], 'x2': new_level_united[i]['x2'], 'y1': new_level_united[i]['y1'], 'y2': new_level_united[i]['y2'], 'tileID': new_level_united[i]['tileID']})

# -------------------------------------

    new_level_united_collision = [
        {'x1': new_level[0]['x'], 'x2': new_level[0]['x'], 'y1': new_level[0]['y'], 'y2': new_level[0]['y']}]

    for i in range(1, len(new_level)):
        if new_level[i]['y'] == new_level_united_collision[-1]['y1'] and new_level[i]['x'] - 1 == new_level_united_collision[-1]['x2']:
            new_level_united_collision[-1]['x2'] = new_level[i]['x']
        else:
            new_level_united_collision.append(
                {'x1': new_level[i]['x'], 'x2': new_level[i]['x'], 'y1': new_level[i]['y'], 'y2': new_level[i]['y']})

    new_level_united_collision.sort(key=lambda block: block['x1'] * 1000 + block['y1'])

    new_level_hole_collision = [
        {'x1': new_level_united_collision[0]['x1'], 'x2': new_level_united_collision[0]['x2'], 'y1': new_level_united_collision[0]['y1'],
         'y2': new_level_united_collision[0]['y2']}]

    for i in range(1, len(new_level_united_collision)):
        if new_level_united_collision[i]['x1'] == new_level_hole_collision[-1]['x1'] and new_level_united_collision[i]['x2'] == new_level_hole_collision[-1][
            'x2'] and new_level_united_collision[i]['y1'] - 1 == new_level_hole_collision[-1]['y2']:
            new_level_hole_collision[-1]['y2'] = new_level_united_collision[i]['y1']
        else:
            new_level_hole_collision.append(
                {'x1': new_level_united_collision[i]['x1'], 'x2': new_level_united_collision[i]['x2'], 'y1': new_level_united_collision[i]['y1'],
                 'y2': new_level_united_collision[i]['y2']})

    # -----------------------
    new_level_name = input('ime nove mape:\n')
    with open(new_level_name + '.level', 'w') as new_level_file:
        for block in new_level_hole:
            print(block['x1'], block['y1'], block['x2'], block['y2'], block['tileID'], file=new_level_file)
    # ------------------------
    with open(new_level_name + '_collision.level', 'w') as new_level_file_collision:
        for block in new_level_hole_collision:
            print(block['x1'], block['y1'], block['x2'], block['y2'], file=new_level_file_collision)