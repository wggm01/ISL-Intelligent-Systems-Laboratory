#include <Wire.h>

#define COMMAND_ADDRESS 0x50 // AD0 AD1 A GND
#define CONFIG_ADDRESS 0x04 //CONFIGURACION
#define INTENSITY10_ADDRESS 0x01 //INTENSIDA 10 AUN NO SE EXACTASMENTE QUE ES PERO PARECE CORRIENTE
#define INTENSITY32_ADDRESS 0x02//INTENSIDA 32 AUN NO SE EXACTASMENTE QUE ES PERO PARECE CORRIENTE
#define SCANLIMIT_ADDRESS 0x03 // SUPONGO QUE DEFINE HASTA QUE PANTALLA SE MOVERA
#define DIGIT0_ADDRESS 0x20 // write Plane 0 PLAN 0 AUN DESCONOCIDO QUE ES EXACTAMENTE
#define DIGIT1_ADDRESS 0x21 // write Plane 0
#define DIGIT2_ADDRESS 0x22 // write Plane 0
#define DIGIT3_ADDRESS 0x23 // write Plane 0


void setup() {
 Wire.begin(); // A qui no va nada por estoy com maestro

//ACCESO AL REGISTRO DE CONFIGURACION 0x04
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(CONFIG_ADDRESS);
 Wire.write(0x05); // combinacion de los bit PXRTEBXS de la hoja de datos.
 Wire.endTransmission();
//ACCESO AL REGISTRO DE INTENSIDAD 10 0x01
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(INTENSITY10_ADDRESS);
 Wire.write(0xEE);  //  E = 15/16 (max), 1 nibble each for digit 0 & 2
 Wire.endTransmission();
 
 //ACCESO AL REGISTRO DE INTENSIDAD 32 0x02
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(INTENSITY32_ADDRESS);
 Wire.write(0xEE);  //  E = 15/16 (max), 1 nibble each for digit 1 & 3
 Wire.endTransmission();

 //ACCESO AL REGISTRO DE SCANLIMIT 32 0x03
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(SCANLIMIT_ADDRESS);
 Wire.write(0x01);  //  01 = 4 display digits
 Wire.endTransmission();

//display test
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(0x07);
 Wire.write(0x01);  //  01 = display test on
 Wire.endTransmission();
 delay (500); // for # of milliseconds
 Wire.beginTransmission(COMMAND_ADDRESS);
 Wire.write(0x07);
 Wire.write(0x00);  //  00 = normal operatiom
 Wire.endTransmission(); // does not change loaded data tho
}
 

void loop() {
   
     // write digit1 register
     Wire.beginTransmission(COMMAND_ADDRESS);
     Wire.write(DIGIT0_ADDRESS);
     Wire.write(0x31);  
     Wire.endTransmission();

      // write digit1 register
     Wire.beginTransmission(COMMAND_ADDRESS);
     Wire.write(DIGIT3_ADDRESS);
     Wire.write(0x30);  
     Wire.endTransmission();
     
     delay(1000);

}
