const int trigPin1 = 6;
const int echoPin1 = 5;

const int trigPin2 = 11;
const int echoPin2 = 10;



float duration1;  
float distance1;
float duration2;  
float distance2;
float duration3;  
float distance3;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
//  pinMode(trigPin3, OUTPUT);
 // pinMode(echoPin3, INPUT);
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
 

// STARTS SENSOR 2

    digitalWrite(trigPin2, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin2, LOW);

    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = (duration2*.0343)/2;
 

// STARTS SENSOR 3

/*    digitalWrite(trigPin3, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin3, HIGH);
    delayMicroseconds(10); 
    digitalWrite(trigPin3, LOW);
    
    duration3 = pulseIn(echoPin3, HIGH);
    distance3 = (duration3*.0343)/2;
    
  */   // RESULT

  //  Serial.print("Distance 1: ");
    Serial.print(distance1);   
    Serial.print(", ");
    Serial.println(distance2);
 
   // Serial.print("Distance 3: ");
  //Serial.println(distance3);
    
   // Serial.println("  ");
  // 
    delay(1000); 
  // put your main code here, to run repeatedly:

}
