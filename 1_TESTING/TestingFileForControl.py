from pynput import keyboard
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import TestingFileForMotors as mtr

scroll_value = 100

def on_press(key):
    try:
        if key.char == 'w':
            mtr.motor_one(throttle=None)
        elif key.char == 's':
            mtr.motor_two()
    except Exception as e:
        print(f"Raised exception:{e}")

def on_release(key):
    if key.char == 'w':
        mtr.motor_one_close()
    elif key.char == 's':
        mtr.motor_two_close()
    elif key == keyboard.Key.esc:
        return False
    
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
    with KeyboardListener(on_press=on_press, 
                           on_release=on_release
                           ) as listener:
        with MouseListener(on_scroll=on_scroll) as listener:
            listener.join()
    listener.start()

if __name__ == "__main__":
    main()