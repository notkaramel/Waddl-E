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
from Delivery import getSideColor, deliverCube, ZONE_COLORS, resetRack
from ColorDetection import Color, detects_RGB, SIDE_SENSOR
from Button import READY_BUTTON, STOP_BUTTON
from time import sleep

REMAINING_CUBES = 6
DEBUG = False

"""
Idea: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""
# <-- Program starts here --> #

def debugLog(debug:False):
    """
    [Not yet finished]
    Log file for debugging
    """
    if debug:
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

def WaddleGoNormally():
    """
    The main function of Waddl-E.
    Waddl-E will go normally on the map until she sees green to "deliver mode".
    WADDL-E GOOOO!!! 
    TODO: add a debug mode
    """
    if DEBUG:
        print("----- Go Normally -----")
    global REMAINING_CUBES
    while True:
        if STOP_BUTTON.is_pressed():
            stop()
            resetRack()
            if DEBUG:
                print("Terminate program suddenly")
            WaddleMain()
        frontColor = getFrontColor()
        
        if REMAINING_CUBES == 0:
            print("YAY! Waddl-E has finished her job.\nNow she will return to the Loading Bay")
            WaddleGoBackToLoadingBay()
            reset()
            break
        
        if frontColor == 'None':
            goStraight(power=15)
            sleep(0.1)
        elif frontColor == 'white':
            goStraight(power=32)
            sleep(0.1)
        elif frontColor == "red":
            slightTurn("left", 0.3)
        elif frontColor == "blue":
            slightTurn("right", 0.3)
        elif frontColor == "green": # Delivering
            WaddleDeliver()
        elif frontColor == "yellow": # Reloading
            pass
        else:
            print(f'None detected')

def WaddleCalibrateToDeliver():
    if DEBUG:
        print("----- Calibrate to Deliver -----")
    if STOP_BUTTON.is_pressed():
        stop()
        resetRack()
        print("Terminate program suddenly")
        WaddleMain()
    frontColor = getFrontColor()
    # Proceed to travel as normal, but slowly
    if frontColor == 'None' or frontColor == "green" or frontColor == "white":
        goStraight(power=20,debug=DEBUG)
        sleep(0.1)
    elif frontColor == "red":
        slightTurn("left", 0.2, debug=DEBUG)
    elif frontColor == "blue":
        slightTurn("right", 0.2, debug=DEBUG)
    
def WaddleGoBackwardToCatchColorAgain():
    if DEBUG:
        print("----- Go backward to catch color -----")
    goStraight(power=-20)
    sleep(0.5)
    stop()

def WaddleDeliver():
    """
    Waddl-E will deliver the cubes to their corresponding location.
    This is called when she detects frontColor = green.
    
    She will get the color of the zone from the side sensor, save it as a variable.
    She will go as normal but with less speed (using front sensor data).
    In the meantime, she will detect the zone color on the side sensor.
    When she detects WHITE again on the side, she will stop and deliver the cube.
    Calibration might be needed.
    """
    if DEBUG:
        print("----- Delivering -----")
    global REMAINING_CUBES
    
    sideColor = getSideColor()
    toBeDelivered = 'None'
    while sideColor == 'None':
        WaddleCalibrateToDeliver()        
        sideColor = toBeDelivered = getSideColor()
        
    # Assume that the sideColor is detected
    if DEBUG:
        print(f"DELIVERING: {toBeDelivered}")
    outOfZone = [Color('white')]
    while detects_RGB(SIDE_SENSOR.get_rgb(), outOfZone) != 'white':
        WaddleCalibrateToDeliver()
        print(f"got into here, toBeDelivered: {toBeDelivered}")
        if toBeDelivered == 'None':
            WaddleGoBackwardToCatchColorAgain()
    
    
    stop()
    if deliverCube(toBeDelivered):
        # if cube is delivered, set speed to continue
        goStraight(20)
        REMAINING_CUBES -= 1
    
def WaddleGoBackToLoadingBay():
    """
    Waddl-E will go back to loading bay once all cubes are delivered.
    If she sees blue, she will turn left.
    Is she sees red, she will turn right.
    She treats green same way as white.
    Once she sees yellow, she will turn around and prompt user to reload cubes.
    She continues to go once the READY_BUTTON is pressed.
    
    Implementation will be similar to WaddleGoNormally()
    """
    if DEBUG:
        print("----- Going back to Loading Bay -----")
    
    # Reset rack to avoid imbalance, because going back will be very fast
    resetRack()
    turnAround()
    
    while True:
        if STOP_BUTTON.is_pressed():
            reset()
            print("Terminate program suddenly")
            WaddleMain()
        
        frontColor = getFrontColor()
        
        if frontColor == 'None':
            goStraight(power=18)
            sleep(0.1)
        elif frontColor == 'white' or frontColor == "green":
            goStraight(power=40)
            sleep(0.1)
        elif frontColor == "red":
            slightTurn("right", 0.2)
        elif frontColor == "blue":
            slightTurn("left", 0.2)
        elif frontColor == "yellow": # Reloading
            turnAround()
            reset()
            break

            # NotLoaded = True
            # while NotLoaded:
            #     if READY_BUTTON.is_pressed():
            #         print(f'Waddl-E is ready to go!')
            #         NotLoaded = False
                    
            #     if STOP_BUTTON.is_pressed():
            #         reset()
            #         print(f'Waddl-E is stopped while reloading.')
            #         NotLoaded = False
        else:
            print(f'None detected')

def reset():
    global REMAINING_CUBES 
    REMAINING_CUBES = 6
    stop()
    resetRack()

def WaddleMain():
    # Debug mode: developer use only
        # DEBUG = True # (input('Debug mode? (y/n): ') == 'y')
        print("""
            Please reload the cubes in order:
            [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]\n
            Press the button when done.
        """)
        while not READY_BUTTON.is_pressed():
            pass
        print(f'Departure in 1 second!')
        sleep(1)
        
        WaddleGoNormally()

# Main function
if __name__ == '__main__':
    try:
        debugChoice = input("Debug? [Y/n]: ")
        if debugChoice.lower == 'Y' or debugChoice == '':
            DEBUG = True
            
        while True:
            WaddleMain()
    except KeyboardInterrupt:
        reset()
        exit()

