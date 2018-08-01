
#include <Stepper.h>
#include <Wire.h>
#define mizq 0x40
const int stepsPerRevolution = 200;  //OBTENIDO POR EXPERIMENTACION
int control;
int velo=150; //velocidad
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11); //AJUSTAR A LOS MOTORES
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,4);
const int analogIn = A0;
const int analogIn1 = A1;
int mVperAmp = 100;
int mVperAmp1 = 100;// Sensibility
int RawValue= 0;
int RawValue1= 0;
int ACSoffset = 2478;
int ACSoffset1 = 2478;// default 2500 
double Voltage = 0;
double Voltage1 = 0;
float Amps = 0;
float Amps1 = 0;
unsigned long time0 = 0;
const long timer = 5000;

void setup() {

  lcd.init();
  lcd.backlight();
  lcd.print("Please Stand By");

  pinMode(analogIn,INPUT);
  

  lcd.clear();
  //COMUNICACION I2C
  Wire.begin(mizq); 
  Wire.onReceive(receiveEvent); 
  Serial.begin(9600);
  myStepper.setSpeed(velo);
  delay(1000);
}
//RECEPCION DE INSTRUCCIONES
void receiveEvent(int howMany) {

if (Wire.available()>0) { 
  control = Wire.read();  
}
Serial.println(control);} 
void loop() {
//MOVIMIENTOS  
switch (control){
  case 1 : 
    myStepper.step(stepsPerRevolution); //HACIA DELANTE
    Serial.println("HACIA DELANTE");
    break;
  case 2 : 
    myStepper.step(-stepsPerRevolution); //HACIA ATRAS
    Serial.println("HACIA ATRAS");
    break;
  case 3 : 
    myStepper.step(stepsPerRevolution); //IZQUIERDA 90 GRADOS ESTA EN CERO PARA QUE GIRE ENTORNO A LA LLANTA IZQUIERDA.
    Serial.println("HACIA A LA IZQ 90 GRADOS");
    break;
  case 4 : 
    myStepper.step(0); //DERECHA 90 GRADOS SETEAR PASOS NECESARIOS PARA QUE GIRE 90 GRADOS.
    Serial.println("HACIA A LA DER 90 GRADOS");
    break;
  case 5 : 
    myStepper.step(stepsPerRevolution); //IZQUIERDA ACKERMAN
    myStepper.setSpeed(velo+10);
    Serial.println("HACIA A LA IZQ ACKERMAN");
    break;
  case 6 : 
    myStepper.step(-stepsPerRevolution); //DERECHA ACKERMAN
    myStepper.setSpeed(velo-10);
    Serial.println("HACIA A LA DER ACKERMAN");
    break;
  case 7 : 
    myStepper.step(-stepsPerRevolution); //IZQUIERDA HACIA ATRAS ACKERMAN
    myStepper.setSpeed(velo+10);
    Serial.println("IZQUIERDA HACIA ATRAS ACKERMAN");
    break;
  case 8 : 
    myStepper.step(-stepsPerRevolution); //DERECHA HACIA ATRAS ACKERMAN
    myStepper.setSpeed(velo-10);
    Serial.println("DERECHA HACIA ATRAS ACKERMAN");
    break;
  case 9 : 
    myStepper.step(stepsPerRevolution); //IZQUIERDA SOBRE EJE
    Serial.println("IZQUIERDA SOBRE EJE");
    break;
  case 10 : 
    myStepper.step(-stepsPerRevolution); //DERECHA SOBRE EJE
    Serial.println("DERECHA SOBRE EJE");
    break;
  case 11 : 
    myStepper.setSpeed(velo+10); //INCREMENTO DE VELOCIDAD
    break;
  case 12 : 
    myStepper.setSpeed(velo-10); //DECREMENTO DE VELOCIDAD
    break;}

 unsigned long time1 = millis(); 
  
  if (time1 - time0 >= timer) {//time0 >> initial time, time1 >> current time
  RawValue = analogRead(analogIn);
  Voltage = (RawValue / 1023.0) * 5000; //for reference in mV
  Amps = ((Voltage - ACSoffset) / mVperAmp);

 lcd.setCursor(0,0);
  lcd.print("P1=" + (String)Voltage);

  lcd.setCursor(0,1);
  lcd.print("C1=" + (String)Amps);

   RawValue1 = analogRead(analogIn1);
  Voltage1 = (RawValue1 / 1023.0) * 5000; //for reference in mV
  Amps = ((Voltage1 - ACSoffset1) / mVperAmp1);
  time0 = time1;
  
  lcd.setCursor(8,0);
  lcd.print("P2=" + (String)Voltage1);

  lcd.setCursor(8,1);
  lcd.print("C2=" + (String)Amps1);
    }
    
}
