# 8b Translator Python program example:

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

# 8b Translator Python program example:

# This Raspberry Pi Python program allows
# users to input decimal numbers, then
# translate them into binary, hexadecimal
# and decimal values using the 74HC595
# shift register.

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

msbs=256

control_shift=data_bit,latch,clock

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

message='8b TRANSLATOR','ENTER 8b NUMBER:'
value_error='BYTE VALUES ONLY','PLEASE: 0-255'
index_error='VALUE EXCEEDS','8b RANGE 0-255'

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
while True:
    try:
        while True:
            try:
                display.lcd_clear()
                display.lcd_display_string(
                message[0],1)
                byte=int(input(display.
                lcd_display_string(message[1],2)))
                if byte>=msbs:
                    display.lcd_clear()
                    for i in range(2):
                        display.lcd_display_string(
                        index_error[i],1+i)
                    wait(2)
                    break       
                display.lcd_clear()
                display.lcd_display_string(
                f'BINARY: {byte:b}',1)
                display.lcd_display_string(
                f'HEX: {byte:X} DEC: {byte:d}',2)
                for i in range(byte,-1,-1):            
                    bin=f'{byte:b}'
                    for j in range(16):                
                        GPIO.output(latch,0)
                        GPIO.output(
                        data_bit,int(bin[j]))
                        GPIO.output(clock,1)
                        GPIO.output(latch,1)
                        GPIO.output(clock,0)
                            
            except ValueError:
                display.lcd_clear()
                for i in range(2):
                    display.lcd_display_string(
                    value_error[i],1+i)            
                wait(2)
                break
            
            except IndexError:
                pass
            wait(3)
            
            for i in range(16):            
                GPIO.output(latch,0)
                GPIO.output(data_bit,0)
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            
# Note: it is recomended that you setup
# a KeyboardInterrupt handler to force
# the GPIO pins to return to a low state/off.

# GPIO.cleanup() sets all GPIO pins to LOW/OFF

    except KeyboardInterrupt:
        exec(stop_program_message)
        
        for i in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        display.lcd_clear()
        display.lcd_backlight(0)
        GPIO.cleanup()
        break