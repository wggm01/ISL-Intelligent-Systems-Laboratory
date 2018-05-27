
int x=0;
//int pincolum[5]={11,16,10,9,5};
//int pinrow[8]={8,13,7,12,18,14,6,15};

int pincolum[5]={5,9,10,16,11};
int pinrow[8]={15,6,14,18,12,7,13,8};

int pin8[5]={0,1,1,1,0};
int pin13[5]={1,0,0,0,1};
int pin7[5]={1,0,0,0,1};
int pin12[5]={1,1,1,1,1};
int pin18[5]={1,0,0,0,1};
int pin14[5]={1,0,0,0,1};
int pin6[5]={1,0,0,0,1};
int pin15[5]={1,0,0,0,1};

// the setup function runs once when you press reset or power the board
void setup() {
  // filas
  pinMode(8, OUTPUT); //9
  pinMode(13, OUTPUT);//14
  pinMode(7, OUTPUT);//8    PINES DE LA HOJA DE DATOS
  pinMode(12, OUTPUT);//12
  pinMode(18, OUTPUT);//5
  pinMode(A0, OUTPUT);//1
  pinMode(6, OUTPUT);//7
  pinMode(15, OUTPUT);//2
  // COLUMNAS
  pinMode(11, OUTPUT);//13
  pinMode(16, OUTPUT);//3
  pinMode(10, OUTPUT);//11
  pinMode(9, OUTPUT);//10
  pinMode(5, OUTPUT);//6 

  digitalWrite(14,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(15,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(6,1);   // turn the LED on (HIGH is the voltage level) 
  digitalWrite(7,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(8,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(12,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(13,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(18,1);   // turn the LED on (HIGH is the voltage level)                    
  digitalWrite(11,1);    // turn the LED off by making the voltage LOW
  digitalWrite(16,1);   // turn the LED on (HIGH is the voltage level) 
  digitalWrite(10,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(9,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(5,1);   // turn the LED on (HIGH is the voltage level)
  
   
}

// the loop function runs over and over again forever
void loop() {
  /*digitalWrite(A0,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(A1,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(6,1);   // turn the LED on (HIGH is the voltage level) 
  digitalWrite(7,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(8,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(12,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(13,1);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(A4,1);   // turn the LED on (HIGH is the voltage level)
  delay(100); */ 

for(int fila = 0; fila<9; fila++){
  digitalWrite(pinrow[fila],1);   // turn the LED on (HIGH is the voltage level)
  delay(200);
  digitalWrite(pinrow[fila],0);   // turn the LED on (HIGH is the voltage level)
   delay(200);
  
}

//for(int repe = 0; repe<50; repe++){
for (int pin = 0; pin<5; pin++){
    
    digitalWrite(pincolum[pin],0);
    delay(200);
    //digitalWrite(pincolum[pin],1);
  
  }
  }
  

