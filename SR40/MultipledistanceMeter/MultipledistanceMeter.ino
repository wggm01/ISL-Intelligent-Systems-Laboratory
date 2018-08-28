// Este codigo fue creado por mi
// Josue Rodriguez Estudiante de Ing Electronica y Telecomm.

const float trigPin1 = 3;
const float echoPin1 = 5;
const float trigPin2 = 6;
const float echoPin2 = 9;
const float trigPin3 = 10;
const float echoPin3 = 11;
String Distancia;
float duration1;  
int distance1;
float duration2;  
int distance2;
float duration3;  
int distance3;
unsigned long previousMillisD1 = 0;
const long intervalD1 = 0.01; 
unsigned long previousMillisD2 = 0;
const long intervalD2 = 0.002; 
unsigned long previousMillis = 0;
const long interval = 100; 

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();
  unsigned long currentMillisD1 = millis();
  unsigned long currentMillisD2 = millis();
  
      digitalWrite(trigPin3, LOW);
      digitalWrite(trigPin2, LOW);
      digitalWrite(trigPin1, LOW);

    if (currentMillisD2 - previousMillisD2 >= intervalD2) {
      previousMillisD2 = currentMillisD2;
      digitalWrite(trigPin1, HIGH);
      digitalWrite(trigPin3, HIGH);
      digitalWrite(trigPin3, HIGH);
    }
    if (currentMillisD1 - previousMillisD1 >= intervalD1) {
      previousMillisD1 = currentMillisD1;
      digitalWrite(trigPin1, LOW);
      digitalWrite(trigPin3, LOW);
      digitalWrite(trigPin3, LOW);
      duration1 = pulseIn(echoPin1, HIGH);
      distance1 = (duration1*.0343)/2;
      duration2 = pulseIn(echoPin2, HIGH);
      distance2 = (duration2*.0343)/2;    
      duration3 = pulseIn(echoPin3, HIGH);
      distance3 = (duration3*.0343)/2;
    }
    Distancia = "Distancia: ," + String(currentMillis) + " , " + String(distance1) + "," + String(distance2) + "," + String(distance3) + ".";                                                                                                          
    Serial.println(Distancia);

}
