#include <TimerOne.h>
#include <Wire.h>
 int vrp; //Vueltas rueda pequeña
 int huecos;
 int RPM; // de rueda pequeña
const byte input=2;
volatile int cdp=0;//Contador de pulsos

void Raw_input (){
  cdp++;
}

void temporizador(){
  Timer1.detachInterrupt();
  vrp = (cdp/huecos)-6; //Por segundo
  Serial.println(vrp);
  RPM = vrp*60;
  Serial.println(RPM);
  cdp=0;
  Timer1.attachInterrupt(temporizador);
  
}
  
void setup() {
  Wire.begin(0X70);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  pinMode(input,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(input),Raw_input,FALLING); 
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(timerIsr);
}


void loop() {

}

void requestEvent(){
  Wire.write(RPM);
  
  }



