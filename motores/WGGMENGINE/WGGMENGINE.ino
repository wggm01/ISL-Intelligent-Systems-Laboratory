#include <Stepper.h>
#include <Wire.h>
#define SLAVE_ADDRESS 0x40
const int stepsPerRevolution = 200;  //OBTENIDO POR EXPERIMENTACION
int control;

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
Serial.println(control);
} 
//MIZQ
void loop() {
  
  myStepper.setSpeed(150);
  switch (control){
        case 1 : 
          myStepper.step(stepsPerRevolution); //HACIA DELANTE
          Serial.println("F");
        break;
        case 2 : 
          myStepper.step(-stepsPerRevolution); //HACIA ATRAS
          Serial.println("B");
        break;
       }}
