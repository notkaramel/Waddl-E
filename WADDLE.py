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
from detect_color import COLORS, detects_RGB
from utils.brick import Motor, EV3ColorSensor, TouchSensor, wait_ready_sensors
from time import sleep

"""
Initialize Motors and Sensors
"""
LeftWheel = Motor("A")
RightWheel = Motor("D")
# Lever = Motor("C")

FrontSensor = EV3ColorSensor(1)
#SideSensor = EV3ColorSensor(4)

#Button = TouchSensor(3)
wait_ready_sensors(True)

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
    wheels.run(LeftWheel, power=speed)
    wheels.run(RightWheel, power=speed)

"""
When Waddl-E sees BLUE, she turns slightly to the right.
"""
def slightRight(delay:float):
    wheels.turn("right", delay)

"""
When Waddl-E sees RED, she turns slightly to the left.
"""
def slightLeft(delay):
    wheels.turn("left", delay)

"""
When Waddl-E sees GREEN, she stops and start delivering.
"""
def deliver():
    sleep(3)
    pass

"""
When Waddl-E sees YELLOW: she stops, turns around, maybe play a tune to tell that she's in loading mode.
"""
def loading():
    pass


"""
List of action based on color for the FrontSensor
""" 
colorAction = {
        "WHITE" : goStraight(),
#        "BLUE"  : slightRight(),
#        "RED"   : slightLeft(),
        "GREEN" : deliver(),
        "YELLOW": loading()
        }

MAP_COLOR = ['white_map', 'blue_map', 'green_map',
        'red_map', 'yellow_map', 'orange_map', 'purple_map']

# Main function
if __name__ == '__main__':
    try:
        while True:
            color = detects_RGB(FrontSensor.get_rgb())
            print(f'Detecting [{color}]')

            #if Button.is_pressed():
            #    exit()
            goStraight()


    except KeyboardInterrupt:
        exit()

