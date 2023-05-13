# 24b Shift Register Fun Python program example:

# Created by Joseph C. Richardson, GitHub.com

# Note: be mindful while working with
# electronics. There are mistakes that
# cannot be corrected should you ignore
# any basic electronics rules. Electronics
# demands basic math skills and knowledge
# of electronics components alike.

# Items needed are as follows:

# Respberry Pi 4 = 1
# breadboard = 1 or more depending
# 74HC595 shift register = 2
# LEDs = 24
# 220 ohm resistor = 24
# jumper wire = 36 or more +2 for the Rasp pi 4 fan

# Note: use two other jumper wires for
# the Raspberry Pi 4 fan, while in use/
# operation.

# 24b Shift Register Fun Python program example:

# This Raspberry Pi 4 Python program allows
# users to have tons of fun, while learning
# how three 8b 74HC595 shift registers work.

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
# program example.

# import functions:

import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

port_pin=7,11,13

GPIO.setup(port_pin[0],GPIO.IN)
GPIO.setup(port_pin[1],GPIO.OUT)
GPIO.setup(port_pin[2],GPIO.OUT)

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

latch=35
data_bit=37
clock=33
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
msb=16_777_215,16_777_216 # most significant bits
lsb=8_388_607,8_388_608 # least significant bits

led_speed=1,.05,.5 # pause duration

computer_science='\nComputer Science is so much FUN!!\n'
choice='\nPress Number keys 1 through 16, then press Enter: '

sentence=[
    'Watch this awesome LED Lightshow!\n',
    'Let\'s go inverse reverse.\n',
    'Let\'s go random flicker flashing.\n',
    'Now, let\'s do a random smooth.\n',
    'Let\'s do a Flicker Flash']

beep_on='''
GPIO.output(port_pin[1],1)
GPIO.output(port_pin[2],1)
'''
beep_off='''
GPIO.output(port_pin[1],0)
GPIO.output(port_pin[2],0)
'''
stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')
'''
control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

led_show1=[
    '110000000000000000000011',
    '000001100000000001100000',
    '000000000001100000000000',
    '000001100000000001100000',
    '110000000000000000000011',    
    '000110000000000000011000',
    '000000011110011110000000']

led_show2=[    
    '100000000001100000000001',
    '100000000010010000000001',
    '100000000100001000000001',
    '100000001000000100000001',
    '100000010000000010000001',
    '100000100000000001000001',
    '100001000000000000100001',
    '100010000000000000010001',
    '100100000000000000001001',
    '101000000000000000000101',
    '110000000000000000000011',
    
    '110000000001100000000011',
    '110000000010010000000011',
    '110000000100001000000011',
    '110000001000000100000011',
    '110000010000000010000011',
    '110000100000000001000011',
    '110001000000000000100011',
    '110010000000000000010011',
    '110100000000000000001011',
    '111000000000000000000111',
    '111000000000000000000111',
    
    '111000000001100000000111',
    '111000000010010000000111',
    '111000000100001000000111',
    '111000001000000100000111',
    '111000010000000010000111',
    '111000100000000001000111',
    '111001000000000000100111',
    '111010000000000000010111',
    '111100000000000000001111',
    
    '111100000001100000001111',
    '111100000010010000001111',
    '111100000100001000001111',
    '111100001000000100001111',
    '111100010000000010001111',
    '111100100000000001001111',
    '111101000000000000101111',
    '111110000000000000011111',
    
    '111110000001100000011111',
    '111110000010010000011111',
    '111110000100001000011111',
    '111110001000000100011111',
    '111110010000000010011111',
    '111110100000000001011111',
    '111111000000000000111111',
    
    '111111000001100000111111',
    '111111000010010000111111',
    '111111000100001000111111',
    '111111001000000100111111',
    '111111010000000010111111',
    '111111100000000001111111',
    
    '111111100001100001111111',
    '111111100010010001111111',
    '111111100100001001111111',
    '111111101000000101111111',
    '111111110000000011111111',
    
    '111111110001100011111111',
    '111111110010010011111111',
    '111111110100001011111111',
    '111111111000000111111111',
    
    '111111111001100111111111',
    '111111111010010111111111',
    '111111111100001111111111',
    
    '111111111101101111111111',
    '111111111110011111111111',
    '111111111111111111111111']
    
led_show3=[    
    '100000000001100000000001',
    '010000000001100000000010',
    '001000000001100000000100',
    '000100000001100000001000',
    '000010000001100000010000',
    '000001000001100000100000',
    '000000100001100001000000',
    '000000010001100010000000',
    '000000001001100100000000',
    '000000000101101000000000',
    '000000000011110000000000',
    
    '100000000011110000000001',
    '010000000011110000000010',
    '001000000011110000000100',
    '000100000011110000001000',
    '000010000011110000010000',
    '000001000011110000100000',
    '000000100011110001000000',
    '000000010011110010000000',
    '000000001011110100000000',
    '000000000111111000000000',
    
    '100000000111111000000001',
    '010000000111111000000010',
    '001000000111111000000100',
    '000100000111111000001000',
    '000010000111111000010000',
    '000001000111111000100000',
    '000000100111111001000000',
    '000000010111111010000000',
    '000000001111111100000000',
    
    '100000001111111100000001',
    '010000001111111100000010',
    '001000001111111100000100',
    '000100001111111100001000',
    '000010001111111100010000',
    '000001001111111100100000',
    '000000101111111101000000',
    '000000011111111110000000',
    
    '100000011111111110000001',
    '010000011111111110000010',
    '001000011111111110000100',
    '000100011111111110001000',
    '000010011111111110010000',
    '000001011111111110100000',
    '000000111111111111000000',
    
    '100000111111111111000001',
    '010000111111111111000010',
    '001000111111111111000100',
    '000100111111111111001000',
    '000010111111111111010000',
    '000001111111111111100000',
    
    '100001111111111111100001',
    '010001111111111111100010',
    '001001111111111111100100',
    '000101111111111111101000',
    '000011111111111111110000',
    
    '100011111111111111110001',
    '010011111111111111110010',
    '001011111111111111110100',
    '000111111111111111111000',
    
    '100111111111111111111001',
    '010111111111111111111010',
    '001111111111111111111100',
    
    '101111111111111111111101',
    '011111111111111111111110',
    '111111111111111111111111']

led_show4=[
    '111111111111111111111111',
    '111111111110011111111111',
    '111111111100001111111111',
    '111111111000000111111111',
    '111111110000000011111111',
    '111111100000000001111111',
    '111111000000000000111111',
    '111110000000000000011111',
    '111100000000000000001111',
    '111000000000000000000111',
    '110000000000000000000011',
    '100000000000000000000001']

led_show5=[
    '111111111111111111111111',
    '011111111111111111111110',
    '001111111111111111111100',
    '000111111111111111111000',
    '000011111111111111110000',
    '000001111111111111100000',
    '000000111111111111000000',
    '000000011111111110000000',
    '000000001111111100000000',
    '000000000111111000000000',
    '000000000011110000000000',
    '000000000001100000000000']

led_show6=[    
    '100000000000000000000001',
    '010000000000000000000010',
    '001000000000000000000100',
    '000100000000000000001000',
    '000010000000000000010000',
    '000001000000000000100000',
    '000000100000000001000000',
    '000000010000000010000000',
    '000000001000000100000000',
    '000000000100001000000000',
    '000000000010010000000000',
    '000000000001100000000000',    
    '000000000010010000000000',
    '000000000100001000000000',
    '000000001000000100000000',
    '000000010000000010000000',
    '000000100000000001000000',
    '000001000000000000100000',
    '000010000000000000010000',
    '000100000000000000001000',
    '001000000000000000000100',
    '010000000000000000000010',
    '100000000000000000000001']

led_show7=[   
    '110000000000000000000011',
    '001100000000000000001100',
    '000011000000000000110000',
    '000000110000000011000000',
    '000000001100001100000000',
    '000000000011110000000000',
    '000000001100001100000000',
    '000000110000000011000000',
    '000011000000000000110000',
    '001100000000000000001100',
    '110000000000000000000011']

led_show8=[   
    '111000000000000000000111',
    '000111000000000000111000',
    '000000111000000111000000',
    '000000000111111000000000',
    '000000111000000111000000',
    '000111000000000000111000',
    '111000000000000000000111']

led_show9=[
    '111100000000000000001111',
    '000011110000000011110000',
    '000000001111111100000000',
    '000011110000000011110000',
    '111100000000000000001111']

led_show10=[    
    '111110000000000000011111',
    '000001111100001111100000',
    '000000000011110000000000',
    '111100000000000000001111',
    '000000000011110000000000',
    '111100000000000000001111',
    '000000000011110000000000',
    '111100000000000000001111',
    '000000000011110000000000',
    '111100000000000000001111',
    '000000000011110000000000',    
    '111111111100001111111111',
    '000000000011110000000000',
    '111111111100001111111111',
    '000000000011110000000000',
    '111111111100001111111111',
    '000000000011110000000000',
    '111111111100001111111111',
    '000000000011110000000000']

led_show11=[    
    '111111111111111111111111',
    '000000000000000000000000',
    '111111111111111111111111',
    '000000000000000000000000',
    '111111111111111111111111',
    '000000000000000000000000']

led_show12=[    
    '110011001100110011001100',
    '001100110011001100110011',
    '110011001100110011001100',
    '001100110011001100110011',
    '110011001100110011001100',
    '001100110011001100110011',
    '110011001100110011001100',
    '001100110011001100110011',
    '110011001100110011001100',
    '001100110011001100110011',
    '110011001100110011001100',
    '001100110011001100110011']

led_show13=[   
    '000000000001100000000000',
    '000000000010010000000000',
    '000000000101101000000000',
    '000000001010010100000000',
    '000000010101101010000000',
    '000000101010010101000000',
    '000001010101101010100000',
    '000010101010010101010000',
    '000101010101101010101000',
    '001010101010010101010100',
    '010101010101101010101010',
    '101010101010010101010101',
    '010101010100001010101010',
    '101010101000000101010101',
    '010101010000000010101010',
    '101010100000000001010101',
    '010101000000000000101010',
    '101010000000000000010101',
    '010100000000000000001010',
    '101000000000000000000101',
    '010000000000000000000010',
    '100000000000000000000001']

led_show14=[
    '100000000000000000000001',
    '010000000000000000000010',
    '101000000000000000000101',
    '010100000000000000001010',
    '101010000000000000010101',
    '010101000000000000101010',
    '101010100000000001010101',
    '010101010000000010101010',
    '101010101000000101010101',
    '010101010100001010101010',
    '101010101010010101010101',
    '010101010101101010101010',
    '001010101010010101010100',
    '000101010101101010101000',
    '000010101010010101010000',
    '000001010101101010100000',
    '000000101010010101000000',
    '000000010101101010000000',
    '000000001010010100000000',
    '000000000101101000000000',
    '000000000010010000000000',
    '000000000001100000000000']    

led_show15=[
    '000000000001100000000000',
    '000000000011110000000000',
    '000000000111111000000000',
    '000000001111111100000000',
    '000000011111111110000000',
    '000000111111111111000000',
    '000001111111111111100000',
    '000011111111111111110000',
    '000111111111111111111000',
    '001111111111111111111100',
    '011111111111111111111110',
    '111111111111111111111111',
    '011111111111111111111110',
    '001111111111111111111100',
    '000111111111111111111000',
    '000011111111111111110000',
    '000001111111111111100000',
    '000000111111111111000000',
    '000000011111111110000000',
    '000000001111111100000000',
    '000000000111111000000000',
    '000000000011110000000000',
    '000000000001100000000000']

led_show16=[
    '100000000000000000000001',
    '110000000000000000000011',
    '111000000000000000000111',
    '111100000000000000001111',
    '111110000000000000011111',
    '111111000000000000111111',
    '111111100000000001111111',
    '111111110000000011111111',
    '111111111000000111111111',
    '111111111100001111111111',
    '111111111110011111111111',
    '111111111111111111111111',
    '111111111110011111111111',
    '111111111100001111111111',
    '111111111000000111111111',
    '111111110000000011111111',
    '111111100000000001111111',
    '111111000000000000111111',
    '111110000000000000011111',
    '111100000000000000001111',
    '111000000000000000000111',
    '110000000000000000000011',
    '100000000000000000000001']

def led_show_one():
    
    for i in led_show1:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)  
        wait(led_speed[2])
        
def led_show_two():
    
    for i in led_show2:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def led_show_three():
    
    for i in led_show3:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def led_show_four():
    
    for i in led_show4:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def led_show_five():
    
    for i in led_show5:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def led_show_six():
    
    for i in led_show6:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def led_show_seven():
    
    for i in led_show7:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])

def led_show_eight():
    
    for i in led_show8:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_nine():
    
    for i in led_show9:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
    
def led_show_ten():
    
    for i in led_show10:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_eleven():
    
    for i in led_show11:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_twelve():
    
    for i in led_show12:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_thirteen():
    
    for i in led_show13:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_fourteen():
    
    for i in led_show14:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_fifteen():
    
    for i in led_show15:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
def led_show_sixteen():
    
    for i in led_show16:
        for j in range(24):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)            
        wait(led_speed[1])
        
for i in range(24):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
led_functions=[
    led_show_one,led_show_two,
    led_show_three,led_show_four,
    led_show_five,led_show_six,
    led_show_seven,led_show_eight,
    led_show_nine,led_show_ten,
    led_show_eleven,led_show_twelve,
    led_show_thirteen,led_show_fourteen,
    led_show_fifteen,led_show_sixteen]

def rerun():
        
    while True:
        for i in range(24):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
            
        message=input(choice)
        if message=='1':
            led_functions[0]()
        elif message=='2':
            led_functions[1]()
        elif message=='3':
            led_functions[2]()
        elif message=='4':
            led_functions[3]()
        elif message=='5':
            led_functions[4]()
        elif message=='6':
            led_functions[5]()
        elif message=='7':
            led_functions[6]()
        elif message=='8':
            led_functions[7]()
        elif message=='9':
            led_functions[8]()
        elif message=='10':
            led_functions[9]()
        elif message=='11':
            led_functions[10]()
        elif message=='12':
            led_functions[11]()
        elif message=='13':
            led_functions[12]()
        elif message=='14':
            led_functions[13]()
        elif message=='15':
            led_functions[14]()
        elif message=='16':
            led_functions[15]()
        else:
            break
        
while True:
    
    for i in range(msb[0],lsb[0],-1):
        if GPIO.input(port_pin[0])==GPIO.HIGH:rerun()
            
        bin=f'{i:b}'
        print(
            f'BINARY Number = {msb[0]-i:b}\n\n'
            f'OCTAL Number = {msb[0]-i:o}\n\n'
            f'HEXADECIMAL Number = {msb[0]-i:X}\n'
            f'DECIMAL Number = {msb[0]-i}')
        
        for j in range(24):
            exec(beep_on)
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        exec(beep_off);wait(.5)            

    for i in range(lsb[1],msb[1]):
        if GPIO.input(port_pin[0])==GPIO.HIGH:rerun()
            
        bin=f'{i:b}'
        print(
            f'BINARY Number = {msb[0]-i:b}\n\n'
            f'OCTAL Number = {msb[0]-i:o}\n\n'
            f'HEXADECIMAL Number = {msb[0]-i:X}\n\n'
            f'DECIMAL Number = {msb[0]-i}')
        
        for j in range(24):
            exec(beep_on)
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        exec(beep_off);wait(.5)