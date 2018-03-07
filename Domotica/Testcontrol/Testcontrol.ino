#include <Wire.h>

void setup() {
  Wire.begin(); 
}



void loop() {
  for (int x=0;x<9;x++){
  Wire.beginTransmission(0X40);         
  Wire.write(x);              
  Wire.endTransmission();    
  delay(1000);
  }
}
