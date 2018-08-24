//1-hacia alfrente
//2-hacia atras
//3-Dobla hacia la izquierda
//4-Dobla hacia la derecha
//5-Detener
#include <Wire.h>
#define SLAVE_ADDRESS 0x50 //Direccion i2c del motor izquierda
/*---------------------------------------------------------------------------------*/
int control;
int delay2 =1;
int a, b;
/*---------------------------------------------------------------------------------*/
//MotorIzquierdo
int aPinm2; //INA 8
int bPinm2; //INB 10
int aPrimePinm2; //IND 9
int bPrimePinm2; //INC 11
/*---------------------------------------------------------------------------------*/

void setup() {
/*---------------------------------------------------------------------------------*/
  Wire.begin(SLAVE_ADDRESS);  // join i2c bus with address 0x50
  Wire.onReceive(receiveEvent); // register event
/*---------------------------------------------------------------------------------*/
  Serial.begin(9600);//inutil
  pinMode(LED_BUILTIN,OUTPUT);
/*---------------------------------------------------------------------------------*/
//Declaracion de pin Motor Izquierdo
  pinMode(aPinm2,      OUTPUT);
  pinMode(bPinm2,      OUTPUT);
  pinMode(aPrimePinm2, OUTPUT);
  pinMode(bPrimePinm2, OUTPUT);
/*---------------------------------------------------------------------------------*/
//bobinas en cero logico
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, LOW);
}

/*---------------------------------------------------------------------------------*/
//Funcion para mover motor izquierdo
void Mov_Mizq (){
  // 1. Set the aPin High
  digitalWrite(aPinm2,      HIGH);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 2. Energize aPin and bPin to HIGH
  digitalWrite(aPinm2,      HIGH);
  digitalWrite(bPinm2,      HIGH);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 3. Set the bPin to High
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      HIGH);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 4. Set the bPin and the aPrimePin to HIGH
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      HIGH);
  digitalWrite(aPrimePinm2, HIGH);
  digitalWrite(bPrimePinm2, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  //  5. Set the aPrime Pin to high
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, HIGH);
  digitalWrite(bPrimePinm2, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 6. Set the aPrimePin and the bPrime Pin to HIGH
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, HIGH);
  digitalWrite(bPrimePinm2, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 7. Set the bPrimePin to HIGH
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);

  // 8. Set the bPrimePin and the aPin to HIGH
  digitalWrite(aPinm2,      HIGH);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay2); // So, delay1 milliseconds
  //delayMicroseconds(delay2);
  }

  void Stop_Mizq(){
  digitalWrite(aPinm2,      LOW);
  digitalWrite(bPinm2,      LOW);
  digitalWrite(aPrimePinm2, LOW);
  digitalWrite(bPrimePinm2, LOW);
  }
//Recepción de Datos provenientes de la raspberry pi3 model B  Rev 2
void receiveEvent(int howMany) {

if (Wire.available()==1) { // loop through all but the last
  control = Wire.read();

  }}
/*---------------------------------------------------------------------------------*/
//Logica de movimiento
void loop() {
/*---------------------------------------------------------------------------------*/
while(control == 1){
      aPinm2 = 8; //INA 8
      bPinm2 = 10; //INB 10
      aPrimePinm2 = 9; //IND 9
      bPrimePinm2 = 11; //INC 11
      Mov_Mizq ();
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
     else if(control==8){break;}}
/*---------------------------------------------------------------------------------*/
/*---------------------------------------------------------------------------------*/
if(control == 2){
b=2;
  for(;;){ 
      aPinm2 = 11; //INC 11
      bPinm2 = 9; //IND 9
      aPrimePinm2 = 10; //INB 10
      bPrimePinm2 = 8; //INA 8
     
      switch (b){
        case 1 : control = 1;
        break;
        case 2 : Mov_Mizq ();
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
        default : control = 8;
        break;
      }
 return 0;
      //digitalWrite(LED_BUILTIN,HIGH);
      //delay(500);
      //digitalWrite(LED_BUILTIN,LOW); //Hacia atras
      //delay(500);
      /*digitalWrite(LED_BUILTIN,HIGH);
      delay(500);
      digitalWrite(LED_BUILTIN,LOW); //Hacia atras
      delay(500);*/
    }control =8; }
/*---------------------------------------------------------------------------------*/
   else if(control == 3){
      Stop_Mizq(); //Doblar hacia la izquierda
      control = 5;
 }
/*---------------------------------------------------------------------------------*/
   else if(control == 4){ 
a =4;
for (int i=0; i<400;){  // 210 para una vuelta de rueda
      aPinm2 = 8; //INA 8
      bPinm2 = 10; //INB 10
      aPrimePinm2 = 9; //IND 9
      bPrimePinm2 = 11; //INC 11
  
      switch (control){
        case 1 : control = 1;
        i = i+400;
        break;
        case 2: control = 2;
        i = i+400;
        break;
        case 3 : control = 3;
        i = i+400;
        break;
        case 4 : Mov_Mizq ();
        
        i = i+1;
        break;
        case 5 : control = 5;
        i = i+400;
        break;
        case 7 : control = 7;
        i = i+400;
        break;
        case 8 : control = 8;
        i = i+400;
        break;
        default : control = 8;
        break;
      }
    //digitalWrite(LED_BUILTIN,HIGH);
    //delay(100);
    //digitalWrite(LED_BUILTIN,LOW);//Dobla hacia la derecha
    //delay(100);
    /*digitalWrite(LED_BUILTIN,HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN,LOW);//Dobla hacia la derecha
    delay(100);*/
} control = 8; }
/*---------------------------------------------------------------------------------*/
 else if(control == 5){
      Stop_Mizq(); //Doblar hacia la izquierda
      control = 8;
 }
/*---------------------------------------------------------------------------------*/
 else if (control == 6){
  for (int i=0; i<2;){
      aPinm2 = 8; //INA 8   // Turbo Giro derecha
      bPinm2 = 10; //INB 10
      aPrimePinm2 = 9; //IND 9
      bPrimePinm2 = 11; //INC 11}
      Mov_Mizq ();
      i = i+1;
  }}
/*---------------------------------------------------------------------------------*/
 else if (control == 7){
   for (int i=0; i<2;){
     aPinm2 = 11; //INC 11 // Turbo Giro izquierda
     bPinm2 = 9; //IND 9
     aPrimePinm2 = 10; //INB 10
     bPrimePinm2 = 8; //INA 8
    Mov_Mizq ();
    i = i+1;
    }
 }
 
/*---------------------------------------------------------------------------------*/
}//Fin de la logica de movimiento

/*---------------------------------------------------------------------------------*/
