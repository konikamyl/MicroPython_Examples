'''
Experiment name: Timer
Version: v1.0
Date: 2021.1
Author: 01Studio
Description： Timer to make LED blink periodically 1 time per second
'''
from machine import Pin,Timer

led=Pin(25, Pin.OUT)

def fun(tim):

    led.toggle()

#building timer
tim = Timer()
tim.init(period=1000, mode=Timer.PERIODIC,callback=fun) #cycle time of 1000ms
