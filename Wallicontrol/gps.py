#Aqui se recojera las mediciones del gps, se ajustaran los  puntos y se calculara la distancia
#GPS.py
import machinarie
import datetime

while(True):

	if machinarie.check_gps == 1:
		data = machinarie.Data()
		if data!= None :
			latitud,longitud = data   #Revision de posicion acual sin procesarself.Data de gps sin tratar
			latitud_raw= latitud
			longitud_raw= longitud
			time= datetime.datetime.now()

			with open ("raw_coords.csv", "a") as pos:
				pos.write("%s, %s, %s \n" % ( latitud_raw, longitud_raw,time ))

        		nrp = machinarie.not_repeatcoord(latitud_raw,longitud_raw) #EVITA LA REPETICION DE COORDENADAS
        		if nrp != None:
				latitud,longitud = nrp
				virtual_0 = machinarie.virtual_pos0(latitud,longitud)
                		
                		latv0,lonv0= virtual_0

                		virtual_1 = machinarie.virtual_pos1(latitud,longitud)
                		
                		latv1,lonv1= virtual_1

                		virtual_2 = machinarie.virtual_pos2(latitud,longitud)
                		
                		latv2,lonv2= virtual_2

                		virtual_3 = machinarie.virtual_pos3(latitud,longitud)
                		
                		latv3,lonv3= virtual_3
                		with open ("Virtual_pos.csv", "a") as pos:
                        		pos.write("%s, %s, %s, %s, %s, %s, %s, %s\n" % ( latv0, lonv0, latv1, lonv1, latv2, lonv2, latv3, lonv3))


                		reg0 = machinarie.check_0drp(latitud,longitud,latv0,lonv0)
                		reg1 = machinarie.check_1drp(latitud,longitud,latv1,lonv1)
                		reg2 = machinarie.check_2drp(latitud,longitud,latv2,lonv2)
                		reg3 = machinarie.check_3drp(latitud,longitud,latv3,lonv3)

                		print("DRP0",reg0,"DRP1",reg1,"DRP2",reg2,"DRP3",reg3)

                		with open ("drp.csv", "a") as pos:
                        		pos.write("%s, %s, %s, %s\n" % ( reg0,reg1,reg2,reg3))
				
				d0=machinarie.distReg0(latv0,lonv0)
				

				d1=machinarie.distReg1(latv1,lonv1)
                                
				
				d2=machinarie.distReg2(latv2,lonv2)

				
				d3=machinarie.distReg3(latv3,lonv3)
				                

