from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()
dcMotor2 = DCMotor()
dcMotor3 = DCMotor()
dcMotor4 = DCMotor()
dcMotor5 = DCMotor()

dcMotor0.setDeviceSerialNumber(487701)
dcMotor0.setChannel(0)
dcMotor1.setDeviceSerialNumber(487701)
dcMotor1.setChannel(1)

dcMotor2.setDeviceSerialNumber(487701)
dcMotor2.setChannel(0)
dcMotor3.setDeviceSerialNumber(487701)
dcMotor3.setChannel(1)

dcMotor4.setDeviceSerialNumber(487701)
dcMotor4.setChannel(0)
dcMotor5.setDeviceSerialNumber(487701)
dcMotor5.setChannel(1)

currentInput0 = CurrentInput()
currentInput1 = CurrentInput()

currentInput0.setDeviceSerialNumber(487701)
currentInput0.setChannel(0)
currentInput1.setDeviceSerialNumber(487701)
currentInput1.setChannel(1)

def onCurrentChange(self, current):
	f = open("DataCollector.txt", "w")
	f.write(f"{round(current, 2)}")
	f.close()
# self.getChannel(), 
def motor_one(throttle):
	if throttle == None:
		throttle = 1
	dcMotor0.openWaitForAttachment(1000)
	dcMotor0.setAcceleration(19.4)
	dcMotor0.setTargetVelocity(throttle)

	currentInput0.openWaitForAttachment(1000)
	currentInput0.setOnCurrentChangeHandler(onCurrentChange)

def motor_two():
	dcMotor1.openWaitForAttachment(1000)
	dcMotor1.setAcceleration(19.4)
	dcMotor1.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(1000)
	# currentInput1.setOnCurrentChangeHandler(onCurrentChange)
def motor_three():
	dcMotor2.openWaitForAttachment(1000)
	dcMotor2.setAcceleration(19.4)
	dcMotor2.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(1000)
	# currentInput1.setOnCurrentChangeHandler(onCurrentChange)
def motor_four():
	dcMotor3.openWaitForAttachment(1000)
	dcMotor3.setAcceleration(19.4)
	dcMotor3.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(1000)
	# currentInput1.setOnCurrentChangeHandler(onCurrentChange)
def motor_five():
	dcMotor4.openWaitForAttachment(1000)
	dcMotor4.setAcceleration(19.4)
	dcMotor4.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(1000)
	# currentInput1.setOnCurrentChangeHandler(onCurrentChange)
def motor_six():
	dcMotor5.openWaitForAttachment(1000)
	dcMotor5.setAcceleration(19.4)
	dcMotor5.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(1000)
	# currentInput1.setOnCurrentChangeHandler(onCurrentChange)

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