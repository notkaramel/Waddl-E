#!/usr/bin/env python3
"""
The final system design of Waddl-E:
the autonomous delivery robot that delivers color foam cubes
to their correspoding location on a map.

Also, I think I'm going to diary as I go on this file :))

Author: Antoine Phan @notkaramel

Naming Convention: CamelCase
System name: Waddl-E
"""

import wheels
# Import Color object and detects_RGB function
from detect_color import Color, detects_RGB
from utils.brick import Motor, EV3ColorSensor, TouchSensor, wait_ready_sensors
from time import sleep

DEBUG = True

"""
Initialize Motors and Sensors
"""

LeftWheel = Motor("A")
RightWheel = Motor("D")
CubeRack = Motor("B")
Lever = Motor("C")

FrontSensor = EV3ColorSensor(1)
SideSensor = EV3ColorSensor(4)

Button = TouchSensor(3)
wait_ready_sensors(DEBUG)

"""
Idea #1: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""
# <-- Program starts here --> #
"""
When Waddl-E sees WHITE, it goes.
"""
def goStraight(speed=30): # speed in %
    print(f'Going straight at {speed}% speed.')
    if DEBUG:
        print(f'\tLeftWheel: {LeftWheel.get_power()}')        
        print(f'\tRightWheel: {RightWheel.get_power()}')
    wheels.run(LeftWheel, power=speed)
    wheels.run(RightWheel, power=speed)

"""
When Waddl-E sees BLUE, it turns slightly to the right.
"""
def slightRight(delay:float):
    print(f'Turning slightly right (delay={delay}))')
    wheels.turn("right", delay)

"""
When Waddl-E sees RED, it turns slightly to the left.
"""
def slightLeft(delay):
    print(f'Turning slightly left (delay={delay}))')
    wheels.turn("left", delay)

"""
When Waddl-E sees GREEN, it stops and start delivering.
The color cubes are given in a fixed order from the beginning at the loading bay.
[purple, blue, green, yellow, orange, red]
"""
def deliver():
    pushCube = lambda: Lever.set_position_relative(90)
    retract = lambda: Lever.set_position_relative(-90)
    
    getCube = lambda color: CubeRack.set_position_relative(90)

    print(f'Delivering...')
    sideColor = detects_RGB(SideSensor.get_rgb())
    if DEBUG:
        print(f'\tSideSensor: {sideColor}')
    
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

"""
When Waddl-E sees YELLOW: it stops, turns around, maybe play a tune to tell that it's in loading mode.
"""
def loading():
    print(f'Entering loading mode...')
    sleep(3)
    pass


"""
List of action based on color for the FrontSensor.
The FrontSensor only detects 5 colors of the map.
Color order: Rainbow, then white
[RED, YELLOW, GREEN, BLUE, WHITE]
""" 
MAP_COLORS = ['red_map', 'yellow_map', 'green_map', 'blue_map', 'white_map']
MAP = [Color(color_i) for color_i in MAP_COLORS]

"""
There are 6 colors for the delivery zones,
each zone corresponds to a color cube.
[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
"""
ZONE_COLORS = ['red_map', 'orange_map', 'yellow_map', 'green_map', 'blue_map', 'purple_map']
ZONE = [Color(color_i) for color_i in ZONE_COLORS]

# Action based on color. 
def colorAction(Sensor: EV3ColorSensor, color:Color):
    # Actions for the FrontSensor that detects the path.
    if Sensor == FrontSensor:
        if color == MAP[0]:   # red_map
            slightLeft(0.2)
        elif color == MAP[1]: # yellow_map
            loading()
        elif color == MAP[2]: # green_map
            deliver()
        elif color == MAP[3]: # blue_map
            slightRight(0.2)
        elif color == MAP[4]: # white_map
            goStraight()
        else: # None
            print(f'Invalid color.')

    # Actions for the SideSensor that detects the delivery zone.
    elif Sensor == SideSensor:
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
    else:
        print(f'Invalid sensor.')


# Main function
if __name__ == '__main__':
    try:
        # Debug mode: developer use only
        DEBUG = True # (input('Debug mode? (y/n): ') == 'y')

        print(detects_RGB([24, 39, 42]))
        while True:
            frontColor = detects_RGB(FrontSensor.get_rgb())
            colorAction(FrontSensor, frontColor)

            if DEBUG:
                print(f'FrontSensor: {frontColor}')
                print(f'SideSensor: {sideColor}')
            
            if Button.is_pressed():
                exit()
            goStraight()


    except KeyboardInterrupt:
        exit()

