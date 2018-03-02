import smbus
import time
slaveAddress2 = 0x40
slaveAddress1 = 0x50
bus = smbus.SMBus(1)

def writeNumber(value):
    bus.write_byte(slaveAddress2, value)
    bus.write_byte(slaveAddress1, value)
   # bus.write_byte_data(address, 0, value)
    return -1

while True:
    var = input("")
    if not var:
        continue

    writeNumber(var)
