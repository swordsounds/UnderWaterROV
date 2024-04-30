from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
from Phidget22.Devices.CurrentInput import *
import time

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()
dcMotor2 = DCMotor()
dcMotor3 = DCMotor()
dcMotor4 = DCMotor()
dcMotor5 = DCMotor()
#---CHANGE THE SERIAL NUMBERS BETWEEN COMMENTS----
# dcMotor0.setDeviceSerialNumber(487701)
# dcMotor0.setChannel(0)
# dcMotor1.setDeviceSerialNumber(487701)
# dcMotor1.setChannel(1)
dcMotor0.setDeviceSerialNumber(487777)
dcMotor0.setChannel(0)
dcMotor1.setDeviceSerialNumber(487777)
dcMotor1.setChannel(1)

# dcMotor2.setDeviceSerialNumber(487901)
# dcMotor2.setChannel(0)
# dcMotor3.setDeviceSerialNumber(487901)
# dcMotor3.setChannel(1)

# dcMotor4.setDeviceSerialNumber(487794)
# dcMotor4.setChannel(0)
# dcMotor5.setDeviceSerialNumber(487794)
# dcMotor5.setChannel(1)
#-----------------------------------
currentInput0 = CurrentInput()
currentInput1 = CurrentInput()
# currentInput2 = CurrentInput()
# currentInput3 = CurrentInput()
# currentInput4 = CurrentInput()
# currentInput5 = CurrentInput()
# currentInput6 = CurrentInput()

currentInput0.setDeviceSerialNumber(487777)
currentInput0.setChannel(0)
currentInput1.setDeviceSerialNumber(487777)
currentInput1.setChannel(1)

# currentInput2.setDeviceSerialNumber(487901)
# currentInput2.setChannel(0)
# currentInput3.setDeviceSerialNumber(487901)
# currentInput3.setChannel(1)

# currentInput4.setDeviceSerialNumber(487794)
# currentInput4.setChannel(0)
# currentInput5.setDeviceSerialNumber(487794)
# currentInput5.setChannel(1)

# dcMotor0.open()
# dcMotor1.open()
# dcMotor2.open()
# dcMotor3.open()
# dcMotor4.open()
# dcMotor5.open()
value0 = 0 
value1 = 0
value2 = 0
value3 = 0
value4 = 0
value5 = 0

def onCurrentChange0(self, current):
	value0 = round(float(current), 2)
	return value0

def onCurrentChange1(self, current):
	value1 = round(float(current), 2)
	return value1

def onCurrentChange2(self, current):
	value2 = round(float(current), 2)
	return value2

def onCurrentChange3(self, current):
	value3 = round(float(current), 2)
	return value3

def onCurrentChange4(self, current):
	value4 = round(float(current), 2)
	return value4	

def onCurrentChange5(self, current):
	value5 = round(float(current), 2)
	return value5

def motor_one(throttle):
	if throttle == None:
		throttle = 1
	dcMotor0.openWaitForAttachment(5000)
	dcMotor0.setAcceleration(19.4)
	dcMotor0.setTargetVelocity(throttle)

	currentInput0.openWaitForAttachment(5000)
	# currentInput0.setDataInterval(1000)
	currentInput0.setOnCurrentChangeHandler(onCurrentChange0)


def motor_two(throttle):
	if throttle == None:
		throttle = 1
	dcMotor1.openWaitForAttachment(5000)
	dcMotor1.setAcceleration(19.4)
	dcMotor1.setTargetVelocity(1)

	currentInput1.openWaitForAttachment(5000)
	currentInput1.setOnCurrentChangeHandler(onCurrentChange1)
	# currentInput1.setDataInterval(1000)

# def motor_three(throttle):
# 	if throttle == None:
# 		throttle = 1
# 	dcMotor2.openWaitForAttachment(5000)
# 	dcMotor2.setAcceleration(19.4)
# 	dcMotor2.setTargetVelocity(1)

# 	currentInput2.openWaitForAttachment(5000)
# 	currentInput2.setOnCurrentChangeHandler(onCurrentChange2)
# def motor_four(throttle):
# 	if throttle == None:
# 		throttle = 1
# 	dcMotor3.openWaitForAttachment(5000)
# 	dcMotor3.setAcceleration(19.4)
# 	dcMotor3.setTargetVelocity(1)

# 	currentInput3.openWaitForAttachment(5000)
# 	currentInput3.setOnCurrentChangeHandler(onCurrentChange3)
# def motor_five(throttle):
# 	if throttle == None:
# 		throttle = 1
# 	dcMotor4.openWaitForAttachment(5000)
# 	dcMotor4.setAcceleration(19.4)
# 	dcMotor4.setTargetVelocity(1)

# 	currentInput4.openWaitForAttachment(5000)
# 	currentInput4.setOnCurrentChangeHandler(onCurrentChange4)
# def motor_six(throttle):
# 	if throttle == None:
# 		throttle = 1
# 	dcMotor5.openWaitForAttachment(5000)
# 	dcMotor5.setAcceleration(19.4)
# 	dcMotor5.setTargetVelocity(1)

# 	currentInput5.openWaitForAttachment(5000)
# 	currentInput5.setOnCurrentChangeHandler(onCurrentChange5)

def motor_one_close():
	dcMotor0.close()

def motor_two_close():
	dcMotor1.close()

# def motor_three_close():
# 	dcMotor2.close()

# def motor_four_close():
# 	dcMotor3.close()

# def motor_five_close():
# 	dcMotor4.close()

# def motor_six_close():
# 	dcMotor5.close()

if __name__ == "__main__":
	# time.sleep(10)
	motor_one(1)
	# time.sleep(5)
	motor_two(1)
	time.sleep(5)
	# motor_three(1)
	# time.sleep(5)
	# motor_four(1)
	# time.sleep(5)
	# motor_five(1)
	# time.sleep(5)
	# motor_six(1)
	# time.sleep(5)