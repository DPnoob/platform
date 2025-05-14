import json

# lode configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# lode level
with open(config['level'] + '.level', 'r') as level_file:
    level = level_file.read().split('\n')

# lode collision
with open(config['level'] + '_collision.level', 'r') as level_file:
    level_collision = level_file.read().split('\n')

# unpacking level
line = 0
while line < len(level):
    tiles = level[line]
    if tiles == '' or tiles[0] == '#':
        level.pop(line)
    else:
        level[line] = {
            'x1': int(tiles.split(' ')[0]),
            'y1': int(tiles.split(' ')[1]),
            'x2': int(tiles.split(' ')[2]),
            'y2': int(tiles.split(' ')[3]),
            'tileID': int(tiles.split(' ')[4])}
        line += 1

# unpacking collision
line = 0
while line < len(level_collision):
    tiles = level_collision[line]
    if tiles == '' or tiles[0] == '#':
        level_collision.pop(line)
    else:
        level_collision[line] = {
            'x1': int(tiles.split(' ')[0]),
            'y1': int(tiles.split(' ')[1]),
            'x2': int(tiles.split(' ')[2]),
            'y2': int(tiles.split(' ')[3])}
        line += 1

# adding new parameter scale
config['scale'] = (config['resolution to scaling'][config['resolution']])
