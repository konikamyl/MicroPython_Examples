'''
Experiment name: OLED display (I2C bus)
Version: v1.0
Date: 2021.1
Author: 01Studio
Community: www.01studio.org
'''


from machine import SoftI2C,Pin         #import I2C, Pin submodules from machine module
from ssd1306 import SSD1306_I2C     #import SSD1306_I2C sub-module from ssd1306 module

i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

oled.text("Hello World!", 0,  0)      #write the contents of line 1
oled.text("MicroPython",  0, 20)      #write the contents of line 2
oled.text("By 01Studio",  0, 50)      #write the contents of line 3

oled.show()   #OLED display execution
