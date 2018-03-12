#include <TimerOne.h>
volatile int RPM=0;
const byte input=2;
unsigned int contador_de_pulsos=0;

void Raw_input (){
  contador_de_pulsos++;
}

void timerIsr(){
  Timer1.detachInterrupt();
  RPM = (contador_de_pulsos/8);
  contador_de_pulsos=0;
  Timer1.attachInterrupt(timerIsr);
  
}
  
void setup() {
  pinMode(input,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(input),Raw_input,RISING); //El mismo para los dos arduinos
  Timer1.initialize(60000000);// Temporizador seteado a 1 segundo
  Timer1.attachInterrupt(timerIsr);
}


void loop() {
  // put your main code here, to run repeatedly:

}


