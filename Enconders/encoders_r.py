

import smbus
import time
slaveAddress3 = 0x60
slaveAddress2 = 0x40
slaveAddress1 = 0x50
bus = smbus.SMBus(1)



Forward=1
Backward =2
Turn= 4
TurnLeftEje = 7
Stop = 5
delay = 1

#distance = 480; #Colocar experimentalmente

print("Programa de prueba de encoder")
distance = input("ingrese la distancia en ticks que desea recorrer\n ")
global distance
while(1):
    bus.write_byte(slaveAddress3, distance)
    time.sleep(.1)
    bus.write_byte(slaveAddress2, Forward)
    bus.write_byte(slaveAddress1, Forward)

if bus.read_byte(slaveAddress3)==9:
    bus.write_byte(slaveAddress2, Stop)
    bus.write_byte(slaveAddress1, Stop)
    #distance = input("ingrese la distancia en ticks que desea recorrer\n ")  
    #time.sleep(.1) 
    #bus.write_byte(slaveAddress3, distance)
        
