import time
from Raspbot_Lib import Raspbot

car = Raspbot()

print("Hello, Raspbot!")

# Light up all LEDs green
car.Ctrl_WQ2812_brightness_ALL(0, 255, 0)

# Beep the buzzer
car.Ctrl_BEEP_Switch(1)
time.sleep(0.5)
car.Ctrl_BEEP_Switch(0)

time.sleep(1)

# Turn off LEDs
car.Ctrl_WQ2812_brightness_ALL(0, 0, 0)

print("Done!")

del car