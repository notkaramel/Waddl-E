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
        WaddleGoNormally(DEBUG)
    
    elif testMode == 2:
        WaddleGoBackToLoadingBay(DEBUG)
    
    elif testMode == 3:
        WaddleDeliver(DEBUG)
        
if __name__ == '__main__':
    try:
        chooseDebug = input("Debug Mode [Y/n]: ")
        if chooseDebug == 'Y' or chooseDebug == '\n':
            DEBUG = True
        while True:
            mainTest()
    except KeyboardInterrupt:
        reset()
        exit()