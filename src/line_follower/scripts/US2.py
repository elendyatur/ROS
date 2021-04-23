import time
import RPi.GPIO as GPIO

# Usamos la referencia BOARD para los pines GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)          # Sin warnings

# Definimos los pines que vamos a usar
GPIO_TRIGGER = 11
GPIO_ECHO = 13

# Configuramos los pines como entradas y salidas
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

# Definimos algunas funciones

def medida():
  # Esta funcion mide una distancia
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

# Ponemos el Trigger en falso (low)
GPIO.output(GPIO_TRIGGER, False)

# Metemos el bloque principal en un Try para asi poder
# comprobar si el usuario presiona Ctrl + C
# y poder ejecutar una limpieza del GPIO, esto tambien
# evita el usuario tener que ver muchos mensajes de error
try:
 while True: # Este bucle se repite siempre

# Lo primero que hago es medir la distancia
        distancia = medida()
# Compruebo si la distancia es menor que 10
# Si es menor que 10 muestro la distancia por pantalla
        print ("Distancia: %.1f" % distancia) # Mostramos la distancia por pantalla
        time.sleep(1) # Esperamos 1 segundo
       
except KeyboardInterrupt: # Si el usuario presiona Crtl + C

  # Limpiamos los pines GPIO y salimos del programa
  print ("Limpiando GPIO")
  GPIO.cleanup()
  print ("GPIO limpio")
  print ("Saliendo...")
  time.sleep(1)
