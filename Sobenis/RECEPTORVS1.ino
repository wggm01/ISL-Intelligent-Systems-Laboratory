#include <Wire.h>

int m2aPin =2; //IN1: coil a one end
int m2bPin =3; //IN2: coil b one end
int m2aPrimePin =4 ; //IN3: coil aPrime other end of coil a
int m2bPrimePin =5;//IN4: coil bPrime other end of coil b
// We do not connect IN5, IN6, or IN7
int delay1 = 2;    // The delay between each step in milliseconds
char a;

void setup() 
{

  pinMode(m2aPin,      OUTPUT);
  pinMode(m2bPin,      OUTPUT);
  pinMode(m2aPrimePin, OUTPUT);
  pinMode(m2bPrimePin, OUTPUT);
 
  // Start with all coils off
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, LOW);
  Serial.begin(9600);
  Wire.begin(1);
 Wire.onReceive(Rece);
}
 void Forwardm2 (){
    // 1. Set the aPin High
  digitalWrite(m2aPin,      HIGH);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 2. Energize aPin and bPin to HIGH
  digitalWrite(m2aPin,      HIGH);
  digitalWrite(m2bPin,      HIGH);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 3. Set the bPin to High
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      HIGH);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 4. Set the bPin and the aPrimePin to HIGH
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      HIGH);
  digitalWrite(m2aPrimePin, HIGH);
  digitalWrite(m2bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  //  5. Set the aPrime Pin to high
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, HIGH);
  digitalWrite(m2bPrimePin, LOW);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 6. Set the aPrimePin and the bPrime Pin to HIGH
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, HIGH);
  digitalWrite(m2bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 7. Set the bPrimePin to HIGH
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds

  // 8. Set the bPrimePin and the aPin to HIGH
  digitalWrite(m2aPin,      HIGH);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, HIGH);
  // Allow some delay between energizing the coils to allow
  //  the stepper rotor time to respond.
  delay(delay1); // So, delay1 milliseconds
  
  }

  void param2 (){
  digitalWrite(m2aPin,      LOW);
  digitalWrite(m2bPin,      LOW);
  digitalWrite(m2aPrimePin, LOW);
  digitalWrite(m2bPrimePin, LOW);
    }

void loop() 

{
  if (a == 'F'){
    
 Forwardm2 ();
  }
  else if (a == 'T'){ 
 param2 ();
  }
}

void Rece(int Hm)
{
  while(Wire.available())
  {
    char x = Wire.read();
    if(x =='F')
    {
   a = 'F';
      }
    else if(x == 'T')
    {
     a = 'T';
    }
  }
}


