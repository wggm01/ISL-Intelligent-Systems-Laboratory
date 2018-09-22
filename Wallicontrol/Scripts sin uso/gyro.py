import machinarie



print("Programa para recoleccion de data")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
#loop para que muestre cada lectura que recibe el gps
while instruccion == 'y':
	machinarie.Data_arduino_gyro()
