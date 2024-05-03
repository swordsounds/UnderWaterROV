from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import time

rcServo0 = RCServo()
rcServo2 = RCServo()

rcServo0.setDeviceSerialNumber(302849)
rcServo0.setChannel(0)
rcServo2.setDeviceSerialNumber(302849)
rcServo2.setChannel(2)

def servo1(angle):
	rcServo0.openWaitForAttachment(5000)
	rcServo0.setVelocityLimit(10)
	rcServo0.setTargetPosition(angle)
	rcServo0.setEngaged(True)
	
def servo2(angle):
	rcServo2.openWaitForAttachment(5000)
	rcServo2.setTargetPosition(angle)
	rcServo2.setEngaged(True)


def servo1_close():
	rcServo0.close()
def servo2_close():
	rcServo2.close()

if __name__ == "__main__":
	servo1(63)
	servo2(90)