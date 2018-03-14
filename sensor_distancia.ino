#include <Wire.h>
const int trigPin = 5;
const int echoPin = 6;

int control;

float duration;  int distance = 60;

void setup() {

  Wire.begin(0X60);             
  Wire.onRequest(requestEvent);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void requestEvent() 
 {
  Wire.write(control);

 }

void loop() {



 if (distance>30) 
 
 {
  
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = (duration*.0343)/2;
    Serial.print("Distance: ");
    Serial.println(distance);
    control=1;  
    Serial.println(control);
  }
  
  else
  {  
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = (duration*.0343)/2;
    Serial.print("Distance: ");
    Serial.println(distance);
    control=4;
    Serial.println(control);
    }
}
  






