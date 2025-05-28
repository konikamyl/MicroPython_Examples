'''
Experiment name: Light up the onboard LED light
Version: v1.0
Date: 2021.1
Author: 01Studio
Community: www.01studio.org
'''

# import Pin module
from machine import Pin

LED = Pin(25, Pin.OUT) #build the LED object
LED.value(1) #light up LED, high level light up