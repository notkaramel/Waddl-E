"""
This programe is for the unloading mechanism of the system
Author: Antoine Phan
"""

#!/usr/bin/env python3
from Unloading import LEVER, TRAY_ROLLER, swingLever, rollTray
from ColorDetection import Color, SIDE_SENSOR, detects_RGB
from time import sleep

"""
Idea: create a test function that only acts on the color of map
This file will be used for delivering the cubes to the correct location zone.
"""

"""
There are 6 colors for the delivery zones,
each zone corresponds to a color cube.
[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
"""
ZONE_COLORS = ['red_map', 'orange_map', 'yellow_map', 'green_map', 'blue_map', 'purple_map']
ZONE = [Color(color_i) for color_i in ZONE_COLORS]

if color == ZONE[0]: # red_map
            pass
        elif color == ZONE[1]: # orange_map
            pass
        elif color == ZONE[2]: # yellow_map
            pass
        elif color == ZONE[3]: # green_map
            pass
        elif color == ZONE[4]: # blue_map
            pass
        elif color == ZONE[5]: # purple_map
            pass
        else: # None
            print(f'Invalid color.')

def f():
    print(f'Delivering...')
    sideColor = detects_RGB(SIDE_SENSOR.get_rgb())  

    if sideColor == 'red_map':
        print(f'\tDelivering RED cube...')
        
    elif sideColor == 'orange_map':
        print(f'\tDelivering ORANGE cube...')
    elif sideColor == 'yellow_map':
        print(f'\tDelivering YELLOW cube...')
    elif sideColor == 'green_map':
        print(f'\tDelivering GREEN cube...')
    elif sideColor == 'blue_map':
        print(f'\tDelivering BLUE cube...')
    elif sideColor == 'purple_map':
        print(f'\tDelivering PURPLE cube...')
    else:
        print(f'\tInvalid color.')
        return

    print(f'\tDone delivering.')