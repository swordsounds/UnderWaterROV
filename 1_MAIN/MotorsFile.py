from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.VoltageRatioInput import *
from multiprocessing import Process
import csv
import pandas as pd
from datetime import datetime
import time

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()
dcMotor2 = DCMotor()
dcMotor3 = DCMotor()
dcMotor4 = DCMotor()
dcMotor5 = DCMotor()
#---CHANGE THE SERIAL NUMBERS BETWEEN COMMENTS----
dcMotor0.setDeviceSerialNumber(487701)
dcMotor0.setChannel(0)
dcMotor1.setDeviceSerialNumber(487701)
dcMotor1.setChannel(1)

dcMotor2.setDeviceSerialNumber(100376)
dcMotor2.setChannel(0)
dcMotor3.setDeviceSerialNumber(100376)
dcMotor3.setChannel(1)

dcMotor4.setDeviceSerialNumber(487794)
dcMotor4.setChannel(0)
dcMotor5.setDeviceSerialNumber(487794)
dcMotor5.setChannel(1)
#-----------------------------------
voltageInput0 = VoltageInput()
voltageRatioInput1 = VoltageRatioInput()

currentInput0 = CurrentInput()
currentInput1 = CurrentInput()
currentInput2 = CurrentInput()
currentInput3 = CurrentInput()
currentInput4 = CurrentInput()
currentInput5 = CurrentInput()
currentInput6 = CurrentInput()

currentInput0.setDeviceSerialNumber(487701)
currentInput0.setChannel(0)
currentInput1.setDeviceSerialNumber(487701)
currentInput1.setChannel(1)

currentInput2.setDeviceSerialNumber(100376)
currentInput2.setChannel(0)
currentInput3.setDeviceSerialNumber(100376)
currentInput3.setChannel(1)

currentInput4.setDeviceSerialNumber(487794)
currentInput4.setChannel(0)
currentInput5.setDeviceSerialNumber(487794)
currentInput5.setChannel(1)


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
	df = pd.DataFrame(data)
	currentInput0.openWaitForAttachment(1000)
	currentInput1.openWaitForAttachment(1000)
	currentInput2.openWaitForAttachment(1000)
	currentInput3.openWaitForAttachment(1000)
	currentInput4.openWaitForAttachment(1000)
	currentInput5.openWaitForAttachment(1000)
	data["time"].append(current_time)
	data["mtr1"].append(currentInput0.getCurrent())
	data["mtr2"].append(currentInput1.getCurrent())
	data["mtr3"].append(currentInput2.getCurrent())
	data["mtr4"].append(currentInput3.getCurrent())
	data["mtr5"].append(currentInput4.getCurrent())
	data["mtr6"].append(currentInput5.getCurrent())
	data["temp"].append(0)
	df.to_csv('data.csv', encoding='utf-8', index=False)


def motor_one(throttle):
	if throttle == None:
		throttle = 1
	dcMotor0.openWaitForAttachment(1000)
	dcMotor0.setAcceleration(19.4)
	dcMotor0.setTargetVelocity(throttle)
	currentInput0.openWaitForAttachment(1000)
	


def motor_two(throttle):
	if throttle == None:
		throttle = 1
	dcMotor1.openWaitForAttachment(1000)
	dcMotor1.setAcceleration(19.4)
	dcMotor1.setTargetVelocity(throttle)

	currentInput1.openWaitForAttachment(1000)

def motor_three(throttle):
	if throttle == None:
		throttle = 1
	dcMotor2.openWaitForAttachment(1000)
	dcMotor2.setAcceleration(19.4)
	dcMotor2.setTargetVelocity(throttle)

	# currentInput2.openWaitForAttachment(1000)
	# currentInput2.setOnCurrentChangeHandler(onCurrentChange2)
def motor_four(throttle):
	if throttle == None:
		throttle = 1
	dcMotor3.openWaitForAttachment(1000)
	dcMotor3.setAcceleration(19.4)
	dcMotor3.setTargetVelocity(throttle)

	# currentInput3.openWaitForAttachment(1000)
	# currentInput3.setOnCurrentChangeHandler(onCurrentChange3)
def motor_five(throttle):
	if throttle == None:
		throttle = 1
	dcMotor4.openWaitForAttachment(1000)
	dcMotor4.setAcceleration(19.4)
	dcMotor4.setTargetVelocity(throttle)

	# currentInput4.openWaitForAttachment(1000)
	# currentInput4.setOnCurrentChangeHandler(onCurrentChange4)
def motor_six(throttle):
	if throttle == None:
		throttle = 1
	dcMotor5.openWaitForAttachment(1000)
	dcMotor5.setAcceleration(19.4)
	dcMotor5.setTargetVelocity(throttle)

	# currentInput5.openWaitForAttachment(1000)
	# currentInput5.setOnCurrentChangeHandler(onCurrentChange5)




def motor_one_close():
	dcMotor0.close()

def motor_two_close():
	dcMotor1.close()

def motor_three_close():
	dcMotor2.close()

def motor_four_close():
	dcMotor3.close()

def motor_five_close():
	dcMotor4.close()

def motor_six_close():
	dcMotor5.close()


if __name__ == "__main__":
	# time.sleep(10)
	motor_one(1)
	time.sleep(2)
	motor_two(1)
	time.sleep(2)
	motor_three(1)
	time.sleep(2)
	motor_four(1)
	time.sleep(2)
	motor_five(1)
	time.sleep(2)
	motor_six(1)
	# time.sleep(60)
 


