
#Vectores como variables globales incializdas en 0 para luego ser modi.
p = [0,0] #Posicion dinamica
xa = [0,0,0,0,] #X1 Y X2 corresponden a abcisas del punto inicio y finalsel.
ya = [0,0,0,0] #Y1 Y Y2 corresponden a ordenadas del punto inicio y finalsel.
q = [0,0] # Puntos virtual trasladado
drp = [0,0,0,0]#una para cada modelo y0,y1,y2,y3

#Latitud(x), Longitud(y)

#Normalización de puntos:
def virtual_pos0 (latitud,longitud):
    p[0]=latitud
    p[1]=longitud
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[0],q[1]

def virtual_pos1 (latitud,longitud):
    p[0]=latitud
    p[1]=longitud
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[0],q[1]

def virtual_pos2 (latitud,longitud):
    p[0]=latitud
    p[1]=longitud
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[0],q[1]

def virtual_pos3 (latitud,longitud):
    p[0]=latitud
    p[1]=longitud
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x#Latitud
    q[1]=y#Longitud
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    #d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))

    return q[0],q[1]

def check_drp (latitud,longitud):
    #Calculo de distancia a los modelos
    #    drp[0]= #y0
    #    drp[1]= #y1
    #    drp[2]= #y2
    #    drp[3]= #y3
    return drp[0],drp[1],drp[2],drp[3]
