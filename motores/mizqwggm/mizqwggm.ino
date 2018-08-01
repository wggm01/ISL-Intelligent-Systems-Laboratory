#include <Stepper.h>
#include <Wire.h>
#define mder 0x50
const int stepsPerRevolution = 200;  //OBTENIDO POR EXPERIMENTACION
int control;
char controlchar [3];
char controlchar1[2];
String int_char;
int step;
int velo=150; //velocidad
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11); //AJUSTAR A LOS MOTORES

void setup() {
  //COMUNICACION I2C
  Wire.begin(mder); 
  Wire.onReceive(receiveEvent); 
  Serial.begin(9600);
  myStepper.setSpeed(velo);
}
//RECEPCION DE INSTRUCCIONES
void receiveEvent(int howMany) {

if (Wire.available()>0) { 
  control = Wire.read();  
}
Serial.println(control);} 
void loop() {
//CONTROL SOFISTICADO
if (control>199){
int_char=String(control);
int_char.toCharArray(controlchar,3);
if (controlchar[1]==0){
  step=controlchar[2]-'0';
  myStepper.step(step);
  }else if (controlchar[1]!= 0)
  controlchar1[0]=controlchar[1];
  controlchar1[1]=controlchar[2];
  step= atoi(controlchar1);
  myStepper.step(step);
}
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
    myStepper.step(0); //IZQUIERDA 90 GRADOS ESTA EN CERO PARA QUE GIRE ENTORNO A LA LLANTA IZQUIERDA.
    Serial.println("HACIA A LA IZQ 90 GRADOS");
    break;
  case 4 : 
    myStepper.step(stepsPerRevolution); //DERECHA 90 GRADOS SETEAR PASOS NECESARIOS PARA QUE GIRE 90 GRADOS.
    Serial.println("HACIA A LA DER 90 GRADOS");
    break;
  case 5 : 
    myStepper.step(stepsPerRevolution); //IZQUIERDA ACKERMAN
    myStepper.setSpeed(velo-10);
    Serial.println("HACIA A LA IZQ ACKERMAN");
    break;
  case 6 : 
    myStepper.step(-stepsPerRevolution); //DERECHA ACKERMAN
    myStepper.setSpeed(velo+10);
    Serial.println("HACIA A LA DER ACKERMAN");
    break;
  case 7 : 
    myStepper.step(-stepsPerRevolution); //IZQUIERDA HACIA ATRAS ACKERMAN
    myStepper.setSpeed(velo-10);
    Serial.println("IZQUIERDA HACIA ATRAS ACKERMAN");
    break;
  case 8 : 
    myStepper.step(-stepsPerRevolution); //DERECHA HACIA ATRAS ACKERMAN
    myStepper.setSpeed(velo+10);
    Serial.println("DERECHA HACIA ATRAS ACKERMAN");
    break;
  case 9 : 
    myStepper.step(-stepsPerRevolution); //IZQUIERDA SOBRE EJE
    Serial.println("IZQUIERDA SOBRE EJE");
    break;
  case 10 : 
    myStepper.step(stepsPerRevolution); //DERECHA SOBRE EJE
    Serial.println("DERECHA SOBRE EJE");
    break;
  case 11 : 
    myStepper.setSpeed(velo+10); //INCREMENTO DE VELOCIDAD
    break;
  case 12 : 
    myStepper.setSpeed(velo-10); //DECREMENTO DE VELOCIDAD
    break;}
}
