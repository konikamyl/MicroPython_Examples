'''
Experimental name: Neopixel RGB Light Strip
Version: v1.0
Date: 2021.3
Author: 01Studio, benevpi (https://github.com/benevpi/pico_python_ws2812b)
Description: Program the strip to cycle through red (RED), green (GREEN) and blue (BLUE).
'''

import time
from ws2812b import ws2812b

#number of beads 30, control pin Pin27
np = ws2812b(num_leds=30, 27)

while True:
    
    #red
    pixels.fill(255,0,0)
    pixels.show()
    time.sleep(1)

    #green
    pixels.fill(0,255,0)
    pixels.show()
    time.sleep(1)

    #blue
    pixels.fill(0,0,255)
    pixels.show()
    time.sleep(1)