#!/usr/bin/env python3
"""
This program uses the color sensor at port S3.

Takes in a RGB value (or a list of sample value)
to detect the seeing color.

It uses data collected generated from `collect_colors.py`
and ./data/color_data_*.csv files

Author: Antoine Phan @notkaramel
Support: GitHub Copilot, ChatGPT
"""

from utils.brick import EV3ColorSensor, wait_ready_sensors
from statistics import mean, stdev
import os

FRONT_SENSOR = EV3ColorSensor(3)
SIDE_SENSOR = EV3ColorSensor(4)

wait_ready_sensors(True)

class Color:
    def __init__(self, name:str):
        self.name = name.lower() # making sure it's lowercase
        # Find color file in ./data/
        color_file = f'./data/color_data_{name}.csv'

        # Normalize the data and set attributes
        self.meanRGB, self.stdevRGB = normalize_data(color_file)

        # print(f'Color {name} is loaded with meanRGB {self.meanRGB} and stdevRGB {self.stdevRGB}')

    def compareWithInput(self, input_rgb:list):
        """
        Return a boolean (True/False) and the standard distance
        Compare the Color data with the input RGB value
        Return True if the input RGB value is within 2 standard deviations
        Method given by Ryan Au from Tutorial 4
        """
        try:    
            mR, mG, mB = self.meanRGB
            sR, sG, sB = self.stdevRGB
            iR, iG, iB = input_rgb

            diffR = (mR - iR)/sR
            diffG = (mG - iG)/sG
            diffB = (mB - iB)/sB

            std_distance = (diffR**2 + diffG**2 + diffB**2)**0.5
            # print(f'Standard distance of {self.name} is {std_distance}')
            return std_distance <= 2, std_distance
        except:
            return False, 0
        
    def __str__(self):
        return f'Color {self.name} with meanRGB {self.meanRGB} and stdevRGB {self.stdevRGB}'

def normalize_data(color_file):
    """Normalize the data from the color file"""
    with(open(color_file, 'r')) as cfile:
        data = cfile.readlines()
        """ 
            At this stage, data is a list of strings, including the newline character
            Also, the line is in format of a string (that looks like a list),
            so we need to convert it to a list of ints.
            e.g. line is `"[1, 2, 3]\n"` and we want to convert it to `[1, 2, 3]`

            Personal note: This is bad explanation. I know, and I'm sorry.
        """
        # from "[1, 2, 3]\n" to "['1', '2', '3']"
        data = [line[1:-2].split(',') for line in data]
        # from "['1', '2', '3']" to "[1, 2, 3]"
        data = [[int(val) for val in line] for line in data]
        
        # Normalize the data
        # Split channels into separate lists
        Rchannel = [line[0] for line in data]
        Gchannel = [line[1] for line in data]
        Bchannel = [line[2] for line in data]

        # Calculate mean and standard deviation
        meanRGB = [mean(Rchannel), mean(Gchannel), mean(Bchannel)]
        stdevRGB = [stdev(Rchannel), stdev(Gchannel), stdev(Bchannel)]

        # Close the file
        cfile.close()
    return meanRGB, stdevRGB

color_files = os.listdir('data')
AVAILABLE_COLORS = [Color(c[11:-4]) for c in color_files]

# COLORS = [Color(color) for color in AVAILABLE_COLORS]

def detects_RGB(input_RGB:list, availableColors:list[Color]) -> str:
    """Detect the color of the input RGB value"""
    color_error = {}
    for color in availableColors:
        detectedColor, error = color.compareWithInput(input_RGB)
        if detectedColor:
            # return color.name (str)
            color_error.update({color.name: error})

    # return the Color object with least error:
    return min(color_error.items(), key=lambda x: x[1])[0] if len(color_error) > 0 else None

