from multiprocessing import Process
import GUI as graph 
import DataFile as data
import ControlsFile as ctrl

def data_file():
    data.main()
def control_file():
    ctrl.main()

def main():
    df = Process(target=data_file)
    df.start()
    cf = Process(target=control_file)
    cf.start()
    graph.main()


if __name__ == '__main__':
    main()