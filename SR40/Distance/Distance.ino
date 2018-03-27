#include <Wire.h>
#include <NewPing.h>

//Primer sensor (costado)
#define TRIGGER_PIN 3 //pwm
#define ECHO_PIN 4
#define MAX_DISTANCE 300
//Segundo sensor (costado)
#define TRIGGER1_PIN 5
#define ECHO1_PIN 7
#define MAX1_DISTANCE 200 
//Tercer sensor (Frente)
#define TRIGGER2_PIN 6
#define ECHO2_PIN 8
#define MAX2_DISTANCE 200 
//Cuarto sensor (Atras)
#define TRIGGER3_PIN 9
#define ECHO3_PIN 12
#define MAX3_DISTANCE 200 

int uS1;
int uS2;
int uS3;
int uS4;

unsigned long startMillis;  //some global variables available anywhere in the program
unsigned long currentMillis;
const unsigned long period = 1000;  //the value is a number of milliseconds

int control;

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
//NewPing sonar1(TRIGGER1_PIN, ECHO1_PIN, MAX1_DISTANCE); // NewPing setup of pins and maximum distance.
//NewPing sonar2(TRIGGER2_PIN, ECHO2_PIN, MAX2_DISTANCE); // NewPing setup of pins and maximum distance.
//NewPing sonar3(TRIGGER3_PIN, ECHO3_PIN, MAX3_DISTANCE); // NewPing setup of pins and maximum distance.
 
void setup() {
   Wire.begin(0X60);                
   Wire.onRequest(logicaControl);
   Serial.begin(9600);
   startMillis = millis();  //initial start time
}


 
void loop() {
  currentMillis = millis();
  if (currentMillis - startMillis >= period)  //test whether the period has elapsed
    {
    uS1 = sonar.ping_cm();
    //uS2 = sonar1.ping_cm();
    //uS3 = sonar2.ping_cm();
    //uS4 = sonar3.ping_cm();

 /* if (uS1 != 0 && uS2 != 0 && uS3 != 0 && uS4 != 0  )
    {
      Serial.print(uS1);
      Serial.print(uS2);
      Serial.print(uS3);
      Serial.print(uS4);
      Serial.println("cm");
    } */  
  startMillis = currentMillis;
}
//Logica de control aqui
/*Si el sensor de alfrente detecta cambio de distancia significa que esta cerca de una cera
 * por lo que debe reajustarse rodando hacia atras luego gira a la izquierda sobre su eje 
 * queda de frente, avanza,vuelve hacer un giro de 90 grados, chequea la distancia y si no 
 * hay obstaculos ni una sigue hacia delante pero si se vuelve a topar con la acera tiene que
 * repetir la secuencia antes mencionada.
 */

 //Entro en la verificacion de distancia
  if (uS1>100 && uS1<190){ //si me topo con un desnivel tomando en cuenta que el sensor esta puesto en la parte superior del robot
    control = 9; //Esto se lo envio a la raspberry para que haga la secuencia de correccion.
  }else if (uS1>=200){
    control = 8; 
  }
   
}

// Envio de data al masta

void logicaControl() {
  Wire.write(control); // respond with message of 6 bytes
  // as expected by master
}
