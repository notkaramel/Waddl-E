#!/usr/bin/env python3

from Unloading import swingLever, rollTray

# 120 DPS for swingLever is good 
# 300 DPS, 110 angle for rollTray is good

def test_swingLever():
    dps = int(input("DPS: "))
    delay = float(input("Delay: "))
    swingLever(dps=dps, delay=delay, angle=45)
    swingLever(dps, 1, angle=-45) 

def test_rollTray():
    dps = int(input("DPS: "))
    angle = int(input("Angle: "))
    delay = 2
    rollTray(dps=dps, delay=delay, angle=angle)
    rollTray(dps, delay, angle=-angle)

def test_LeverAndTray():
    print("TRAY: (using blind test results)")
    tray_dps = 400 # int(input("Tray DPS: ")) 
    tray_angle = 120
    retrieve = lambda slot: rollTray(tray_dps, abs(slot//2), slot*tray_angle)
    
    lever_dps = 600
    lever_angle = 45
    swing = lambda angle : swingLever(lever_dps, 0.3, angle)
    
    slot = int(input("Slots to roll (+/-<int>): "))
    retrieve(slot)
    swing(lever_angle)
    swing(-lever_angle)
    retrieve(-slot)

def test():
    try:
        while True:
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

