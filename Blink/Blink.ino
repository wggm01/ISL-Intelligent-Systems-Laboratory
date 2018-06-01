
int x=0;
//int pincolum[5]={11,16,10,9,5};
//int pinrow[8]={8,13,7,12,18,14,6,15};
int pincolum[5]={5,9,10,16,11};
int pinrow[8]={15,6,14,18,12,7,13,8};
int pin8[5];
int pin13[5];
int pin7[5];
int pin12[5];  //A
int pin18[5];
int pin14[5];
int pin6[5];
int pin15[5];
/*
int pin8[5]={0,1,1,1,0};
int pin13[5]={1,0,0,0,1};
int pin7[5]={1,0,0,0,1};
int pin12[5]={1,1,1,1,1};  //A
int pin18[5]={1,0,0,0,1};
int pin14[5]={1,0,0,0,1};
int pin6[5]={1,0,0,0,1};
int pin15[5]={1,0,0,0,1};
*/
/*
int pin8[5]={1,0,0,0,1};
int pin13[5]={1,0,0,0,1};
int pin7[5]={1,0,0,0,1};
int pin12[5]={1,1,1,1,1};  //H
int pin18[5]={1,0,0,0,1};
int pin14[5]={1,0,0,0,1};
int pin6[5]={1,0,0,0,1};
int pin15[5]={1,0,0,0,1};
*/
/*
int pin8[5]={1,1,1,1,1};
int pin13[5]={1,0,0,0,1};
int pin7[5]={1,0,0,0,1};
int pin12[5]={1,0,0,0,1};  //O
int pin18[5]={1,0,0,0,1};
int pin14[5]={1,0,0,0,1};
int pin6[5]={1,0,0,0,1};
int pin15[5]={1,1,1,1,1};
*/
/*
int pin8[5]={0,0,0,0,1};
int pin13[5]={0,0,0,0,1};
int pin7[5]={0,0,0,0,1};
int pin12[5]={0,0,0,0,1};  //L
int pin18[5]={0,0,0,0,1};
int pin14[5]={0,0,0,0,1};
int pin6[5]={0,0,0,0,1};
int pin15[5]={1,1,1,1,1};
*/
/*
int pin8[5]={1,1,1,1,1};
int pin13[5]={0,0,1,0,0};
int pin7[5]={0,0,1,0,0};
int pin12[5]={0,0,1,0,0};  //I
int pin18[5]={0,0,1,0,0};
int pin14[5]={0,0,1,0,0};
int pin6[5]={0,0,1,0,0};
int pin15[5]={1,1,1,1,1};
*/
void h(){
  pin8[0]=1;pin8[1]=0;pin8[2]=0;pin8[3]=0;pin8[4]=1;
  pin13[0]=1;pin13[1]=0;pin13[2]=0;pin13[3]=0;pin13[4]=1;
  pin7[0]=1;pin7[1]=0;pin7[2]=0;pin7[3]=0;pin7[4]=1;
  pin12[0]=1;pin12[1]=1;pin12[2]=1;pin12[3]=1;pin12[4]=1;
  pin18[0]=1;pin18[1]=0;pin18[2]=0;pin18[3]=0;pin18[4]=1;
  pin14[0]=1;pin14[1]=0;pin14[2]=0;pin14[3]=0;pin14[4]=1;
  pin6[0]=1;pin6[1]=0;pin6[2]=0;pin6[3]=0;pin6[4]=1;
  pin15[0]=1;pin15[1]=0;pin15[2]=0;pin15[3]=0;pin15[4]=1;
  }
void o(){
  pin8[0]=1;pin8[1]=1;pin8[2]=1;pin8[3]=1;pin8[4]=1;
  pin13[0]=1;pin13[1]=0;pin13[2]=0;pin13[3]=0;pin13[4]=1;
  pin7[0]=1;pin7[1]=0;pin7[2]=0;pin7[3]=0;pin7[4]=1;
  pin12[0]=1;pin12[1]=0;pin12[2]=0;pin12[3]=0;pin12[4]=1;
  pin18[0]=1;pin18[1]=0;pin18[2]=0;pin18[3]=0;pin18[4]=1;
  pin14[0]=1;pin14[1]=0;pin14[2]=0;pin14[3]=0;pin14[4]=1;
  pin6[0]=1;pin6[1]=0;pin6[2]=0;pin6[3]=0;pin6[4]=1;
  pin15[0]=1;pin15[1]=1;pin15[2]=1;pin15[3]=1;pin15[4]=1;
  }
void l(){
  pin8[0]=0;pin8[1]=0;pin8[2]=0;pin8[3]=0;pin8[4]=1;
  pin13[0]=0;pin13[1]=0;pin13[2]=0;pin13[3]=0;pin13[4]=1;
  pin7[0]=0;pin7[1]=0;pin7[2]=0;pin7[3]=0;pin7[4]=1;
  pin12[0]=0;pin12[1]=0;pin12[2]=0;pin12[3]=0;pin12[4]=1;
  pin18[0]=0;pin18[1]=0;pin18[2]=0;pin18[3]=0;pin18[4]=1;
  pin14[0]=0;pin14[1]=0;pin14[2]=0;pin14[3]=0;pin14[4]=1;
  pin6[0]=0;pin6[1]=0;pin6[2]=0;pin6[3]=0;pin6[4]=1;
  pin15[0]=1;pin15[1]=1;pin15[2]=1;pin15[3]=1;pin15[4]=1;
  }
void i(){
  pin8[0]=1;pin8[1]=1;pin8[2]=1;pin8[3]=1;pin8[4]=1;
  pin13[0]=0;pin13[1]=0;pin13[2]=1;pin13[3]=0;pin13[4]=0;
  pin7[0]=0;pin7[1]=0;pin7[2]=1;pin7[3]=0;pin7[4]=0;
  pin12[0]=0;pin12[1]=0;pin12[2]=1;pin12[3]=0;pin12[4]=0;
  pin18[0]=0;pin18[1]=0;pin18[2]=1;pin18[3]=0;pin18[4]=0;
  pin14[0]=0;pin14[1]=0;pin14[2]=1;pin14[3]=0;pin14[4]=0;
  pin6[0]=0;pin6[1]=0;pin6[2]=1;pin6[3]=0;pin6[4]=0;
  pin15[0]=1;pin15[1]=1;pin15[2]=1;pin15[3]=1;pin15[4]=1;
  }


// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  // filas
  pinMode(8, OUTPUT); //9
  pinMode(13, OUTPUT);//14
  pinMode(7, OUTPUT);//8    PINES DE LA HOJA DE DATOS
  pinMode(12, OUTPUT);//12
  pinMode(18, OUTPUT);//5
  pinMode(14, OUTPUT);//1
  pinMode(6, OUTPUT);//7
  pinMode(15, OUTPUT);//2
  // COLUMNAS
  pinMode(11, OUTPUT);//13
  pinMode(16, OUTPUT);//3
  pinMode(10, OUTPUT);//11
  pinMode(9, OUTPUT);//10
  pinMode(5, OUTPUT);//6 
 
}

// the loop function runs over and over again forever
void loop() {
switch (x) {
  case 0:
    h();
    break;
  case 1:
    o();
    break;
  case 2:
    l();
    break;
  case 3:
    i();
    break;
  case 4:
    h();
    break;
    
  default:
  x =0;
   break;
 
}
  
for(int repe = 0; repe<50; repe++){  
for (int pin = 0; pin<5; pin++){
   
    //Serial.println(pin8[pin]);
    digitalWrite(8,pin8[pin]);
    digitalWrite(13,pin13[pin]);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(7,pin7[pin]);   // turn the LED on (HIGH is the voltage level) 
    digitalWrite(12,pin12[pin]);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(18,pin18[pin]);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(14,pin14[pin]);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(6,pin6[pin]);   // turn the LED on (HIGH is the voltage level)
    digitalWrite(15,pin15[pin]);   // turn the LED on (HIGH is the voltage level)
    delay(1);
    digitalWrite(pincolum[pin],0);
    delay(1);
    digitalWrite(pincolum[pin],1);
  
  }}
  x=x+1;
 delay(100);
  }
  

