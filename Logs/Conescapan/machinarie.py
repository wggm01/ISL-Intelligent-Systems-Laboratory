

#Inicializacion de librerias
import datetime
import time
#import serial
import csv
import math


delay = 5 #NO CREO QUE LO USE.
limit = 3
#Connecion al puerto serial
#gps = serial.Serial('COM14', 4800)
#gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)
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
    m1 =(ya[0]-ya[3])/(xa[0]-xa[3])
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



    





"""
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
