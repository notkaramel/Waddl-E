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
from unit.ColorDetection import Color, detects_RGB
from subsystems.Vehicle import go, stop, turn
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



# Action based on color. 
def colorAction(Sensor: EV3ColorSensor, color:Color):
    # Actions for the FrontSensor that detects the path.
    if Sensor == FrontSensor:
        

    # Actions for the SideSensor that detects the delivery zone.
    elif Sensor == SideSensor:
        
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

