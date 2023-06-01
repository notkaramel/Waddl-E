# Final Project
Software Lead: Antoine Phan
Consulting for software: Adam Corbier

## Wirings
### Sensors
- Front color sensor: Port S3
- Side color sensor: Port S4

### Motors
- Left wheel: Port D
- Right wheel: Port A
- Cube rack/holder: Port B
- Lever: Port C

## File Structure
```shell
# System level
├── WADDLE.py
├── subsystem
│	# subsystem level
│   ├── components
│   │   # component level
│   ├── Delivery.py
│   ├── Vehicle.py
│   │   │ # unit level
│   │   ├── utils # utility API
│   │   │   ├── brick.py
│   │   │   ├── ...
│   │   ├── CollectColors.py
│   │   ├── ColorDetection.py
│   │   ├── Wheels.py
│   │   ├── Button.py
└───────└── Unloading.py
```

## System breakdown
### A. System level: ***WADDLE***
- The final system that will be run on the robot

### B. Subsystem level
#### B.1. Vehicle
- In charge of the movement of the robot
#### B.2. Delivery
- In charge of the delivery of the cubes to the designated area on the map

### C. Component level
#### C.1. Wheels
- The wheels will turn the system using spinning motion around itself, rather than pivotal rotation movement.

- List of functions (can be imported from `Wheels.py`)

```python
# Runs a motor at a power level (-100 to 100). Default power level is 50 [%]
run(motor: Motor, power:int)

# Make both wheels go, given an input power level. This is like a wrapper function of run(). Default power level is 50[%]
go(power:int)

# Stop a motor from running, effectively setting its power to 0
stop(motor: Motor)

# Rotate the system for a duration of time
# The angle of rotation is relative to the delay time and current power of motor
# Direction must be "left" or "right" string value, excluding the double quotes. Delay is a floating point number.
turn(direction: str, delay:float)
```
- Testing the wheels:
	- [x] Basic movements (forward, backward, standstill)
	- [x] Turning movements (turn left, turn right)

#### C.2. Color Detection
- Files: 
  - `ColorDetection.py`: color detection algorithm
- Component testings
	- `Test_ColorDetection.py`: testing color detection algorithm

- List of functions (can be imported from `ColorDetection.py`)
```python
# Color class/object
Color()
# attributes: name, meanRGB, stdevRGB

# Given a list of RGB values (and a list of wanted colors as Color objects), return the color that is closest to the input RGB values
detects_RGB(input_RGB:list, availableColors:list[Color])

# Sensors
FRONT_SENSOR, SIDE_SENSOR
```
#### C.3. Unloading
- Implementation of the unloading mechanism

### D. Unit level
- Define "Unit": Down to the most basic piece of hardware (e.g. motor, sensor, button)
- Motor: testing of basic functions from the `utils.brick` API
  - Testing `Motor.set_power(power)` for continuous movement
	- `power` is a number from -100 to 100
	- Positive `power` is for clockwise movement
	- Negative `power` is for counter-clockwise movement
- Color sensor: testing different modes, getting rgb values from the sensor
- Unit files:
	- `CollectColors.py`: 
    	- Collecting data using the color sensor
    	- Using color sensor to obtain rgb value of a selected color
    	- Write the colected data into `./data/color_data_[color]`, where `[color]` is the selected color
    	- Data will be used for color detection
	- `Wheels.py`: controlling the wheels


















