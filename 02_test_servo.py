import time
import sys
from Raspbot_Lib import Raspbot
sys.path.append('/home/pi/software/oled_yahboom/')
from yahboom_oled import *

bot = Raspbot()
print("Testing Servo Control...")

def set_servo_positions(s1, s2):
    bot.Ctrl_Servo(1, s1)
    bot.Ctrl_Servo(2, s2)
    
    return s1, s2

def task_pan():
    min = 5
    max = 175
    rate = 0.1
    speed = 2
    
    if not hasattr(task_pan, "last_time"):
        task_pan.last_time = time.time()
    if not hasattr(task_pan, "current_angle"):
        task_pan.current_angle = min
    if not hasattr(task_pan, "direction"):
        task_pan.direction = 1

    if time.time() - task_pan.last_time >= rate:
        task_pan.last_time = time.time()
        set_servo_positions(task_pan.current_angle, 25)
        task_pan.current_angle += speed * task_pan.direction
        if task_pan.current_angle >= max or task_pan.current_angle <= min:
            task_pan.direction *= -1
        
    
    time.sleep(.01)

def main():
    try:
        min = 5
        max = 175
        
        while True:
            task_pan()
                    
    except KeyboardInterrupt:
        print("Servo control test interrupted.")
    
    set_servo_positions(90, 25)
    time.sleep(1)

    
if __name__ == "__main__":
    main()
    del bot 