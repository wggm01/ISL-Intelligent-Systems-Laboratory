#1-hacia alfrente
#2-hacia atras
#3-Dobla hacia la izquierda
#4-Dobla hacia la derecha
#5-Detener

#-------------Librerias--------------------------
import serial
import time
#import machinarie
import math
import smbus
#-----------Variables principales-----------------
Forward=1
Turn= 4
Stop = 5
delay = 5 #Este valor hay que estimarlo al ojo.
slaveAddress2 = 0x40 #MotorIzquierdo
slaveAddress1 = 0x50 #MotorDerecho
#bus = smbus.SMBus(1) #Bus por el cual se comunican
#Region 1
#latref =9.02318033
#longref = -79.53151733
#Region 2
#latref2=9.023149167
#lonref2=-79.53156583
region2 = 0
#-------------------------------------------------

#-----------Conecciones----------------------------
gps = serial.Serial("/dev/ttyACM0", baudrate = 9600)
#arduino = serial.Serial('/dev/ttyUSB0', 9600)
#gps = serial.Serial('COM3', 9600)
#--------------------------------------------------


instruccion = raw_input("Cuando este listo presione y para iniciar \n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
    region = 1 + region2
    print(region)
    gps_sentece = gps.readline()
    gps_sentences_fields = gps_sentece.split(",")
    #FILTRO DE LA SENTENCIA $GPRMC
    if gps_sentences_fields[0] == "$GPRMC" and  gps_sentences_fields[2] == "A":
        get_unformated_latitude = float(gps_sentences_fields[3])
        get_unformated_longitude = float(gps_sentences_fields[5])
        latdeg = int(get_unformated_latitude/100)
        latmin = get_unformated_latitude - latdeg*100
        lat = latdeg + (latmin/60)
        latitud = round(lat,5)

        longdeg = int(get_unformated_longitude/100)
        longmin = get_unformated_longitude - longdeg*100
        longi = longdeg + (longmin/60)
        longitud = round(longi,5)

        if gps_sentences_fields[4] == "S":
            latitud = -latitud
        if  gps_sentences_fields[6] == "W":
            longitud = -longitud


        if region == 3:
            region =2
            print(region)



#-----------Calculo de distancia usando Harversine para region 1----------------------------
        if region == 1 :
            #Region 1   # 9.02318033 -79.53151733 original
            #Pruebas 9.04525 -79.40719
            latref =9.02327
            longref = -79.53143
            radius = 6371 # km
            dlat = math.radians(latref-latitud)
            dlon = math.radians(longref-longitud)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
            * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = int((radius*c)*1000)
            print d
            #Limites para las region1
            min1=80
            max1=4
            min2=4
            print("Region 1")
        	#min1 = 34
        	#max1 = 6  # min<--------------Region1--------------------------->max
        	#min2 = 6
        	#max2 =25"""
            #Prueba
            if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
                    #arduino.write(Forward) #Mandar un comando hacia Arduino
                bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
                print("Moviendo")

            if d <= min2:#Establece cuando curvara
                    #arduino.write(Turn)#Mandar un comando hacia Arduino
                bus.write_byte(slaveAddress2, Turn)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Turn)#Mandar un comando hacia MotorIzquierdo
                print("Curvando")
                time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
                region2=2


#-----------Calculo de distancia usando Harversine para region2----------------------------
        if region == 2 :
            #Region 2  #9.023149167 -79.53156583 original
            #Pruebas 9.04485 -79.40695
            latref2=9.02321
            lonref2=-79.53147
            radius = 6371 # km
            dlat = math.radians(latref2-latitud)
            dlon = math.radians(lonref2-longitud)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
            * math.cos(math.radians(latref2)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = int((radius*c)*1000)
            print d
            #Limite para Region 2
            min1=80
            max1=4
            min3=4
            print("Region 2")
    		#min1 = 7
    		#max1 = 2 # min<--------------Region2--------------------------->max
    		#min3 = 1
    		#max2 = 8"""
            #Prueba
            if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
                    #arduino.write(Forward) #Mandar un comando hacia Arduino
                bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
                print("Moviendo")

            if d <= min3:#Establece cuando curvara
                print("Detener")
                bus.write_byte(slaveAddress2, Stop)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Stop)#Mandar un comando hacia MotorIzquierdo
