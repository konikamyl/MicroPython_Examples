'''
Experiment name: PWM (Buzzer)
Version: v1.0
Date: 2021-1
Author: 01Studio
Description： Drive a passive buzzer to emit sound of different frequencies by outputting PWM signals with different frequencies.
'''

from machine import Pin, PWM
import time

Beep = PWM(Pin(22)) # pin is 25, create and configure the PWM in the same statement
Beep.duty_u16(32768) # duty cycle 50 per cent, equivalent to a square wave;

#buzzer with a frequency of 200 Hz
Beep.freq(200)
time.sleep_ms(1000)

#buzzer with a frequency of 400 Hz
Beep.freq(400)
time.sleep_ms(1000)

#buzzer with a frequency of 600 Hz
Beep.freq(600)
time.sleep_ms(1000)

#buzzer with a frequency of 800 Hz
Beep.freq(800)
time.sleep_ms(1000)

#buzzer with a frequency of 1000 Hz
Beep.freq(1000)
time.sleep_ms(1000)

#discontinue
Beep.deinit()

