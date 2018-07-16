import smbus2
from smbus2 import SMBus
from smbus2 import SMBusWrapper
import time
mizq = 0x40
mder = 0x50
bus = smbus.SMBus(1)

def wr_i2c (instruction):
    with SMBusWrapper(1) as bus:
    # Write a byte to address 80, offset 0
        data = instruction  
        bus.write_byte_data(mizq, 0, instruction)
        bus.write_byte_data(mder, 0, instruction)

while True:
    instruction = raw_input("Enter the data to be sent : ")
	data_list = list(instruction)
	for i in data_list:
    	#Sends to the Slaves 
        wr_i2c(int(ord(i)))
        time.sleep(.1)
  
