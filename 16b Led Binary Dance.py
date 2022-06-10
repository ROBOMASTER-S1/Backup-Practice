# 16b Binary Dance Python program example:

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi = 1
# breadboard = 1
# LCD display = 1
# 74HC595 shift register = 2
# RGB led = 2
# LEDs = 16
# 220 ohm resistor = 22
# jumper wire = 33 or more +2 for the Rasp pi fan

# Note: use two other jumper wires for
# the Raspberry Pi fan, while in use/
# operation.

# 16b Binary Dance Python program example:

# This Raspberry Pi Python program allows
# users to have fun while they learn all
# about how binary data bits work with two
# 74HC595 shift registers.

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

# Note: if you study these strings
# and arrays, you can use them to make
# the two RGB leds be different colours.

from RGBProgram import*

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display
display.lcd_clear() # clear the LCD screen

latch=33
data_bit=35
clock=31

msbs=65535,65536
lsbs=32767,32768

on_off=0,1,0,1,0,1,0,1,0,1,0

RGB_led1=[13,11,7]
RGB_led2=[21,19,15]

RGB_mix1=[[13,11],[13,7],[11,7]]
RGB_mix2=[[21,19],[21,15],[19,15]]

blue_green='''
GPIO.output(RGB_led1[2],1)
GPIO.output(RGB_led2[1],1)'''

green_blue='''
GPIO.output(RGB_led1[1],1)
GPIO.output(RGB_led2[2],1)'''

red_yellow='''
GPIO.output(RGB_led1[0],1)
GPIO.output(RGB_mix2[0],1)'''

yellow_red='''
GPIO.output(RGB_led2[0],1)
GPIO.output(RGB_mix1[0],1)'''

pink_cyan='''
GPIO.output(RGB_mix1[1],1)
GPIO.output(RGB_mix2[2],1)'''

cyan_pink='''
GPIO.output(RGB_mix1[2],1)
GPIO.output(RGB_mix2[1],1)'''

blue='''
GPIO.output(RGB_led1[2],1)
GPIO.output(RGB_led2[2],1)'''

pink='''
GPIO.output(RGB_mix1[1],1)
GPIO.output(RGB_mix2[1],1)'''

cyan='''
GPIO.output(RGB_mix1[2],1)
GPIO.output(RGB_mix2[2],1)'''

RGB_off='''
for i in RGB_led1,RGB_led2:
    GPIO.output(i,0)'''

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

title='16b BINARY DANCE ','Python Program  '
programmer='BY Joseph C. Richardson, GitHub.com '

led_loop1=blue_green,green_blue
led_loop2=red_yellow,yellow_red
led_loop3=pink_cyan,cyan_pink

buz=23,29

led_speed=.18

for i in buz:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

for i in RGB_led1,RGB_led2:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

control_shift=latch,data_bit,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(16):            
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
            programmer[i:i+16],2);wait(0.2)
        wait(led_speed)
        display.lcd_clear()
        
        for i in range(msbs[0],lsbs[0],-1):
            display.lcd_display_string(
            f'{msbs[0]-i:b}',1)
            display.lcd_display_string(
            f'H: {msbs[0]-i:X} D: {msbs[0]-i:d}',2)
            bin=f'{i:b}'
            for x in range(2):
                exec(RGB_off)
                exec(led_loop2[x])
                GPIO.output(buz[x],1);wait(.0099)
                for j in range(16):
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(bin[j])-1)
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                GPIO.output(buz[x],0)
                wait(led_speed)
            
        for i in range(lsbs[1],msbs[1]):
            display.lcd_display_string(
            f'{i:b}',1)
            display.lcd_display_string(
            f'H: {i:X} D: {i:d}',2)
            bin=f'{i:b}'
            for x in range(2):
                exec(RGB_off)
                exec(led_loop3[x])
                GPIO.output(buz[x],1);wait(.0099)
                for j in range(16):                
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(bin[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                GPIO.output(buz[x],0)
                wait(led_speed)  
                    
        for i in range(11):
            for j in range(16):
                GPIO.output(latch,0)
                GPIO.output(data_bit,on_off[i])
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
                
            for x in range(2):
                exec(RGB_off)
                exec(led_loop4[x])
                GPIO.output(buz[x],1)
                wait(led_speed)
                GPIO.output(buz[x],0)
        display.lcd_clear()
        display.lcd_backlight(0)
        exec(RGB_off)
        break

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