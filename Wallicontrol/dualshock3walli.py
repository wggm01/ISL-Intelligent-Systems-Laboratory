import smbus
from triangula.input import SixAxisResource, SixAxis
slaveAddress2 = 0x40 #MotorIzquierdo
slaveAddress1 = 0x50 #MotorDerecho
bus = smbus.SMBus(1)
with SixAxisResource() as joystick:
    # Create a handler function
    def mov_f(button):
        bus.write_byte(slaveAddress2, 1)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 1)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i Hacia adelante")
    def mov_b(button):
        bus.write_byte(slaveAddress2, 2)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 2)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i Hacia atras")
    def mov_tr(button):
        bus.write_byte(slaveAddress2, 8)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 8)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i derecha")
    def mov_tl(button):
        bus.write_byte(slaveAddress2, 9)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 9)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i izquierda")
    def mov_sr(button):
        bus.write_byte(slaveAddress2, 6)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 6)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i esta rotando hacia la derecha")
    def mov_sl(button):
        bus.write_byte(slaveAddress2, 7)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 7)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i acutalmente esta rotando hacia la izquierda")
    def mov_s(button):
        bus.write_byte(slaveAddress2, 5)#Mandar un comando hacia MotorDerecho
        bus.write_byte(slaveAddress1, 5)#Mandar un comando hacia MotorIzquierdo
        print("Wall-i me detuve")

    # Register the handler to the SQUARE button
    joystick.register_button_handler(mov_f, SixAxis.BUTTON_D_UP)
    joystick.register_button_handler(mov_b, SixAxis.BUTTON_D_DOWN)
    joystick.register_button_handler(mov_tr, SixAxis.BUTTON_D_RIGHT)
    joystick.register_button_handler(mov_tl, SixAxis.BUTTON_D_LEFT)
    joystick.register_button_handler(mov_sr, SixAxis.BUTTON_R1)
    joystick.register_button_handler(mov_sl, SixAxis.BUTTON_L1)
    joystick.register_button_handler(mov_f, SixAxis.BUTTON_CROSS)
    while 1:
        # Do stuff here, only register the button handlers once, not in this loop!
        # If the buttons are pressed, your handlers will be called but not from this thread.
        pass
