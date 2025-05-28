'''
Experiment name: Servo - 180°
Version: v1.0
Date: 2021.1
Author: 01Studio
Description： Control the servo to rotate different angles.
'''

from machine import Pin, PWM
import time

S1 = PWM(Pin(0)) # Servo1 pin is 0
S1.freq(50) #Servo control signal frequency

'''
Description: Servo control function
Function: 180 degree servo: angle:-90 to 90 indicates the corresponding angle.
     360 degree continuous rotation servo: angle:-90 to 90 rotation direction and speed value.
'''
def Servo(servo,angle):
    a = int(((angle+90)*2/180+0.5)/20*65535)
    print(a)
    S1.duty_u16(a)

while True:
    
    #-90 degrees
    Servo(S1,-90)
    time.sleep(1)

    #-45 degrees
    Servo(S1,-45)
    time.sleep(1)

    #0 degrees
    Servo(S1,0)
    time.sleep(1)

    #45 degrees
    Servo(S1,45)
    time.sleep(1)

    #90 degrees
    Servo(S1,90)
    time.sleep(1)