#1-hacia alfrente
#2-hacia atras
#3-Dobla hacia la izquierda
#4-Dobla hacia la derecha
#5-Detener

#-------------Librerias--------------------------
#import serial
import time
#import machinarie
import math
import smbus
#-----------Variables principales-----------------
Forward=1
Turn= 4
Stop = 5
delay = 10 #Este valor hay que estimarlo al ojo.
slaveAddress2 = 0x40 #MotorIzquierdo
slaveAddress1 = 0x50 #MotorDerecho
bus = smbus.SMBus(1) #Bus por el cual se comunican
#-------------------------------------------------

#-----------Conecciones----------------------------
gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#gps = serial.Serial('COM3', 9600)
#--------------------------------------------------


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
#-----------Calculo de distancia usando Harversine----------------------------
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
#------------------------------------------------------------------------------
#--------comando = instrucion enviada al arduino---------------------------
#----Los limites se definen mediante las coordenadas de referencias-------
	if latref == 9.02318033 and longref == -79.53151733 :
        #Limites para las region1
		min1 = 34
		max1 = 6  # min<--------------Region--------------------------->max
		min2 = 6
		#max2 =25
		print("Region 1")
	if latref == 9.023149167 and longref == -79.53156583 :
        #Limite para Region 2
		min1 = 7
		max1 = 2 # min<--------------Region--------------------------->max
		min2 = 1
		#max2 = 8
		print("Region 2")
        if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
               #arduino.write(Forward) #Mandar un comando hacia Arduino
               bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
               bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
               print("Moviendo")

        if d <= min2:#Establece cuando curvara
               #arduino.write(Turn)#Mandar un comando hacia Arduino
               bus.write_byte(slaveAddress2, Turn)#Mandar un comando hacia MotorDerecho
               bus.write_byte(slaveAddress1, Turn)#Mandar un comando hacia MotorIzquierdo
               print("Curvand")
            #time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
               latref=9.023149167 #Cambio de la referencia para la region2
               lonref=-79.53156583
