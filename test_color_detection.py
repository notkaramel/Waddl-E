#!/usr/bin/env python3
from time import sleep
from detect_color import Color
from utils.brick import EV3ColorSensor, wait_ready_sensors


AVAILABLE_COLORS = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'white',
        'white_map', 'blue_map', 'green_map', 'red_map', 'yellow_map', 'orange_map', 'purple_map']
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
    | Input Source | RGB Value | Detected Color |
    """
    print(f'|{expected_color}\t|{input_RGB}\t\t| {detect_color(input_RGB)}\t|')

def test_color_detection():
    """
    Test the color detection
    Procedure:
        #1: Run with a RGB value from the sensor
    """
    # print("Testing color detection... - Test 1")

    print("""| Input Source | RGB Value | Detected Color |\n|--------------|-----------|-------------|""")
    SENSOR = EV3ColorSensor(3)
    wait_ready_sensors()
    i = 0
    while True:
        test(getSampleColor(SENSOR), 'user input', f'2.{i+1}')
        i += 1
        sleep(0.5)

test_color_detection()
