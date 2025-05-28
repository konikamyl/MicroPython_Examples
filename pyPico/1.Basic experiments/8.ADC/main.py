'''
Experiment name: ADC-voltage measurement
Version: v1.0
Date: 2021.1
Author: 01Studio
Description： Through the ADC data acquisition, converted into voltage on the display. ADC precision 12 bits (note that the return is 0-65535), voltage 0-3.3V.
'''

#importing related modules
from machine import Pin,SoftI2C,ADC
from ssd1306 import SSD1306_I2C
import time

#initialising oled
i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#initialise adc
adc = ADC(0) #Pin = 26

while True:
    
    value = adc.read_u16()
    
    oled.fill(0)  # clear screen with black background
    oled.text('01Studio', 0, 0)  # first line display 01Studio
    oled.text('ADC', 0, 15)      # the next line displays the name of the experiment

    #get ADC values
    oled.text(str(value),0,40)
    oled.text('(65535)',40,40)

    #calculation of the voltage value, the data obtained 0-4095 corresponds to 0-3V, (‘%.2f’%) means that 2 decimals are retained
    oled.text(str('%.2f'%(value/65535*3.3)),0,55)
    oled.text('V',40,55)

    oled.show()
    time.sleep_ms(300)
