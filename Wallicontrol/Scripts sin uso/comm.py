import socket, traceback
from struct import *
host = '192.168.0.247'
port = 5556

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while 1:
    try:
        data, address = s.recvfrom(8192)
        #print message
        azimut= unpack_from ('!f', data, 36)
        azimap=azimut[0]
        print azimap
        #print "received message: ", "%1.4f" %unpack_from ('!f', data, 36) #DATA DEL ANGULO AZIMUTH
        
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
