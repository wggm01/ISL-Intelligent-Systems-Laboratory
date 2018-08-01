import smbus
import time

bus =smbus.SMBus(1)
def inputd (value):
	bus.write_byte(0x50,value)
        bus.write_byte(0x40,value)
	return -1
while True:
	instruction = input("") 
	inputd(int(instruction))
	time.sleep(.1)


	
 
