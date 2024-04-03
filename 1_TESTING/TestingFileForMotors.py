from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()

currentInput0 = CurrentInput()
currentInput1 = CurrentInput()

dcMotor0.setDeviceSerialNumber(487701)
dcMotor0.setChannel(0)
dcMotor1.setDeviceSerialNumber(487701)
dcMotor1.setChannel(1)

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

def motor_one_close():
	dcMotor0.close()

def motor_two_close():
	dcMotor1.close()