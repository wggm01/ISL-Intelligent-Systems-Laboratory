 int del = 1; 
 int a = 8;
 int b = 10;
 int c = 9;
 int d = 11;
void setup() 
{
  // inicio pines utilizados
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
 
  // 1
  digitalWrite(a, HIGH);                     
  digitalWrite(b, LOW);   
  digitalWrite(c, LOW);  
  digitalWrite(d, LOW);   
  delay(del);
   //2
  digitalWrite(a, HIGH);
  digitalWrite(b, HIGH);   
  digitalWrite(c, LOW);   
  digitalWrite(d, LOW);   
  delay(del); 
  //3
  digitalWrite(a, LOW);
  digitalWrite(b, HIGH);  
  digitalWrite(c, LOW);
  digitalWrite(d, LOW);   
  delay(del);
  //4
  digitalWrite(a, LOW);
  digitalWrite(b, HIGH); 
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);   
  delay(del);
    //5
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);  
  digitalWrite(c, HIGH);
  digitalWrite(d, LOW);   
  delay(del);
    //6
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);   
  digitalWrite(c, HIGH);
  digitalWrite(d, HIGH);   
  delay(del);
    //7
  digitalWrite(a, LOW);
  digitalWrite(b, LOW);  
  digitalWrite(c, LOW); 
  digitalWrite(d, HIGH);   
  delay(del);
      //8
  digitalWrite(a, HIGH);
  digitalWrite(b, LOW); 
  digitalWrite(c, LOW); 
  digitalWrite(d, HIGH);   
  delay(del);                  
}
