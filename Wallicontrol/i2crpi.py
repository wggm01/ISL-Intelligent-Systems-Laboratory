import smbus
import time
mizq = 0x40
mder = 0x50
bus = smbus.SMBus(1)
def writeins (value):
	 
	bus.write_byte_data(mizq,value)
#        bus.write_byte_data(mder,0,instruction)
	return -1
while True:
	instruction = input("") 
        writeins(instruction)
#	print(instruction)
        time.sleep(.1)
 
