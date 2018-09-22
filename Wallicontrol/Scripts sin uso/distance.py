import smbus

slaveAddress2 = 0x40
slaveAddress1 = 0x50
slave= 0x60
bus = smbus.SMBus(1)

def get():
     enco = bus.read_byte(slave)
     return enco
      

while True:

     if get() == 2:
	#bus.write_byte(slaveAddress1,1)
	bus.write_byte(slaveAddress2,1)
     elif get() == 5:
        #bus.write_byte(slaveAddress1,5)
        bus.write_byte(slaveAddress2,5)
