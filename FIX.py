import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # disable setwarnings

dataPin = 19
latchPin = 21
clockPin = 15

digitPin = [40,7,11,13]

num = (
    0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90)

counter = 0

t = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)

for i in digitPin:
    GPIO.setup(i,GPIO.OUT)