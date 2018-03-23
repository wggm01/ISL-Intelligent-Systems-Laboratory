import time
import serial
import csv
import math
from vincenty import vincenty

#gps = serial.Serial('COM14', 4800)
gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)



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

        return latitud,longitud

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
