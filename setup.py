import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
config['scale'] = (config['resolutin to scaling'][config['resolucija']])


def setup():
    import main
    main.startGame()
