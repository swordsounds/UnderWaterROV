from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.VoltageRatioInput import *
import time

voltageInput0 = VoltageInput()
voltageRatioInput1 = VoltageRatioInput()

def onSensorChange(self, sensorValue, sensorUnit):
    print(sensorValue, sensorUnit.symbol)

def onVoltageChange(self, voltage):
    print("Voltage [" + str(self.getChannel()) + "]: " + str(voltage * 3200))

def main():

    voltageInput0.setDeviceSerialNumber(107414)
    voltageInput0.setChannel(0)

    voltageRatioInput1.setDeviceSerialNumber(107414)
    voltageRatioInput1.setChannel(1)

    voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
    # voltageRatioInput1.setOnSensorChangeHandler(onSensorChange)

    voltageInput0.openWaitForAttachment(5000)
    voltageRatioInput1.openWaitForAttachment(5000)

    voltageRatioInput1.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1124)

    time.sleep(600)

# def close():
#     voltageInput0.close()
#     voltageInput1.close()

if __name__ == "__main__":
    main()