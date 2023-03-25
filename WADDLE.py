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
Wheels:
    Left: Motor A (port MA)
    Right: Motor D (port MD)
    Rack: Motor B (port MB)
    Lever: Motor C (port MC)

Sensors:
    Front: port S3
    Side: port S4
    Buttons: the remainings
"""

LeftWheel = Motor("A")
RightWheel = Motor("D")
CubeHolder = Motor("B")
Lever = Motor("C")

FrontSensor = EV3ColorSensor(3)
SideSensor = EV3ColorSensor(4)

Button = TouchSensor(1)
wait_ready_sensors(DEBUG)

"""
Idea: each color detected from the front sensor will correspond to an action. 
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

def debug_log(DEBUG:bool):
    if DEBUG:
        with open('log.txt') as logfile:
            leftSpeed = LeftWheel.get_power()
            rightSpeed = RightWheel.get_power()
            front_rgb = FrontSensor.get_rgb()
            frontColor = detects_RGB(front_rgb)
            side_rgb = SideSensor.get_rgb()
            sideColor = detects_RGB(side_rgb)

            logfile.write(f'<----------------->')
            logfile.write(f'Left: {leftSpeed} | Right: {rightSpeed}')
            logfile.write(f'FRONT: RGB: {front_rgb} \t >>> {frontColor}')
            logfile.write(f'SIDE:  RGB: {front_rgb} \t >>> {sideColor}')
            logfile.write(f'<----------------->')

def deliver():
    pass

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
            slightLeft(0.5)
        elif color == MAP[1]: # yellow_map
            loading()
        elif color == MAP[2]: # green_map
            deliver()
        elif color == MAP[3]: # blue_map
            slightRight(0.5)
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
        while True:
            frontColor = detects_RGB(FrontSensor.get_rgb())
            colorAction(FrontSensor, frontColor)
            
            if Button.is_pressed():
                exit()


    except KeyboardInterrupt:
        exit()

