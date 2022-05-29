import RPi.GPIO as GPIO,drivers,threading
from time import sleep as wait

# Breadboard Metod:
# Actual GPIO Pinouts

red_bin_leds=[13,15,19,21,23,29,31,33]

blue_leds=[11,35]

yellow_leds=[7,37]

RGB_led=[18,16,12]

RGB_mix=[[18,12],[18,16],[16,12]]

RGB_logic=[18,16,12,[18,16],
[18,12],[12,16],[18,16,12,16]]

hz=500 # LED dimmer herz value

led_speed=1

on_off=0,1

GPIO.setmode(GPIO.BOARD) # breadboard method
GPIO.setwarnings(False) # disable setwarnings

display=drivers.Lcd() # enable the LCD display
display.lcd_clear() # clear the LCD screen
display.lcd_backlight(1)

for i in red_bin_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,0)
    
for i in yellow_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in blue_leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
    
for i in RGB_led:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)

def binary_nums():
    for i in range(1,256):
        display.lcd_display_string(
        f'Binary: {i:b}',1)
        display.lcd_display_string(
        f'Hex: {i:X} Dec: {i:d}',2)
        wait(led_speed)    

threading.Thread(target=binary_nums).start()

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)    
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)

GPIO.output(29,1)
GPIO.output(23,0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(31,1)

for i in range(6):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)

GPIO.output(29,1)
GPIO.output(23,0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(33,1)

for i in range(7):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
    
GPIO.output(15,0)
wait(led_speed)
GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0) 
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)

GPIO.output(29,1)
GPIO.output(23,0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(31,1)

for i in range(6):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)

GPIO.output(29,1)
GPIO.output(23,0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(23,1)

for i in range(4):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(21,1)

for i in range(3):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)
GPIO.output(19,1)

for i in range(2):
    GPIO.output(red_bin_leds[i],0)
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for j in range(2):
    GPIO.output(red_bin_leds[j],on_off[j])
wait(led_speed)

GPIO.output(13,1)
wait(led_speed)

for i in red_bin_leds:
    GPIO.output(i,1)