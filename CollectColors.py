#!/usr/bin/env python3
"""
This program collects data from the colour sensor.
The data will be stored in ./data/color_data_<number>.csv
The program belongs to the `component` testing stage.

Author: Antoine Phan @notkaramel
"""

from utils.brick import EV3ColorSensor, wait_ready_sensors
from Button import READY_BUTTON
from time import sleep
import os

COLOR_SENSOR = EV3ColorSensor(3)  # initialize color sensor at S3
wait_ready_sensors(True)
COLOR_SENSOR.set_mode('component')

""" The method to collect color data from the sensor"""
def collect_data():
    print("Start collecting data")

    # letting tester to collect data of a color of choice
    color = input("Color? (red, green, yellow): ").lower() # making sure color's name is lowercase
    data_location = f'data/color_data_{color}.csv'
    if (data_location in os.listdir('./data')):
        os.system(f'touch {data_location}')
    print(f'Output data is at {data_location}')
    
    try:
        outfile = open(data_location, "a")
        
        while True:
            if READY_BUTTON.is_pressed():
                rgb = COLOR_SENSOR.get_rgb()
                print(rgb)
                outfile.write(f'{rgb}\n')
                sleep(0.25)
    except KeyboardInterrupt:
        print("done")
        outfile.close()
        exit()

if __name__=='__main__':
    collect_data()


