#!/usr/bin/env python3

from Wheels import RIGHT_WHEEL, LEFT_WHEEL, run, stopMotor
from ColorDetection import FRONT_SENSOR, detects_RGB, Color
from time import sleep

"""
Define map colors
"""
MAP_COLORS_STR = ['white', 'blue', 'red', 'green', 'yellow']
MAP_COLORS = [Color(c) for c in MAP_COLORS_STR]

def go(power=50):
    """
    ~ Small action ~ 
    Waddl-E just go straight
    """
    run(RIGHT_WHEEL, power)
    run(LEFT_WHEEL, power)

def stop():
    """
    ~ Small action ~ 
    Waddl-E stops
    """
    stopMotor(RIGHT_WHEEL)
    stopMotor(LEFT_WHEEL)

def pause(pauseDelay: float, afterPauseDelay: float = 0.5):
    """
    ~ Small action ~ 
    Waddl-E sees green, she stops for pauseDelay seconds
    then she goes straight for afterPauseDelay seconds to make sure she is not stuck on green
    """
    leftPower_temp = LEFT_WHEEL.get_power()
    rightPower_temp = RIGHT_WHEEL.get_power()
    stop()
    sleep(pauseDelay)
    run(LEFT_WHEEL, leftPower_temp)
    run(RIGHT_WHEEL, rightPower_temp)
    sleep(afterPauseDelay)
                
def turn(direction: str, delay: float, debug=False):
    """
    ~ Small action, but a bit complex ~ 
    The method turns the system base on its direction and time delay

    @params:
    - direction (str): "left" or "right"
    - delay (float): [in seconds] the system will turn for a time delay in seconds
    - debug (bool, optional): Print turning direction and delay. Defaults to False.
    """
        
    if debug:
        print(f'Vehicle will turn {direction} for {delay}')
    
    leftSpeed = LEFT_WHEEL.get_power()    
    rightSpeed = RIGHT_WHEEL.get_power()
    
    if(leftSpeed == 0 or rightSpeed == 0):
        LEFT_WHEEL.set_power(10)
        RIGHT_WHEEL.set_power(10)

    if direction == "right":
        RIGHT_WHEEL.set_power(-rightSpeed)
        sleep(delay)
        RIGHT_WHEEL.set_power(rightSpeed)
    elif direction == "left":
        LEFT_WHEEL.set_power(-leftSpeed)
        sleep(delay)
        LEFT_WHEEL.set_power(leftSpeed)


# <-- IMPORT THESE FUNCTIONS TO INTEGRATION -->
def getFrontColor() -> str:
    frontRGB = FRONT_SENSOR.get_rgb()
    frontColor = detects_RGB(frontRGB, MAP_COLORS)
    return frontColor
    

def goStraight(power=30, debug=False): # speed in %
    """
    When Waddl-E sees WHITE, it goes.
    The function uses go()
    """
    if debug:
        print(f'Going straight at {power}% speed.')
    go(power)

def slightTurn(direction:str, delay:float, debug=False):
    """
    When Waddl-E sees BLUE, it turns slightly to the right.
    When Waddl-E sees RED, it turns slightly to the left.

    @params:
    - direction (str): "left" or "right"
    - delay (float): [in seconds] the system will turn for a time delay in seconds
    """
    
    if debug:
        print(f'Turning slightly right (delay={delay}))')
    turn(direction, delay)

def turnAround(power=50, timeDelay=0.9):
    """
    ~ Small action ~
    When Waddl-E sees YELLOW, it turns around to reload (second trip).
    Waddl-E turns to her left to avoid collecting the cube that just gets dropped
    @param:
    - power [%]: vehicle power level
    - timeDelay [s]: delay time for the turning motion
    
    Default values are taken from the tests for optimal motions.
    """
    go(power=power)
    # import random
    # direction = random.choice(['left', 'right'])
    direction = 'left'
    turn(direction=direction, delay=timeDelay)
    stop()
    
    