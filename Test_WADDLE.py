#!/usr/bin/env python3

from WADDLE import *

DEBUG = False

def mainTest():
    testMode = int(input("""
                         Input your desired test mode:
                         [1] Waddl-E goes normally (all features except ready button at start)
                         [2] Waddl-E goes back to loading bay
                         [3] Waddl-E delivers
                         """))
    if testMode == 1:
        WaddlEGoesNormally()
    
    elif testMode == 2:
        WaddleGoBackToLoadingBay()
    
    elif testMode == 3:
        WaddlEDelivers()
        
if __name__ == '__main__':
    try:
        chooseDebug = input("Debug Mode [Y/n]: ")
        if chooseDebug == 'Y' or chooseDebug == '':
            DEBUG = True
        while True:
            mainTest()
    except KeyboardInterrupt:
        WaddleReset()
        exit()