#include "DHT.h"        //DHT SENSOR LIBRARY 
#include <TM1637.h>     //TM1637 LIBRARY


__author__      = "risk"
__copyright__   = "Copyright (c) 2024 RISK"


  DHT dht(12 , DHT11); //DHT SENSOR PIN & SENSOR TYPE
  TM1637 tm(9,8);      //TM1637 CLK & DIO PINs TO ARDUINO

  byte S1   = 4; //SWITCH 1 TO SET BRIGHTNESS
  byte S2   = 3; //SWITCH 2 TO CHANGE TEMPERATURE & HUMIDITY
  byte switch1=0;
  byte switch2=0;
  byte COUNT=0;
  byte SET=0;
  byte GETSENSOR = 0;
  byte SHIFT=0;

void setup()

  { 
    Serial.begin(9600);
    pinMode(S1,INPUT);
    pinMode(S2,INPUT);

     dht.begin();
     tm.begin();
     tm.setBrightness(1);
     delay(700);
  }
  
void loop() 
  { 
    switch1=digitalRead(S1);
    switch2=digitalRead(S2);    
 // Serial.print("COUNT :");    
 // Serial.println(COUNT);   

//SETTING DISPLAY BRIGHTNESS USING SWITCH 1
  
 if(switch1==1)
   {
    COUNT++;
    SET=1;
   }
    if(SET==1)
      {
       if(COUNT==1)
         {
          tm.setBrightness(2);
          SET=0;
         }
       else
       if(COUNT==2)
         {
          tm.setBrightness(3);
          SET=0;
         }
      else
      if(COUNT==3)
        {
         tm.setBrightness(4);
         SET=0;
        }
      else
      if(COUNT==4)
        {
         tm.setBrightness(5);
         SET=0;
        }
      else
      if(COUNT==5)
        {
         tm.setBrightness(6);
         SET=0;
        }
     else
     if(COUNT==6)
       {
        tm.setBrightness(7);
        SET=0;
       } 
     else
     if(COUNT==7)
       {
        tm.setBrightness(1);
        COUNT=0;
        SET=0;
       }
    }

//SELECT WHAT YOU NEED TO SHOW ON DISPLAY USING SWITCH 2

    if(switch2==1 && SHIFT==0)
      {
    // Serial.println("temperature"); 
       GETSENSOR=0;
      }  
        
    if(switch2==1 && SHIFT==1)
      {
    // Serial.println("humidity");
       GETSENSOR=1;
      }

    if(switch2==1 && SHIFT==2)
      {
    // Serial.println("temperature & humidity");
       GETSENSOR=2;
      }      
          
     GET_DATA();
  }
  
void GET_DATA() 
  {   
   if(GETSENSOR==0)
     {
      int temperature = dht.readTemperature();    
   // Serial.println(temperature);     
      tm.display("C", false,1,3);  //for 4 digit display 
   // tm.display("C", false,false); //for more than 4 digit display  
      tm.display(temperature, false, false); 
      SHIFT=1;      
      delay(1000); 
     }
   if(GETSENSOR==1)
     {
      int humidity = dht.readHumidity();   
   // Serial.println(humidity);
      tm.display("H", false,1,3); //for 4 digit display  
   // tm.display("H", false,false); //for more than 4 digit display       
      tm.display(humidity, false, false);  
      SHIFT=2; 
      delay(1000);
     }
     
   if(GETSENSOR==2)
     {
      int temperature = dht.readTemperature();    
   // Serial.println(temperature);     
      tm.display("C", false,1,3);  //for 4 digit display 
   // tm.display("C", false,false); //for more than 4 digit display  
      tm.display(temperature, false, false);           
      delay(1000); 
      
      int humidity = dht.readHumidity();   
   // Serial.println(humidity);
      tm.display("H", false,1,3); //for 4 digit display  
   // tm.display("H", false,false); //for more than 4 digit display       
      tm.display(humidity, false, false);  
      SHIFT=0; 
      delay(1000);
     }
  }
