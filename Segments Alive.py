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

control_shift=data_bit,latch,clock
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
pins=[40,7,11,13]

stop_program_message='''
print('Stop program Execution/run:')
print('cleanup/release all GPIO pinouts \
to LOW state.')'''

led_speed=1,.5 # pause duration

zero=[0,1,0,0,0,0,0,0]      
one=[0,1,1,1,1,0,0,1]
two=[0,0,1,0,0,1,0,0]
three=[0,0,1,1,0,0,0,0]
four=[0,0,0,1,1,0,0,1]
five=[0,0,0,1,0,0,1,0]
six=[0,0,0,0,0,0,1,0]
seven=[0,1,1,1,1,0,0,0]
eight=[0,0,0,0,0,0,0,0]
nine=[0,0,0,1,0,0,0,0]
a=[1,0,0,0,1,0,0,0]
b=[1,0,0,0,0,0,1,1]
c=[1,1,0,0,0,1,1,0]
d=[1,0,1,0,0,0,0,1]
e=[1,0,0,0,0,1,1,0]
f=[1,0,0,0,1,1,1,0]

nums=[
    zero,one,two,three,
    four,five,six,seven,
    eight,nine,a,b,c,d,e,f]

for i in pins:GPIO.setup(i,GPIO.OUT)

for i in control_shift:GPIO.setup(i,GPIO.OUT) # setup desired GPIO pinouts

for i in range(8):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,1)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)

for i in pins:
    GPIO.output(i,1)
    
input()
    
while True:
    try:        
        for x in range(4):
            GPIO.output(pins[x],1)
            for i in nums:
                for j in range(8):            
                    GPIO.output(latch,0)
                    GPIO.output(data_bit,int(i[j]))
                    GPIO.output(clock,1)
                    GPIO.output(latch,1)
                    GPIO.output(clock,0)
                wait(led_speed[1])
            GPIO.output(pins[x],0)
                        
    except KeyboardInterrupt:
        exec(stop_program_message)
        
        for i in range(8):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,0)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        break
            
GPIO.cleanup()