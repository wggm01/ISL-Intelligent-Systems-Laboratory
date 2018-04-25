
#Vectores como variables globales incializdas en 0 para luego ser modi.
p = [0,0] #Posicion dinamica
xa = [0,0] #X1 Y X2 corresponden a abcisas del punto inicio y finalsel.
ya = [0,0] #Y1 Y Y2 corresponden a ordenadas del punto inicio y finalsel.
q = [0,0] # Puntos virtual trasladado

#Latitud(x), Longitud(y)

#Normalización de puntos:
def in_dyna_gps (latitud,longitud):
    p[0]=latitud*1000
    p[1]=longitud*1000
    #Calculo de pendientes:
    m1 =(ya[1]-ya[0])/(xa[1]-xa[0])
    m2 = -1/m1
    #calculo de interseccion de ambas rectas,esto me da la lat,long (virtual)
    x = (m1*xa[0]-ya[0]+p[1]-m2*p[0])/(m1-m2)
    y = m1*(x-xa[0])+ya[0]
    q[0]=x
    q[1]=y
    #calculo de distancia entre punto virtual trasladado y punto de referenciaself.
    d_rest = math.sqrt(math.pow(xa[1]-q[0],2)+ math.pow(ya[1]-q[1],2))
    return d_rest
