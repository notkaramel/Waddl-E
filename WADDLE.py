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
from Vehicle import goStraight, turnAround, slightTurn, stop, pause, getFrontColor
from Delivery import getSideColor, deliverCube, resetRack, ZONE_COLORS_STR, ZONE_COLORS
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
            WaddleReset()
            break
        
        if frontColor == 'None':
            goStraight(power=18)
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
        WaddleReset()
        print("Terminated Delivery")
        WaddleMain()
    frontColor = getFrontColor()
    # Proceed to travel as normal, but slowly
    
    if frontColor == 'None' or frontColor == "white":
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
    slightTurn("left", 0.1) # will turn right because power is negative
    sleep(0.3)
    stop()

def WaddleDeliver():
    """
    Waddl-E will deliver the cube to the corresponding zone. 
    """
    """
    # Below is the pseudocode:
    # 1. She will get the color of the side sensor.
    sideColor = getSideColor()
    
    # 2. If the color is not detected/ is white, she will calibrate.
    # Calibrate means that she will go backward and turn left/right to see the color again.
    
    if sideColor == none or sideColor == white:
        calibrateToGetColor()
            
    # 3. Once a color is detected, she assigns the color to a variable.
    if sideColor != none and sideColor != white:
        toBeDelivered = sideColor
        
    # 4. She has to align to the zone before delivering, i.e., go until see white on the side sensor
    while getSideColor() != white:
        calibrateToDeliver()
        
    # 5. Once she sees white, she will stop to deliver the cube.
    deliverCube(toBeDelivered)    
    
    """
    print("----- Delivering -----")
    global REMAINING_CUBES
        
    # 1, 2
    while getSideColor() == 'None' or getSideColor() == 'white':
        # calibrate
        WaddleGoBackwardToCatchColorAgain()
    
    # 3
    toBeDelivered = getSideColor()        
    if DEBUG:
        print(f"DELIVERING: {toBeDelivered}")
    
    # 4
    while getSideColor() != 'white':
        WaddleCalibrateToDeliver()
    
    # 5
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
    
    resetRack()
    turnAround()
    
    while True:
        if STOP_BUTTON.is_pressed():
            WaddleReset()
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
        elif frontColor == "yellow": # Finished returning
            turnAround()
            break
        else:
            print(f'None detected')

def WaddleReset():
    global REMAINING_CUBES 
    REMAINING_CUBES = 6
    stop()
    resetRack()

def WaddleMain():
    print("Please reload the cubes in order: [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]\nPress the button when done.")
    while True:
        if READY_BUTTON.is_pressed():
            break
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
        WaddleReset()
        exit()

