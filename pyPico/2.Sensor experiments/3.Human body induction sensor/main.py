'''
Experiment name: Human body sensing sensor
Version: v1.0
Date: 2021.1
Author: 01Studio
Community: www.01studio.org
'''
import time
from machine import SoftI2C,Pin    #import I2C, Pin submodules from machine module
from ssd1306 import SSD1306_I2C    #import SSD1306_I2C sub-module from ssd1306 module

#initialising oled
i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#key configuration
human = Pin(27, Pin.IN, Pin.PULL_UP)

#OLED initial information display
oled.fill(0)  # clear screen with black background
oled.text("01Studio", 0, 0)  # write the contents of line 1
oled.text("Human body test:", 0, 15)  # write the contents of line 2
oled.show()  # OLED display execution

def Display(human): #Get People blinks 5 times for effect!

    for i in range(5):
        oled.fill(0)  # clear screen with black background
        oled.text("01Studio", 0, 0)  # write the contents of line 1
        oled.text("Human body test:", 0, 15)  # write the contents of line 2
        oled.text("Get People!!!", 0, 40)  # write the contents of line 3
        oled.show()  # OLED display execution
        time.sleep_ms(500)

        oled.fill(0)  # clear screen with black background
        oled.text("01Studio", 0, 0)  # write the contents of line 1
        oled.text("Human body test:", 0, 15)  # write the contents of line 2
        oled.text("            ", 0, 40)  # write the contents of line 3
        oled.show()  # OLED display execution
        time.sleep_ms(500)


human.irq(Display,Pin.IRQ_RISING) #define interrupt, falling edge trigger
