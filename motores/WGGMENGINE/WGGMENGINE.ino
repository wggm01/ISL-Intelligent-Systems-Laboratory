#include <Stepper.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x40
const int stepsPerRevolution = 827;  //OBTENIDO POR EXPERIMENTACION
char control;

Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11); //AJUSTAR A LOS MOTORES

void setup() {
  //COMUNICACION I2C
  Wire.begin(SLAVE_ADDRESS); 
  Wire.onReceive(receiveEvent); 
  Serial.begin(9600);
}
//RECEPCION DE INSTRUCCIONES
void receiveEvent(int howMany) {

if (Wire.available()>0) { 
  control = Wire.read();
}
} 
//MIZQ
void loop() {
  myStepper.setSpeed(velo); //VELOCIDAD MAS BAJA
  switch (b){
        case "w" : 
          myStepper.step(stepsPerRevolution); //HACIA DELANTE
        break;
        case "s" : 
          myStepper.step(-stepsPerRevolution); //HACIA ATRAS
        break;
        case "a" :
          myStepper.step(stepsPerRevolution);//IZQ
        break;
        case "d" : 
          myStepper.step(0);//DER SOBRE LLANTA OPUESTA
        break;
        case "q" : 
          myStepper.step(stepsPerRevolution);//ACKERMAN IZQ
          myStepper.setSpeed(velo+10); //AJUSTE NECESARIO
        break;
        case "e" : 
          myStepper.step(stepsPerRevolution);//ACKERMAN DER
          myStepper.setSpeed(velo-10); //AJUSTE NECESARIO
        break;
        case "z" : 
          myStepper.step(-stepsPerRevolution);//ACKERMAN IZQ HACIA ATRAS
          myStepper.setSpeed(velo+10); //AJUSTE NECESARIO
        break;
        case "c": 
          myStepper.step(-stepsPerRevolution);//ACKERMAN DER HACIA ATRAS
          myStepper.setSpeed(velo-10); //AJUSTE NECESARIO
        break;
        case "x" : 
          myStepper.step(0);
        break;
        case "o" : 
          myStepper.step(-stepsPerRevolution);
        break;
        case "p" : 
          myStepper.step(stepsPerRevolution);
        break;}
  
}
