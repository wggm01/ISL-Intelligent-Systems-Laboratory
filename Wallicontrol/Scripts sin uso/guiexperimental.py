from tkinter import *
from tkinter import ttk
#import smbus
#import controlbeta
#comandos
Forward=1
Backward=2
Turnleft=3
Turnright= 4
Stop = 5
Turnrighteje=7
Turnlefteje=6
TurnleftA=8
TurnrightA=9
#Funciones de control
def F():
        bus.write_byte(0X50, Forward)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Forward)#Mandar un comando hacia MotorIzquierdo
def B():
        bus.write_byte(0X50, Backward)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Backward)#Mandar un comando hacia MotorIzquierdo
def TI():
        bus.write_byte(0X50, Turnleft)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Turnleft)#Mandar un comando hacia MotorIzquierdo
def TD():
        bus.write_byte(0X50, Turnright)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Turnright)#Mandar un comando hacia MotorIzquierdo
def TIE():
        bus.write_byte(0X50, Turnlefteje)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Turnlefteje)#Mandar un comando hacia MotorIzquierdo
def TDE():
        bus.write_byte(0X50, Turnrighteje)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Turnrighteje)#Mandar un comando hacia MotorIzquierdo
def TIA():
        bus.write_byte(0X50, TurnleftA)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Turnlefta)#Mandar un comando hacia MotorIzquierdo
def TDA():
        bus.write_byte(0X50, TurnrightA)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, TurnrightA)#Mandar un comando hacia MotorIzquierdo
def S():
        bus.write_byte(0X50, Stop)#Mandar un comando hacia MotorDerecho
        bus.write_byte(0X40, Stop)#Mandar un comando hacia MotorIzquierdo

root = Tk()

"""ds1_input=str(bus.read_data(0x80,sensor1))
ds2_input=str(bus.read_data(0x80,sensor2))
ds3_input=str(bus.read_data(0x80,sensor3))
imu_xinput=str(bus.read_data())
imu_yinput=str(bus.read_data())
rpm_derinput=str(bus.read_data(0x50))
rpm_izqinput=str(bus.read_data(0x40))
gps_disinput=str(d)
bus = smbus.SMBus(1)"""

ds1_input=str("NAN")
ds2_input=str("NAN")
ds3_input=str("NAN")
imu_xinput=str("NAN")
imu_yinput=str("NAN")
rpm_derinput=str("NAN")
rpm_izqinput=str("NAN")
gps_disinput=str("NAN")


ds1_input_str=StringVar()
ds2_input_str=StringVar()
ds3_input_str=StringVar()
imu_xinput_str=StringVar()
imu_yinput_str=StringVar()
rpm_inputder_str=StringVar()
rpm_inputizq_str=StringVar()
gps_disinput_str=StringVar()

#Titulos
ds = ttk.Label(root, text='Distancia_sensores',relief='sunken',padding=10)
imu = ttk.Label(root, text='IMU',relief='sunken',padding=10)
rpm = ttk.Label(root, text='RPM',relief='sunken',padding=10)
cm = ttk.Label(root, text='Control manual',relief='sunken',padding=10)
gps = ttk.Label(root, text='gps_distancia',relief='sunken',padding=10)
#Subtitulos
ds1 = ttk.Label(root, text='Distancia_sensor1',relief='sunken',padding=10)
ds2 = ttk.Label(root, text='Distancia_sensor2',relief='sunken',padding=10)
ds3 = ttk.Label(root, text='Distancia_sensor3',relief='sunken',padding=10)
imu_x = ttk.Label(root, text='IMU_x',relief='sunken',padding=10)
imu_y = ttk.Label(root, text='IMU_y',relief='sunken',padding=10)
rpm_derecho = ttk.Label(root, text='RPM_der',relief='sunken',padding=10)
rpm_izquierdo = ttk.Label(root, text='RPM_izq',relief='sunken',padding=10)

#Espaciones en blanco para los valores
ds1_value = ttk.Label(root,textvariable=ds1_input_str,relief='sunken',padding=5)
ds2_value = ttk.Label(root,textvariable=ds2_input_str,relief='sunken',padding=5)
ds3_value = ttk.Label(root,textvariable=ds3_input_str,relief='sunken',padding=5)
imu_x_value = ttk.Label(root,textvariable=imu_xinput_str,relief='sunken',padding=5)
imu_y_value = ttk.Label(root,textvariable=imu_yinput_str,relief='sunken',padding=5)
rpm_derecho_value = ttk.Label(root,textvariable=rpm_inputder_str,relief='sunken',padding=5)
rpm_izquierdo_value = ttk.Label(root,textvariable=rpm_inputizq_str,relief='sunken',padding=5)
gps_dist_value = ttk.Label(root,textvariable=gps_disinput_str,relief='sunken',padding=5)


#Botones para control manual
F = ttk.Button(root, text='F',command=F)
B = ttk.Button(root, text='B',command=B)
TI = ttk.Button(root, text='TL',command=TI)
TD = ttk.Button(root, text='TR',command =TD)
TIE = ttk.Button(root, text='TLE',command=TIE)
TDE = ttk.Button(root, text='TRE',command=TDE)
TIA = ttk.Button(root, text='TLA',command=TIA)
TDA = ttk.Button(root, text='TRA',command=TDA)
S = ttk.Button(root, text='S')

#Titulos para los sensores
ds.grid(column=0, row=0)
imu.grid(column=0, row=2)
rpm.grid(column=0, row=4)
cm.grid(column=0, row=7)
gps.grid(column=0, row=6)
#Subtitulos para cuando hay mas de un sensor del mismo tipo
ds1.grid(column=1, row=0)
ds2.grid(column=2, row=0)
ds3.grid(column=3, row=0)
imu_x.grid(column=1, row=2)
imu_y.grid(column=2, row=2)
rpm_derecho.grid(column=1, row=4)
rpm_izquierdo.grid(column=2, row=4)

#Espacios en blanco para valores
ds1_value.grid(column=1, row=1)
ds2_value.grid(column=2, row=1)
ds3_value.grid(column=3, row=1)
imu_x_value.grid(column=1, row=3)
imu_y_value.grid(column=2, row=3)
rpm_derecho_value.grid(column=1, row=5)
rpm_izquierdo_value.grid(column=2, row=5)
gps_dist_value.grid(column=1, row=6)
#Botones para el control manual
F.grid(column=1, row=7)
B.grid(column=2, row=7)
TI.grid(column=3, row=7)
TD.grid(column=4, row=7)
TIE.grid(column=5, row=7)
TDE.grid(column=6, row=7)
TIA.grid(column=7, row=7)
TDA.grid(column=8, row=7)
S.grid(column=9, row=7)

ds1_input_str.set(ds1_input)
ds2_input_str.set(ds2_input)
ds3_input_str.set(ds3_input)
imu_xinput_str.set(imu_xinput)
imu_yinput_str.set(imu_yinput)
rpm_inputder_str.set(rpm_derinput)
rpm_inputizq_str.set(rpm_izqinput)
gps_disinput_str.set(gps_disinput)




root.mainloop()
