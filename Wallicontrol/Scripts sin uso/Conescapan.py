import datetime
import machinarie
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

p = [0,0] #Posicion dinamica
xa = [-79.53169299,-79.53152138,-79.53177739,-79.53184155] #X1 Y X2 corresponden a abcisas del punto inicio y finalsel.
ya = [9.023410836,9.023175628,9.022897331,9.023147334] #Y1 Y Y2 corresponden a ordenadas del punto inicio y finalsel.
q = [0,0] # Puntos virtual trasladado
drp = [0,0,0,0]#una para cada modelo y0,y1,y2,y3

#Stream data
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-b4c2e4df-fb98-4907-85f7-8e6392a93e48"
pnconfig.subscribe_key = "sub-c-05449d3a-b73e-11e7-a84a-1e64a053e7fc"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

print("Programa para recoleccion de data")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
    data = machinarie.Data()
    if data!= None :
        latitud,longitud = data
        envelope = pubnub.publish().channel("map2-channel").message({
        'lat': float(latitud),'lng': float(longitud)}).sync()
        p[0]=longitud #x
        p[1]=latitud
        print(latitud,longitud)
        #Calculo de pendientes:
        m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
        m2 = -1/m1
        #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
        x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
        y = m1*(x-xa[0])+ya[0]
        q[0]=x#Longitud
        q[1]=y#Latitud
        print(x,y)
        #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
        #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

