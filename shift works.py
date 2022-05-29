import RPi.GPIO as GPIO
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

data=37
latch=35
clock=33

pins=data,latch,clock

for i in pins:
    GPIO.setup(i,GPIO.OUT)

while True:
    try:
        for i in range(255,127,-1):
            for j in range(8):
                bin=f'{i:b}'
                GPIO.output(latch,0)
                GPIO.output(data,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(clock,0)
            GPIO.output(latch,1)
            wait(.5)
            
        for i in range(128,256):    
            for j in range(8):
                bin=f'{i:b}'
                GPIO.output(latch,0)
                GPIO.output(data,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(clock,0)
            GPIO.output(latch,1)
            wait(.5)
        wait(2)
        
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        
        for j in range(8):            
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data,0)
            GPIO.output(clock,1)
            GPIO.output(clock,0)
        GPIO.output(latch,1)
        GPIO.cleanup()
        break