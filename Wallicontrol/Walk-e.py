#CODIGO ARMADO POR WVALDO GABRIEL GRAELL MANZANE WGGM
#VERSION: RETO TOKIO
import gps
import machinarie
limit = 3




while(True):

#Recepcion de variables
		
	if  gps.reg0 <= limit:
        	
        	machinarie.region0Bounds(gps.d0,gps.reg0)

	elif gps.reg1 <= limit:
        	machinarie.region1Bounds(gps.d1,gps.reg1)


	elif gps.reg2 <= limit:
        	machinarie.region2Bounds(gps.d2,gps.reg2)

		
	elif gps.reg3 <= limit:
        	machinarie.region3Bounds(gps.d3,gps.reg3)    

	else:
		print("no se donde estoy")
