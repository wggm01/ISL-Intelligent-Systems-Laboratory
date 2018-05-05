//#include <TimerOne.h>
#include <Wire.h>
volatile int RPM=0;
const byte input1=2;
const byte input2=3;
unsigned int ticks1=0;
unsigned int ticks2=0;
int distance; 

void ticks1 (){
  ticks1++;
}

void ticks2 (){
  ticks2++;
}

/*void timerIsr(){
  Timer1.detachInterrupt();
  RPM = (contador_de_pulsos/8);
  contador_de_pulsos=0;
  Timer1.attachInterrupt(timerIsr);
  
}*/
  
void setup() {
  Wire.begin(0X60); 
  Wire.onRequest(logicaControl);
  Wire.onReceive(receiveEvent);
  pinMode(input1,INPUT_PULLUP);
  pinMode(input2,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(input1),ticks1,RISING);
  attachInterrupt(digitalPinToInterrupt(input2),ticks2,RISING);//El mismo para los dos arduinos
  //Timer1.initialize(60000000);// Temporizador seteado a 1 segundo
  //Timer1.attachInterrupt(timerIsr);
}


void loop() {
  
  if ((ticks1+ticks2)/2 >= distance){
    control = 5;
    delay(500);
    control = 9;
    }
  

}
void logicaControl() { //Envio
  Wire.write(control);
}

void receiveEvent(int howMany) {
  int distance = Wire.read();    // Recibo
}


