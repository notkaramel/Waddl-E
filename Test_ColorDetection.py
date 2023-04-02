#!/usr/bin/env python3
from time import sleep
from ColorDetection import detects_RGB, SIDE_SENSOR, FRONT_SENSOR, AVAILABLE_COLORS
from utils.brick import wait_ready_sensors


# def test(input_RGB:list):
#     """
#     A single test for color detection.
#     Display result in markdown form for README.md
#     | Input Source | RGB Value | Detected Color |
#     """
#     print(f'{input_RGB} \t| {detects_RGB(input_RGB, AVAILABLE_COLORS)}\t|')

def test_color_detection():
    """
    Test the color detection
    Procedure:
        #1: Run with a RGB value from the sensor
    """
    FRONT_SENSOR.set_mode("component")
    SIDE_SENSOR.set_mode("component")
    print("""| RGB Value \t| Detected Color |""")
    wait_ready_sensors(True)
    while True:
        frontRGB = FRONT_SENSOR.get_rgb()
        sideRGB = SIDE_SENSOR.get_rgb()
        print(f"Front: \t{frontRGB} \t{detects_RGB(frontRGB, AVAILABLE_COLORS)}")
        # test(FRONT_SENSOR.get_rgb())
        print(f"Side: \t{sideRGB} \t{detects_RGB(sideRGB, AVAILABLE_COLORS)}")
        # test(SIDE_SENSOR.get_rgb())
        sleep(0.75)

test_color_detection()
