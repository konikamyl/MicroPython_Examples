'''
Experiment name: Atmospheric pressure sensor
Version: v1.0
Date： 2021.1
Author： 01Studio 【www.01Studio.org】
Description： Measure BMP280 temperature, barometric pressure and calculate altitude value and display it on OLED.
'''

import time,bmp280
from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C

#initialising oled
i2c1 = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c1, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#initialisation of BMP280, software emulation of I2C
i2c2 = SoftI2C(scl=Pin(4), sda=Pin(5))   #SoftI2C initialisation: scl --> 4, sda --> 5
BMP = bmp280.BMP280(i2c2)

while True:

    oled.fill(0)  # clear screen, black background
    oled.text('01Studio', 0, 0)
    oled.text('Air Pressure:', 0, 15)

    # display temperature
    oled.text(str(BMP.getTemp()) + ' C', 0, 35)
    # display humidity
    oled.text(str(BMP.getPress()) + ' Pa', 0, 45)
    # display altitude
    oled.text(str(BMP.getAltitude()) + ' m', 0, 55)

    oled.show()

    time.sleep_ms(1000)  # acquisition at 1-second intervals
