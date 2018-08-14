#include <AccelStepper.h>
#include <Wire.h>
int control;
int velo;
#define hardrst 7;


AccelStepper mizq(AccelStepper::HALF4WIRE,8,9,10,11);

void setup()
{
  //COMUNICACION I2C
    Wire.begin(0x40);
    Wire.onReceive(receiveEvent);
    Serial.begin(9600); //UART
 //STEPPER
    mizq.setMaxSpeed(1000);
    mizq.setAcceleration(800);

    //hard reset
    digitalWrite(hardrst,HIGH);
    pinMode(hardrst,OUTPUT); //conectar pin7 a pin res
}

void receiveEvent(int howMany) {

  if (Wire.available()>0) {
  control = Wire.read(); }}

void loop()
{
  mizq.setCurrentPosition(0);

  if (control>14){
  int steps =  (control*1700)/0.31;
  mizq.run();
  mizq.runToNewPosition(steps);
  if(mizq.currentPosition()== steps){mizq.disableOutputs();}
  control=11;
  }
//MOVIMIENTOS
if (control == 1){
  //HACIA DELANTE

    //mizq.runSpeedToPosition();
    mizq.runToNewPosition(1700);
    mizq.moveTo(1700);
    if(mizq.currentPosition()== 1700){mizq.disableOutputs();}
    //Serial.print(control);
    //Serial.println("Hacia delante");
    control=11;

}else if(control == 4){
  //DERECHA 90 GRADOS CW
    mizq.run();
    mizq.runToNewPosition(1700);
    if(mizq.currentPosition()== 1700){mizq.disableOutputs();}
    control=11;

}else if (control == 3 || control== 13){
  //DETENER Y  IZQUIERDA 90 GRADOS
    //mizq.disableOutputs();
    mizq.disableOutputs();



}else if (control== 10){
  //DERECHA SOBRE EJE
    //mizq.enableOutputs();
    mizq.run();
    mizq.runToNewPosition(1700);
    if(mizq.currentPosition()== 1700){mizq.disableOutputs();}
    //control=11;


}else if(control==9){
  //IZQUIERDA SOBRE EJE GIRA  CCW
    //mizq.enableOutputs();
    mizq.run();
    mizq.move(-90);
    control=11;

}else if (control==2){
 //HACIA ATRAS
  mizq.run();
  mizq.runToNewPosition(-1700);
  if(mizq.currentPosition()== -1700){mizq.disableOutputs();}
  control=11;

}else if (control==5){
  //IZQUIERDA ACKERMAN DISMINUYE VELOCIDAD CW
    mizq.setSpeed(velo-10);
    mizq.runSpeed();
    mizq.move(360);
    //mizq.enableOutputs();
    control=11;


}else if (control == 6){
  //DERECHA ACKERMAN DISMINUYE VELOCIDAD CW
    mizq.setMaxSpeed(1000);
    mizq.setAcceleration(800);
    mizq.runToNewPosition(6800);
    if(mizq.currentPosition()== 6800){mizq.disableOutputs();}
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

}else if (control==20){
  //HARD RESET
  delay(3000);
  digitalWrite(hardrst,LOW);

}




}
