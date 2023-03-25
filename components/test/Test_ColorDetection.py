#!/usr/bin/env python3
from time import sleep
from ColorDetection import detects_RGB, FRONT_SENSOR
from utils.brick import wait_ready_sensors

# def detect_color_Antoine(input_RGB:list):
#     """Detect the color of the input RGB value, using Antoine's method"""
#     for color in COLORS:
#         if color.compareWithInput_Antoine(input_RGB):
#             return color.name
#     return None

def test(input_RGB:list, expected_color:str):
    """
    A single test for color detection.
    Display result in markdown form for README.md
    | Input Source | RGB Value | Detected Color |
    """
    print(f'|{expected_color}\t|{input_RGB}\t\t| {detects_RGB(input_RGB)}\t|')

def test_color_detection():
    """
    Test the color detection
    Procedure:
        #1: Run with a RGB value from the sensor
    """
    # print("Testing color detection... - Test 1")

    print("""| RGB Value | Detected Color |""")
    wait_ready_sensors()
    i = 0
    while True:
        test(FRONT_SENSOR.get_rgb(), 'user input', f'2.{i+1}')
        i += 1
        sleep(0.5)

test_color_detection()
