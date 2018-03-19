
#include <Wire.h>
const int X_pin = 0; // analog pin connected to X output
const int Y_pin = 1; // analog pin connected to Y output
int control;

void setup() {
  Wire.begin(0X70);
  Wire.onRequest(requestEvent);
  Serial.begin(115200);
}

void loop() {
int X = analogRead(X_pin);
 int Y = analogRead(Y_pin);
int map_x=map(X,0,1023,1,-1);
 int map_y=map(Y,0,1023,2,-2);
 //Serial.println(map_x);
 //Serial.println(map_y);
if(map_x == 2){
  control = 1;
  }else if (map_x == -2){
    
    control = 2;
    }
    
if(map_x == 1){
  control = 3;
  }else if (map_x == -1){
    
    control = 4;
    }
}

void requestEvent() {
  Wire.write(control); // respond with message of 6 bytes
  // as expected by master
}
