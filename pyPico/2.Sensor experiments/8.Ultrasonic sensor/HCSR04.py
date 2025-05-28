
from time import sleep_us,ticks_us,sleep

class HCSR04():
    def __init__(self,trig,echo):
        self.trig=trig
        self.echo=echo

    def getDistance(self):
        distance=0
        self.trig.value(1)
        sleep_us(20)
        self.trig.value(0)
        while self.echo.value() == 0:
            pass
        if self.echo.value() == 1:
            ts=ticks_us()                   #starting time
            while self.echo.value() == 1:   #wait for the end of the pulse high level
                pass
            te=ticks_us()                   #end time
            tc=te-ts                        #reverberation time (in us, 1us=1*10^(-6)s)
            distance=(tc*170)/10000         #distance calculation (unit: cm)
        return distance