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
import detect_color
from utils.brick import Motor, EV3ColorSensor, TouchSensor

"""
Initialize Motors and Sensors
"""
LeftWheel = Motor("A")
RightWheel = Motor("D")
# Lever = Motor("C")

FrontSensor = EV3ColorSensor(1)
SideSensor = EV3ColorSensor(4)

Button = TouchSensor(3)

"""
Idea #1: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""

"""
When Waddl-E sees WHITE, it goes.
"""
def go(speed=30): # speed in %
    wheels.run(LeftWheel, power=speed)
    wheels.run(RightWheel, power=speed)

"""
When Waddl-E sees BLUE, she turns slightly to the right.
"""
def slightRight():
    pass

"""
When Waddl-E sees RED, she turns slightly to the left.
"""
def slightLeft():
    pass

"""
When Waddl-E sees GREEN, she stops and start delivering.
"""
def deliver():
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
        "WHITE" : go(),
        "BLUE"  : slightRight(),
        "RED"   : slightLeft(),
        "GREEN" : deliver(),
        "YELLOW": loading()
        }

if __name__ == '__main__':
    try:
        while True:
            if Button.is_pressed():
                exit()
            go()


    except KeyboardInterrupt:
        exit()

