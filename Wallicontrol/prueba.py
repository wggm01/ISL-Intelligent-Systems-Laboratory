import smbus
import pygame,sys
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
joystick_count = pygame.joystick.get_count()
print "There is " + str(joystick_count) + " joystick/s"

if joystick_count == 0:
    # if no joysticks, quit program safely
    print ("Error, I did not find any joysticks")
    pygame.quit()
    sys.exit()
else:
    # initialise joystick
    joystick = pygame.joystick.Joystick(0)
joystick.init()

if joystick.get_button(4)== True:
    print ("f")
if joystick.get_button(6)==True:
    print ("b")
if joystick.get_button(5)==True:
    print("tr")
if joystick.get_button(7)==True:
    print("tl")
