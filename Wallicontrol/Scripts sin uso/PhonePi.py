import sys
from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/orientation')
def echo_socket(ws):
        f=open("orientation.txt","a")
        while True:
                message = ws.receive()
                splitdata=message.split(",")
                azimut=splitdata[0]
                print(azimut)
                #print(message)
                ws.send(message)
                print>>f,message
                      
        f.close()


@app.route('/')
def hello():
	return 'Hello World!'

if __name__ == "__main__":
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
