 int del = 2; 
void setup() 
{
  // inicio pines utilizados
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  // 1
  digitalWrite(2, HIGH);                     
  digitalWrite(3, LOW);   
  digitalWrite(4, LOW);  
  digitalWrite(5, LOW);   
  delay(del);
   //2
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);   
  digitalWrite(4, LOW);   
  digitalWrite(5, LOW);   
  delay(del); 
  //3
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH);  
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);   
  delay(del);
  //4
  digitalWrite(2, LOW);
  digitalWrite(3, HIGH); 
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);   
  delay(del);
    //5
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);  
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);   
  delay(del);
    //6
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);   
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);   
  delay(del);
    //7
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);  
  digitalWrite(4, LOW); 
  digitalWrite(5, HIGH);   
  delay(del);
      //8
  digitalWrite(2, HIGH);
  digitalWrite(3, LOW); 
  digitalWrite(4, LOW); 
  digitalWrite(5, HIGH);   
  delay(del);                  
}
