#!/usr/bin/env python3

from Unloading import swingLever, rollTray

def test_swingLever():
    dps = int(input("DPS: "))
    swingLever(dps=dps, delay=1, position=90)
    swingLever(dps, 1, position=-90) 

test_swingLever()
