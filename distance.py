import smbus
import time
slaveAddress2 = 0x40
slaveAddress1 = 0x50
bus = smbus.SMBus(1)

def writeNumber(value):
    bus.write_byte(slaveAddress2, value) #Funcion
    bus.write_byte(slaveAddress1, value)
   # bus.write_byte_data(address, 0, value)
    return -1
#def readnumber():
 #   bus.read_byte(0X60)
  #  return -1

while True:
#    var = input("")
 #   if not var:
  #      continue
     if bus.read_byte(0X60) == 1:
	bus.write_byte(slaveAddress1,1)
	bus.write_byte(slaveAddress2,1)
	print("F")
     if bus.read_byte(0X60) == 4:
	bus.write_byte(slaveAddress1,4)
	bus.write_byte(slaveAddress2,4)
    	print("Derecha")
 #   writeNumber(var)
