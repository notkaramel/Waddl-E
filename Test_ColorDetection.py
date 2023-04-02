#!/usr/bin/env python3
from time import sleep
from ColorDetection import detects_RGB, SIDE_SENSOR, FRONT_SENSOR, AVAILABLE_COLORS
from utils.brick import wait_ready_sensors

def test(input_RGB:list):
    """
    A single test for color detection.
    Display result in markdown form for README.md
    | Input Source | RGB Value | Detected Color |
    """
    print(f'{input_RGB} \t| {detects_RGB(input_RGB, AVAILABLE_COLORS)}\t|')

def test_color_detection():
    """
    Test the color detection
    Procedure:
        #1: Run with a RGB value from the sensor
    """
    print("""| RGB Value \t| Detected Color |""")
    wait_ready_sensors(True)
    while True:
        print("Front: ", end="")
        test(FRONT_SENSOR.get_rgb())
        print("Side: ", end="")
        test(SIDE_SENSOR.get_rgb())
        sleep(0.75)

test_color_detection()
