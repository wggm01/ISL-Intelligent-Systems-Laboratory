import smbus
import time
mizq = 0x40
mder = 0x50
bus = smbus.SMBus(1)
def wr_i2c (value):
	bus.write_byte(mizq,value)
#   bus.write_byte_data(mder,0,instruction)
	return -1
while True:
	instruction = input("") 
	wr_i2c(int(instruction))

	time.sleep(.1)
 
