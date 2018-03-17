import smbus
import pygame
import sys
bus = smbus.SMBus(1) #Bus por el cual se comunican
slaveAddress2 = 0x40 #MotorIzquierdo
slaveAddress1 = 0x50 #MotorDerecho
f=1
b=2
tr= 3
tl= 4
tlre=6
tre=7
s=5
#bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
#bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
 # initialise joystick
pygame.init()
j=pygame.joystick.Joystick(0)
j.init()

print(j.get_axis(0))
print(j.get_name())
