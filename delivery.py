"""
This programe is for the unloading mechanism of the system
Author: Antoine Phan
"""

#!/usr/bin/env python3
from utils.brick import Motor
from detect_color import Color
from time import sleep

"""
Idea: create a test function that only acts on the color of map
This file will be used for delivering the cubes to the correct location zone.
"""



    print(f'Delivering...')
    sideColor = detects_RGB(SideSensor.get_rgb())  

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

    pushCube()
    sleep(1)
    retract()
    sleep(1)

    print(f'\tDone delivering.')