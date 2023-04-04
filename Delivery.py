"""
This program is for the unloading mechanism of the system
Author: Antoine Phan
"""

#!/usr/bin/env python3
from Unloading import swingLever, rollTray
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
ZONE_COLORS_STR = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
ZONE_COLORS = [Color(color_i) for color_i in ZONE_COLORS_STR]

"""
Idea: the lever will be used to push the cubes to the correct location.
It starts at position 0, which is the red cube.
The lever position will be updated after each delivery.
To deliver other cubes, the lever will get to the relative position of the cube.
"""
LEVER_POSITION = 0

"""
This function rolls the tray to the cube color.
@param:
- color: the color of the cube (use getSideColor())
- trayDPS: the speed of the tray
- trayAngle: the angle the tray will roll. Default: 120 degrees clockwise
"""   
def rollTrayToCube(color:str, trayDPS: int, trayAngle:int=120) -> bool:
    DONE = False
    global LEVER_POSITION # int, [0 - 5]
    
    # Get the relative position of the cube
    
    if(color in ZONE_COLORS_STR):
        relativePosition = ZONE_COLORS_STR.index(color) - LEVER_POSITION
        trayDelay = abs(relativePosition)/2
        rollTray(trayDPS, trayDelay, trayAngle*relativePosition)
        LEVER_POSITION = ZONE_COLORS_STR.index(color)
    else:
        print(f'ERROR: {color} is not a valid color. Recalibrating...')
        return DONE

    print(f'Rolled tray to {color} cube.')
    DONE = True
    return DONE

"""
This function unloads the cube by swinging the lever.
@param: 
- leverDPS: the speed of the lever
- leverDelay: the time the lever will swing each way
- leverAngle: the angle the lever will swing. By default it's 90
"""
def unloadCube(leverDPS:int, leverDelay:float, leverAngle:int=90) -> bool:
    DONE = False
    swingLever(leverDPS, leverDelay, leverAngle)
    swingLever(leverDPS, leverDelay, -leverAngle)
    DONE = True
    return DONE

"""
Reset the rack to the initial position (red cube)
"""
def resetRack(dps=400, angle=120) -> bool:
    DONE = False
    rollTrayToCube('red',dps,angle)
    DONE = True
    return DONE

def getSideColor() -> str:
    """
    Get color from the side sensor, using debouncing technique to avoid false detection.
    """
    sideColor = None
    while sideColor == None:
        sideColor = detects_RGB(SIDE_SENSOR.get_rgb(), ZONE_COLORS)
        
    # print(f'Delivering {sideColor.capitalize()} cube...')
    return str(sideColor)

def deliverCube(color:str) -> bool:
    """
    deliverCube: Deliver the cube based on the color detected from the side sensor
    
    IDEA: The sensor will detect a color based on the RGB value from the sensor.
    The detects_RGB() will take in 2 arguments: the rgb value as list [R, G, B],
    and ZONE which is a list of Color object defined aboved (only the Zone's colors)
    """
    
    # Settings parameters
    leverDPS = 500
    leverDelay = 1
    leverAngle = 90
    
    trayDPS = 400
    trayAngle = 120
    
    Delivered = False
    if rollTrayToCube(color=color, trayDPS=trayDPS, trayAngle=trayAngle):
        if unloadCube(leverDPS, leverDelay, leverAngle):
            print(f'Delivered!')
            sleep(1)
            Delivered = True
            
    else:
        print(f'ERROR: Could not deliver cube.')
        
    return Delivered
