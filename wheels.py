#!/usr/bin/python3.9
""" This program runs the wheel of the vehicle."""
# Author: Antoine Phan @notkaramel

from utils.brick import Motor

LeftWheel = Motor("A")
RightWheel = Motor("D")

POWER_LIMIT = 80    # Power limit: up to 100 [%]
SPEED_LIMIT = 1560  # [Degree per second] up to 1560dps

def init_motor(motor: Motor):
    motor.reset_encoder()
    motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
    motor.set_power(0)

def forwardLeft():
    LeftWheel.set_position(-360)







