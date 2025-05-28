'''
Experiment Name: External interrupt
Version: v1.0
Date: 2021-1
Author: 01Studio
Community: www.01studio.org
'''

from machine import Pin
import time

#building the LED object
led=Pin(25, Pin.OUT)

#key configuration
key = Pin(14, Pin.IN, Pin.PULL_UP)

state=0 #LED Pin status

#LED state flip-flop
def fun(key):

    global state
    time.sleep_ms(10) #eliminate jitter
    if key.value()==0: #confirmation button pressed
        state = not state
        led.value(state)
    
key.irq(fun,Pin.IRQ_FALLING) #define interrupt, falling edge trigger