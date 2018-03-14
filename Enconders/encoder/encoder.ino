#include <TimerOne.h>
#include <Wire.h>
 int vrp; //Vueltas rueda pequeña
 int RPM; // de rueda grande
const byte input=2;
volatile int cdp=0;//Contador de pulsos
int c=0;

void Raw_input (){
  cdp++;
}

void timerIsr(){
  Timer1.detachInterrupt();
  Serial.println(cdp);
  //RPM = vrp*60;
  //Serial.println(RPM);
  cdp=0;
  Timer1.attachInterrupt(timerIsr);
  
}
  
void setup() {
  Wire.begin(0X70);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  pinMode(input,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(input),Raw_input,FALLING); //El mismo para los dos arduinos
  Timer1.initialize(1000000);// Temporizador seteado a 1.63 segundo
  Timer1.attachInterrupt(timerIsr);
}


void loop() {

}

void requestEvent(){
  Wire.write(RPM);
  
  }



