'''
Experiment name: Temperature and humidity sensor experiment DTH11
Version: v1.0
Date: 2021.1
Author: ikornaselur (https://github.com/ikornaselur/pico-dht11)
TRANSLATION AND NOTE: Temperature and humidity data is programmed to be collected and displayed on an OLED.
'''

#introduction of related modules
from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C
from dht import DHT11, InvalidChecksum
import time

#initialising oled
i2c = SoftI2C(scl=Pin(10), sda=Pin(11))   #pyPico I2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c


# delay 1 second waiting for DHT11 to stabilise
time.sleep(1)

#create DTH11 object dt
dt = DHT11(machine.Pin(17))

while True:
    
    te=dt.temperature  #getting the temperature value
    dh=dt.humidity    #getting the humidity value
    
    oled.fill(0) #clear screen with black background
    oled.text('01Studio', 0, 0)
    oled.text('DHT11 test:',0,15)

    #display temperature
    oled.text(str(te)+' C',0,40)

    #display humidity
    oled.text(str(dh)+' %',55,40)

    oled.show()
    
    time.sleep_ms(2000)          #acquisition every 2 seconds
