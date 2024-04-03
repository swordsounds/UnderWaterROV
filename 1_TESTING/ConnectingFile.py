import TestingFileGUI as gui
import TestingFileForControl as control_test
import threading

running = False

def main():
    global running
    if not running:
        running = True
        threading.Thread(target=process).start()
    gui.main()

def process():
    control_test.main()

if  __name__ == '__main__':
    main()