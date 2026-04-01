import time
import sys
from Raspbot_Lib import Raspbot
sys.path.append('/home/pi/software/oled_yahboom/')
from yahboom_oled import *

bot = Raspbot()
print("Testing OLED Display...")

oled = Yahboom_OLED(debug=False)

def get_distance():
    diss_H =bot.read_data_array(0x1b,1)[0]
    diss_L =bot.read_data_array(0x1a,1)[0]
    distance = (diss_H << 8) + diss_L
    return distance

def main():
    try:
        bot.Ctrl_Ulatist_Switch(1)
        oled.init_oled_process()
        
        while True:

            distance = get_distance()
            
            oled.clear()
            dist_str = f"Distance: {distance} mm"
            oled.add_line(dist_str)
            oled.refresh()
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        bot.Ctrl_Ulatist_Switch(0)
        # Uncomment to start the default OLED display process again
        # os.system("python3 /home/pi/software/oled_yahboom/yahboom_oled.py &")
        print("Ultrasonic sensor turned off.")

if __name__ == "__main__":
    main()
    bot.Ctrl_Ulatist_Switch(0)
    del bot