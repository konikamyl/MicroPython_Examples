'''
Experiment name: Running lights
Version: v2.0
Date: 2021.1
Author: 01Studio
'''

#import related modules
from machine import Pin
import time

#building LED objects
LED1 = Pin(18, Pin.OUT)
LED2 = Pin(19, Pin.OUT)
LED3 = Pin(20, Pin.OUT)

LEDS = [LED1,LED2,LED3]

# equivalent to for i in [0, 1, 2]，LED[i].low() executed 3 times, respectively LED 1，2，3
for i in range(3):
    LEDS[i].low()
    
while True:
    #using a for loop
    for i in range(3):
        LEDS[i].high()
        time.sleep_ms(1000) #delay 1000 milliseconds, i.e. 1 second
        LEDS[i].low()

