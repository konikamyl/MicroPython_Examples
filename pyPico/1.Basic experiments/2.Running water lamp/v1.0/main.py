'''
Experiment name: Running lights
Version: v1.0
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

#switch off all LEDs
LED1.low()
LED2.low()
LED3.low()

#while True indicates a continuous loop
while True:

    #LED1 on for 1 second
    LED1.high()
    time.sleep_ms(1000)
    LED1.low()

    #LED2 on for 1 second
    LED2.value(1)
    time.sleep_ms(1000)
    LED2.value(0)

    #LED3 on for 1 second
    LED3.value(1)
    time.sleep_ms(1000)
    LED3.value(0)