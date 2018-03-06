#include <Wire.h>
int aPin =8; //IN1: coil a one end
int bPin =9; //IN2: coil b one end
int aPrimePin =10 ; //IN3: coil aPrime other end of coil a
int bPrimePin =11; //IN4: coil bPrime other end of coil b
int delay1 = 2;    // The delay between each step in milliseconds
char a, b, x;



void setup() 
{
  Serial.begin(9600);
  Wire.begin();
 pinMode(aPin,      OUTPUT);
  pinMode(bPin,      OUTPUT);
  pinMode(aPrimePin, OUTPUT);
  pinMode(bPrimePin, OUTPUT);

  // Start with all coils off
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
}
//motores  m1||------||m2
void Forwardm1 (){
   // 1. Set the aPin High
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 2. Energize aPin and bPin to HIGH
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 3. Set the bPin to High
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 4. Set the bPin and the aPrimePin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      HIGH);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  //  5. Set the aPrime Pin to high
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 6. Set the aPrimePin and the bPrime Pin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, HIGH);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 7. Set the bPrimePin to HIGH
  digitalWrite(aPin,      LOW);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 8. Set the bPrimePin and the aPin to HIGH
  digitalWrite(aPin,      HIGH);
  digitalWrite(bPin,      LOW);
  digitalWrite(aPrimePin, LOW);
  digitalWrite(bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds
  
  }

void loop() 
{ b= Serial.read();
         while (a =='F')
           {Forwardm1 ();
              if (b != 'F')
              {x = 'T';
                break;}
           }
  while(Serial.available())
  {
     x = Serial.read();
    if(x == 'F')
    {
      a = 'F';
      Wire.beginTransmission(1);
      Wire.write('F');
      Wire.endTransmission();
  
    }
    else if(x == 'T')
    {
      Wire.beginTransmission(1);
      Wire.write('T');
      Wire.endTransmission();
     }
   }
}
  
