import RPi.GPIO as GPIO
import smbus
import time

slaveAddress2 = 0x40
slaveAddress1 = 0x50
bus = smbus.SMBus(1)

Forward=1
Backward =2
Turn= 4
TurnLeftEje = 7
Stop = 5
delay = 1

ticks1 = 0;
ticks2 = 0;

GPIO.setmode(GPIO.BCM)
enco1=27
enco2=22
GPIO.setup(enco1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(enco2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#Funciones acciondas por cambio
def ticks1_count (self):
    global ticks1
    ticks1 = ticks1+1
    #return ticks1
def ticks2_count (self):
    global ticks2
    ticks2 = ticks2+1
    #return ticks2


GPIO.add_event_detect(enco1,GPIO.RISING,callback=ticks1_count)
GPIO.add_event_detect(enco2,GPIO.RISING,callback=ticks2_count)



print("Programa de prueba de encoder")
distance = raw_input("ingrese la distancia en ticks que desea recorrer\n ")

while(1):
    if ticks1>=distance  and ticks2>=distance :
        bus.write_byte(slaveAddress2, Stop)
        bus.write_byte(slaveAddress1, Stop)
        time.sleep(delay)
        ticks1 =0
        ticks2=0
        try:
            distance = raw_input("ingrese la distancia en ticks que desea recorrer\n ")
        except:
            distance = raw_input("no ha ingresado distancia en ticks..ingresar ahora\n ")


    elif:
        bus.write_byte(slaveAddress2, Forward)
        bus.write_byte(slaveAddress1, Forward)
