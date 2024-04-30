from pynput import keyboard
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import TestingFileForMotors as mtr


scroll_value = 100

def on_press(key):
    try:
        if key.char == 'w':
             mtr.motor_four(throttle=scroll_value)
        elif key.char == 's':
            mtr.motor_two(throttle=scroll_value)
        elif key.char == 'a':
            mtr.motor_one(throttle=scroll_value)
            mtr.motor_three(throttle=scroll_value)
            mtr.motor_five(throttle=scroll_value)
            mtr.motor_six(throttle=scroll_value)
        elif key.char == 'd':
            mtr.motor_one(throttle=-scroll_value)
            mtr.motor_three(throttle=-scroll_value)
            mtr.motor_five(throttle=-scroll_value)
            mtr.motor_six(throttle=-scroll_value)
    except Exception as e:
        print(f"Raised exception:{e}")

def on_release(key):
    if key.char == 'w':
        mtr.motor_one_close()
    elif key.char == 's':
        mtr.motor_two_close()
    elif key == keyboard.Key.esc:
        return False
    elif key.char == 'a':
        mtr.motor_three_close()
        mtr.motor_four_close()
        mtr.motor_five_close()
        mtr.motor_six_close()
    elif key.char == 'd':
        mtr.motor_three_close()
        mtr.motor_four_close()
        mtr.motor_five_close()
        mtr.motor_six_close()
    
def on_scroll(x, y, dx, dy):
    global scroll_value
    scroll_value += dy * 5
    if -100 <= scroll_value <= 100:
        mtr.motor_one(round(scroll_value * 0.01, 2))
    elif scroll_value <= -100:
        scroll_value = -100
    elif scroll_value >= 100:
        scroll_value = 100



def main():
    listenerKeyboard = KeyboardListener(on_press=on_press, on_release=on_release)
    listenerMouse = MouseListener(on_scroll=on_scroll)
    listenerKeyboard.start()
    listenerMouse.start()

if __name__ == "__main__":
    main()