import datetime
import machinarie



print("Programa para recoleccion de data")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':


    data = machinarie.Data()
    if data!= None :
        latitud,longitud = data
        now = datetime.datetime.now()
 	with open ("conescapan.csv", "a") as pos:
		pos.write("%s, %s, %s\n" % ( latitud, longitud,now))
