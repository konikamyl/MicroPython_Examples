'''
Experiment name: Ultrasonic sensor
Version: v1.0
Date： 2021.1
Author： 01Studio 【www.01Studio.org】
Description： Range measurement by ultrasonic sensor and display on OLED.
'''

#importing related modules
from HCSR04 import HCSR04     #how to call under sub-folders
from machine import Pin,SoftI2C
from ssd1306 import SSD1306_I2C
import time

#initialising oled
i2c1 = SoftI2C(scl=Pin(10), sda=Pin(11))   #SoftI2C initialisation: scl --> 10, sda --> 11
oled = SSD1306_I2C(128, 64, i2c1, addr=0x3c) #OLED display initialisation: 128*64 resolution, OLED's I2C address is 0x3c

#initialise interface trig=4,echo=5
trig = Pin(4,Pin.OUT)
echo = Pin(5,Pin.IN)
HC=HCSR04(trig,echo)

while True:

    oled.fill(0)  # clear screen, black background
    oled.text('01Studio', 0, 0)
    oled.text('Distance test:', 0, 15)

    Distance = HC.getDistance() #measuring distance

    # OLED distance display
    oled.text(str(Distance) + ' CM', 0, 35)

    oled.show()

    #serial port printing
    print(str(Distance)+' CM')

    time.sleep_ms(500) #1 acquisition per second
