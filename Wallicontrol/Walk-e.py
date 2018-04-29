import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
#Stream data
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-b4c2e4df-fb98-4907-85f7-8e6392a93e48"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

limit = 0
#Ciclo repetido
print("Wall-i actualmente se encuentra esperando su instruccion")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
while instruccion == 'y':

data = machinarie.Data()
if data!= None :
    latitud,longitud = data   #Revision de posicion acual sin procesarself.
    envelope = pubnub.publish().channel("map2-channel").message({
    'lat': float(latitud),'lng': float(longitud)}).sync()
    region = machinarie.check_drp(latitud,longitud)
    reg0,reg1,reg2,reg3= region #Separacion de las regiones

    if  reg0 <= limit:
        #codigo
        virtual = machinarie.virtual_pos0()
        latv,lonv= virtual
        d=machinarie.distReg0(latv,longv)
        machinarie.region0Bounds(d,reg0)

    elif reg1 <= limit:
        #codigo
        virtual = machinarie.virtual_pos1()
        latv,longv= virtual
        d=machinarie.distReg1(latv,longv)
        machinarie.region1Bounds(d,reg1)
    elif reg2 <= limit:
        #codigo
        virtual = machinarie.virtual_pos2()
        latv,longv= virtual
        d=machinarie.distReg2(latv,longv)
        machinarie.region2Bounds(d,reg2)
    elif reg3 <= limit;
        #codigo
        virtual = machinarie.virtual_pos3()
        latv,longv= virtual
        d=machinarie.distReg3(latv,longv)
        machinarie.region3Bounds(d,reg3)
