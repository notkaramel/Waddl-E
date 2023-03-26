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

def test_LeverAndTray():
    print("TRAY: (using blind test results)")
    tray_dps = 300 # int(input("Tray DPS: ")) 
    tray_angle = 110
    retrieve = lambda slot: rollTray(tray_dps, 2, slot*tray_angle)
    
    lever_dps = 120
    lever_angle = 90
    swing = lambda angle : swingLever(lever_dps, 2, angle)
    
    retrieve(1)
    swing(-lever_angle)
    swing(lever_angle)
    retrieve(-1)

def test():
    try:
        test_mode = int(input("[1] swingLever test:\n[2] rollTray test:\n[3] Lever and Tray test\nTest mode: "))
        if test_mode == 1:
            test_swingLever()
        elif test_mode == 2:
            test_rollTray()
        elif test_mode == 3:
            test_LeverAndTray()
        else:
            print("Try again")
            test()
    except KeyboardInterrupt:
        print(f'Exiting')
        exit()

test()

