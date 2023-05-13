import RPi.GPIO as GPIO
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

sensor_pin=7
LED_pin=11

GPIO.setup(sensor_pin,GPIO.IN)
GPIO.setup(LED_pin,GPIO.OUT)

while True:
    if GPIO.input(sensor_pin)==1:
        print('Motion Detected!')
        GPIO.output(LED_pin,1)
        wait(3)
    else:
        GPIO.output(LED_pin,0)