#!/usr/bin/env python3.9
""" This program runs the wheel of the vehicle."""
# Author: Antoine Phan @notkaramel

from utils.brick import Motor, BP
from time import sleep

LeftWheel = Motor("A")
RightWheel = Motor("D")

POWER_LIMIT = 80    # Power limit: up to 100 [%]
SPEED_LIMIT = 1560  # [Degree per second] up to 1560dps

def init_motor(motor: Motor):
    motor.reset_encoder()
    motor.set_limits(POWER_LIMIT, SPEED_LIMIT)

def run(motor:Motor, power=50):
    """
    Make right wheel go forward at a certain speed
    """
    motor.set_power(power)

def stop(motor: Motor):
    motor.set_power(0)
    
"""
The method below turns the system base on its direction and time delay

@param direction: "left" or "right"
@param delay (s): the system will turn for a time delay in seconds
"""
def turn(direction: str, delay: int):
    print(f'Vehicle will turn {direction} for {delay}')
    leftSpeed = LeftWheel.get_power()    
    rightSpeed = RightWheel.get_power()

    # angle turned = wheel power * time delay
    print(f'Expected turning angle: {leftSpeed*delay}')
    if direction == "left":
        RightWheel.set_power(-rightSpeed)
        sleep(delay)
        RightWheel.set_power(rightSpeed)
    elif direction == "right":
        LeftWheel.set_power(-leftSpeed)
        sleep(delay)
        LeftWheel.set_power(leftSpeed)
    
# main method to test things out
if __name__=='__main__':
    try:
        sp = int(input("Speed (positive: clockwise, negative: counter-clockwise): "))
        

        run(RightWheel, power=sp)
        run(LeftWheel, power=sp)
        sleep(2)
        turn("left", 3)
    except KeyboardInterrupt:
        BP.reset_all()

