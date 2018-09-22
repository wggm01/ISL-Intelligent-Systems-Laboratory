import RPi.GPIO as GPIO
import time
#RECEPCION DE PAQUETES POR UDP
import socket, traceback
from struct import *
host = '192.168.25.100'
port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

#CONTROL DE SERVO CON LIBRERIA RPI
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
count=30
p = GPIO.PWM(servoPIN, 50) 
p.start(7.5)
def angle(ang):
	duty=1./18.*(ang)+1
	if duty > 11:
		duty=7
	return duty

def mapazimut(ang_raw,in_min,in_max,out_min,out_max):
	angle=(ang_raw-in_min)*(out_max-out_min)/(in_max-in_min)+out_min
	return angle 
try:
  while True:
    data, address = s.recvfrom(8192)
    
    azimut= unpack_from ('!f', data, 36)
    
    azimap_raw=azimut[0]
    azimap=int(azimap_raw)
    desireang=mapazimut(azimap,-127,77,30,180)
#    print (desireang,azimut)
    p.ChangeDutyCycle(angle(desireang))
#    time.sleep(0.1)
	
except KeyboardInterrupt:
  print("Bye Bye")
  p.stop()
  GPIO.cleanup()
