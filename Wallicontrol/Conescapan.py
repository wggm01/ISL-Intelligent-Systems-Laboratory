import datetime
import machinarie
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

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
