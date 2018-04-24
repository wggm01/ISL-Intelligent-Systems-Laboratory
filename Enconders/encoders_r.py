ticks = 0;
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=27
button2=22
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while(1):
    if GPIO.input(button1)== 0 and GPIO.input(button2)== 0 :
        ticks = ticks + 1
        print( "ticks")
