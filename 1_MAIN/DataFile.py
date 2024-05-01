import csv
import random
import time
from datetime import datetime
# import MotorsFile as mtr
import provingGrounds as pv
from Phidget22.Phidget import *
from Phidget22.Devices.CurrentInput import *


now = datetime.now()

current_time = now.strftime("%H:%M:%S") 

time_now = 0
mtr_1 = 0
mtr_2 = 0
mtr_3 = 0
mtr_4 = 0
mtr_5 = 0
mtr_6 = 0
temp = 0
dept = 0

fieldnames = ['time_now', 'mtr_1', 'mtr_2', 'mtr_3', 'mtr_4', 'mtr_5', 'mtr_6', 'temp', 'dept']

with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

def main():

    global time_now, mtr_1,mtr_2, mtr_3, mtr_4, mtr_5, mtr_6, temp, dept

    while True:
       
        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S") 
            info = {
                "time_now": time_now,
                "mtr_1": mtr_1,
                "mtr_2": mtr_2,
                "mtr_3": mtr_3,
                "mtr_4": mtr_4,
                "mtr_5": mtr_5,
                "mtr_6": mtr_6,
                "temp": temp,
                "dept": dept
            }


            csv_writer.writerow(info)

            time_now = current_time
            pv.main()
            mtr_1 = pv.onCurrentChange0(self=pv.onCurrentChange0, current=pv.current)
            # mtr_2 = mtr.getCurrentChange0()
            # mtr_3 = mtr.getCurrentChange0()
            # mtr_4 = mtr.getCurrentChange0()
            # mtr_5 = mtr.getCurrentChange0()
            # mtr_6 = mtr.getCurrentChange0()
            # temp = mtr.getCurrentChange0()
            # dept = mtr.getCurrentChange0()

        time.sleep(1)
    
if __name__ == '__main__':
    main()