//code created to implement distance sensor in navigation
//created by josue rodriguez 

#include <Wire.h>

// PIN declaration

                      // Right Sensor {1}
const int trigPinr = 3;
const int echoPinr = 5;
                      // Center Sensor {2}
const int trigPinc = 6;
const int echoPinc = 9;
                      // LEFT SENSOR {3}
const int trigPinl = 10; 
const int echoPinl = 11; 


int control; // control movement variable


// variable declaracion
  // Right Sensor {1}
  
float durationr;  
int distancer;

    // Center Sensor {2}
float durationc;  
int distancec;

    // LEFT SENSOR {3}
float durationl;  
int distancel;

void setup() {

   Wire.begin(0X60);             
  Wire.onRequest(requestEvent);
  // Pin Setup
   
  pinMode(trigPinr, OUTPUT);
  pinMode(echoPinr, INPUT);
  pinMode(trigPinc, OUTPUT);
  pinMode(echoPinc, INPUT);
  pinMode(trigPinl, OUTPUT);
  pinMode(echoPinl, INPUT);
  Serial.begin(9600);


}

void requestEvent() 
 {
  Wire.write(control);

void loop() {

// STARTS SENSOR 1 left sensor

    digitalWrite(trigPinr, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPinr, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPinr, LOW);

    durationr = pulseIn(echoPinr, HIGH);
    distancer = (durationr*.0343)/2;
 

// STARTS SENSOR 2 Center Sensor

    digitalWrite(trigPinc, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPinc, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPinc, LOW);

    durationc = pulseIn(echoPinc, HIGH);
    distancec = (durationc*.0343)/2;
 

// STARTS SENSOR 3 Right Sensor

    digitalWrite(trigPinl, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPinl, HIGH);
    delayMicroseconds(10); 
    digitalWrite(trigPinl, LOW);
    
    durationl = pulseIn(echoPinl, HIGH);
    distancel = (durationl*.0343)/2;
    
   // Serial Prinf of distances 

    Serial.print("Distance RIGHT: ");
    Serial.println(distancer);
    
    Serial.print("Distance CENTER: ");
    Serial.println(distancec);

    Serial.print("Distance Left: ");
    Serial.println(distancel);
    

     Serial.println();
   
//delay(2000);

    // Drive condition
    
   if ( distancer<22 && distancec<22 && distancel<22)

      {
        control=1;
        Serial.println("MOVEMENT");
        Serial.println("        Drive");
        Serial.println();
  //      delay(1000);
      }

    // turn to Right condition DUE TO Front Collition Warning  
   

      

    
if (distancel>25 && distancec<22 && distancer>25)

      {
        control=7;
        Serial.println("MOVEMENT");
        Serial.println("        turn right");
        Serial.println();
        
      }
    

if (distancel<22 && distancec<22 && distancer>25)

    {
      
        control=6;
        Serial.println("MOVEMENT");
        Serial.println("        turn LEFT");
        Serial.println();
        
      
    } 


}




