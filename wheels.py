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

def run(motor:Motor, power=50, speed = 300):
    """
    Make right wheel go forward at a certain speed
    """

    #motor.set_dps(speed)
    motor.set_power(power)

if __name__=='__main__':
    try:
        init_motor(RightWheel)
        sp = int(input("Speed (positive: clockwise, negative: counter-clockwise): "))
        while True:
            run(RightWheel, power=sp)
            run(LeftWheel, power=-sp)
    except KeyboardInterrupt:
        BP.reset_all()

