from RPi import GPIO
from time import sleep

clk1 = 5 
dt1 = 13

clk2 = 6
dt2 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Derecha1 = 0
izquierda1 = 0
Derecha2 = 0
izquierda2 = 0

CLS1 = GPIO.input(clk1)
CLS2 = GPIO.input(clk2)

	while True:
                CS1 = GPIO.input(clk1)
                DTS1 = GPIO.input(dt1)
		CS2 = GPIO.input(clk2)
                DTS2 = GPIO.input(dt2)
                if CS1 != CLS1:
                        if DTS1 != CS1:
                                derecha1 += 1
                        else:
                                izquierda1 += 1
                        print derecha1
			print izquierda1
		 if CS2 != CLS2:
                        if DTS2 != CS2:
                                derecha2 += 1
                        else:
                                izquierda2 += 1
                        print derecha2
			print izquierda2
                CLS1 = CS1
		CLS2 = CS2
                sleep(0.01)

GPIO.cleanup()
