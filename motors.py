#!/usr/bin/python3

from utils.brick import Motor, BP
import time
import math

RED_MOTOR = Motor("A")
# ORANGE_MOTOR = Motor("D")


POWER_LIMIT = 80        # Power limit = 80% 
SPEED_LIMIT = 1500       # Speed limit = 720dps | MAX = 1560 dps

MOTOR_POLL_DELAY = 0.01


def init_motor(motor: Motor):
    try: 
        motor.reset_encoder()                      # Reset encoder to 0 value
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT) # Set power and speed limits
        motor.set_power(0)                         # Stop the motor as well
    except IOError as error:
        print(error)

def wait_for_motor(motor: Motor):
    "Function to block until motor completion"
    while math.isclose(motor.get_speed(), 0):    # Wait for motor to spin up   (start)
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):    # Wait for motor to spin down (stop)
        time.sleep(MOTOR_POLL_DELAY)

def rotate_RED_MOTOR(angle, speed):
    "Function to rotate in place by a user specified angle and speed"
    try:
        # Set speeds of motors
        RED_MOTOR.set_limits(POWER_LIMIT, speed)
        RED_MOTOR.set_dps(speed)
       
        RED_MOTOR.set_position(angle)   # Rotate L Wheel +ve
        time.sleep(0.25)


        RED_MOTOR.set_position(-angle)
        
        time.sleep(0.25)
        #wait_for_motor(RED_MOTOR)
        # sleep_for_motor(int(distance * DIST_TO_DEG), speed)
    except IOError as error:
        print(error)

# def rotate_ORANGE_MOTOR(angle, speed):
#     "Function to rotate in place by a user specified angle and speed"
#     try:
#         # Set speeds of motors
#         ORANGE_MOTOR.set_limits(POWER_LIMIT, speed)
#         ORANGE_MOTOR.set_dps(speed)
        
#         #ORANGE_MOTOR.set_position_relative(angle) # Rotate R Wheel -ve
#         ORANGE_MOTOR.set_position(angle)

#         wait_for_motor(ORANGE_MOTOR)

#         #ORANGE_MOTOR.set_position_relative(-angle) # Rotate R Wheel -ve
#         ORANGE_MOTOR.set_position(-angle)
#         time.sleep(0.01)
#         #wait_for_motor(ORANGE_MOTOR)
#         # sleep_for_motor(int(distance * DIST_TO_DEG), speed)
#     except IOError as error:
#         print(error)

if __name__=='__main__':
    try:
        print('TEST') # Banner
        init_motor(RED_MOTOR)       # Initialize L Motor
        # init_motor(ORANGE_MOTOR)      # Initialize R Motor

        # Prompt for drive loop
        while True:
            # rotate_ORANGE_MOTOR(45, 800)
            rotate_RED_MOTOR(45, 400)
            
            
    except KeyboardInterrupt: # Abort program using ^C (Ctrl+C)
        BP.reset_all()

    
