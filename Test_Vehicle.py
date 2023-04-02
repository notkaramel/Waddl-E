#!/usr/bin/env python3

from Button import STOP_BUTTON
from Vehicle import *

def GoByColor():
    print(f'Waddl-E is running...')
    old_color = None
    while True:
        if STOP_BUTTON.is_pressed():
            print("Emergency stop pressed!")
            exit()
        front_rgb = FRONT_SENSOR.get_rgb()
        frontColor = detects_RGB(front_rgb, MAP_COLORS)
        print(f'FR: {front_rgb} \t{frontColor}\t OLD: {old_color}')
        
        if frontColor == 'None':
            print(f'None detected')
            goStraight(power=18)
            sleep(0.1)
        elif frontColor == 'white':
            goStraight(power=42)
            sleep(0.1)
        elif frontColor == "red":
            slightTurn("left", 0.4)
        elif frontColor == "blue":
            slightTurn("right", 0.4)
        elif frontColor == "green": # Delivering
            pause(pauseDelay=1, afterPauseDelay=0.2) 
        elif frontColor == "yellow": # Reloading
            turnAround()

        if frontColor != None:
            old_color = frontColor 


# main method to test things out
if __name__=='__main__':
    mode = int(input("\t[1] Basic motions\n\t[2] Turning motions\n\t[3] Map Navigation\nSelect testing mode [1/2/3]: "))

    try:
        if mode == 1:
            sp = int(input("Speed (+: clockwise, -: counter-clockwise): "))
            while True:
                # Could be replaced with go(sp)
                run(RIGHT_WHEEL, power=sp)
                run(LEFT_WHEEL, power=sp)
                sp = int(input("New value for speed: "))
        elif mode == 2:
            sp = int(input("Speed (+: clockwise, -: counter-clockwise): "))
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

