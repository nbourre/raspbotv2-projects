# Raspbot Project

## Raspbot Class - Available Functions

The `Raspbot` class provides control over various hardware components of the Raspbot robot. Below is a detailed description of all available functions.

### Motor Control

#### `Ctrl_Car(motor_id, motor_dir, motor_speed)`
Controls a motor with specified direction and speed.
- **Parameters:**
  - `motor_id` (int): Identifier for the motor to control
  - `motor_dir` (int): Direction of rotation (0 = forward, 1 = backward)
  - `motor_speed` (int): Speed of the motor (0-255, clamped automatically)
- **Description:** Controls motor movement with separated direction and speed parameters. Speed values are automatically clamped between 0-255.

#### `Ctrl_Muto(motor_id, motor_speed)`
Controls a motor with speed and automatic direction determination.
- **Parameters:**
  - `motor_id` (int): Identifier for the motor to control
  - `motor_speed` (int): Speed value (-255 to 255)
    - Positive values: forward direction
    - Negative values: backward direction
- **Description:** Simplified motor control where direction is automatically determined based on speed sign. Speed range is -255 to 255, automatically clamped.

### Servo Control

#### `Ctrl_Servo(id, angle)`
Controls a servo motor to a specific angle.
- **Parameters:**
  - `id` (int): Identifier for the servo (values: 1, 2, etc.)
  - `angle` (int): Target angle in degrees (0-180)
    - Note: Servo ID 2 is limited to 0-110 degrees
- **Description:** Positions a servo to the specified angle. Angle values are automatically clamped to valid ranges (0-180, or 0-110 for servo ID 2).

### LED/WQ2812 RGB Strip Control

#### `Ctrl_WQ2812_ALL(state, color)`
Controls all LEDs in the WQ2812 RGB strip with on/off state and color.
- **Parameters:**
  - `state` (int): 0 = off, 1 = on
  - `color` (int): Color code (0-255 or custom color index)
- **Description:** Turns all LEDs on or off with a specified color. State is automatically clamped to 0 or 1.

#### `Ctrl_WQ2812_Alone(number, state, color)`
Controls a single LED in the WQ2812 RGB strip.
- **Parameters:**
  - `number` (int): LED position/number to control
  - `state` (int): 0 = off, 1 = on
  - `color` (int): Color code (0-255 or custom color index)
- **Description:** Controls an individual LED independently. Useful for selective lighting patterns.

#### `Ctrl_WQ2812_brightness_ALL(R, G, B)`
Controls the brightness of all LEDs using RGB values.
- **Parameters:**
  - `R` (int): Red component (0-255)
  - `G` (int): Green component (0-255)
  - `B` (int): Blue component (0-255)
- **Description:** Sets all LEDs to a specific color using RGB values. Values are automatically clamped to 0-255.

#### `Ctrl_WQ2812_brightness_Alone(number, R, G, B)`
Controls the brightness of a single LED using RGB values.
- **Parameters:**
  - `number` (int): LED position/number to control
  - `R` (int): Red component (0-255)
  - `G` (int): Green component (0-255)
  - `B` (int): Blue component (0-255)
- **Description:** Sets a specific LED to a color using RGB values. Values are automatically clamped to 0-255.

### IR Control

#### `Ctrl_IR_Switch(state)`
Controls the infrared remote control receiver.
- **Parameters:**
  - `state` (int): 0 = off, 1 = on
- **Description:** Enables or disables the IR receiver. State is automatically clamped to 0 or 1.

### Buzzer Control

#### `Ctrl_BEEP_Switch(state)`
Controls the buzzer/beeper.
- **Parameters:**
  - `state` (int): 0 = off, 1 = on
- **Description:** Turns the buzzer on or off. Useful for audio feedback or alerts. State is automatically clamped to 0 or 1.

### Ultrasonic Distance Control

#### `Ctrl_Ulatist_Switch(state)`
Controls the ultrasonic distance sensor.
- **Parameters:**
  - `state` (int): 0 = off, 1 = on
- **Description:** Enables or disables the ultrasonic distance measurement module. State is automatically clamped to 0 or 1.

## Sensor Reading Functions

#### `read_data_array(reg, len)`
Reads an array of bytes from a specified I2C register.
- **Parameters:**
  - `reg` (int): Register address to read from
  - `len` (int): Number of bytes to read
- **Returns:** List of bytes read from the register
- **Description:** Low-level I2C read function used to retrieve sensor data. Used internally by sensor functions and can be used directly for advanced applications.

#### `read_data_byte()`
Reads a single byte from the I2C device.
- **Returns:** Single byte value
- **Description:** Low-level I2C read function for reading a single byte.

## Usage Examples

### Basic Control Example

```python
from Raspbot_Lib import Raspbot
import time

# Initialize the robot
car = Raspbot()

# Move forward on motor 1 at speed 200
car.Ctrl_Car(1, 0, 200)

# Set LED to green
car.Ctrl_WQ2812_brightness_ALL(0, 255, 0)

# Beep the buzzer
car.Ctrl_BEEP_Switch(1)
time.sleep(0.5)
car.Ctrl_BEEP_Switch(0)

# Move servo to 90 degrees
car.Ctrl_Servo(1, 90)

# Stop motor
car.Ctrl_Car(1, 0, 0)

# Turn off LED
car.Ctrl_WQ2812_brightness_ALL(0, 0, 0)
```

### Ultrasonic Distance Sensor Example

```python
from Raspbot_Lib import Raspbot
import time

# Initialize the robot
car = Raspbot()

# Enable the ultrasonic sensor
car.Ctrl_Ulatist_Switch(1)
time.sleep(1)  # Wait for sensor to stabilize

# Read distance data from the sensor
# Distance is stored in two 8-bit registers that need to be combined
distance_high_byte = car.read_data_array(0x1b, 1)[0]  # High byte from register 0x1b
distance_low_byte = car.read_data_array(0x1a, 1)[0]   # Low byte from register 0x1a

# Combine bytes to get full distance value
distance_mm = (distance_high_byte << 8) | distance_low_byte

print(f"Distance: {distance_mm}mm")

# Disable the ultrasonic sensor
car.Ctrl_Ulatist_Switch(0)
```

### Reading Multiple Sensor Values in a Loop

```python
from Raspbot_Lib import Raspbot
import time

# Initialize the robot
car = Raspbot()

# Enable the ultrasonic sensor
car.Ctrl_Ulatist_Switch(1)
time.sleep(1)

# Read distance values continuously
for i in range(10):
    distance_high = car.read_data_array(0x1b, 1)[0]
    distance_low = car.read_data_array(0x1a, 1)[0]
    distance = (distance_high << 8) | distance_low
    
    print(f"Reading {i+1}: {distance}mm")
    time.sleep(0.5)

# Disable the sensor
car.Ctrl_Ulatist_Switch(0)
```

## Notes

- I2C communication errors are caught and printed to console, allowing the robot to continue operating gracefully
- Speed and angle values are automatically clamped to valid ranges
- All control functions use I2C protocol for communication with the robot
