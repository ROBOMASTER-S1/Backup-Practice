import RPi.GPIO as GPIO,random
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

red1,red2=12,32
green1,green2=16,36
blue1,blue2=18,38

RGB_pins1=12,32,16,36,18,38

RGB1=red1,green1,blue1
RGB2=red2,green2,blue2

RGB_col_mix1=(
    [red1,green1],  # yellow
    [red1,blue1],   # pink
    [green1,blue1]) # cyan

RGB_col_mix2=(
    [red2,green2],  # yellow
    [red2,blue2],   # pink
    [green2,blue2]) # cyan

for i in range(3):
    GPIO.setup(RGB1[i],GPIO.OUT)
    GPIO.setup(RGB2[i],GPIO.OUT)

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

sentence=[
    'Watch this awesome LED Lightshow!\n',
    'Let\'s go inverse reverse.\n',
    'Let\'s go random flicker flashing.\n',
    'Now, let\'s do a random smooth.\n',
    'Let\'s do a Flicker Flash']

red_on='''
GPIO.output(red1,1)
GPIO.output(red2,1)
'''
red_off='''
GPIO.output(red1,0)
GPIO.output(red2,0)
'''
green_on='''
GPIO.output(green1,1)
GPIO.output(green2,1)
'''
green_off='''
GPIO.output(green1,0)
GPIO.output(green2,0)
'''
blue_on='''
GPIO.output(blue1,1)
GPIO.output(blue2,1)
'''
blue_off='''
GPIO.output(blue1,0)
GPIO.output(blue2,0)
'''    
yellow_on='''
GPIO.output(RGB_col_mix1[0],1)
GPIO.output(RGB_col_mix2[0],1)
'''
yellow_off='''
GPIO.output(RGB_col_mix1[0],0)
GPIO.output(RGB_col_mix2[0],0)
'''
pink_on='''
GPIO.output(RGB_col_mix1[1],1)
GPIO.output(RGB_col_mix2[1],1)
'''
pink_off='''
GPIO.output(RGB_col_mix1[1],0)
GPIO.output(RGB_col_mix2[1],0)
'''
cyan_on='''
GPIO.output(RGB_col_mix1[2],1)
GPIO.output(RGB_col_mix2[2],1)
'''
cyan_off='''
GPIO.output(RGB_col_mix1[2],0)
GPIO.output(RGB_col_mix2[2],0)
'''
white_on='''
GPIO.output(RGB1,1)
GPIO.output(RGB2,1)
'''
white_off='''
GPIO.output(RGB1,0)
GPIO.output(RGB2,0)
'''
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

for i in range(3):
    GPIO.output(RGB1[i],0)
    GPIO.output(RGB2[i],0)
    
for i in range(24):
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)    

