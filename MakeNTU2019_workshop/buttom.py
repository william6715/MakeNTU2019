import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN)

while True:
    inputValue = GPIO.input(2)
    if (inputValue == False): ##because it is put down
        print("dont touch me.")
        while(inputValue==False):
            time.sleep(0.3)
