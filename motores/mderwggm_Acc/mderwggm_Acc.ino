#include <AccelStepper.h>
#include <Wire.h>

int control;
int velo=150; //velocidad

AccelStepper mder(AccelStepper::HALF4WIRE,8,9,10,11);

void setup() {
  //LCD
 
  
  //COMUNICACION I2C
  Wire.begin(0x50); 
  Wire.onReceive(receiveEvent);
  
  //STEPPER 
 
  mder.setMaxSpeed(2000);
  mder.setSpeed(1000);
  Serial.begin(9600);
  
}
//RECEPCION DE INSTRUCCIONES
void receiveEvent(int howMany) {

if (Wire.available()>0) { 
  control = Wire.read();  
}
}
 
void loop() {
  
//MOVIMIENTOS  
if (control == 1){
  //HACIA DELANTE 
    //mizq.enableOutputs();
    mder.runSpeed();
    
    
}else if (control == 4 || control== 13){
  //DETENER Y  IZQUIERDA 90 GRADOS
    //mizq.disableOutputs();
     mder.disableOutputs();
    
    
}else if(control == 3){
  //DERECHA 90 GRADOS CW
    mder.run();
    mder.move(360);
 
}else if (control== 10){
  //DERECHA SOBRE EJE
    //mizq.enableOutputs();
    mder.run();
    mder.move(-90);  
    control=11; 
    
}else if(control==9){
  //IZQUIERDA SOBRE EJE GIRA  CCW
    //mizq.enableOutputs();
    mder.run();
    mder.move(90);
    control=11;
    
}else if (control==2){
 //HACIA ATRAS 
  mder.setPinsInverted(true,true,true,true,true);
  mder.runSpeed();
      
}else if (control==5){
  //IZQUIERDA ACKERMAN DISMINUYE VELOCIDAD CW
    mder.setSpeed(velo+10);
    mder.runSpeed();
    mder.move(360);
    //mizq.enableOutputs();
    control=11;
        
}else if (control == 6){
  //DERECHA ACKERMAN AUMENTA VELOCIDAD CW
    mder.setSpeed(velo-10);
    mder.runSpeed();
    mder.move(360);
    //mizq.enableOutputs();
    control=11;
   
}else if (control==7){
  //IZQUIERDA HACIA ATRAS ACKERMAN DISMINUYE VELOCIDAD  CCW
    //mizq.enableOutputs();
    mder.setSpeed(velo+10);
    mder.runSpeed();
    mder.move(-360);
    control=11;  
     
}else if (control==8){
  //DERECHA HACIA ATRAS ACKERMAN AUMENTA VELOCIDAD CCW
    //mizq.enableOutputs();
    mder.setSpeed(velo-10);
    mder.runSpeed();
    mder.move(-360);
    
    control=11;
}

 
    
}
