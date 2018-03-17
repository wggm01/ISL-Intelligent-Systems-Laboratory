
import machinarie



print("Programa para recoleccion de data")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
    data = machinarie.Data()
    if data!= None :
        latitud,longitud = data
 	with open ("Data_azuero.csv", "a") as pos:
		pos.write("%s, %s\n" % ( latitud, longitud))
    machinarie.Data_arduino()	
