import time
import RPi.GPIO as GPIO
import board
import adafruit_dht 
dhtDevice = adafruit_dht.DHT11(board.D23, use_pulseio=False)
import mail
import DiscordWebhook

#PIN_A = 19
#PIN_B = 20
#PIN_C = 21
#PIN_D = 22
#PIN_E = 23
#PIN_F = 24
#PIN_G = 25
point = 5
comA1 = 6
comA2 = 13
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
GPIO.setwarnings(False)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(point, GPIO.OUT)
GPIO.setup(comA1, GPIO.OUT)
GPIO.setup(comA2, GPIO.OUT)
def affichage(num1, num2):
    for i in range(0, 250):    
        for i in range(0, 6):
            GPIO.output((i+19), Segment[i][num1])
        GPIO.output(comA1, LOW)
        GPIO.output(comA2, HIGH)
        time.sleep(0.01)
        for i in range(0, 6):
            GPIO.output((i+19), Segment[i][num2])
        GPIO.output(comA1, HIGH)
        GPIO.output(comA2, LOW)
        time.sleep(0.01)
while True:
    try:        
        temperature_c = dhtDevice.temperature
        temp = int(temperature_c)
        ltemp = list(str(temp))
        prm = ltemp[0]
        scd = ltemp[1]
        affichage(int(prm), int(scd))
        GPIO.output(PIN_P, GPIO.LOW)
        print("Temperature: ",temperature_c)
    except RuntimeError as error:
        # Les erreurs sont assez fréquentes, les DHT sont difficiles à lire, passez à autre chose.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    try:        
        humidity = dhtDevice.humidity
        hum = int(humidity)
        lhum = list(str(hum))
        hprm = lhum[0]
        hscd = lhum[1]
        affichage(int(hprm), int(hscd))
        GPIO.output(PIN_P, GPIO.HIGH)
        print("Humidite: ",humidity)
    except RuntimeError as error:
        # Les erreurs sont assez fréquentes, les DHT sont difficiles à lire, passez à autre chose.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    if (temp > 25 and humidity > 76): # Définition repsective des variable dans le mail.py et le discordwebhook.py 
        mail.sendHtmlEmailTo
        DiscordWebhook.alert
