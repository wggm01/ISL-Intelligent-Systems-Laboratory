import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
#Stream data
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-b4c2e4df-fb98-4907-85f7-8e6392a93e48"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)

limit = 2
#Ciclo repetido
print("Wall-i actualmente se encuentra esperando su instruccion")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
while instruccion == 'y':

data = machinarie.Data()
if data!= None :
    latitud,longitud = data   #Revision de posicion acual sin procesarself.
    envelope = pubnub.publish().channel("map2-channel").message({
    'lat': float(latitud),'lng': float(longitud)}).sync()
    
    virtual_0 = machinarie.virtual_pos0()
    latv0,lonv0= virtual_0
    
    virtual_1 = machinarie.virtual_pos1()
    latv1,lonv1= virtual_1
    
    virtual_2 = machinarie.virtual_pos2()
    latv2,lonv2= virtual_2
    
    virtual_3 = machinarie.virtual_pos3()
    latv3,lonv3= virtual_3
    
    reg0 = machinarie.check_0drp(latitud,longitud,latv0,lonv0)
    reg1 = machinarie.check_0drp(latitud,longitud,latv1,lonv1)
    reg2 = machinarie.check_0drp(latitud,longitud,latv2,lonv2)
    reg3 = machinarie.check_0drp(latitud,longitud,latv3,lonv3)
    
    if  reg0 <= limit:
        #codigo
        #virtual = machinarie.virtual_pos0()
        #latv,lonv= virtual
        d=machinarie.distReg0(latv0,longv0)
        machinarie.region0Bounds(d,reg0)

    elif reg1 <= limit:
        #codigo
        #virtual = machinarie.virtual_pos1()
        #latv,longv= virtual
        d=machinarie.distReg1(latv1,longv1)
        machinarie.region1Bounds(d,reg1)
        
    elif reg2 <= limit:
        #codigo
        #virtual = machinarie.virtual_pos2()
        #latv,longv= virtual
        d=machinarie.distReg2(latv2,longv2)
        machinarie.region2Bounds(d,reg2)
        
    elif reg3 <= limit;
        #codigo
        #virtual = machinarie.virtual_pos3()
        #latv,longv= virtual
        d=machinarie.distReg3(latv3,longv3)
        machinarie.region3Bounds(d,reg3)
