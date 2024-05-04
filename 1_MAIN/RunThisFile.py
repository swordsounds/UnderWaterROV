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
  "mtr6": [0],
  "temp": [0],
}

def Compiler():
        while True:
            mtr.currentInput0.openWaitForAttachment(1000)
            mtr.currentInput1.openWaitForAttachment(1000)
            mtr.currentInput2.openWaitForAttachment(1000)
            mtr.currentInput3.openWaitForAttachment(1000)
            mtr.currentInput4.openWaitForAttachment(1000)
            mtr.currentInput5.openWaitForAttachment(1000)
            df = pd.DataFrame(data)
            data["time"].append(current_time)
            data["mtr1"].append(mtr.currentInput0.getCurrent())
            data["mtr2"].append(mtr.currentInput1.getCurrent())
            data["mtr3"].append(mtr.currentInput2.getCurrent())
            data["mtr4"].append(mtr.currentInput3.getCurrent())
            data["mtr5"].append(mtr.currentInput4.getCurrent())
            data["mtr6"].append(mtr.currentInput5.getCurrent())
            data["temp"].append(0)
            df.to_csv('data.csv', encoding='utf-8', index=False)
            return data

def data_file():
    Compiler()

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