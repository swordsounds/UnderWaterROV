from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()

dcMotor0.setChannel(0)
dcMotor1.setChannel(1)

def main():
	
	dcMotor0.openWaitForAttachment(1000)
	dcMotor1.openWaitForAttachment(1000)


	dcMotor0.setAcceleration(19.4)
	dcMotor1.setAcceleration(19.4)

	dcMotor0.setTargetVelocity(-1)
	dcMotor1.setTargetVelocity(-1)

def close():
	dcMotor0.close()
	dcMotor1.close()

if __name__ == "__main__":
	main()
	