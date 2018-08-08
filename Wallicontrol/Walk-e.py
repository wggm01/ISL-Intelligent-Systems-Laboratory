#CODIGO ARMADO POR WVALDO GABRIEL GRAELL MANZANE WGGM
#VERSION: RETO TOKIO
import os  #modulo para interactuar con el sistema
from gps import* #modulo para trabajar con el gpsd
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

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
	gpsp = GpsPoller() # create the thread
	try:
		gpsp.start()
		print("Wall-i actualmente se encuentra esperando su instruccion")
		instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
		while instruccion == 'y':

    #data = machinarie.Data()
    #if data!= None :
    #    global latitud
    #    global longitud
    #    latitud,longitud = data   #Revision de posicion acual sin procesarself.
        #envelope = pubnub.publish().channel("map2-channel").message({
        #'lat': float(latitud),'lng': float(longitud)}).sync()
			#data de gps sin tratar
			global latitud
			global longitud
			latitud= gpsd.fix.latitude
			longitud= gpsd.fix.longitude
			
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

			with open ("Virtual_pos.csv", "a") as pos:
				pos.write("%s, %s, %s, %s, %s, %s, %s, %s\n" % ( latv0, lonv0, latv1, lonv1, latv2, lonv2, latv3, lonv3 ))
    
			reg0 = machinarie.check_0drp(latitud,longitud,latv0,lonv0)
			reg1 = machinarie.check_1drp(latitud,longitud,latv1,lonv1)
			reg2 = machinarie.check_2drp(latitud,longitud,latv2,lonv2)
			reg3 = machinarie.check_3drp(latitud,longitud,latv3,lonv3)
			print("DRP0",reg0,"DRP1",reg1,"DRP2",reg2,"DRP3",reg3)
			
			with open ("drp.csv", "a") as pos:
				pos.write("%s, %s, %s, %s\n" % ( reg0,reg1,reg2,reg3))
    
			if  reg0 <= limit:
            #codigo
            #virtual = machinarie.virtual_pos0()
            #latv0,lonv0= virtual
				d=machinarie.distReg0(latv0,lonv0)
            #print(d)
				with open ("d0.csv", "a") as pos:
					pos.write("%s\n" % (d))

			"""	flag_sensor_dist= flag_sensor_dist()
				if flag_sensor_dist == 8:
					while flag_sensor == 8:
						wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
						elif flag_sensor_dist == 9:
							while flag_sensor == 9:
								wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
				else: 
					print("Aun no me desvio") """

				machinarie.region0Bounds(d,reg0)

			elif reg1 <= limit:
				#codigo
				#virtual = machinarie.virtual_pos1()
				#latv,longv= virtual
					d=machinarie.distReg1(latv1,lonv1)
				#print(d)
					with open ("d1.csv", "a") as pos:
						pos.write("%s\n" % (d))

				"""	flag_sensor_dist= flag_sensor_dist()
					if flag_sensor_dist == 8:
						while flag_sensor == 8:
							wr_i2c (softleft)
							if flag_sensor_dist() == 1:
								break
							elif flag_sensor_dist == 9:
								while flag_sensor == 9:
									wr_i2c (softleft)
							if flag_sensor_dist() == 1:
								break
					else: 
						print("Aún no me desvio")"""         

				machinarie.region1Bounds(d,reg1)
			
			elif reg2 <= limit:
				#codigo
				#virtual = machinarie.virtual_pos2()
				#latv,longv= virtual
				d=machinarie.distReg2(latv2,lonv2)
				print(d)
				with open ("d2.csv", "a") as pos:
					pos.write("%s\n" % (d))

			"""	flag_sensor_dist= flag_sensor_dist()
				if flag_sensor_dist == 8:
					while flag_sensor == 8:
						wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
				elif flag_sensor_dist == 9:
					while flag_sensor == 9:
						wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
				else: 
					print("Aún no me desvio") """

				machinarie.region2Bounds(d,reg2)
			
			elif reg3 <= limit:
				#codigo
				#virtual = machinarie.virtual_pos3()
				#latv,longv= virtual
				d=machinarie.distReg3(latv3,lonv3)
				print(d)
				with open ("d3.csv", "a") as pos:
					pos.write("%s\n" % (d))

			"""	flag_sensor_dist= flag_sensor_dist()
				if flag_sensor_dist == 8:
					while flag_sensor == 8:
						wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
				elif flag_sensor_dist == 9:
					while flag_sensor == 9:
						wr_i2c (softleft)
						if flag_sensor_dist() == 1:
							break
				else: 
					print("Aún no me desvio") """           

				machinarie.region3Bounds(d,reg3)
			else
				print("No se donde estoy")
			#time.sleep(1)
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
		print "Cerrando programa"
		gpsp.running = False
		gpsp.join() # wait for the thread to finish what it's doing
	print "bye"
