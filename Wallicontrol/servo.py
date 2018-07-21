import RPi.GPIO as GPIO
import time

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
try:
  while True:
    angulo=input("angulo pliz")
    desireang=angle(angulo)
    p.ChangeDutyCycle(desireang)
    time.sleep(0.1)
	
except KeyboardInterrupt:
  print("Bye Bye")
  p.stop()
  GPIO.cleanup()
