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
from Vehicle import goStraight, turnAround, slightTurn, stop, pause, getFrontColor, betterTurn
from Delivery import getSideColor, deliverCube, resetRack, ZONE_COLORS_STR, ZONE_COLORS
from ColorDetection import Color, detects_RGB, SIDE_SENSOR
from Button import READY_BUTTON, STOP_BUTTON
from time import sleep

REMAINING_CUBES = 6
DEBUG = False
LAST_TURN = None
"""
Idea: each color detected from the front sensor will correspond to an action. 
The program will run on an infinite `while True:` loop
Each action will be triggered based on the condition changes, i.e., a <color> detected.
The button (for now?) will be used for sudden stop.
"""
# <-- Program starts here --> #

def WaddlEGoesNormally():
    """
    The main function of Waddl-E.
    Waddl-E will go normally on the map until she sees green to "deliver mode".
    WADDL-E GOOOO!!! 
    """
    if DEBUG:
        print("----- Go Normally -----")
    
    global REMAINING_CUBES, LAST_TURN
    while True:
        if STOP_BUTTON.is_pressed():
            stop()
            resetRack()
            if DEBUG:
                print("Terminate program suddenly")
            WaddleMain()
        frontColor = getFrontColor()
        if DEBUG:
            print(frontColor)
        
        if REMAINING_CUBES == 0:
            print("YAY! Waddl-E has finished her job.\nNow she will return to the Loading Bay")
            goStraight(20)
            sleep(2.1)
            WaddleGoBackToLoadingBay()
            WaddleReset()
            break
        
        if frontColor == 'None':
            goStraight(power=16)
            sleep(0.05)
        elif frontColor == 'white':
            goStraight(power=32)
            sleep(0.05)
        elif frontColor == "red":
            betterTurn("left")
            LAST_TURN = "left"
            # slightTurn("left", 0.3)
        elif frontColor == "blue":
            betterTurn("right")
            LAST_TURN = "right"
            # slightTurn("right", 0.3)
        elif frontColor == "green": # Delivering
            if LAST_TURN != None:
                slightTurn(LAST_TURN, 0.05)
            WaddlEDelivers()
            LAST_TURN = None
        elif frontColor == "yellow": # Reloading
            # break
            pass
        else:
            print(f'None detected')

def WaddlETriesToCatchColor() -> str:
    """
    Waddl-E will try to catch the color from the side sensor.
    # Below is the pseudocode:
    # 1. She will get the color of the side sensor.
    sideColor = getSideColor()

    # 2.1. Assume that she has detected the color, she will just deliver the cube.
    toBeDelivered = sideColor
    
    # 2.2. Assume that Waddl-E has NOT detected the color, she will calibrate.
    # Waddl-E will see if she sees white, meaning that she's already passed the zone.
    ? what if she sees white but she hasn't passed the zone yet?
    
    # Here, she goes backward to catch the color again.
    """
    
    toBeDelivered = 'None'
    while True:
        sideColor = getSideColor()
        if sideColor in ['None', 'white'] : # act according to the side sensor
            WaddlECalibratesToDeliver() # go according to the front sensor
        # elif sideColor == 'white': # ahead of the zone | ? before the zone
            # WaddlEGoesBackwardToCatchColorAgain() # go backward to catch the color again
        else:
            toBeDelivered = sideColor
            if DEBUG:
                print(f"DELIVERING: {toBeDelivered}")
            break
    return toBeDelivered

def WaddlECalibratesToDeliver():
    if DEBUG:
        print("----- Calibrate to Deliver -----")
    
    if STOP_BUTTON.is_pressed():
        WaddleReset()
        print("Terminated Delivery")
        WaddleMain()
    frontColor = getFrontColor()
    # Proceed to travel as normal, but slowly
    
    if frontColor == 'None' or frontColor == "white":
        goStraight(power=15,debug=DEBUG)
        sleep(0.05)
    elif frontColor == "red":
        # betterTurn("left")
        slightTurn("left", 0.15, debug=DEBUG)
    elif frontColor == "blue":
        # betterTurn("right")
        slightTurn("right", 0.15, debug=DEBUG)
    
def WaddlEDelivers():
    """
    Triggered when Waddl-E sees green.
    Waddl-E will deliver the cube to the corresponding zone. 
    """
    print("----- Delivering -----")
    global REMAINING_CUBES
        
    """
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
    toBeDelivered = WaddlETriesToCatchColor()
    
    # Assume that Waddl-E has detected the color, she will:
    # 1. Go until she sees white on the side sensor
    # 2. Stop to deliver the cube
            
    while getSideColor() != 'white': # ahead of the zone
        WaddlECalibratesToDeliver()
        
    stop()
    if deliverCube(toBeDelivered):
        # if cube is delivered, set speed to continue
        REMAINING_CUBES -= 1
    
    if DEBUG:
        print(f'DELIVERED: {toBeDelivered}\nREMAINING CUBES: {REMAINING_CUBES}')
    # sleep(0.01)
    # goStraight(30)

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
    
    global LAST_TURN
    LAST_TURN = None
    resetRack()
    turnAround(returning=True)
    
    while True:
        if STOP_BUTTON.is_pressed():
            WaddleReset()
            print("Terminate program suddenly")
            WaddleMain()
        
        frontColor = getFrontColor()
        
        if frontColor == 'None':
            goStraight(power=18)
            sleep(0.05)
        elif frontColor == "green":
            if LAST_TURN != None:
                slightTurn(LAST_TURN, 0.12)
            goStraight(power=30)
            LAST_TURN = None
            sleep(0.05)
        elif frontColor == 'white':
            goStraight(power=32)
            sleep(0.05)
        elif frontColor == "red":
            betterTurn("right")
            LAST_TURN = "right"
            # slightTurn("right", 0.2)
        elif frontColor == "blue":
            betterTurn("left")
            LAST_TURN = "left"
            # slightTurn("left", 0.2)
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
    print("----- Waddle Main -----")
    WaddleReset()
    print("Please reload the cubes in order: [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]\nPress the button when done.")
    while True:
        if READY_BUTTON.is_pressed():
            break
    print(f'Departure in 1 second!')
    sleep(1)

# Main function
if __name__ == '__main__':
    try:
        DEBUG = True
            
        while True:
            WaddleMain()
            WaddlEGoesNormally()
    except KeyboardInterrupt:
        WaddleReset()
        exit()

