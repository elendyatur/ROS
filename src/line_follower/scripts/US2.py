import time
import RPi.GPIO as GPIO

# Referencia BOARD para los pines GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)          # Sin warnings

# Pines a utilizar
GPIO_TRIGGER = 11
GPIO_ECHO = 13

# Configuracion de pines
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

def medida():
  # Medicion de distancia
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()

  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distancia = (elapsed * 34300)/2
  return distancia

# Programa principal

print ("Medida con sensor de ultrasonidos")

# Trigger en falso (low)
GPIO.output(GPIO_TRIGGER, False)
r
try:
 while True: # Este bucle se repite siempre

# Se mide la distancia
        distancia = medida()
# Se comprueba si la distancia es menor que 10
# Si es menor que 10 se muestra la distancia por pantalla
        print ("Distancia: %.1f" % distancia) # Se muestra la distancia por pantalla
        time.sleep(1)
       
except KeyboardInterrupt: # Si el usuario presiona Crtl + C

  # Limpiar los pines GPIO y salir del programa
  print ("Limpiando GPIO")
  GPIO.cleanup()
  print ("GPIO limpio")
  print ("Saliendo...")
  time.sleep(1)
