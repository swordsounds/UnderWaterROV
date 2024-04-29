from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import time

def main():
	rcServo0 = RCServo()
	rcServo1 = RCServo()
	rcServo2 = RCServo()

	rcServo0.setDeviceSerialNumber(302849)
	rcServo0.setChannel(0)
	rcServo1.setDeviceSerialNumber(302849)
	rcServo1.setChannel(1)
	rcServo2.setDeviceSerialNumber(302849)
	rcServo2.setChannel(2)

	rcServo0.openWaitForAttachment(5000)
	rcServo1.openWaitForAttachment(5000)
	rcServo2.openWaitForAttachment(5000)

	rcServo0.setTargetPosition(90)
	rcServo0.setEngaged(True)
	rcServo1.setTargetPosition(90)
	rcServo1.setEngaged(True)
	rcServo2.setTargetPosition(90)
	rcServo2.setEngaged(True)

	time.sleep(5)

	rcServo0.close()
	rcServo1.close()
	rcServo2.close()

main()