import RPi.GPIO as GPIO,threading
import time

LSBFIRST=1
MSBFIRST=2

dataPin=19
latchPin=21
clockPin=15

num=(
    0xc0,0xf9,0xa4,0xb0,0x99,
    0x92,0x82,0xf8,0x80,0x90)

def setup():
    GPIO.setmode(GPIO.BOARD) # breadboard method
    GPIO.setwarnings(False) # disable setwarnings
    GPIO.setup(40,GPIO.OUT)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    
    GPIO.setup(dataPin,GPIO.OUT)
    GPIO.setup(latchPin,GPIO.OUT)
    GPIO.setup(clockPin,GPIO.OUT)
    
    GPIO.output(7,1)

def shiftOut(dPin,cPin,order,val):
    for i in range(0,8):
        GPIO.output(cPin,GPIO.LOW)
        if(order==LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order==MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH)
        
def loop():
    shiftOut(40,7,11,13)
    while True:
        for i in range(0,len(num)):
            GPIO.output(latchPin,GPIO.LOW)
            shiftOut(dataPin,clockPin,MSBFIRST,num[i])
            GPIO.output(latchPin,GPIO.HIGH)
            time.sleep(0.5)
            
        for i in range(0,len(num)):
            GPIO.output(latchPin,GPIO.LOW)
            shiftOut(dataPin,clockPin,MSBFIRST,num[i]&0x7f)
            GPIO.output(latchPin,GPIO.HIGH)
            time.sleep(0.5)
            
def destroy():
    GPIO.cleanup
            
if __name__ == '__main__':
    print('Program is starting')
    
setup()
try:
    loop()
except KeyboardInterrupt:
    destroy(1,2,3,4)
                     
            


