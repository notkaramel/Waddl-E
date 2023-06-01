#!/usr/bin/env python3.9
""" This program runs the wheel of the vehicle."""
# Author: Antoine Phan @notkaramel

from utils.brick import Motor

LEFT_WHEEL = Motor("A")
RIGHT_WHEEL = Motor("D")

POWER_LIMIT = 80    # Power limit: up to 100 [%]


def run(motor: Motor, power=50):
    """
    Use for `vehicle.py`
    Make right wheel go forward or backward at a certain speed.
    """
    motor.set_power(power)


def stopMotor(motor: Motor):
    """
    Use for `vehicle.py`
    Stop a motor
    """
    motor.set_power(0)
