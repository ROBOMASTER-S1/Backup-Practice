# 16b Translator Python program example:

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
# 74HC595 shift register = 2
# LEDs = 16
# 220 ohm resistor = 16
# jumper wire = 27 or more +2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi fan, while in use/
# operation.

# 16b Translator Python program example:

# This Raspberry Pi Python program allows
# users to input decimal numbers, then
# translate them into binary, hexadecimal
# and decimal values using the 74HC595
# shift register.

# Please note: if you input numbers higher
# than 30000, the Raspberry Pi will take
# some processing time before it outputs
# its given value/number through the LEDs
# which are on the breadboard. However,
# the lcd display remains unaffected and
# will show you the value, while waiting
# for the Ras Pi to process the output
# via through the LEDs, which all will
# show are on, until done processing.

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

latch=33
data_bit=35
clock=31

msbs=65536

control_shift=data_bit,latch,clock

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

message='16b TRANSLATOR','ENTER 16b NUMBER'
value_error='BYTE VALUES ONLY','PLEASE: 0-65535'
index_error='VALUE EXCEEDS','16b RANGE 0-65535'

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
                f'{byte:b}',1)
                display.lcd_display_string(
                f'H: {byte:X} D: {byte:d}',2)
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