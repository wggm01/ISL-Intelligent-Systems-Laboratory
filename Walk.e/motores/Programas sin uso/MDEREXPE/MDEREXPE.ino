//1-hacia alfrente
//2-hacia atras
//3-Dobla hacia la izquierda
//4-Dobla hacia la derecha
//5-Detener
#include <Wire.h>
#define SLAVE_ADDRESS 0x40 //Direccion i2c del motor derecho
/*---------------------------------------------------------------------------------*/
int control;
int control_old;
int delay1= 1;
int count=1;
//float delay1= 1;
/*---------------------------------------------------------------------------------*/
//MotorDerecho
int aPin; //INA 2
int bPin; //IND 3
int aPrimePin; //INB 4
int bPrimePin; //INC 5
//Estados logicos

/*---------------------------------------------------------------------------------*/

void setup() {
/*---------------------------------------------------------------------------------*/
  Wire.begin(SLAVE_ADDRESS); // join i2c bus with address 0x40
 Wire.onReceive(receiveEvent); // register event
/*---------------------------------------------------------------------------------*/
  Serial.begin(9600);//inutil
  pinMode(LED_BUILTIN,OUTPUT);
/*---------------------------------------------------------------------------------*/
  //Declaracion de pin Motor Derecho
  pinMode(aPin,      OUTPUT);
  pinMode(bPin,      OUTPUT);
  pinMode(aPrimePin, OUTPUT);
  pinMode(bPrimePin, OUTPUT);
/*---------------------------------------------------------------------------------*/
  //bobinas en cero logico
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
}
/*---------------------------------------------------------------------------------*/
//Funcion para mover motor derecho
void Stop_Mder(){
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  }

void Mov_Mder (int control_rec){
  control_rec = control_old;
  if(control_old == 2){aPin=11;bPin=9;aPrimePin=10;bPrimePin=8;}
  else{aPin=8;bPin=10;aPrimePin=9;bPrimePin=11;}
  
  while (control_old == control){
   switch (count) {
  case 1:digitalWrite(aPin,HIGH);delayMicroseconds(delay1);break;
  case 2:digitalWrite(bPin,HIGH);delayMicroseconds(delay1);break;
  case 3:digitalWrite(aPin,LOW);delayMicroseconds(delay1);break;
  case 4:digitalWrite(aPrimePin,HIGH);delayMicroseconds(delay1);break;
  case 5:digitalWrite(bPin,LOW);delayMicroseconds(delay1);break;
  case 6:digitalWrite(bPrimePin,HIGH);delayMicroseconds(delay1);break;
  case 7:digitalWrite(aPrimePin,LOW);delayMicroseconds(delay1);break;
  case 8:digitalWrite(aPin,HIGH);delayMicroseconds(delay1);break;
  default:count=1;break;}count = count+1;
  if(control_old != control){break;}
  
  }}



void loop() {
if(control == 1 || control==2){
Mov_Mder (control);}
else if (control == 3 || control==5){Stop_Mder();}
}


/*---------------------------------------------------------------------------------*/
//Recepción de Datos provenientes de la raspberry pi3 model B  Rev 2
void receiveEvent(int howMany) {

if (Wire.available()== 1) { // loop through all but the last
  control = Wire.read();

 }}                                                                                                                                                                

