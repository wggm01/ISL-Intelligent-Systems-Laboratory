import serial
import time
import machinarie
import math

Forward='F'
Turn='T'
Stop = 'S'
delay = 10 #Este valor hay que estimarlo al ojo.

#Lectura del puerto serial
gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)
arduino = serial.Serial('/dev/ttyUSB0', 9600)
#gps = serial.Serial('COM3', 9600)


instruccion = raw_input("When u're ready press y to start  \n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
    gps_sentece = gps.readline()
    gps_sentences_fields = gps_sentece.split(",")
    #FILTRO DE LA SENTENCIA $GPRMC
    if gps_sentences_fields[0] == "$GPRMC" and  gps_sentences_fields[2] == "A":
        get_unformated_latitude = float(gps_sentences_fields[3])
        get_unformated_longitude = float(gps_sentences_fields[5])
        latdeg = int(get_unformated_latitude/100)
        latmin = get_unformated_latitude - latdeg*100
        lat = latdeg + (latmin/60)

        longdeg = int(get_unformated_longitude/100)
        longmin = get_unformated_longitude - longdeg*100
        longi = longdeg + (longmin/60)
        if gps_sentences_fields[4] == "S":
            lat = -lat
        if  gps_sentences_fields[6] == "W":
            longi = -longi
         #Calculo para saber cuanto falta para terminar region 1
        latref =9.02318033
        longref = -79.53151733 #region1
        radius = 6371 # km
        dlat = math.radians(latref-lat)
        dlon = math.radians(longref-longi)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat)) \
        * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = int((radius*c)*1000)
        print d
        #comando = instrucion enviada al arduino
	if latref == 9.02318033 and longref == -79.53151733 :
		min1 = 34#se puede quedar asi
		max1 = 6#cambiar
		min2 = 6 #Minimo y max para cuando inicia la region
		#max2 =25
		print("Region 1")
	if latref == 9.023149167 and longref == -79.53156583 :
		min1 = 7#se puede quedar asi
		max1 = 2#cambiar
		min2 = 1 #Minimo y max para cuando termina la region
		#max2 = 8
		print("Region 2")
        if d < min1 and d >= max1: #Establecer limites manualmente para mover
               arduino.write(Forward) #Mandar un comando hacia Arduino
               print("Moviendo")
        
        if d <= min2:#Establecer limites manualmente para cuando esta terminando la region  
               arduino.write(Turn)#Mandar un comando hacia Arduino
               print("Curvo")
            #time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
               latref=9.023149167
               lonref=-79.53156583
        
	   
           
        
    

   
