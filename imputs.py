# normal imports
import pygame

# variables used in other files

# imports from other files

# variables used in this file

def keys():
    # Get all key states
    pressed_keys = pygame.key.get_pressed()
    key_positions = {}

    # Assining keys to bools
    for key_code in range(len(pressed_keys)):
        key_positions[pygame.key.name(key_code)] = pressed_keys[key_code]

    return key_positions