import smbus
from smbus import SMBus
import time
mizq = 0x40
mder = 0x50
bus =SMBus(1)
def inputd (value):
	bus.write_byte(mder,value)
#        bus.write_byte(mder,value)
	return -1
while True:
	instruction = input("") 
	inputd(int(instruction))
	time.sleep(.1)


	
 
