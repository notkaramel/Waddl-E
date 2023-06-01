#!/usr/bin/env python3
"""
This program is for the unloading mechanism of the system
Author: Antoine Phan
"""

from components.Unloading import swingLever, rollTray
from components.ColorDetection import Color, SIDE_SENSOR, detects_RGB

"""
Idea: create a test function that only acts on the color of map
This file will be used for delivering the cubes to the correct location zone.
"""

"""
There are 6 colors for the delivery zones,
each zone corresponds to a color cube.
[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
"""
ZONE_COLORS_STR = ['red', 'orange', 'yellow',
                   'green', 'blue', 'purple', 'white']
ZONE_COLORS = [Color(color_i) for color_i in ZONE_COLORS_STR]

"""
Idea: the lever will be used to push the cubes to the correct location.
It starts at position 0, which is the red cube.
The lever position will be updated after each delivery.
"""
LEVER_POSITION = 0  # int, [0 - 5]

"""
This function rolls the tray to the cube color.
@param:
- color: the color of the cube (use getSideColor())
- trayDPS: the speed of the tray
- trayAngle: the angle the tray will roll. Default: 120 degrees clockwise

Default values are from tests.
- DPS: 600
- Tray Angle: 120
- Time delay of rollTray: relativePosition//2
"""


def rollTrayToCube(color: str, trayDPS: int = 600, trayAngle: int = 120):
    DONE = False
    global LEVER_POSITION  # int, [0 -> 5]

    # Get the relative position of the cube

    if (color in ZONE_COLORS_STR):
        relativePosition = ZONE_COLORS_STR.index(color) - LEVER_POSITION
        trayDelay = abs(relativePosition/2)
        rollTray(trayDPS, trayDelay, trayAngle*relativePosition)
        LEVER_POSITION = ZONE_COLORS_STR.index(color)
        DONE = True
    else:
        print(f'ERROR: {color} is not a valid color. Recalibrating...')
        return DONE

    print(f'Rolled tray to {color} cube.')
    return DONE


"""
This function unloads the cube by swinging the lever.
@param:
- leverDPS: the speed of the lever
- leverDelay: the time the lever will swing each way
- leverAngle: the angle the lever will swing. By default it's 90
"""


def unloadCube(leverDPS: int, leverDelay: float, leverAngle: int = 90) -> bool:
    DONE = False
    swingLever(leverDPS, leverDelay, leverAngle)
    swingLever(leverDPS, leverDelay, -leverAngle)
    DONE = True
    return DONE


def resetRack(dps=400, angle=120) -> bool:
    """
    Reset the rack to the initial position (red cube)
    Default value taken from the tests
    - DPS: xxx
    - Angle: 120deg
    """
    DONE = False
    rollTrayToCube('red', dps, angle)
    DONE = True
    return DONE


def getSideColor() -> str:
    """
    Get color from the side sensor,
    using debouncing technique to avoid false detection.
    """
    sideColor = None
    while sideColor is None:
        # sleep(0.1)
        sideColor = detects_RGB(SIDE_SENSOR.get_rgb(), ZONE_COLORS)

    # print(f'Delivering {sideColor.capitalize()} cube...')
    return str(sideColor)


def deliverCube(color: str) -> bool:
    """
    deliverCube: Deliver the cube based on the color detected from the side sensor

    IDEA: The sensor will detect a color based on the RGB value from the sensor.
    The detects_RGB() will take in 2 arguments: the rgb value as list [R, G, B],
    and ZONE which is a list of Color object defined aboved (only the Zone's colors)
    """

    # Settings parameters
    leverDPS = 250
    leverDelay = 1
    leverAngle = 80

    trayDPS = 500
    trayAngle = 120

    Delivered = False
    if rollTrayToCube(color=color, trayDPS=trayDPS, trayAngle=trayAngle):
        if unloadCube(leverDPS, leverDelay, leverAngle):
            print('Delivered!')
            Delivered = True

    else:
        print('ERROR: Could not deliver cube.')

    if LEVER_POSITION in [4, 5]:
        # This is to make sure the system is balanced
        resetRack()

    return Delivered
