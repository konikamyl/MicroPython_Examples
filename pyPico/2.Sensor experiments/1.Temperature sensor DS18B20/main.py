'''
Experiment name: Temperature sensor DS18B20
Version: v1.0
Date: 2021.1
Author: 01Studio
Description： Acquire temperature data by programming and display on OLED.
'''

#cite related modules
from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C
from onewire import OneWire
from ds18x20 import DS18X20
import time

#initialising oled
i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #pyBoard I2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#initialising the DS18B20
ow= OneWire(Pin(27))   #enable Single Bus
ds = DS18X20(ow)        #the sensor is a DS18B20
rom = ds.scan()         #scanning of sensor addresses on a single bus, supports simultaneous connection of multiple sensors

while True:
	
	ds.convert_temp()   #temperature acquisition conversion
	temp = ds.read_temp(rom[0]) #display temperature, rom[0] for 1st DS18B20

	#show data
	oled.fill(0)   #clear screen with black background
	oled.text('01Studio', 0, 0)
	oled.text('Temp test:',0,20)
	oled.text(str('%.2f'%temp)+' C',0,40) #display temperature with 2 decimal places.
	oled.show()

	time.sleep_ms(1000)
