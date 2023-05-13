# 16b Binary Translator Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electroics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1
# LCD display = 1
# 74HC595 shift register = 2
# LEDs = 16
# 220 ohm resistor = 16
# jumper wire = 39 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 16b Binary Translator Python program example:

# This Raspberry Pi 4 Python program allows
# users to input decimal numbers, then
# translate them into binary, hexadecimal
# and decimal values using two 74HC595
# shift registers.

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

# import functions:

import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

# Create variables for the latch, data bit and the clock.

# You can rename all these variables to any names you wish,
# but keep in mind that you must also rename any variables
# in your program as well. Click the Find and Replace command
# on the IDLE menu to make any renaming changes faster to cover
# any variables you want to rename. However, you should stick
# to meaningful names, so other programmers can learn and
# understand what's happening throughout the program's
# execution/run.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Note: Python executes its programs from the top, downward.
# You must place these variables in this correct order as shown.
# These pinout values won't execute right if you don't.

latch=33
data_bit=35
clock=31
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
msb=65535,65536 # most significant bits
lsb=32767,32768 # least significant bits

num1=0
num2=1
fib=[num1,num2]

led_speed=.5

control_shift=data_bit,latch,clock

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

for i in control_shift:GPIO.setup(i,GPIO.OUT)

for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

for i in range(msb[0],lsb[0],-1): # reverse forloop and step value -1
    bin=f'{i:b}'
    for j in range(16):
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(bin[j])-1) # with 2's complement value -1
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)

for i in range(lsb[1],msb[1]): # forward forloop
    bin=f'{i:b}'
    for j in range(16):
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(bin[j])) # without 2's complement
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
    
'''
num1=0
num2=1
fib=[num1,num2]

display.lcd_display_string(
f'16 Fibits: {num3}',1)
display.lcd_display_string(bin,2)

for i in range(23):
    num3=num1+num2
    fib.append(num3)
    num1=num2
    num2=num3
'''
