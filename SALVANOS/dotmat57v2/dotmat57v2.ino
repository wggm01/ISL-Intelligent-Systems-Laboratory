#include <Wire.h>

#define deviceaddress 0x50 // default address MAX6953 
int dig3 = 0x23; // register numbers are taken from the documentation 
int dig2 = 0x22; 
int dig1 = 0x21; 
int dig0 = 0x20;



void setup() {
// ==== initializing the matrix ===== 
Wire.begin (); // connect i2c bus 
Wire.beginTransmission (deviceaddress); // write to the device 
Wire.write (0x04); // register of configuration 

// MAX6953 Table 6 - table number in the description 
Wire.write (0x01); // turn off the shutdown mode; 
Wire.endTransmission (); 

// MAX6953 Table 23 - the next step: 
Wire.beginTransmission (deviceaddress); 
Wire.write (0x01); // Intensity of bits 0 and 2 
Wire.write (0xFF); // all segments to maximum = 20 mA 
Wire.endTransmission (); 

// MAX6953 Table 24 - the next step: 
Wire.beginTransmission (deviceaddress); 
Wire.write (0x02); // Intensity of digits 1 and 3
Wire.write (0xFF); // all segments to maximum = 20 mA 
Wire.endTransmission (); 
// Turn on the test mode for verification: all the LEDs are lit 

// MAX6953 Table 22 
Wire.beginTransmission (deviceaddress); 
Wire.write (0x07); 
Wire.write (0x01); 
Wire.endTransmission (); 
delay (1000); // second delay 

// turn off test mode 
// MAX6953 Table 22 
Wire.beginTransmission (deviceaddress); 
Wire.write (0x07); 
Wire.write (0x00); 
Wire.endTransmission (); 
// ===== end of initialization ======= 

}
// write the value symbol to disp 
void writeChar (byte value, byte disp){ 
Wire.beginTransmission (0x50); 
Wire.write (disp); 
if (value == '0') Wire.write ('O'); // replace zero with the letter O !! 
else Wire.write (value); 
Wire.endTransmission (); 
}

void loop () {

// matrix: 
writeChar ('0', dig3); 
writeChar ('2', dig2); 
writeChar ('0', dig1); 
writeChar ('3', dig0); 
delay (500); 
 
writeChar ('6', dig3); 
writeChar ('0', dig2); 
writeChar ('8', dig1); 
writeChar ('0', dig0); 
delay (500); 

}

