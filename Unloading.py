#!/usr/bin/env python3

from utils.brick import Motor
from Button import READY_BUTTON
from time import sleep

SPEED_LIMIT = 1560  # [Degree per second] up to 1560dps

LEVER = Motor("C")
TRAY_ROLLER = Motor("B")

def swingLever(dps=400, delay=2, position=0):
    """
    Use for `delivery.py`
    Make a motor swing at a certain speed for a certain time.
    """
    # LEVER.reset_encoder()
    LEVER.set_dps(dps)
    # LEVER.set_position(position=position)
    LEVER.set_position_relative(position)
    sleep(delay)

def rollTray(dps=100, delay=2, position=0):
    """
    Use for `delivery.py`
    Make a motor roll at a certain speed for a certain time.
    """
    TRAY_ROLLER.set_dps(dps)
    TRAY_ROLLER.set_position_relative(position)
    sleep(delay)

def readyToDeliver():
    return READY_BUTTON.is_pressed()