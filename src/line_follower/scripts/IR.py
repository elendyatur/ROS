import RPi.GPIO as GPIO
import time

# Definición de pines
#D0=8    #Pin al que conectamos D0
#A0=7    #Pin al que conectamos A0

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
        #print ("A0 = ", GPIO.input(7))    # Imprime el valor que tenga en A0
        #print ("D0 = ", GPIO.input(8))
       #if (GPIO.input(D0)==False):
       #   print ("Sensor False")
       #else : print ("Sensor True")

        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()

