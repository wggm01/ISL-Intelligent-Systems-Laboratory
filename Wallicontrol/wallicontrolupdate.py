
import serial
import sys
import time
import machinarie
import smbus
region2=0
#Lectura del puerto serial
<<<<<<< HEAD
#gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)
=======
"""gps = serial.Serial("/dev/ttyACM0", baudrate = 4800)"""
>>>>>>> ba805980c0210b3a65b6a4a1a9fef22be178efda
#gps = serial.Serial('COM14', 4800)
delay = 5 #Este valor hay que estimarlo al ojo.
Forward=1
Turn= 4
Stop = 5
delay = 5 #Este valor hay que estimarlo al ojo.
slaveAddress2 = 0x40 #MotorIzquierdo
slaveAddress1 = 0x50 #MotorDerecho
bus = smbus.SMBus(1) #Bus por el cual se comunican"""

print("Wall-i actualmente se encuentra esperando su instruccion")
instruccion = raw_input("Presion y luego enter para empezar\n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
    region = 1 + region2
    if region == 3:
            region =2
    #velo=machinarie.veloWalli()
    #if velo != None:
     #   print ("La velocidad de Wall-i es de :",velo/1000,"m/s")
    data = machinarie.Data()
    if data!= None :
        latitud,longitud = data
        #print (latitud)
        #print (longitud)
        #reg1=machinarie.distReg1(latitud,longitud)
        #print(reg1)
        #reg2=machinarie.distReg2(latitud,longitud)
        #print(reg2)
        if region==1:
            #d=machinarie.distReg1(latitud,longitud)
            d=machinarie.distReg1_v(latitud,longitud)
            #drp = machinarie.angVariant(latitud,longitud,d)
            print("Wall-i esta a:",d," m De su objetivo")
            #print("Distancia a modelo:",drp)
            min1=80
            max1=2
            min2=2
            if d < min1 and d >= max1: #Establece hasta donde se movera en linea recta
                #arduino.write(Forward) #Mandar un comando hacia Arduino
                bus.write_byte(slaveAddress2, Forward)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Forward)#Mandar un comando hacia MotorIzquierdo
                print("Wall-i acutalmente se esta moviendo")

            if d <= min2:#Establece cuando curvara
                #arduino.write(Turn)#Mandar un comando hacia Arduino
                bus.write_byte(slaveAddress2, Turn)#Mandar un comando hacia MotorDerecho
                bus.write_byte(slaveAddress1, Turn)#Mandar un comando hacia MotorIzquierdo
                print("Wall-i actualmente esta curvando")
                time.sleep(delay) #tiempo que demora en hacer un giro de 90 grados aprox
                region2=2

        if region == 2:
            #d=machinarie.distReg2(latitud,longitud)
            d=machinarie.distReg2_v(latitud,longitud)
            print("Wall-i esta a:",d,"m De su objetivo")
            min1=80
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
