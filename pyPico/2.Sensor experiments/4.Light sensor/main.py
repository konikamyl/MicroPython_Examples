'''
Experiment name: Photosensitive sensor
Version: v1.0
Date： 2021.1
Author： 01Studio 【www.01Studio.org】
Description： Measurement and display of external environmental light intensity by photosensitive sensor.
'''

#importing related modules
from machine import Pin,SoftI2C,ADC
from ssd1306 import SSD1306_I2C
import time

#initialising oled
i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#initialise ADC1,Pin=27
Light = ADC(1)

while True:

	oled.fill(0)  # clear screen with black background
	oled.text('01Studio', 0, 0)  # first line display 01Studio
	oled.text('Light test:', 0, 15)      # the next line displays the name of the experiment

	value=Light.read_u16() #get ADC values

    #display value
	oled.text(str(value)+' (65535)',0,40)
 	#calculation of the voltage value, the data obtained 0-4095 corresponds to 0-3V, (‘%.2f’%) means that 2 decimals are retained
	oled.text(str('%.2f'%(value/65535*3.3))+' V',0,55)

	#judge the light intensity and display it in 3 levels.
	if 0 < value <=21845:
		oled.text('Bright', 60, 55)

	if 21845 < value <= 43690:
		oled.text('Normal', 60, 55)

	if 43690 < value <= 65535:
		oled.text('Weak  ', 60, 55)

	oled.show()
	time.sleep_ms(1000)
