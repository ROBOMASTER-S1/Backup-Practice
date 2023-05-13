# import functions:

import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

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

latch=19
data_bit=21
clock=15
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
led_speed=1,.1 # pause duration

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

all_bits_set=['1001010011010011']

top_1rows=['0000000000010000']
top_2rows=['0000000000010010']
top_3rows=['0000000001010010']
top_4rows=['0000000001010011']

bottom_1rows=['1000000000000000']
bottom_2rows=['1000010000000000']
bottom_3rows=['1000010010000000']
bottom_4rows=['1001010010000000']

top_bottom_1rows=['1000000000010000']
top_bottom_2rows=['1000010000010010']
top_bottom_3rows=['1000010011010010']
top_bottom_4rows=['1001010011010011']

right_1columns=['1111011111111111']
right_2columns=['1111011111111011']
right_3columns=['1111011111110011']
right_4columns=['1011011111110011']

left_1columns=['1111111011111111']
left_2columns=['1111110011111111']
left_3columns=['1101110011111111']
left_4columns=['1101110011011111']

right_left_1columns=['1111011011111111']
right_left_2columns=['1111010011111011']
right_left_3columns=['1101010011110011']
right_left_4columns=['1001010011010011']

cascade_up=['0001010001010000']
cascade_down=['1000000010000011']
cascade_right=['1111010111010111']
cascade_left=['1001111011111011']

foll_top_1rows=['0000000000010000']
foll_top_2rows=['0000000000000010']
foll_top_3rows=['0000000001000000']
foll_top_4rows=['0000000000000001']
foll_top_5rows=['0001000000000000']
foll_top_6rows=['0000000010000000']
foll_top_7rows=['0000010000000000']
foll_top_8rows=['1000000000000000']

foll_left_column1=['1111011111111111']
foll_left_column2=['1111111111111011']
foll_left_column3=['1111111111110111']
foll_left_column4=['1011111111111111']
foll_left_column5=['1111111111011111']
foll_left_column6=['1101111111111111']
foll_left_column7=['1111110111111111']
foll_left_column8=['1111111011111111']

foll_top_bottom_1rows=['1000000000010000']
foll_top_bottom_2rows=['0000010000000010']    
foll_top_bottom_3rows=['0000000011000000']
foll_top_bottom_4rows=['0001000000000001']

foll_right_left_1columns=['1111011011111111']    
foll_right_left_2columns=['1111110111111011']
foll_right_left_3columns=['1101111111110111']    
foll_right_left_4columns=['1011111111011111']

top_bottom_inward_1rows=['0001000000000001']
top_bottom_inward_2rows=['0001000011000001']
top_bottom_inward_3rows=['0001010011000011']
top_bottom_inward_4rows=['1001010011010011']

right_left_inward_1columns=['1011111111011111']
right_left_inward_2columns=['1001111111010111']
right_left_inward_3columns=['1001110111010011']
right_left_inward_4columns=['1001010011010011']

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

def all_leds_off():
    
    for i in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,0)
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed[0])       
        
def all_leds_on():
    
    for i in all_bits_set:
        for j in range(16):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def all_leds_flash():
    
    for x in range(4):    
        for i in all_bits_set:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
    
        for i in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])

def dance_matrix_forward():
    
    cascade_right_left=[
        cascade_up,cascade_right,
        cascade_down,cascade_left]
    
    for y in range(4):
        for x in range(4):
            for i in cascade_right_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])

def dance_matrix_reverse():
    
    cascade_right_left=[
        cascade_up,cascade_right,
        cascade_down,cascade_left]
    
    for y in range(4):
        for x in range(3,-1,-1):
            for i in cascade_right_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])

def led_border_forward():
    
    led_border=[
        top_1rows,right_1columns,
        bottom_1rows,left_1columns]
    
    for y in range(3):
        for x in range(4):
            for i in led_border[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                    
def led_border_reverse():
    
    led_border=[
        top_1rows,right_1columns,
        bottom_1rows,left_1columns]
    
    for y in range(3):
        for x in range(3,-1,-1):
            for i in led_border[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                            
def top_bottom_rows_open():
    
    top_bottom_rows_open=[
        top_bottom_1rows,top_bottom_2rows,
        top_bottom_3rows,top_bottom_4rows]
    
    for x in range(3,-1,-1):
        for i in top_bottom_rows_open[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def top_bottom_rows_close():
    
    top_bottom_rows_open=[
        top_bottom_1rows,top_bottom_2rows,
        top_bottom_3rows,top_bottom_4rows]
    
    for x in range(4):
        for i in top_bottom_rows_open[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])

def right_left_columns_open():
    
    right_left_columns_open=[
        right_left_1columns,
        right_left_2columns,
        right_left_3columns,
        right_left_4columns]
    
    for x in range(3,-1,-1):
        for i in right_left_columns_open[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def right_left_columns_close():
    
    right_left_columns_close=[
        right_left_1columns,
        right_left_2columns,
        right_left_3columns,
        right_left_4columns]
    
    for x in range(4):
        for i in right_left_columns_close[x]:
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def random_bits_on():
    
    for i in range(20):
        for j in range(16):
            randbit=random.randint(0,1)
            GPIO.output(latch,0)
            GPIO.output(data_bit,randbit)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])
        
def cascade_right_left():
    
    cascade_right_left=[
        cascade_right,cascade_left]
    
    for y in range(6):
        for x in range(2):
            for i in cascade_right_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def cascade_left_right():
    
    cascade_right_left=[
        cascade_right,cascade_left]
    
    for y in range(6):
        for x in range(1,-1,-1):
            for i in cascade_right_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def cascade_up_down():
    
    cascade_up_down=[
        cascade_up,cascade_down]
    
    for y in range(6):
        for x in range(2):
            for i in cascade_up_down[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])

def binary_counter():
    
    msb=7,8 # most significant bits
    lsb=3,4 # least significant bits

    for i in range(msb[0],lsb[0],-1):  # reverse forloop and step value -1
        bin=f'{i:b}'
        for j in range(3):
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(bin[j])-1) # with 2's complement value -1
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed[1])

        for i in range(lsb[1],msb[1]): # forward forloop
            bin=f'{i:b}'
            for j in range(3):
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(bin[j])) # without 2's complement
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def flip_flop_top_bottom():
    
    flip_flop=[
        top_4rows,bottom_4rows]
    
    for y in range(6):
        for x in range(2):
            for i in flip_flop[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
            
def flip_flop_right_left():
    
    flip_flop=[
        left_4columns,right_4columns]
    
    for y in range(6):
        for x in range(2):
            for i in flip_flop[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def flip_around_forward():
    
    flip_around=[
        right_4columns,bottom_4rows,
        left_4columns,top_4rows]
    
    for y in range(4):
        for x in range(4):
            for i in flip_around[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def flip_around_reverse():
    
    flip_around=[
        right_4columns,bottom_4rows,
        left_4columns,top_4rows]
    
    for y in range(4):
        for x in range(3,-1,-1):
            for i in flip_around[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def follow_top_rows():
    
    follow_top=[
        foll_top_1rows,foll_top_2rows,
        foll_top_3rows,foll_top_4rows,
        foll_top_5rows,foll_top_6rows,
        foll_top_7rows,foll_top_8rows]
    
    for y in range(2):
        for x in range(8):
            for i in follow_top[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
        for x in range(7,-1,-1):
            for i in follow_top[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
        
def follow_left_columns():
    
    follow_left=[
        foll_left_column1,foll_left_column2,
        foll_left_column3,foll_left_column4,
        foll_left_column5,foll_left_column6,
        foll_left_column7,foll_left_column8]
    
    for y in range(2):
        for x in range(7,-1,-1):
            for i in follow_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
        for x in range(8):
            for i in follow_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def follow_right_columns():
    
    follow_left=[
        foll_left_column1,foll_left_column2,
        foll_left_column3,foll_left_column4,
        foll_left_column5,foll_left_column6,
        foll_left_column7,foll_left_column8]
    
    for y in range(2):
        for x in range(8):
            for i in follow_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
        for x in range(7,-1,-1):
            for i in follow_left[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])

def follow_up_down_rows():
    
    follow_up_down=[
        foll_top_bottom_1rows,
        foll_top_bottom_2rows,    
        foll_top_bottom_3rows,
        foll_top_bottom_4rows]
    
    for y in range(1):
        for x in range(3,-1,-1):
            for i in follow_up_down[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
        for x in range(4):
            for i in follow_up_down[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def follow_right_left_columns():
    
    follow_right_left_columns=[
        foll_right_left_1columns,    
        foll_right_left_2columns,
        foll_right_left_3columns,    
        foll_right_left_4columns]   

    for y in range(1):
        for x in range(4):
            for i in follow_right_left_columns[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
        for x in range(3,-1,-1):
            for i in follow_right_left_columns[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                
def lines():
    
    lines_xyz=[
        foll_right_left_4columns,
        foll_top_bottom_4rows]        
                
    for y in range(4):
        for x in range(2):
            for i in lines_xyz[x]:            
                for j in range(16):               
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
                            
def matrix_rows_collapse():
    
    matrix_rows_inward=[
        top_bottom_inward_1rows,
        top_bottom_inward_2rows,
        top_bottom_inward_3rows,
        top_bottom_inward_4rows]
                
    for x in range(3,-1,-1):
        for i in matrix_rows_inward[x]:            
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def matrix_rows_expand():
    
    matrix_rows_outward=[
        top_bottom_inward_1rows,
        top_bottom_inward_2rows,
        top_bottom_inward_3rows,
        top_bottom_inward_4rows]
                
    for x in range(4):
        for i in matrix_rows_outward[x]:            
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])

def matrix_columns_collapse():
    
    matrix_columns_inward=[
        right_left_inward_1columns,
        right_left_inward_2columns,
        right_left_inward_3columns,
        right_left_inward_4columns]
                
    for x in range(3,-1,-1):
        for i in matrix_columns_inward[x]:            
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
def matrix_columns_expand():
    
    matrix_columns_outward=[
        right_left_inward_1columns,
        right_left_inward_2columns,
        right_left_inward_3columns,
        right_left_inward_4columns]
                
    for x in range(4):
        for i in matrix_columns_outward[x]:            
            for j in range(16):               
                GPIO.output(latch,0)
                GPIO.output(data_bit,int(i[j]))
                GPIO.output(clock,1)
                GPIO.output(latch,1)
                GPIO.output(clock,0)
            wait(led_speed[1])
            
matrix_functions=[
    all_leds_flash,right_left_columns_open,
    follow_right_left_columns,right_left_columns_close,
    matrix_columns_collapse,lines,follow_up_down_rows,
    matrix_rows_expand,top_bottom_rows_open,
    all_leds_flash,dance_matrix_forward,
    all_leds_flash,dance_matrix_reverse,
    all_leds_flash,random_bits_on,
    led_border_forward,follow_left_columns,
    led_border_reverse,follow_top_rows,
    cascade_up_down,all_leds_flash,
    cascade_right_left,all_leds_flash,
    flip_flop_top_bottom,all_leds_flash,
    flip_flop_right_left,all_leds_flash,
    flip_around_forward,all_leds_flash,
    flip_around_reverse,all_leds_flash]          

for i in matrix_functions:i()

print(len(matrix_functions),'Matrix Functions:')