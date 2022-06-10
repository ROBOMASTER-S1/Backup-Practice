import RPi.GPIO as GPIO,drivers,threading

from time import sleep as wait
from variables import*

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings
display=drivers.Lcd() # enable the LCD display

display.lcd_clear() # clear the LCD screen
display.lcd_backlight(0)

for i in RGB_led1,RGB_led2:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)

for i in control_shift:GPIO.setup(i,GPIO.OUT)

def dedication():
    for i in range(10):
        display.lcd_display_string(title1[i],1)
        display.lcd_display_string(title2[i],2)
        wait(3)
        
    display.lcd_clear()
    display.lcd_display_string(dedication_title,1)
    display.lcd_display_string(name_dedication,2)
    wait(2)
    
    for i in range(len(name_dedication)):
        display.lcd_display_string(
        name_dedication[i:i+16],2)
        wait(.3)   
           
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
input()    
threading.Thread(target=dedication).start()

for x in range(9):
    exec(RGB_off);exec(led_loop4[x])
    for i in strings[x]:
        for j in range(16):               
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in flash_dance:
    exec(RGB_off);exec(led_loop4[0])
    for j in range(16):
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
        
for x in range(3):
    exec(RGB_off);exec(RGB_logic[x])
    for i in double_left:
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)        

for i in flash_dance:
    exec(RGB_off);exec(led_loop4[1])
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
    
for x in range(3):
    exec(RGB_off);exec(RGB_logic[x])
    for i in double_right:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in flash_dance:
    exec(RGB_off);exec(led_loop4[1])
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
        
for x in range(3):
    exec(RGB_off);exec(RGB_logic[x])
    for i in flip_flop:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in flash_dance:
    exec(RGB_off);exec(led_loop4[1])
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
    
for x in range(8,-1,-1):
    exec(RGB_off);exec(led_loop4[x])
    for i in strings[x]:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j])-1)
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in flash_dance:
    exec(RGB_off);exec(led_loop4[1])
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
        
for x in range(3):
    exec(RGB_off);exec(RGB_logic[x])
    for i in led_follow_left:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in flash_dance:
    exec(RGB_off);exec(led_loop4[1])
    for j in range(16):            
        GPIO.output(latch,0)
        GPIO.output(data_bit,int(i[j]))
        GPIO.output(clock,1)
        GPIO.output(latch,1)
        GPIO.output(clock,0)
    wait(led_speed)
        
for x in range(3):
    exec(RGB_off);exec(RGB_logic[x])
    for i in led_follow_right:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for x in range(9):
    exec(RGB_off);exec(led_loop4[x])
    for i in on_off:        
        for j in range(16):            
            GPIO.output(latch,0)
            GPIO.output(data_bit,int(i[j]))
            GPIO.output(clock,1)
            GPIO.output(latch,1)
            GPIO.output(clock,0)
        wait(led_speed)
        
for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,int(bits_on[i]))
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
wait(1)

for i in range(16):            
    GPIO.output(latch,0)
    GPIO.output(data_bit,0)
    GPIO.output(clock,1)
    GPIO.output(latch,1)
    GPIO.output(clock,0)
GPIO.cleanup()