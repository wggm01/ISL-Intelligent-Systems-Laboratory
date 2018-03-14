//code created to implement distance sensor in navigation
//created by josue rodriguez 

// Right Sensor {1}
const int trigPinr = 3;
const int echoPinr = 5;

// Center Sensor {2}
const int trigPinc = 6;
const int echoPinc = 9;

// LEFT SENSOR {3}
const int trigPinl = 10; 
const int echoPinl = 11; 


float durationr;  
int distancer;
float durationc;  
int distancec;
float durationl;  
int distancel;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPinr, OUTPUT);
  pinMode(echoPinr, INPUT);
  pinMode(trigPinc, OUTPUT);
  pinMode(echoPinc, INPUT);
  pinMode(trigPinl, OUTPUT);
  pinMode(echoPinl, INPUT);
  Serial.begin(9600);


}

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
    
   // RESULT

    Serial.print("Distance RIGHT: ");
    Serial.println(distancer);
    
    Serial.print("Distance CENTER: ");
    Serial.println(distancec);

    Serial.print("Distance Left: ");
    Serial.println(distancel);
    

     Serial.println();
   
    delay(500); 
