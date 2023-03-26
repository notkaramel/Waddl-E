#!/usr/bin/env python3

from Unloading import swingLever, rollTray

def test_swingLever():
    dps = int(input("DPS: "))
    swingLever(dps=dps, delay=2, position=-90)
    swingLever(dps, 2, position=90) 

def test_rollTray():
    dps = int(input("DPS: "))
    delay = 2
    rollTray(dps=dps, delay=delay, position=45)
    rollTray(dps, delay, position=-45)

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

