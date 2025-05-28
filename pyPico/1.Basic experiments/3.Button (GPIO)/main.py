'''
Experiment name: Keypad (GPIO)
Version: v1.0
Date: 2021-1
Author: 01Studio
Community: www.01studio.org
'''

from machine import Pin

#building the LED object
led=Pin(25, Pin.OUT)

#key configuration
key = Pin(14, Pin.IN, Pin.PULL_UP)

while True:

    if key.value()==0: #KEY is pressed to ground
        led.high()    #light up the LED
        
    else:
        led.low()     #switch off the LED