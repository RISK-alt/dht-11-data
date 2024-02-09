#include "DHT.h"        //DHT SENSOR LIBRARY 
#include <TM1637.h>     //TM1637 LIBRARY


__author__      = "risk -alt"
__copyright__   = "Copyright (c) 2024 RISK"

#import librairies 
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
import time

# Initialisez le dispositif dht avec la broche de données connectée à la broche 16 (GPIO 23) du Raspberry Pi :
dhtDevice = adafruit_dht.DHT11(board.D23, use_pulseio=False)

# Inistialisez broches & GPIO
#Segments 
#PIN A : 19
#PIN B : 20
#PIN C : 21
#PIN D : 22
#PIN E : 23
#PIN F : 24
#PIN G : 25
#PIN P : point
point = 5 

Segment = {
  0: (1,0,1,1,0,1,1,1,1,1), #A 
  1: (1,1,1,1,1,0,0,1,1,1), #B
  2: (1,1,0,1,1,1,1,1,1,1), #C
  3: (1,0,1,1,0,1,1,0,1,1), #D
  4: (1,0,1,0,0,0,1,0,1,0), #E
  5: (1,0,0,0,1,1,1,0,1,1), #F
  6: (0,0,1,1,1,1,1,0,1,1), #G
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarings(False) 
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(point, GPIO.OUT)

while True:
    try:
        # Imprimer les valeurs via l'interface série
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))

      # Afficher les valeurs, sur l'afficheur 7 segments 
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))

    except RuntimeError as error:
        # Les erreurs sont assez fréquentes, les DHT sont difficiles à lire, passez à autre chose.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
      SHIFT=0; 
      delay(1000);
     }
  }
