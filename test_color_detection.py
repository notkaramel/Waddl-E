#!/usr/bin/env python3
from time import sleep
from detect_color import Color
from utils.brick import EV3ColorSensor, wait_ready_sensors


AVAILABLE_COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white']
COLORS = [Color(color) for color in AVAILABLE_COLORS]

def detect_color(input_RGB:list):
    """Detect the color of the input RGB value"""
    color_error = {}
    for color in COLORS:
        detectedColor, error = color.compareWithInput(input_RGB)
        if detectedColor:
            color_error.update({color.name: error})
            # return color.name

    # return the color with least error:
    return min(color_error.items(), key=lambda x: x[1])[0] if len(color_error) > 0 else None

def detect_color_Antoine(input_RGB:list):
    """Detect the color of the input RGB value, using Antoine's method"""
    for color in COLORS:
        if color.compareWithInput_Antoine(input_RGB):
            return color.name
    return None

def getSampleColor(sensor:EV3ColorSensor):
    """Get the sample color from the sensor"""
    return sensor.get_rgb()

def test(input_RGB:list, expected_color:str, testcode:str):
    """
    A single test for color detection.
    Display result in markdown form for README.md
    | Input Source | RGB Value | Ryan's Algo | Antoine's |
    """
    print(f'|{expected_color}.csv \t|{input_RGB} \t| {detect_color(input_RGB)} \t| {detect_color_Antoine(input_RGB)} |')

def test_color_detection():
    """
    Test the color detection
    Procedure:
        # Test 1: Run with pre-defined RGB values (randomly taken from a data file)
            - Take a random RGB value from a data file
            - Run the program with that RGB value
            - Check if the program returns the correct color
        # Test 2: Run with a RGB value from the sensor
    """
    print("Testing color detection... - Test 1")

    print("""
    | Input Source | RGB Value | Ryan's Algo | Antoine's |
    |--------------|-----------|-------------|-----------|

          """)
    # print("Blue tests")
    test([17, 33, 48], 'blue', '1.1-B')
    test([8, 17, 30], 'blue', '1.2-B')

    # print("Green tests")
    test([22, 101, 32], 'green', '1.3-G')
    test([17, 81, 24], 'green', '1.4-G')
    
    # print("Red tests")
    test([215, 27, 26], 'red', '1.5-R')
    test([76, 12, 13], 'red', '1.6-R')

    # print("Yellow tests")
    test([284, 187, 22], 'yellow', '1.7-Y')
    test([76, 60, 9], 'yellow', '1.8-Y')
    
    # print("Orange tests")
    test([173, 47, 33], 'orange', '1.9-O')
    test([76, 21, 20], 'orange', '1.10-O')
    
    # print("Purple tests")
    test([20, 15, 23], 'purple', '1.11-P')
    test([74, 49, 75], 'purple', '1.12-P')

    print("Testing color detection... - Test 2")
    SENSOR = EV3ColorSensor(3)
    wait_ready_sensors()
    i = 0
    while True:
        test(getSampleColor(SENSOR), 'user input', f'2.{i+1}')
        i += 1
        sleep(0.1)

test_color_detection()
