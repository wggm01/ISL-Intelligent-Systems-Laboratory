
#include <Wire.h>
#define SLAVE_ADDRESS 0X40
//Variable que decide que se hace
int control;
//Pines correspondientes a cada Relay
int RA=2;
int RB=3;
int RC=4;
int RD=5;

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveEvent);
  pinMode(RA,OUTPUT);
  pinMode(RB,OUTPUT);
  pinMode(RC,OUTPUT);
  pinMode(RD,OUTPUT);
}

void loop() {
 switch (control){
//Para encender relay's individualmente
  case 1:
    digitalWrite(RA,HIGH);
    control=9;
    break;
  case 2:
    digitalWrite(RB,HIGH);
    control=9;
    break;
  case 3:
    digitalWrite(RC,HIGH);
    control=9;
    break;
  case 4:
    digitalWrite(RD,HIGH);
    control=9;
    break;
//Para apagar relay's individualmente
  case 5:
    digitalWrite(RA,LOW);
    control=9;
    break;
  case 6:
    digitalWrite(RB,LOW);
    control=9;
    break;
  case 7:
    digitalWrite(RC,LOW);
    control=9;
    break;
  case 8:
    digitalWrite(RD,LOW);
    control=9;
    break;
  
  //default:
    // statements

  } 

}

//Recepción de Datos provenientes de la raspberry pi3 model B  Rev 2
void receiveEvent(int howMany) {

if (Wire.available()==1) { // loop through all but the last
  control = Wire.read();

  }}
