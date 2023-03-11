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
- 