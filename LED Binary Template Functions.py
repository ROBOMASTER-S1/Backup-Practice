# Led Binary Template Functions Python:
# program example:

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi = 1
# breadboard = 1
# 74HC595 shift register = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 16+2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi fan, while in use/
# operation.

# Led Binary Template Functions Python:
# program example:

# This Raspberry Pi Python program allows
# users to learn all about how binary data
# bits work with the 74HC595 shift register.
# Users can have some serious LED binary fun...

# We will use the breadboard method:

# GPIO.setmode(GPIO.BOARD)

# This method is for the GPIO pinouts
# not the GPIO numbers, such as BCM

# You can also use the Broadcom SOC
# Channel method if you prefer:

# GPIO.setmode(GPIO.BCM)
# This allows GPIO numbers, not GPIO
# pinouts, such as the breadboard
# method illustrates in our Python
# program example:

import RPi.GPIO as GPIO
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

latch=35
data_bit=37
clock=33

led_speed=.5

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

def binary_leds_default():
    
    for i in range(255,127,-1):
        for j in range(8):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(128,256):
        for j in range(8):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
def binary_leds_inverse():
    
    for i in range(255,127,-1):
        for j in range(8):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(128,256):
        for j in range(8):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

def binary_leds_mirror():
    
    for i in range(255,127,-1):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(128,256):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
def binary_leds_mirror_inverse():
    
    for i in range(255,127,-1):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
    
    for i in range(128,256):
        for j in range(7,-1,-1):
            bin=f'{i:b}'
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
while True:
    try:
        binary_leds_default()
        binary_leds_mirror_inverse()
        break
    
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        print('\nStop program Execution/run:')
        print('cleanup/release all GPIO pinouts \
to LOW state.')
        
        for i in range(8):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        GPIO.cleanup()
        break