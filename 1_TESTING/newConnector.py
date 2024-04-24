from multiprocessing import Process
import newGraph as graph 
import dataGen as data

def process():
    data.main()

def main():
    p = Process(target=process)
    p.start()
    graph.main()

if __name__ == '__main__':
    main()