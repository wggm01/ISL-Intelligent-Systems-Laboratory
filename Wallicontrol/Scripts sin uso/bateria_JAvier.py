from RPi import GPIO
global IN_OPTO
global OUT_OPTO

IN_OPTO=18
OUT_OPTO=23

#configuracion de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN_OPTO, GPIO.IN)
GPIO.setup(OUT_OPTO, GPIO.OUT)

if(IN_OPTO==1)
	OUT_OPTO=1
else
	OUT_OPTO=0

