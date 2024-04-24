import TestingFileGUI as gui
# import TestingFileGraph as graph
import TestingFileForControl as control_test
import multiprocessing as mp

def main():
    control_test.main()
    mp.set_start_method('spawn')
    p = mp.Process(target=control)
    p.start()
    p.join()
    p.terminate()
    p.close()
    # graph.main()

def control():
    gui.main()

if  __name__ == '__main__':
    main()