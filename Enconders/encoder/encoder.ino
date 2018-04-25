//#include <TimerOne.h>
#include <Wire.h>
 //int vrp; //Vueltas rueda pequeña
 //int huecos;
 //int RPM; // de rueda pequeña
const byte input1=2;//MDER
const byte input2=3;//MIZQ
volatile int ticks1=0;//Contador de pulsos
volatile int ticks2=0;//Contador de pulsos
int control;
int distance=0; //cantidad de ticks para moverse una x distancia. 

void Ticks (){
  ticks1++;
  ticks2++;
  Serial.println(ticks1);
  Serial.println(ticks2);

  if (ticks1>=distance and ticks2>= distance){
    control = 5;
    
    }
}

/*void temporizador(){
  Timer1.detachInterrupt();
  vrp = (cdp/huecos)-6; //Por segundo
  Serial.println(vrp);
  RPM = vrp*60;
  Serial.println(RPM);
  cdp=0;
  Timer1.attachInterrupt(temporizador);*/
  
}
  
void setup() {
  Wire.begin(0X70);
  Wire.onRequest(requestEvent);
  Serial.begin(9600);
  pinMode(input1,INPUT_PULLUP);
  pinMode(input2,INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(input1),Ticks,LOW);
  attachInterrupt(digitalPinToInterrupt(input2),Ticks,LOW);
  //Timer1.attachInterrupt(timerIsr);
}


void loop() {

}

void requestEvent(){
  Wire.write(control);
  
  }



