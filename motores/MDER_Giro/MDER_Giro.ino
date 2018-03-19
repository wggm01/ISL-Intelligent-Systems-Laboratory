//1-hacia alfrente
//2-hacia atras
//3-Dobla hacia la izquierda
//4-Dobla hacia la derecha
//5-Detener
#include <Wire.h>
#define SLAVE_ADDRESS 0x40 //Direccion i2c del motor derecho
/*---------------------------------------------------------------------------------*/
int control;
int delay1;
int a, b;
/*---------------------------------------------------------------------------------*/
//MotorDerecho
int aPin; //INA 2
int bPin; //IND 3
int aPrimePin; //INB 4
int bPrimePin; //INC 5
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
void Mov_Mder (){
  // 1. Set the aPin High
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 2. Energize aPin and bPin to HIGH
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 3. Set the bPin to High
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 4. Set the bPin and the aPrimePin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  //  5. Set the aPrime Pin to high
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 6. Set the aPrimePin and the bPrime Pin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 7. Set the bPrimePin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);

  // 8. Set the bPrimePin and the aPin to HIGH
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delayMicroseconds(delay1); // So, delay1 milliseconds
  //delayMicroseconds(delay1);
  }

void Stop_Mder(){
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  }
  //Recepción de Datos provenientes de la raspberry pi3 model B  Rev 2
void receiveEvent(int howMany) {

if (Wire.available()==1) { // loop through all but the last
  control = Wire.read();
}
} 
/*---------------------------------------------------------------------------------*/
//Logica de movimiento
void loop() {
/*---------------------------------------------------------------------------------*/
while(control == 1 || control == 9){
      aPin = 8; //INA 8
      bPin = 10; //INB 10
      aPrimePin = 9; //IND 9
      bPrimePin= 11; //INC 11
      delay1= 1000;
      Mov_Mder ();
      //digitalWrite(LED_BUILTIN,HIGH);
      //delay(1000);
      //digitalWrite(LED_BUILTIN,LOW); //Hacia alfrente
      //delay(1000);
      /*digitalWrite(LED_BUILTIN,HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN,LOW); //Hacia alfrente
      delay(1000);*/
      if(control==2){break;}
     else if(control==3){break;}
     else if(control==4){break;}
     else if(control==5){break;}
     else if(control==6){break;}
     else if(control==7){break;}
     else if(control==8){break;}
     else if(control==9){break;}
     else if(control==10){break;}}
/*---------------------------------------------------------------------------------*/
/*---------------------------------------------------------------------------------*/
if(control == 2){
b=2;
  for(int a =0; a<2;){ 
      aPin = 11; //INC 11
      bPin = 9; //IND 9
      aPrimePin = 10; //INB 10
      bPrimePin = 8; //INA 8
 
    switch (b){
        case 1 : control = 1;
        break;
        case 2 : 
        delay1= 1000;
        Mov_Mder ();
        b= control;
        break;
        case 3 : control = 3;
        break;
        case 4 : control = 4; 
        break;
        case 5 : control = 5;
        break;
        case 6 : control = 6;
        break;
        case 7 : control = 7;
        break;
        case 8: control = 8;
        break;
        case 9 : control = 9;
        break;
        default : control = 10;
        break;
     a = a+1;
      }
 
      //digitalWrite(LED_BUILTIN,HIGH);
      //delay(500);
      //digitalWrite(LED_BUILTIN,LOW); //Hacia atras
      //delay(500);
      /*digitalWrite(LED_BUILTIN,HIGH);
      delay(500);
      digitalWrite(LED_BUILTIN,LOW); //Hacia atras
      delay(500);*/
     
  }}
/*---------------------------------------------------------------------------------*/
   if(control == 3){
for (int i=0; i<400;){
      aPin = 8; //INA 8
      bPin = 10; //INB 10
      aPrimePin = 9; //IND 9
      bPrimePin = 11; //INC 11
      delay1= 1000;
    Mov_Mder ();
    //digitalWrite(LED_BUILTIN,HIGH);
    //delay(250);
    //digitalWrite(LED_BUILTIN,LOW);//Dobla hacia la izquierda
    //delay(250);
    /*digitalWrite(LED_BUILTIN,HIGH);
    delay(250);
    digitalWrite(LED_BUILTIN,LOW);//Dobla hacia la izquierda
    delay(250);*/
    i = i+1;

  }control = 10;}
/*---------------------------------------------------------------------------------*/
   if(control == 4){
      delay1= 1000;
      Stop_Mder(); //Doblar hacia la Derecha
      control = 5;
 }
/*---------------------------------------------------------------------------------*/
  else if(control == 5){
      Stop_Mder(); //Doblar hacia la izquierda
      control = 10;
 }
/*---------------------------------------------------------------------------------*/
 else if (control == 6){
  for (int i=0; i<2;){
      aPin = 11; //INC 11
      bPin = 9; //IND 9
      aPrimePin = 10; //INB 10
      bPrimePin = 8; //INA 8
      delay1= 1000;
      Mov_Mder ();
      i = i+1;
  }}
/*---------------------------------------------------------------------------------*/
 else if (control == 7){
   for (int i=0; i<2;){
      aPin = 8; //INA 8
      bPin = 10; //INB 10
      aPrimePin = 9; //IND 9
      bPrimePin = 11; //INC 11
      delay1= 1000;
    Mov_Mder ();
    i = i+1;
    }
 }
 
/*---------------------------------------------------------------------------------*/
 else if (control == 8){
     for ( int a =0; a<2;){
      aPin = 8; //INA 8
      bPin = 10; //INB 10
      aPrimePin = 9; //IND 9
      bPrimePin= 11; //INC 11
      delay1= 900;
      Mov_Mder ();
      a = a+1;
     }
 }


 
}


//Fin de la logica de movimiento                                                      
