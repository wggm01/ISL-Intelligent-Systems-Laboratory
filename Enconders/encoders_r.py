from time import sleep
ticks = 0;
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button1=12
#button2=22
GPIO.setup(button1,GPIO.IN)
#GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
sensor = GPIO.input(button1)

while True:
	
	sensor=GPIO.input(button1)
	
	if sensor == 1 :
		ticks = ticks + 1
		print( ticks )
		sleep(.5)
		
