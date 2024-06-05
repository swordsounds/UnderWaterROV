from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import MotorsFile as mtr
import ServosFile as rc

angle = 0
scroll_value = 100
multiplier = 1

def on_press(key):
    global angle
    try:
        if key == keyboard.Key.shift:
            #  mtr.motor_four(throttle=1 * multiplier)
             mtr.motor_three(throttle=-1 * multiplier)
        elif key.char == 'f':
            mtr.motor_three(throttle=1 * multiplier)
            # mtr.motor_two(throttle=-1 * multiplier)
        elif key.char == 'q':
            mtr.motor_five(throttle=1 * multiplier)
            mtr.motor_six(throttle=-1 * multiplier)
            mtr.motor_one(throttle=1 * multiplier)
            mtr.motor_four(throttle=-1 * multiplier)
        elif key.char == 'e':
            mtr.motor_five(throttle=-1 * multiplier)
            mtr.motor_six(throttle=1 * multiplier)
            mtr.motor_one(throttle=-1 * multiplier)
            mtr.motor_four(throttle=1 * multiplier)
        elif key.char == 'w':
            mtr.motor_six(throttle=1 * multiplier)
            mtr.motor_five(throttle=1 * multiplier)
            mtr.motor_one(throttle=1 * multiplier)
            mtr.motor_four(throttle=1 * multiplier)
        elif key.char == 's':
            mtr.motor_six(throttle=-1 * multiplier)
            mtr.motor_five(throttle=-1 * multiplier)
            mtr.motor_one(throttle=-1 * multiplier)
            mtr.motor_four(throttle=-1 * multiplier)
        elif key.char == 'd':
            mtr.motor_one(throttle=1 * multiplier)
            mtr.motor_four(throttle=-1 * multiplier)
            mtr.motor_five(throttle=-1 * multiplier)
            mtr.motor_six(throttle=1 * multiplier)
        elif key.char == 'a':
            mtr.motor_one(throttle=-1 * multiplier)
            mtr.motor_four(throttle=1 * multiplier)
            mtr.motor_five(throttle=1 * multiplier)
            mtr.motor_six(throttle=-1 * multiplier)
        elif key.char == 'r':
            rc.servo1(180)
        elif key.char == 'g':
            rc.servo1(63)
        # elif key.char == '1':
        #     angle = 180
        #     rc.servo2(angle)
        #     return angle
        # elif key.char == '2':
        #     angle = 0
        #     rc.servo2(0)
        #     return angle
    except Exception as e:
        print(f"Raised exception:{e}")

def on_release(key):
    
        if key == keyboard.Key.shift:
            # mtr.motor_four_close()
            mtr.motor_three_close()
            # mtr.motor_two_close()
        elif key.char == 'f':
            mtr.motor_three_close()
            # mtr.motor_two_close()
        elif key.char == 'q':
            mtr.motor_five_close()
            mtr.motor_six_close()
            mtr.motor_one_close()
            mtr.motor_four_close()
        elif key.char == 'e':
            mtr.motor_five_close()
            mtr.motor_six_close()
            mtr.motor_one_close()
            mtr.motor_four_close()
        elif key.char == 'w':
            mtr.motor_five_close()
            mtr.motor_six_close()
            mtr.motor_one_close()
            mtr.motor_four_close()
        elif key.char == 's':
            mtr.motor_five_close()
            mtr.motor_six_close()
            mtr.motor_one_close()
            mtr.motor_four_close()
        elif key.char == 'd':
            mtr.motor_one_close()
            mtr.motor_four_close()
            mtr.motor_five_close()
            mtr.motor_six_close()
        elif key.char == 'a':
            mtr.motor_one_close()
            mtr.motor_four_close()
            mtr.motor_five_close()
            mtr.motor_six_close()
        elif key.char == 'r':
            rc.servo1_close()
        elif key.char == 'g':
            rc.servo1_close()
        # elif key.char == '1':
        #     rc.servo2_close()
        # elif key.char == '2':
        #     rc.servo2_close()
        elif key == keyboard.Key.esc:
            return False
    
    
def on_scroll(x, y, dx, dy):
    global scroll_value
    global multiplier
    scroll_value += dy * 5
    if -100 <= scroll_value <= 100:
        print(multiplier)
        multiplier = round(scroll_value * 0.01, 2)
        return multiplier
    elif scroll_value <= 0:
        scroll_value = 0
    elif scroll_value >= 100:
        scroll_value = 100

# def on_click(x, y, button, pressed):
#     global angle
#     if button == mouse.Button.left:
#          rc.servo1(63)
#     rc.servo1_close()
        


def main():
    listenerKeyboard = KeyboardListener(on_press=on_press, on_release=on_release)
    listenerMouse = MouseListener(on_scroll=on_scroll)
    listenerKeyboard.start()
    listenerMouse.start()
    listenerKeyboard.join()
    listenerMouse.join()
    

if __name__ == "__main__":
     main()