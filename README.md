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
```sh
├── collect_colors.py           # (COMPONENT) Collecting colors' data
├── data                        # Storing data of colors
│   ├── color_data_blue.csv
│   ├── color_data_green.csv
│   ├── color_data_orange.csv
│   ├── color_data_purple.csv
│   ├── color_data_red.csv
│   ├── color_data_white.csv
│   └── color_data_yellow.csv
├── detect_color.py             # (UNIT) Color detection algorithm
├── docs                        # Users' Requirement document
├── LICENSE                     # LICENSE of this FOSS project
├── README.md                   # The file you're reading.
├── test_color_detection.py     # (COMPONENT TEST) Test for the color detection
├── utils                       # API of the project, built by Ryan Au
│   ├── brick.py
│   ├── dummy.py
│   ├── remote.py
│   ├── sound.py
│   └── ...
├── WADDLE.py                   # (SYSTEM) The final system file
├── wheels.py                   # (COMPONENT) Controlling the wheels
└── vehicle.py					# (SUBSYSTEM + UNIT TEST) Controlling the vehicle
```

## System diagram
### Component level
- Define "Component": Down to the most basic piece of hardware
- Motor: testing of basic functions from the `utils.brick` API
- Color sensor: testing different modes, getting rgb values from the sensor
- Files:
	- `collect_colors.py`: collecting data of colors
	- `test_color_detection.py`: testing color detection algorithm
	- `detect_color.py`: color detection algorithm
	- `wheels.py`: controlling the wheels

### Unit level
#### Wheels
- Major design decisions:
	- The wheels will turn the system using spinning motion around itself, rather than pivotal rotation movement.
	- Tests will be implemented directly to the main method of the 

- List of functions (can be imported from `wheels.py`)

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
	- [ ] Turning movements (turn left, turn right)

#### Color Detection
- Major design decisions:
	- 
- List of functions (can be imported from `detect_color.py`
```python
# 
```
## Procedure
### Unit implementation/testing
- [x] Testing `Motor.set_power(power)` for continuous movement
	- `power` is a number from -100 to 100
	- Positive `power` is for clockwise movement
	- Negative `power` is for counter-clockwise movement
	- Result: successful!

- [x] Collecting data using the color sensor (CollectColor.py)
	- Using color sensor to obtain rgb value of a selected color
	- Write the colected data into `./data/color_data_[color]`, where `[color]` is the selected color
	- Data will be used for color detection
- [ ] Accurate color detection
	- Consider all possible parameters that would affect the result
		- Collected data: color name, mean, standard deviation
	- Detection algorithm: given the input data as `input_RGB`
		- TA Ryan's: normalize the input data, compare with Color's data to obtain standard distance (in 3D space)
			- Pros: accurate, able to differenciate the error of different detections
			- Cons: Require math knowledge on statistics. Made life too easy for us
		- Antoine's: verify if the input data is within range of mean +- standard deviation of the color
			- Pros: Intuitive, easy to read and understand
			- Cons: Not very accurate, could not differentciate error (for now)

### Component implementation/testing
- Implementing `detect_color.py` to detect color
    - Implementing `Color` class to store:
      - Name of the color
      - Normalized rgb value of the color data
      - Standard deviation of the color data
    - Design choice: Using `Class` instead or normal data type for scalability





