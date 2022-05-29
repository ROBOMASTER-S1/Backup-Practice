import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

latch=33
data_bit=35
clock=31

#sensor=38

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

red='''
GPIO.output(RGB_led1[0],1)
GPIO.output(RGB_led2[0],1)'''

green='''
GPIO.output(RGB_led1[1],1)
GPIO.output(RGB_led2[1],1)'''

blue='''
GPIO.output(RGB_led1[2],1)
GPIO.output(RGB_led2[2],1)'''

yellow='''
GPIO.output(RGB_mix1[0],1)
GPIO.output(RGB_mix2[0],1)'''

pink='''
GPIO.output(RGB_mix1[1],1)
GPIO.output(RGB_mix2[1],1)'''

cyan='''
GPIO.output(RGB_mix1[2],1)
GPIO.output(RGB_mix2[2],1)'''

RGB_off='''
for y in RGB_led1,RGB_led2:
    GPIO.output(y,0)'''

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

led_loop1=blue_green,green_blue
led_loop2=red_yellow,yellow_red
led_loop3=pink_cyan,cyan_pink
led_loop4=red,green,blue,yellow,pink,cyan

RGB_logic=[
    led_loop1[0],led_loop1[1],
    led_loop2[0],led_loop2[1],
    led_loop3[0],led_loop3[1]]

led_speed=.1

#GPIO.setup(sensor,GPIO.IN)

control_shift=latch,data_bit,clock
    
on_off=[
    '1111111111111111',
    '0000000000000000']

bits_on='1111111111111111'

single_pass=[
    '1000000000000001','0100000000000010',
    '0010000000000100','0001000000001000',
    '0000100000010000','0000010000100000',
    '0000001001000000','0000000110000000',       
    '0000001001000000','0000010000100000',
    '0000100000010000','0001000000001000',
    '0010000000000100','0100000000000010']

double_pass=[
    '1000000000000001','1100000000000011',
    '0110000000000110','0011000000001100',
    '0001100000011000','0000110000110000',
    '0000011001100000','0000001111000000',
    '0000000110000000','0000001111000000',
    '0000011001100000','0000110000110000',
    '0001100000011000','0011000000001100',
    '0110000000000110','1100000000000011']

triple_pass=[
    '1000000000000001','1100000000000011',
    '1110000000000111','0111000000001110',
    '0011100000011100','0001110000111000',
    '0000111001110000','0000011111100000',
    '0000001111000000','0000000110000000',
    '0000001111000000','0000011111100000',
    '0000111001110000','0001110000111000',
    '0011100000011100','0111000000001110',
    '1110000000000111','1100000000000011']

single_right=[
    '1001001001001001',
    '0100100100100100',
    '0010010010010010']

single_left=[
    '1001001001001001',
    '0010010010010010',
    '0100100100100100']

double_right=[
    '1100110011001100',
    '0110011001100110',
    '0011001100110011',
    '1001100110011001']

double_left=[
    '0011001100110011',
    '0110011001100110',
    '1100110011001100',
    '1001100110011001']

join_inward=[
    '1000000000000001','1100000000000011',
    '1110000000000111','1111000000001111',
    '1111100000011111','1111110000111111',
    '1111111001111111','1111111111111111']

split_outward=[
    '1111111001111111',
    '1111110000111111',
    '1111100000011111',
    '1111000000001111',
    '1110000000000111',
    '1100000000000011',
    '1000000000000001']    
    
collapse_inward=[
    '0111111111111110','0011111111111100',
    '0001111111111000','0000111111110000',
    '0000011111100000','0000001111000000',
    '0000000110000000']

expand_outward=[
    '0000001111000000','0000011111100000',
    '0000111111110000','0001111111111000',
    '0011111111111100','0111111111111110',
    '1111111111111111']

stack_inward=[
    '0100000000000010','0010000000000100',
    '0001000000001000','0000100000010000',
    '0000010000100000','0000001001000000',
    '0000000110000000','1000000110000001',
    '0100000110000010','0010000110000100',
    '0001000110001000','0000100110010000',
    '0000010110100000','0000001111000000',
    '1000001111000001','0100001111000010',
    '0010001111000100','0001001111001000',
    '0000101111010000','0000011111100000',
    '1000011111100001','0100011111100010',
    '0010011111100100','0001011111101000',
    '0000111111110000','1000111111110001',
    '0100111111110010','0010111111110100',
    '0001111111111000','1001111111111001',
    '0101111111111010','0011111111111100',
    '1011111111111101','0111111111111110',
    '1111111111111111']

stack_outward=[
    '0000001001000000','0000010000100000',
    '0000100000010000','0001000000001000',
    '0010000000000100','0100000000000010',
    '1000000000000001','1000000110000001',
    '1000001001000001','1000010000100001',
    '1000100000010001','1001000000001001',
    '1010000000000101','1100000000000011',
    '1100000110000011','1100001001000011',
    '1100010000100011','1100100000010011',
    '1101000000001011','1110000000000111',
    '1110000110000111','1110001001000111',
    '1110010000100111','1110100000010111',
    '1111000000001111','1111000110001111',
    '1111001001001111','1111010000101111',
    '1111100000011111','1111100110011111',
    '1111101001011111','1111110000111111',
    '1111110110111111','1111111001111111',
    '1111111111111111']

flash_dance=[
    '1100000000000011',
    '0000000110000000',
    '1100000000000011',
    '0000000110000000',
    '1100000000000011',
    '0000000110000000',
    '1100000000000011',
    '0000000110000000',
    ]    

flip_flop=[
    '1111111100000000',
    '0000000011111111',]

strings=[
    single_pass,double_pass,
    triple_pass,join_inward,
    collapse_inward,stack_outward,
    split_outward,stack_inward,
    collapse_inward,flash_dance]

for i in RGB_led1,RGB_led2:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
    
for x in range(10):
    for i in strings[x]:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for x in range(5):
    for i in double_left:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)        

for i in flash_dance:        
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
    
for x in range(5):
    for i in double_right:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for x in range(5):
    for i in flip_flop:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

for x in range(3):
    for i in on_off:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(.5)        
        
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,int(bits_on[i]))
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

'''
for x in range(3):
    for i in strings[x]:
        for j in range(16):
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)

for p in RGB_logic:    
    exec(RGB_off);exec(p)
    wait(1)

for p in RGB_logic1:    
    for x in p:
        exec(RGB_off);exec(x)
        
exec(RGB_off)
exec(RGB_logic2[1])
'''