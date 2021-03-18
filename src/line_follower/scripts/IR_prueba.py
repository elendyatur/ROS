import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)     # Sin warnings
GPIO.setmode(GPIO.BCM)      # Modo pinout BOARD
GPIO.setup(8, GPIO.IN)      # Pin 8 (D0) como entrada de datos a la RPi
GPIO.setup(7, GPIO.IN)      # Pin 7 (A0) como entrada de datos a la RPi

try:                        # Ejecuta
    while True:             # Mientras no haya interrupciones
        val = GPIO.input(7)
        print ("A ", val)
        val1 = GPIO.input(8)
        print ("D ", val1)
        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()
