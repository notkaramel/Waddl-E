#!/usr/bin/env python3

from utils.brick import Motor
from time import sleep

def swing(motor: Motor, dps=50, delay=2):
    """
    Use for `delivery.py`
    Make a motor swing at a certain speed for a certain time.
    """
    motor.set_dps(dps)
    motor.set_position(0)
    sleep(delay)