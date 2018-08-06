#include <AccelStepper.h>
#include <Wire.h>
int control;
int velo=800;


AccelStepper mizq(AccelStepper::HALF4WIRE,8,9,10,11); 

void setup()
{  
    Wire.begin(0x40); 
    Wire.onReceive(receiveEvent); 
    Serial.begin(9600);
    mizq.enableOutputs();
    mizq.setMaxSpeed(1000);
    mizq.setSpeed(800);
    
}

void receiveEvent(int howMany) {

  if (Wire.available()>0) { 
  control = Wire.read();  
    }}
    
void loop()
{ 
//MOVIMIENTOS
if (control == 1){
  //HACIA DELANTE 
    //mizq.enableOutputs();
    mizq.runSpeed();
    //Serial.print(control);
    //Serial.println("Hacia delante");
    //control=11;
    
}else if(control == 4){
  //DERECHA 90 GRADOS CW
    mizq.run();
    mizq.move(360);
 
}else if (control == 3 || control== 13){
  //DETENER Y  IZQUIERDA 90 GRADOS
    //mizq.disableOutputs();
    mizq.disableOutputs();
  
    
}else if (control== 10){
  //DERECHA SOBRE EJE
    //mizq.enableOutputs();
    mizq.run();
    mizq.move(90);  
    control=11;
    
  
}else if(control==9){
  //IZQUIERDA SOBRE EJE GIRA  CCW
    //mizq.enableOutputs();
    mizq.run();
    mizq.move(-90);
    control=11;
    
}else if (control==2){
 //HACIA ATRAS 
  mizq.run();
  mizq.move(-360);
      
}else if (control==5){
  //IZQUIERDA ACKERMAN DISMINUYE VELOCIDAD CW
    mizq.setSpeed(velo-10);
    mizq.runSpeed();
    mizq.move(360);
    //mizq.enableOutputs();
    control=11;
    
    
}else if (control == 6){
  //DERECHA ACKERMAN AUMENTA VELOCIDAD CW
    mizq.setSpeed(velo+10);
    mizq.runSpeed();
    mizq.move(360);
    //mizq.enableOutputs();
    control=11;
    
  
}else if (control==7){
  //IZQUIERDA HACIA ATRAS ACKERMAN DISMINUYE VELOCIDAD  CCW
    //mizq.enableOutputs();
    mizq.setSpeed(velo-10);
    mizq.runSpeed();
    mizq.move(-360);
   
    
    control=11;
    
    
}else if (control==8){
  //DERECHA HACIA ATRAS ACKERMAN AUMENTA VELOCIDAD CCW
    //mizq.enableOutputs();
    mizq.setSpeed(velo+10);
    mizq.runSpeed();
    mizq.move(-360);
    
    control=11;
}




}
