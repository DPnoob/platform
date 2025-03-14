import json

# lode configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# adding new parameter scale
config['scale'] = (config['resolutin to scaling'][config['resolucija']])
