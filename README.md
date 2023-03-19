# Final Project
> Software Lead: Antoine Phan

## File Structure
├── collect_colors.py
├── data
│   ├── color_data_blue.csv
│   ├── color_data_green.csv
│   ├── color_data_orange.csv
│   ├── color_data_purple.csv
│   ├── color_data_red.csv
│   ├── color_data_white.csv
│   └── color_data_yellow.csv
├── detect_color.py
├── Diary.md
├── docs
│   ├── DPM Practical Design Tutorial.pdf
│   ├── W2023 Design Week Information (highlighted).pdf
│   ├── W2023 Design Week Information.pdf
│   └── W2023 Final Project Client Needs Description.pdf
├── LICENSE
├── __pycache__
│   └── detect_color.cpython-310.pyc
├── README.md
├── test_color_detection.py
├── utils
│   ├── brick.py
│   ├── dummy.py
│   ├── filters.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__
│   │   ├── brick.cpython-310.pyc
│   │   ├── brick.cpython-39.pyc
│   │   ├── dummy.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   └── sound.cpython-39.pyc
│   ├── remote.py
│   ├── rmi.py
│   ├── sound.py
│   └── telemetry.py
├── WADDLE.py
└── wheels.py

```
|- README.md  	# Documenting the test
|- Diary.md	# Documenting the designing process
|- [utils/](utils/) 	# The API for the BrickPi
|- [wheels.py](wheels.py) 	# The wheel of the system
|- [collect_colors](collect_colors.py) # Collecting color data and put them in data/
```

|- [data/](data/)	# Contains colors' data
|------------|-----------------|----------------|
| Motors     | 	Wheels	       | Vehicle,Loader |
| Sensors    |  ColorDetector  | Navigator      |
| Button     |  Ready, StopButton | Ready, StopButton|
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
- Testing `detect_color.py`
	-  Test 1: Using data from the training data
		- Result: Using Ryan's algorithm vs Antoine's algorithm

		| Input Source | RGB Value | Ryan's Algo | Antoine's Algo|
		|---------------|-----------|---------|-------|
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

		- Test 2: More accurate purple, red; blue is better at close range

		| Input Source | RGB Value | Ryan's Algo | Antoine's |
		|---------------|-----------|---------|-------|
		|blue.csv       | [17, 33, 48]  | blue  | blue |
		|blue.csv       | [8, 17, 30]   | orange        | None |
		|green.csv      | [22, 101, 32]         | green         | green |
		|green.csv      | [17, 81, 24]  | green         | green |
		|red.csv        | [215, 27, 26]         | orange        | None |
		|red.csv        | [76, 12, 13]  | orange        | None |
		|yellow.csv     | [284, 187, 22]        | None  | None |
		|yellow.csv     | [76, 60, 9]   | yellow        | None |
		|orange.csv     | [173, 47, 33]         | orange        | orange |
		|orange.csv     | [76, 21, 20]  | orange        | orange |
		|purple.csv     | [20, 15, 23]  | orange        | None |
		|purple.csv     | [74, 49, 75]  | None  | None |






