#Librerias de gpio
from RPi import GPIO
global clk1
global dt1
global clk2
global dt2
clk1=5
dt1=13
clk2=6
dt2=19
#seteo de pines del gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #ENCODER
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
derecha1 = 0
izquierda1 = 0
derecha2 = 0
izquierda2 = 0

CLS1 = GPIO.input(clk1)
CLS2 = GPIO.input(clk2)


#Inicializacion de librerias
import datetime
import time
import serial
import csv
import math
import smbus2
from smbus2 import SMBus
from smbus2 import SMBusWrapper
#from vincenty import vincenty
#Variables y Esclavos
slaveAddress2 = 0x40                    #LIBRERIAS, ESCLAVOS Y INSTRUCCIONES
slaveAddress1 = 0x50
sensorAdress = 0x60
bus = SMBus(1)
Forward=1
Backward =2
Turn= 4
TurnLeftEje = 7
Stop = 5
delay = 5
limit = 2
#Connecion al puerto serial
#gps = serial.Serial('COM14', 4800)
gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)
#ard_gyro = serial.Serial("/dev/ttyACM1", baudrate = 9600)
#ard_ultra = serial.Serial("/dev/ttyACM", baudrate = 9600)

#Vectores como variables globales incializdas en 0 para luego ser modi.
global p
global xa
global ya
global q
global drp
p = [0,0] #Posicion dinamica
xa = [-79.53169299,-79.53152138,-79.53177739,-79.53184155] #X1 Y X2 corresponden a abcisas del punto inicio y finalsel.
ya = [9.023410836,9.023175628,9.022897331,9.023147334] #Y1 Y Y2 corresponden a ordenadas del punto inicio y finalsel.
q = [0,0] # Puntos virtual trasladado
drp = [0,0,0,0]#una para cada modelo y0,y1,y2,y3

def wr_i2c (instruction):
    with SMBusWrapper(1) as bus:
    # Write a byte to address 80, offset 0
        data = instruction  
        bus.write_byte_data(slaveAddress1, 0, data)
        bus.write_byte_data(slaveAddress2, 0, data)

#Latitud(x), Longitud(y)
def Data():
    gps_sentece = gps.readline()
    gps_sentences_fields = gps_sentece.split(",")
    #FILTRO DE LA SENTENCIA $GPRMC
    if gps_sentences_fields[0] == "$GPRMC" and  gps_sentences_fields[2] == "A":
        get_unformated_latitude = float(gps_sentences_fields[3])
        get_unformated_longitude = float(gps_sentences_fields[5])


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
        now = datetime.datetime.now()
    else:
        print("Aun no se recibe informacion viable del gps")
        with open ("conescapan.csv", "a") as pos:
            pos.write("%s, %s, %s\n" % ( latitud, longitud,now))
    #else:
     #   print("Esperando senal de aprobacion por parte del gps")
        return latitud,longitud

#Calculo de de distancia para cada region (cambiar referencia en cada uno)
def distReg0(latitud,longitud):
    latref =9.023175628
    longref = -79.53152138 #UTP
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 0"
    with open ("logreg0.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg1(latitud,longitud):
    latref2=9.022897331#UTP
    lonref2=-79.53177739
    radius = 6371 # km
    dlat = math.radians(latref2-latitud)
    dlon = math.radians(lonref2-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 1"
    with open ("logreg1.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg2(latitud,longitud):
    latref =9.023147334
    longref = -79.53184155 #UTP
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 2"
    with open ("logreg2.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

def distReg3(latitud,longitud):
    latref2=9.023410836 #UTP
    lonref2=-79.53169299
    radius = 6371 # km
    dlat = math.radians(latref2-latitud)
    dlon = math.radians(lonref2-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    re= "Region 3"
    with open ("logreg3.csv", "a") as pos:
        pos.write("%s, %s, %s, %s\n" % ( latitud, longitud, d, re ))
    return d

#Limites de desplazamiento del robot
def region0Bounds(d,reg0):
    min1=200 #colocar
    max1=2
    min2=3
    ed0 = enco_check_reg0(d)
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
       # wr_i2c(Forward)
        print("Wall-i acutalmente se esta moviendo reg0")

    if d <= min2 and ed0 != 0:#Establece cuando curvara
        #arduino.write(Turn)#Mandar un comando hacia Arduino
        #wr_i2c(Turn)
        print("Wall-i actualmente esta curvandoreg0")
        time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
        #bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
        #bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo

def region1Bounds(d,reg1):
    min1=200 #colocar
    max1=2
    min3=3
    ed1 = enco_check_reg1(d)
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
        wr_i2c(Forward)
        print("Wall-i acutalmente se esta moviendoreg1")

    if d <= min3 and ed1 != 0:#Establece cuando curvara
        wr_i2c(Turn)
        print("Wall-i actualmente esta curvando reg1")
        time.sleep(delay)

def region2Bounds(d,reg2):
    min1=200 #colocar
    max1=2
    min2=3
    ed2 = enco_check_reg2(d)
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
        wr_i2c(Forward)
        print("Wall-i acutalmente se esta moviendoreg2")

    if d <= min2 and ed2!= 0:#Establece cuando curvara
        wr_i2c(Turn)
        print("Wall-i actualmente esta curvandoreg2")
        time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
        #bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
        #bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo

def region3Bounds(d,reg3):
    min1=200 #colocar
    max1=2
    min3=3
    ed3 = enco_check_reg3(d)
    if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
        wr_i2c(Forward)
        print("Wall-i acutalmente se esta moviendoreg3")

    if d <= min3 and ed3!= 0:#Establece cuando curvara
        wr_i2c(Turn)
        print("Wall-i actualmente esta curvandoreg3")
        time.sleep(delay)

#Traslacion de coordenadas
def virtual_pos0 (latitud,longitud):
    p[0]=longitud#x
    p[1]=latitud
    
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x#Longitud
    q[1]=y#Latitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[1],q[0]

def virtual_pos1 (latitud,longitud):
    p[0]=longitud#x
    p[1]=latitud
    #Calculo de pendientes:
    m1 =(ya[2]-ya[1])/(xa[2]-xa[1])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[1]-ya[1]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[1])+ya[1]
    q[0]=x#Longitud
    q[1]=y#Latitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[1],q[0]

def virtual_pos2 (latitud,longitud):
    p[0]=longitud#x
    p[1]=latitud
    #Calculo de pendientes:
    m1 =(ya[3]-ya[2])/(xa[3]-xa[2])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[2]-ya[2]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[2])+ya[2]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[1],q[0]

def virtual_pos3 (latitud,longitud):
    p[0]=longitud#x
    p[1]=latitud
    #Calculo de pendientes:
    m1 =(ya[1]-ya[3])/(xa[1]-xa[3])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[3]-ya[3]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[3])+ya[3]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[1],q[0]

#Chequeo de punto actual del robot a recta
def check_0drp (latitud,longitud,latref,longref):
    #Calculo de distancia a los modelos
    #latv0=latref
    #lonv0=longref
    print(latitud,longitud,latref,longref)
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    drp[0]= d
    
    return drp[0]

def check_1drp (latitud,longitud,latv1,lonv1):
    #Calculo de distancia a los modelos
    latref = latv1
    longref = lonv1
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    drp[1]=d
    
    return drp[1]

def check_2drp (latitud,longitud,latv2,lonv2):
    #Calculo de distancia a los modelos
    latref = latv2
    longref = lonv2
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    drp[2]=d
    
    return drp[2]

def check_3drp (latitud,longitud,latv3,lonv3):
    #Calculo de distancia a los modelos
    latref = latv3
    longref = lonv3
    radius = 6371 # km
    dlat = math.radians(latref-latitud)
    dlon = math.radians(longref-longitud)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitud)) \
    * math.cos(math.radians(latref)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d_raw = float((radius*c)*1000)
    d = int(d_raw)
    drp[3]=d
  
    return drp[3]

#------------------------
def enco_check_reg0(d):
    i=0
    for n in range (0,i+1)
	count_R=d
        break

    count = (91*count_R)/31 # distancia de region en ticks
    CS1 = GPIO.input(clk1)
    DTS1 = GPIO.input(dt1)
    CS2 = GPIO.input(clk2)
    DTS2 = GPIO.input(dt2)
    if CS1 != CLS1:
        if DTS1 != CS1:
            derecha1 += 1
    if CS2 != CLS2:
        if DTS1 != CS1:
            derecha2 += 1
    if (derecha1 > count) or (derecha2 > count):
        edr0 = 1
        return edr0
    else:
        edr0 = 0
         

     
#--------------------------
def enco_check_reg1(d):
    count = 294 # distancia de region en ticks
    CS1 = GPIO.input(clk1)
    DTS1 = GPIO.input(dt1)
    CS2 = GPIO.input(clk2)
    DTS2 = GPIO.input(dt2)
    if CS1 != CLS1:
        if DTS1 != CS1:
            derecha1 += 1
    if CS2 != CLS2:
        if DTS1 != CS1:
            derecha2 += 1
    if (derecha1 > count) or (derecha2 > count):
        edr1 = 1
        return edr0
    else:
        edr1 = 0
#--------------------------      
def enco_check_reg2(d):
    count = 294 # distancia de region en ticks
    CS1 = GPIO.input(clk1)
    DTS1 = GPIO.input(dt1)
    CS2 = GPIO.input(clk2)
    DTS2 = GPIO.input(dt2)
    if CS1 != CLS1:
        if DTS1 != CS1:
            derecha1 += 1
    if CS2 != CLS2:
        if DTS1 != CS1:
            derecha2 += 1
    if (derecha1 > count) or (derecha2 > count):
        edr2 = 1
        return edr0
    else:
        edr2 = 0
#--------------------------
def enco_check_reg3(d):
    count = 294 # distancia de region en ticks
    CS1 = GPIO.input(clk1)
    DTS1 = GPIO.input(dt1)
    CS2 = GPIO.input(clk2)
    DTS2 = GPIO.input(dt2)
    if CS1 != CLS1:
        if DTS1 != CS1:
            derecha1 += 1
    if CS2 != CLS2:
        if DTS1 != CS1:
            derecha2 += 1
    if (derecha1 > count) or (derecha2 > count):
        edr3 = 1
        return edr0
    else:
        edr3 = 0         
      
def flag_sensor_dist():
    if bus.read_byte(slave_dist_sensor)==8:
        return 8
    elif bus.read_byte(slave_dist_sensor)== 9:
        return 9

    else:
        return 1
    





"""
def Data_arduino_gyro():
    arduino = ard_gyro.readline()

    with open ("gyrodata.txt", "a") as pos:
        pos.write("%s\n" % (arduino))
    print(arduino)

def Data_arduino_ultra():
    arduino = ard.readline()
    arduino_input = arduino.split(",") #Le falta trabajo
    arduino_input[0] = s1
    arduino_input[1] = s2
    arduino_input[2] = s3
    arduino_input[3] = s4
    with open ("dataultrasonicos.csv", "a") as pos:
        pos.write("%s, %s\n" % ( x,y))

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
"""
