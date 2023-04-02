"""
This program is for the unloading mechanism of the system
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
def resetRack():
    pass

ZONE_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
ZONE = [Color(color_i) for color_i in ZONE_COLORS]

def getSideColor():
    sideColor = None
    while sideColor == None:
        sideColor = detects_RGB(SIDE_SENSOR.get_rgb(), ZONE)
        sleep(0.1)
        
    print(f'Delivering {sideColor.capitalize()} cube...')


def deliverCube(color:str):
    """
    deliverCube: Deliver the cube based on the color detected from the side sensor
    
    IDEA: The sensor will detect a color based on the RGB value from the sensor.
    The detects_RGB() will take in 2 arguments: the rgb value as list [R, G, B],
    and ZONE which is a list of Color object defined aboved (only the Zone's colors)
    """
    getCube = lambda slot: rollTray(delay=slot*1, angle=slot*90)
    pushCube = lambda: swingLever(angle=90)
    
    
    if color == 'red':      # position 0
        getCube(slot=0)
        pushCube()
        pushCube()
    elif color == 'orange': # position 1
        getCube(slot=1)
    elif color == 'yellow': # position 2
        getCube(slot=2)
    elif color == 'green':  # position 3
        getCube(slot=3)
    elif color == 'blue':   # position 4
        getCube(slot=4)
    elif color == 'purple': # position 5
        getCube(slot=5)
        
    else:
        
        return

    print(f'\tDone delivering.')