# Final Project
> Software Lead: Antoine Phan

## Software Architecture
| Unit level | Component Level | System Level 	|
|------------|-----------------|----------------|
| Motors     | 	Wheels	       | Vehicle,Loader |
| Sensors    |  ColorDetector  | Navigator      |
| Button     |  Ready, StopButton | Ready, StopButton|

## Procedure
### Unit implementation/testing
- Testing `Motor.set_power(power)` for continuous movement
	- `power` is a number from -100 to 100
	- Positive `power` is for clockwise movement
	- Negative `power` is for counter-clockwise movement
	- Result: successful!

- Collecting data using the color sensor (CollectColor.py)
	- Using color sensor to obtain rgb value of a selected color
	- Write the colected data into `./data/color_data_[color]`, where `[color]` is the selected color
	- Data will be used for color detection

### Component implementation/testing
- Implementing `detect_color.py` to detect color
    - Implementing `Color` class to store:
      - Name of the color
      - Normalized rgb value of the color data
      - Standard deviation of the color data
    - Design choice: Using `Class` instead or normal data type for scalability
- Testing `detect_color.py`
	-  Test 1: Using data from the training data
		- Result: Using Ryan's algorithm vs Antoine's algorithm

| Training file | RGB value | Color detected  | 
|---------------|-----------|---------|-------|
| Input Source | RGB Value | Ryan's Algo | Antoine's |
|blue.csv 	| [17, 33, 48] 	| blue 	| blue |
|blue.csv 	| [8, 17, 30] 	| orange 	| None |
|green.csv 	| [22, 101, 32] 	| green 	| green |
|green.csv 	| [17, 81, 24] 	| green 	| green |
|red.csv 	| [215, 27, 26] 	| red 	| None |
|red.csv 	| [76, 12, 13] 	| orange 	| None |
|yellow.csv 	| [284, 187, 22] 	| None 	| None |
|yellow.csv 	| [76, 60, 9] 	| yellow 	| None |
|orange.csv 	| [173, 47, 33] 	| orange 	| orange |
|orange.csv 	| [76, 21, 20] 	| orange 	| orange |
|purple.csv 	| [20, 15, 23] 	| orange 	| None |
|purple.csv 	| [74, 49, 75] 	| None 	| None |






