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
    #motor.set_power(20)

def run(motor:Motor, power=50):
    """
    Make right wheel go forward at a certain speed
    """
    motor.set_power(power)

def stop(motor: Motor):
    motor.set_power(0)
    
def turn(angle: int, dps=800):
    # angle turned = wheel power * time sleep  
    stop(RightWheel) 
#    LeftWheel.set_position_relative(angle)
#    RightWheel.set_position_relative(-angle)
    sleep(2)

# main method to test things out
if __name__=='__main__':
    try:
        init_motor(RightWheel)
        sp = int(input("Speed (positive: clockwise, negative: counter-clockwise): "))
        while True:
            run(RightWheel, power=sp)
            run(LeftWheel, power=sp)
            sleep(2)
            turn(180)
    except KeyboardInterrupt:
        BP.reset_all()

