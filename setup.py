import json

# lode configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# lode level from level.txt
with open('level.txt', 'r') as level_file:
    level = level_file.read().split('\n')

# unpacking level
for line, tiles in enumerate(level):
    level[line] = {'tileID': int(tiles.split(' ')[0]),
                   'x1': int(tiles.split(' ')[1]),
                   'y1': int(tiles.split(' ')[2]),
                   'x2': int(tiles.split(' ')[3]),
                   'y2': int(tiles.split(' ')[4])}

# adding new parameter scale
config['scale'] = (config['resolution to scaling'][config['resolution']])
