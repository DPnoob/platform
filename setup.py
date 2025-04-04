import json

# lode configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# lode level from level.txt
with open('level.txt', 'r') as level_file:
    level = level_file.read().split('\n')

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

# adding new parameter scale
config['scale'] = (config['resolution to scaling'][config['resolution']])
