import RPi.GPIO as GPIO
import time
#RECEPCION DE PAQUETES 
import sys
from flask import Flask
from flask_sockets import Sockets
app = Flask(__name__)
sockets = Sockets(app)
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

@sockets.route('/orientation')
def echo_socket(ws):
        try:
                f=open("orientation.txt","a")      
                while True:
                        message = ws.receive()
                        splitdata=message.split(",")
                        azimut=float(splitdata[0])
                        #print(message)
                        ws.send(message)
                        print>>f,message
                        
                        azimap_raw=azimut
                        azimap=int(azimap_raw)
                        desireang=mapazimut(azimap,44,240,30,180)
                        print (desireang,azimut)
                        p.ChangeDutyCycle(angle(desireang))
                        #time.sleep(0.1)
                f.close()
        except KeyboardInterrupt:
                print("Bye Bye")
                p.stop()
                GPIO.cleanup()
@app.route('/')
def hello():
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
