# 8b Binary Counter Python program example:

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi = 1
# breadboard = 1
# LCD display = 1
# 74HC595 shift register = 1
# LEDs = 8
# 220 ohm resistor = 8
# jumper wire = 20 or more +2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi fan, while in use/
# operation.

# 8b Binary Counter Python program example:

# This Raspberry Pi Python program allows
# users to learn all about how binary data
# bits work with the 74HC595 shift register.

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

import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

latch=23
data_bit=29
clock=21

msbs=255,256
lsbs=127,128

on_off=0,1,0,1,0,1,0

led_speed=.5

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

title='8b BINARY COUNT ','Python Program  '
programmer='BY Joseph C. Richardson, GitHub.com '

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)    
    GPIO.output(latch,1)
    GPIO.output(clock,0)    

while True:
    display.lcd_display_string(title[0],1)
    display.lcd_display_string(title[1],2)
    wait(2)
    try:
        display.lcd_display_string(title[0],1)
        display.lcd_display_string(programmer,2)
        wait(1)

        for i in range(len(programmer)):
            display.lcd_display_string(
            programmer[i:i+16],2)
            wait(0.2)
        wait(led_speed)
        display.lcd_clear()
            
        for i in range(msbs[0],lsbs[0],-1):
            display.lcd_display_string(
            f'Binary: {msbs[0]-i:b}',1)
            display.lcd_display_string(
            f'Hex: {msbs[0]-i:X} Dec: {msbs[0]-i:d}',2)
            bin=f'{i:b}'
            for j in range(8):                
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])-1)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)                
            wait(led_speed)
            
        for i in range(lsbs[1],msbs[1]):
            display.lcd_display_string(
            f'Binary: {i:b}',1)
            display.lcd_display_string(
            f'Hex: {i:X} Dec: {i:d}',2)
            bin=f'{i:b}'
            for j in range(8):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed)
            
        for i in range(7):
            for j in range(8):
                GPIO.output(latch,0)
                GPIO.output(data_bit,on_off[i])
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed)
        break
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message)
        
        for i in range(8):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup()
        break