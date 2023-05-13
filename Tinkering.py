import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # disable setwarnings

LSBFIRST = 1
MSBFIRST = 2

latch=19
data_bit=21
clock=15

num = (
    0xc0,0xf9,0xa4,0xb0,0x99,
    0x92,0x82,0xf8,0x80,0x90)

digitPin = (40,7,11,13)

counter = 0

t = 0

GPIO.setup(data_bit,GPIO.OUT)
GPIO.setup(latch,GPIO.OUT)
GPIO.setup(clock,GPIO.OUT)

for i in digitPin:
    GPIO.setup(i,GPIO.OUT)

for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,1)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
GPIO.output(latch,GPIO.LOW)
shiftOut(data_bit,clockPin,MSBFIRST,data)
GPIO.output(latch,GPIO.HIGH)

