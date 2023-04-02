#!/usr/bin/env python3
"""
The final system design of Waddl-E:
the autonomous delivery robot that delivers color foam cubes
to their correspoding location on a map.

Also, I think I'm going to diary as I go on this file :))

Author: Antoine Phan @notkaramel

Naming Convention: CamelCase
System name: Waddl-E

<----------------->

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
    
<----------------->
"""

# Import Subsystems
from Vehicle import goStraight, turnAround, slightTurn, stop, pause, getFrontColor, MAP_COLORS
from Delivery import getSideColor, deliverCube, ZONE_COLORS
from Button import READY_BUTTON, STOP_BUTTON
from time import sleep


"""
Idea: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""
# <-- Program starts here --> #

def debugLog(DEBUG:bool):
    """
    [Not yet finished]
    Log file for debugging
    """
    if DEBUG:
        from ColorDetection import FRONT_SENSOR, SIDE_SENSOR, detects_RGB
        from Vehicle import LEFT_WHEEL, RIGHT_WHEEL
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

def WaddleGoNormally(debug=False):
    """
    The main function of Waddl-E.
    Waddl-E will go normally on the map until she sees green to "deliver mode".
    WADDL-E GOOOO!!! 
    TODO: add a debug mode
    """
    while True:
        if STOP_BUTTON.is_pressed():
            print("Terminate program suddenly")
        
        frontColor = getFrontColor()
        sideColor = getSideColor()
        
        if frontColor == None:
            goStraight(power=18)
            sleep(0.1)
        elif frontColor == 'white':
            goStraight(power=42)
            sleep(0.1)
        elif frontColor == "red":
            slightTurn("left", 0.4)
        elif frontColor == "blue":
            slightTurn("right", 0.4)
        elif frontColor == "green": # Delivering
            stop()
            while(sideColor not in ZONE_COLORS):
                sideColor = getSideColor()
                goStraight(power=10)
                sleep(0.1)
            deliverCube(sideColor)
        elif frontColor == "yellow": # Reloading
            turnAround()
            stop()
            print("""
                  Please reload the cubes in order:
                  [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]\n
                  Press the button when done.
                  """)
            NotFinished = True
            while NotFinished:
                if READY_BUTTON.is_pressed():
                    print(f'Waddl-E is ready to go!')
                    NotFinished = False
                if STOP_BUTTON.is_pressed():
                    print(f'Waddl-E is stopped while reloading.')
                    NotFinished = False
        else:
            print(f'None detected')

def WaddleDeliver():
    """
    Waddl-E will deliver the cubes to their corresponding location.
    She will get the color of the zone from the side sensor, save it as a variable.
    She will go as normal but with less speed (using front sensor data).
    In the meantime, she will detect the zone color on the side sensor.
    When she detects WHITE again on the side, she will stop and deliver the cube.
    Calibration might be needed.
    """

    
# Main function
if __name__ == '__main__':
    try:
        # Debug mode: developer use only
        # DEBUG = True # (input('Debug mode? (y/n): ') == 'y')
        WaddleGoNormally()
    except KeyboardInterrupt:
        exit()

