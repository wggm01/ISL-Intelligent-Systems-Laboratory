#Inicializacion de librerias
import time
import serial
import csv
import math
import smbus
from vincenty import vincenty
#Variables y Esclavos
slaveAddress2 = 0x40
slaveAddress1 = 0x50
sensorAdress = 0x60
bus = smbus.SMBus(1)
Forward=1
Backward =2
Turn= 4
TurnLeftEje = 7
Stop = 5
delay = 5
#Connecion al puerto serial
#gps = serial.Serial('COM14', 4800)
gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)
ard_gyro = serial.Serial("/dev/ttyACM1", baudrate = 57600)
#ard_ultra = serial.Serial("/dev/ttyACM", baudrate = 9600)


def Data():
    gps_sentece = gps.readline()
    gps_sentences_fields = gps_sentece.split(",")
    #FILTRO DE LA SENTENCIA $GPRMC
    if gps_sentences_fields[0] == "$GPRMC" and  gps_sentences_fields[2] == "A":
        get_unformated_latitude = float(gps_sentences_fields[3])
        get_unformated_longitude = float(gps_sentences_fields[5])
	time = gps_sentences_fields[1]
	date = gps_sentences_fields[9]

        latdeg = int(get_unformated_latitude/100)
        latmin = get_unformated_latitude - latdeg*100
        lat = latdeg + (latmin/60)
        latitud = round(lat,7)

        longdeg = int(get_unformated_longitude/100)
        longmin = get_unformated_longitude - longdeg*100
        longi = longdeg + (longmin/60)
        longitud = round(longi,7)

        if gps_sentences_fields[4] == "S":
            latitud = -latitud
        if  gps_sentences_fields[6] == "W":
            longitud = -longitud
        return latitud,longitud,date,time
    else:
        print ("Data no disponible aun,espere")

def Data_arduino_gyro():
    arduino = ard_gyro.readline()
    arduino_input = arduino.split(",")
    arduino_input[0] = x
    arduino_input[1] = y
    with open ("gyrodataazuero.csv", "a") as pos:
        pos.write("%s, %s\n" % ( x,y))

def Data_arduino_ultra():
    arduino = ard.readline()
    arduino_input = arduino.split(",")
    arduino_input[0] = s1
    arduino_input[1] = s2
    arduino_input[2] = s3
    arduino_input[3] = s4
    with open ("dataultrasonicos.csv", "a") as pos:
        pos.write("%s, %s\n" % ( x,y))

        

def distReg1(latitud,longitud):
    #Region 1 original 9.02318033 -79.53151733 (no forma parte del mapeo hecho orignalmente)
    #Promedio  9.0232113 -79.5315376 (Si forma parte del mapeo)
    #Pruebas alrededor de casa 9.04525 -79.40719
    #latref =9.04525 #Casa
    #longref = -79.40719
    latref =9.02318033
    longref = -79.53151733 #UTP
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 1"
    with open ("logreg1.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg1_v(latitud,longitud):
    input_gps= (latitud,longitud)
    #ref = (9.04525,-79.40719)
    ref = (9.02318033,-79.53151733)
    d = vincenty(input_gps,ref)*1000
    re= "Region 1"
    with open ("logreg1_v.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg1_pi(latitud,longitud):
    latref =9.02318033
    longref = -79.53151733 #UTP
    a=latref-latitud
    b=longref-longitud
    d=math.sqrt(math.pow(a,2)+math.pow(b,2))
    return d



def distReg2(latitud,longitud):
    #Region 2 orignal 9.023149167 -79.53156583 (demasiado de cerca de region 1)
    #Promedio 9.0230422 -79.5316507
    #Pruebas 9.04485 -79.40695 alrededor casa
    #latref2=9.04485 #casa
    #lonref2=-79.40695
    latref2=9.0230422 #UTP
    lonref2=-79.5316507
    radius = 6371 # km
    dlat = math.radians(latref2-latitud)
    dlon = math.radians(lonref2-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 2"
    with open ("logreg2.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg2_v(latitud,longitud):
    input_gps= (latitud,longitud)
    #ref = (9.04485,-79.40695)
    ref = (9.023149167,-79.53156583)
    d = vincenty(input_gps,ref)*1000
    re= "Region 2"
    with open ("logreg2_V.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg2_pi(latitud,longitud):
    latref2 =9.023149167
    longref2 = -79.53156583 #UTP
    a=latref2-latitud
    b=longref2-longitud
    d=math.sqrt(math.pow(a,2)+math.pow(b,2))
    return d

def veloWalli():
    gps_sentece = gps.readline()
    gps_sentences_fields = gps_sentece.split(",")
    #FILTRO DE LA SENTENCIA $GPRMC
    if gps_sentences_fields[0] == "$GPVTG":
        velocidad = float(gps_sentences_fields[7])
        return velocidad

def angVariant(latitud,longitud,d): #Usar bajo su propio riesgo
    #Distancia punto a recta
    top = 0.69738*latitud+longitud
    absolute= math.fabs(top)
    bottom = math.sqrt(math.pow(0.69738,2)+ 1)
    dpr = absolute/bottom
    #Calculo de angulo porque se forma un triangulo rectangulo.
    #angle = math.atan(dpr/d)
    return drp

def secCorrec ():
    if bus.read_byte(sensorAdress) == 9:
        bus.write_byte(slaveAddress2, Stop)
        bus.write_byte(slaveAddress1, Stop)
        time.sleep(2)
        bus.write_byte(slaveAddress2,Backward )
        bus.write_byte(slaveAddress1,Backward)
        time.sleep(2)
        bus.write_byte(slaveAddress2,Stop)
        bus.write_byte(slaveAddress1,Stop)
        time.sleep(2)
        bus.write_byte(slaveAddress2,TurnLeftEje)
        bus.write_byte(slaveAddress1,TurnLeftEje)
        time.sleep(3.21)
        bus.write_byte(slaveAddress2,Stop)
        bus.write_byte(slaveAddress1,Stop)
        time.sleep(2)
        bus.write_byte(slaveAddress2,Forward)
        bus.write_byte(slaveAddress1,Forward)
        time.sleep(2)
        bus.write_byte(slaveAddress2,Stop)
        bus.write_byte(slaveAddress1,Stop)
        time.sleep(2)
        bus.write_byte(slaveAddress2, Turn)
        bus.write_byte(slaveAddress1, Turn)
        time.sleep(3)
        
    elif bus.read_byte(sensorAdress) == 8:
        checkD2=2
        return checkD2
    
    else:
        bus.write_byte(slaveAddress2, Forward)
        bus.write_byte(slaveAddress1, Forward)
        
    
        
        
    

def region1Bounds(d):
    min1=200
    max1=2
    min2=2
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
        #arduino.write(Forward) #Mandar un comando hacia Arduino
        bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i acutalmente se esta moviendo")

    if d <= min2 :#Establece cuando curvara
        #arduino.write(Turn)#Mandar un comando hacia Arduino
        bus.write_byte(slaveAddress2, Turn)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, Turn)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i actualmente esta curvando")
        time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
        region2=2

def region2Bounds(d):
    min1=200
    max1=2
    min3=2
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
        #arduino.write(Forward) #Mandar un comando hacia Arduino
        bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i acutalmente se esta moviendo")

    if d <= min3:#Establece cuando curvara
        print("Wall-i actualmente esta curvando")
        bus.write_byte(slaveAddress2, Stop)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, Stop)#Mandar un comando hacia MotorIzquierdo


    
