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

# Import Subsystems
from Vehicle import *
from Delivery import *
from time import sleep

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

"""
Idea: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""
# <-- Program starts here --> #

"""
When Waddl-E sees GREEN, it stops and start delivering.
The color cubes are given in a fixed order from the beginning at the loading bay.
[purple, blue, green, yellow, orange, red]
"""

def debug_log(DEBUG:bool):
    if DEBUG:
        with open('log.txt') as logfile:
            leftSpeed = LEFT_WHEEL.get_power()
            rightSpeed = RIGHT_WHEEL.get_power()
            front_rgb = FRONT_SENSOR.get_rgb()
            frontColor = detects_RGB(front_rgb)
            side_rgb = SIDE_SENSOR.get_rgb()
            sideColor = detects_RGB(side_rgb)

            logfile.write(f'<----------------->')
            logfile.write(f'Left: {leftSpeed} | Right: {rightSpeed}')
            logfile.write(f'FRONT: RGB: {front_rgb} \t >>> {frontColor}')
            logfile.write(f'SIDE:  RGB: {front_rgb} \t >>> {sideColor}')
            logfile.write(f'<----------------->')



"""
List of action based on color for the FrontSensor.
The FrontSensor only detects 5 colors of the map.
Color order: Rainbow, then white
[RED, YELLOW, GREEN, BLUE, WHITE]
""" 
MAP_COLORS = ['red_map', 'yellow_map', 'green_map', 'blue_map', 'white_map']
MAP = [Color(color_i) for color_i in MAP_COLORS]



# Main function
if __name__ == '__main__':
    try:
        # Debug mode: developer use only
        DEBUG = True # (input('Debug mode? (y/n): ') == 'y')
        while True:



    except KeyboardInterrupt:
        exit()

