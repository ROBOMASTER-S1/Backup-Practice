import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setwarnings(False) # disable setwarnings

datapin=19
latchpin=21
clockpin=15

control_shift=datapin,latchpin,clockpin

lsbfirst=1
msbfirst=2

num=(
    0xc0,0xf9,0xa4,0xb0,0x99,
    0x92,0x82,0xf8,0x80,0x90)

digitpins=[7,11,13,40]

counter=0
t=0

def setup():
    GPIO.setmode(GPIO.BOARD) # breadboard method
    
    GPIO.setup(datapin,GPIO.OUT)
    GPIO.setup(latchpin,GPIO.OUT)
    GPIO.setup(clockpin,GPIO.OUT)
    
    for pin in digitpins:
        GPIO.setup(pin,GPIO.OUT)
    
def shiftout(dpin,cpin,order,val):
    
    for i in range(0,8):
        GPIO.output(cpin,GPIO.LOW);
        
        if(order==msbfirst):
            GPIO.output(
                dpin,(0x01&(
                    val>>i)==0x01)and GPIO.HIGH or GPIO.LOW)
        
        

