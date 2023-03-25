#!/usr/bin/env python3

from Wheels import *

def go(power=50):
    run(RightWheel, power)
    run(LeftWheel, power)

def stop():
    stopMotor(RightWheel)
    stopMotor(LeftWheel)
    
"""
The method below turns the system base on its direction and time delay

@param direction: "left" or "right"
@param delay (s): the system will turn for a time delay in seconds
"""
def turn(direction: str, delay: float, debug=False):
    if debug:
        print(f'Vehicle will turn {direction} for {delay}')
    
    leftSpeed = LeftWheel.get_power()    
    rightSpeed = RightWheel.get_power()

    if direction == "right":
        RightWheel.set_power(-rightSpeed)
        sleep(delay)
        RightWheel.set_power(rightSpeed)
    elif direction == "left":
        LeftWheel.set_power(-leftSpeed)
        sleep(delay)
        LeftWheel.set_power(leftSpeed)

# main method to test things out
if __name__=='__main__':
    mode = input("Select testing mode: \n\t[1] Basic motions\n\t[2] Turning motions\n")
    try:
        sp = int(input("Speed (+: clockwise, -: counter-clockwise): "))
        if mode == "1":
            while True:
                # Could be replaced with go(sp)
                run(RightWheel, power=sp)
                run(LeftWheel, power=sp)
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
        else:
            print("Unrecognize mode")
    except KeyboardInterrupt:
        BP.reset_all()