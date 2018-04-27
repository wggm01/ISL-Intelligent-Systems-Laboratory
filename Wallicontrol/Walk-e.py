

limit = 0
#Ciclo repetido
print("Wall-i actualmente se encuentra esperando su instruccion")
instruccion = raw_input("Presion ""y"" y luego enter para empezar\n ")
while instruccion == 'y':

data = machinarie.Data()
if data!= None :
    latitud,longitud = data   #Revision de posicion acual sin procesarself.

    region = machinarie.check_drp(latitud,longitud)
    reg0,reg1,reg2,reg3= region #Separacion de las regiones

    if  reg0 <= limit:
        #codigo
        virtual = machinarie.virtual_pos0()
        latv,lonv= virtual
        d=machinarie.distReg1(latv,longv)
        machinarie.region0Bounds(d,reg0)

    elif reg1 <= limit:
        #codigo
        virtual = machinarie.virtual_pos1()
        latv,longv= virtual
        d=machinarie.distReg1(latv,longv)
        machinarie.region0Bounds(d,reg1)
    elif reg2 <= limit:
        #codigo
        virtual = machinarie.virtual_pos2()
        latv,longv= virtual
        d=machinarie.distReg1(latv,longv)
        machinarie.region0Bounds(d,reg2)
    elif reg3 <= limit;
        #codigo
        virtual = machinarie.virtual_pos3()
        latv,longv= virtual
        d=machinarie.distReg1(latv,longv)
        machinarie.region0Bounds(d,reg3)
