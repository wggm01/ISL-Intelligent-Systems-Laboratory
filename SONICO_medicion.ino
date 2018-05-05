
const int trigPin1 = 3;
const int echoPin1 = 5;
float duration1;  
float distance1;


void setup() {
  
  // Sets up trigger and reception 
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  Serial.begin(9600);


}

void loop() {

// STARTS SENSOR 1

  digitalWrite(trigPin1, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);

    duration1 = pulseIn(echoPin1, HIGH);
    distance1 = (duration1*.0343)/2;
 

    
   // RESULT

    Serial.println(distance1);   
    delay(10); 
  
}
