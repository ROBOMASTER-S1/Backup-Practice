import RPi.GPIO as GPIO,drivers
from time import sleep as wait

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen

latch=23
data_bit=29
clock=21

control_shift=data_bit,latch,clock

for i in control_shift:GPIO.setup(i,GPIO.OUT)
    
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)    
    GPIO.output(latch,1)
    GPIO.output(clock,0)