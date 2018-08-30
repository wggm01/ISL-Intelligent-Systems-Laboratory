#control de ejecucion de scripts
#main.py

#para correr multiples scripts en paralelo primero se crea una tupla con el nombre de todos los scripts.

#necesitamos una funcion que ejecute los comandos para correr los scripts para uso la libreria OS y el metodo
#.system, este permite ejecutar comando en la terminal (incluir sudo si es necesario).

#  necesito una clase pool de la libreria multiprocessing.

import os

from multiprocessing import tool

os.system('clear')
os.system('i2cdetect -y 1')
processes =('ultra.py','imu.py','batt.py')

def run_process(process):
        os.system('sudo python {}'.format(process))

pool = Pool(processes=3)
pool.map(run_process,processes)
