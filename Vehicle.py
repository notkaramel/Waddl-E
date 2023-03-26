#!/usr/bin/env python3

from Wheels import RIGHT_WHEEL, LEFT_WHEEL, run, stopMotor
from ColorDetection import FRONT_SENSOR, detects_RGB, Color
from time import sleep


def go(power=50):
    run(RIGHT_WHEEL, power)
    run(LEFT_WHEEL, power)

def stop():
    stopMotor(RIGHT_WHEEL)
    stopMotor(LEFT_WHEEL)
    
"""
The method below turns the system base on its direction and time delay

@param direction: "left" or "right"
@param delay (s): the system will turn for a time delay in seconds
"""
def turn(direction: str, delay: float, debug=False):
    if debug:
        print(f'Vehicle will turn {direction} for {delay}')
    
    leftSpeed = LEFT_WHEEL.get_power()    
    rightSpeed = RIGHT_WHEEL.get_power()

    if direction == "right":
        RIGHT_WHEEL.set_power(-rightSpeed)
        sleep(delay)
        RIGHT_WHEEL.set_power(rightSpeed)
    elif direction == "left":
        LEFT_WHEEL.set_power(-leftSpeed)
        sleep(delay)
        LEFT_WHEEL.set_power(leftSpeed)

MAP_COLORS_STR = ['white_map', 'blue_map', 'red_map', 'green_map', 'yellow_map']
MAP_COLORS = [Color(c) for c in MAP_COLORS_STR]

def GoByColor():
    print(f'Waddl-E is running...')
    old_color = None
    while True:
        front_rgb = FRONT_SENSOR.get_rgb()
        frontColor = detects_RGB(front_rgb, MAP_COLORS)
        if (frontColor != old_color):
            sleep(0.25)
        elif frontColor == "white":
            go()
            sleep(0.5)
        elif frontColor == "blue":
            slightRight(0.5)
        elif frontColor == "red":
            slightLeft(0.5)
        elif frontColor == "green":
            stop()
        else:
            print(f'None detected: {frontColor}')
            sleep(0.25)
"""
When Waddl-E sees WHITE, it goes.
"""
def goStraight(speed=30): # speed in %
    print(f'Going straight at {speed}% speed.')
    go(speed)

"""
When Waddl-E sees BLUE, it turns slightly to the right.
"""
def slightRight(delay:float):
    print(f'Turning slightly right (delay={delay}))')
    turn("right", delay)

"""
When Waddl-E sees RED, it turns slightly to the left.
"""
def slightLeft(delay):
    print(f'Turning slightly left (delay={delay}))')
    turn("left", delay)


# main method to test things out
if __name__=='__main__':
    mode = input("\t[1] Basic motions\n\t[2] Turning motions\n\t[3] Map Navigation mode\nSelect testing mode [1/2/3]: ")

    try:
        sp = int(input("Speed (+: clockwise, -: counter-clockwise): "))
        if mode == "1":
            while True:
                # Could be replaced with go(sp)
                run(RIGHT_WHEEL, power=sp)
                run(LEFT_WHEEL, power=sp)
                sp = int(input("New value for speed: "))
        elif mode == "2":
            timeDelay = float(input("Delay time (s): "))
            direction = input(f'Direction ("left" or "right"): ')
            go(sp)
            sleep(2)
            turn(direction, timeDelay)
            go(0)
            sleep(1)

            go(sp)
            sleep(2)
            
            go(0)
            sleep(1)
            print("returning...")
            go(-sp)
            sleep(2)
            turn(direction, timeDelay)
            go(-sp)
            sleep(2)
        elif mode == 3:
            GoByColor()
        else:
            print("Unrecognize mode")
    except KeyboardInterrupt:
        exit()