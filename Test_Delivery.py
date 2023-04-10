#!/usr/bin/env python3

from Delivery import ZONE_COLORS, getSideColor, deliverCube, resetRack

if '__main__' == __name__:
    try:
        while True:
            sideColor = getSideColor()
            if (sideColor != 'white'):
                deliverCube(sideColor)
                print(f'Delivered {sideColor.capitalize()} cube!')
    except KeyboardInterrupt:
        resetRack()
        exit()