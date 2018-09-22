#CODIGO ARMADO POR WVALDO GABRIEL GRAELL MANZANE WGGM
#CODIGO DESTINADO PARA PRUEBAS
import gps_test
import machinarie
limit = 3



print("Walk-e_test ha sido ejecutado")
while(True):

#Recepcion de variables

        if  gps_test.reg0 <= limit:

                machinarie.region0Bounds(gps_test.d0,gps_test.reg0)
		print("estoy en la region 0 wii!")

        elif gps_test.reg1 <= limit:
                machinarie.region1Bounds(gps_test.d1,gps_test.reg1)
		print("estoy en la region 1 wii!")

        elif gps_test.reg2 <= limit:
                machinarie.region2Bounds(gps_test.d2,gps_test.reg2)
		print("estoy en la region 2 wii!")

        elif gps_test.reg3 <= limit:
                machinarie.region3Bounds(gps_test.d3,gps_test.reg3)    
		print("estoy en la region 3 wii!")
        else:
                print("no se donde estoy :C ")

