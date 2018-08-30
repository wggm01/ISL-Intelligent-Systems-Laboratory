#CODIGO ARMADO POR WVALDO GABRIEL GRAELL MANZANE WGGM
#VERSION: RETO TOKIO
import os  #modulo para interactuar con el sistema
import subprocess
import time
import  threading
from time import* #modulo para los retrasos
import pubnub # modulo para enviar datos de gps
import datetime #modulo para fecha y tiempo
import machinarie #modulo original de  wggm
from pubnub.pnconfiguration import PNConfiguration #configuraciones para pubnub
from pubnub.pubnub import PubNub
#CONFIGURACION PARA PUBNUB
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-b4c2e4df-fb98-4907-85f7-8e6392a93e48"
pnconfig.subscribe_key = "sub-c-05449d3a-b73e-11e7-a84a-1e64a053e7fc"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)
limit = 3
#Instruciones de correccion de recorrido.
softleft = 6
softright = 7

gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)
os.system('i2cdetect -y 1')
#os.system('sudo cat /dev/ttyACM0') #clear the terminal (optional)
#os.system('cgps') #clear the terminal (optional)
#os.system('sudo gpsd /dev/ttyACM0 -F /var/run/gpsd.sock')
try:

    print("El Programa empezara al recibir la confirmacion por parte del gps")

    while machinarie.gps_check() == 1:

        data = machinarie.Data()

        if data!= None :
            latitud,longitud = data   #Revision de posicion acual sin procesarself.

        #envelope = pubnub.publish().channel("map2-channel").message({
        #'lat': float(latitud),'lng': float(longitud)}).sync()
			#data de gps sin tratar
		global latitud
		global longitud

		latitud_raw= latitud
		longitud_raw= longitud
		time= datetime.datetime.now()

		with open ("raw_coords.csv", "a") as pos:
            pos.write("%s, %s, %s \n" % ( latitud_raw, longitud_raw,time ))

		machinarie.get_data_gyro()
		machinarie.get_data_ultra()

		nrp = machinarie.not_repeatcoord(latitud_raw,longitud_raw) #EVITA LA REPETICION DE COORDENADAS
		      if nrp != None:
                  latitud,longitud = nrp

		virtual_0 = machinarie.virtual_pos0(latitud,longitud)
		global latv0
		global lonv0
		latv0,lonv0= virtual_0

		virtual_1 = machinarie.virtual_pos1(latitud,longitud)
		global latv1
		global lonv1
		latv1,lonv1= virtual_1

		virtual_2 = machinarie.virtual_pos2(latitud,longitud)
		global latv2
		global lonv2
		latv2,lonv2= virtual_2

		virtual_3 = machinarie.virtual_pos3(latitud,longitud)
		global latv3
		global lonv3
		latv3,lonv3= virtual_3

<<<<<<< HEAD
			if  reg0 <= limit:
            #codigo
            #virtual = machinarie.virtual_pos0()
            #latv0,lonv0= virtual
				d=machinarie.distReg0(latv0,lonv0)
				print(d)
            #print(d)
				with open ("d0.csv", "a") as pos:
					pos.write("%s\n" % (d))
=======
		with open ("Virtual_pos.csv", "a") as pos:
            pos.write("%s, %s, %s, %s, %s, %s, %s, %s\n" % ( latv0, lonv0, latv1, lonv1, latv2, lonv2, latv3, lonv3 ))
>>>>>>> 38a1d9cb125c9822503c702990817c9f7e672bbf

		reg0 = machinarie.check_0drp(latitud,longitud,latv0,lonv0)
		reg1 = machinarie.check_1drp(latitud,longitud,latv1,lonv1)
		reg2 = machinarie.check_2drp(latitud,longitud,latv2,lonv2)
		reg3 = machinarie.check_3drp(latitud,longitud,latv3,lonv3)

		print("DRP0",reg0,"DRP1",reg1,"DRP2",reg2,"DRP3",reg3)

		with open ("drp.csv", "a") as pos:
            pos.write("%s, %s, %s, %s\n" % ( reg0,reg1,reg2,reg3))

<<<<<<< HEAD
			elif reg1 <= limit:
            #codigo
            #virtual = machinarie.virtual_pos1()
            #latv,longv= virtual
				d=machinarie.distReg1(latv1,lonv1)
				print(d)
=======
		if  reg0 <= limit:
            d=machinarie.distReg0(latv0,lonv0)
            with open ("d0.csv", "a") as pos:
                pos.write("%s\n" % (d))
>>>>>>> 38a1d9cb125c9822503c702990817c9f7e672bbf

            machinarie.region0Bounds(d,reg0)

		elif reg1 <= limit:
            d=machinarie.distReg1(latv1,lonv1)

			with open ("d1.csv", "a") as pos:
                pos.write("%s\n" % (d))

<<<<<<< HEAD
			elif reg2 <= limit:
            #codigo
            #virtual = machinarie.virtual_pos2()
            #latv,longv= virtual
				d=machinarie.distReg2(latv2,lonv2)
				print(d)
=======
            machinarie.region1Bounds(d,reg1)
>>>>>>> 38a1d9cb125c9822503c702990817c9f7e672bbf

		elif reg2 <= limit:
            d=machinarie.distReg2(latv2,lonv2)

            with open ("d2.csv", "a") as pos:
                pos.write("%s\n" % (d))

            machinarie.region2Bounds(d,reg2)

		elif reg3 <= limit:

<<<<<<< HEAD
			elif reg3 <= limit:
            #codigo
            #virtual = machinarie.virtual_pos3()
            #latv,longv= virtual
				d=machinarie.distReg3(latv3,lonv3)
				print(d)
=======
            d=machinarie.distReg3(latv3,lonv3)
>>>>>>> 38a1d9cb125c9822503c702990817c9f7e672bbf

            with open ("d3.csv", "a") as pos:
                pos.write("%s\n" % (d))

            machinarie.region3Bounds(d,reg3)

		else:
            print("No se donde estoy")

except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    machinarie.hardrst(int(20))

    print "Cerrando programa, bye :D"
