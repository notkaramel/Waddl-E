#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

# Add your imports here, if any
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor
import time

COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

# complete this based on your hardware setup
COLOR_SENSOR = EV3ColorSensor(2)
TOUCH_SENSOR = TouchSensor(1)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.


def collect_color_sensor_data():
    print("Start collecting data")
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "w")
        while True:
            # rgb_data = COLOR_SENSOR.get_rgb()
            # print("Touch to record data")
            if TOUCH_SENSOR.is_pressed():
                rgb_data = COLOR_SENSOR.get_rgb()
                print("Touch sensor is pressed\n")
                if ((rgb_data is not None) and (rgb_data != [0, 0, 0]) and (rgb_data != [None, None, None])):
                    print(rgb_data)
                    output_file.write(f"{rgb_data}\n")
                time.sleep(1)

    except BaseException: 
        pass
    finally:
        print("DONE!")
        output_file.close()
        exit()
    
if __name__ == "__main__":
    collect_color_sensor_data()
