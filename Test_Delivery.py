#!/usr/bin/env python3

from Delivery import ZONE_COLORS, getSideColor, deliverCube

if '__main__' == __name__:
    while True:
        sideColor = getSideColor()
        deliverCube(sideColor)
        print(f'Delivered {sideColor.capitalize()} cube!')