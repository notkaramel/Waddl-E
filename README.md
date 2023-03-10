# Final Project
> Software Lead: Antoine Phan

## Software Architecture
| Unit level | Component Level | System Level |
|------------|-----------------|--------------|
| Motors     | 	Wheels	       | The Vehicle  |
| Sensors    |  PathDetector   | Guide        |
| Button     |  ReadyButton    | ReadyButton  |

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

