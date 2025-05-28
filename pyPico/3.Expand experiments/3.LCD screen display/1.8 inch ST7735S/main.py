'''
Experiment name: LCD liquid crystal display
Version: v1.0
Date: 2020.12
Author： 01Studio
Description： Programming to achieve a variety of LCD display functions, including drawing dots, lines, rectangles, circles, displaying English, displaying pictures and so on.
refer: https://github.com/AnthonyKNorman/MicroPython_ST7735
'''

import machine,time,lcd_gfx,st7735,time
from bmp import BMP

#initialising the LCD
spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
d = st7735.ST7735(spi, rst=13, ce=9, dc=12)
d.reset()
d.begin()

#white background
d._bground = 0xffff
d.fill_screen(d._bground)

#draw dot, (0,0,0) means black
d.pixel(5, 5, d.rgb_to_565(0,0,0))

#draw a line, (0,0,0) means black
lcd_gfx.drawLine(5,10,80,10,d,d.rgb_to_565(0,0,0))

#draw a rectangle, (0,0,0) means black.
lcd_gfx.drawRect(5,20,80,40,d,d.rgb_to_565(0,0,0))

#drawing a circle, (0,0,0) means black.
lcd_gfx.drawCircle(40,90,20,d,d.rgb_to_565(0,0,0))

#write characters
d.p_string(10,130,'Hello 01Studio!',d.rgb_to_565(255,0,0))

time.sleep_ms(2000) #2 seconds delay

#show picture
BMP('flower128x160.bmp',d,0,0,1)