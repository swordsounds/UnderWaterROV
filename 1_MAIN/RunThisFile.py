from multiprocessing import Process
import GUI as graph 
# import DataFile as data
import ControlsFile as ctrl
from datetime import datetime
import pandas as pd
import MotorsFile as mtr
now = datetime.now()

current_time = now.strftime("%H:%M:%S") 

data = {
  "time": [current_time],
  "mtr1": [0],
  "mtr2": [0],
  "mtr3": [0],
  "mtr4": [0],
  "mtr5": [0],
  "mtr6": [0]
}
df = pd.DataFrame(data)

df.to_csv('data.csv', encoding='utf-8', index=False)
def data_file():
    mtr.Compiler()

def control_file():
    ctrl.main()

def main():
    df = Process(target=data_file)
    df.start()
    cf = Process(target=control_file)
    cf.start()
    df.join()
    graph.main()


if __name__ == '__main__':
    main()