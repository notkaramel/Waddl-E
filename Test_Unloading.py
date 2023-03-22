#!/usr/bin/env python3

from Unloading import swingLever, rollTray

# 120 DPS for swingLever is good 
# 300 DPS, 110 angle for rollTray is good

def test_swingLever():
    dps = int(input("DPS: "))
    swingLever(dps=dps, delay=2, position=-90)
    swingLever(dps, 2, position=90) 

def test_rollTray():
    dps = int(input("DPS: "))
    angle = int(input("Angle: "))
    delay = 2
    rollTray(dps=dps, delay=delay, position=angle)
    rollTray(dps, delay, position=-angle)

def test():
    try:
        test_mode = int(input("[1] swingLever test:\n[2] rollTray test:\nTest mode: "))
        if test_mode == 1:
            test_swingLever()
        elif test_mode == 2:
            test_rollTray()
        else:
            print("Try again")
            test()
    except KeyboardInterrupt:
        print(f'Exiting')
        exit()

test()

