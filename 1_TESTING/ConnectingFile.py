# import TestingFileGUI as gui
import TestingFileGraph as graph
import TestingFileForControl as control_test
import threading

def main():
    threading.Thread(target=process).start()
    # gui.main()
    graph.main()

def process():
    control_test.main()

if  __name__ == '__main__':
    main()