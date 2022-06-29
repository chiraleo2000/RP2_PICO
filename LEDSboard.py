from machine import Pin, PWM
import utime 

class LEDSboard:
    def __init__(self,ledlist):
        self.ledlist = ledlist
    def blink(self,delay=1,n=1): ## I need to find a way to insert defalut value so no requiement of delay and n without error
        for i in range (len(self.ledlist)):
            Pin(self.ledlist[i],Pin.OUT,Pin.PULL_DOWN)
        for i in range (n):
            for j in range (len(self.ledlist)):
                Pin(self.ledlist[j],Pin.OUT).on()
            utime.sleep(delay)
            for k in range (len(self.ledlist)):
                Pin(self.ledlist[k],Pin.OUT).off()
            utime.sleep(delay)     
    def on(self):
        for i in range (len(self.ledlist)):
            Pin(self.ledlist[i],Pin.OUT,Pin.PULL_DOWN)
        for j in range (len(self.ledlist)):
            Pin(self.ledlist[j],Pin.OUT).on()
    def off(self):
        for i in range (len(self.ledlist)):
            Pin(self.ledlist[i],Pin.OUT,Pin.PULL_DOWN)
        for k in range (len(self.ledlist)):
            Pin(self.ledlist[k],Pin.OUT).off()    
    def value(self,valuelist):
        for a in range (len(self.ledlist)):
            PWM(Pin(self.ledlist[a])).freq(1000)
        for b in range (len(valuelist)):
            power = int(((float(valuelist[b])*65536)-1))
            PWM(Pin(self.ledlist[b])).duty_u16(power)
    def right(self,delay=1,n=1):
        for i in range (len(self.ledlist)):
            Pin(self.ledlist[i],Pin.OUT,Pin.PULL_DOWN)
        for j in range (len(self.ledlist)):
            Pin(self.ledlist[j],Pin.OUT).on()
            utime.sleep(delay)
        for k in range (len(self.ledlist)):
            Pin(self.ledlist[k],Pin.OUT).off()
            utime.sleep(delay)
        
    def left(self,delay=1,n=1):
        for i in range (len(self.ledlist)):
            Pin(self.ledlist[i],Pin.OUT,Pin.PULL_DOWN)
        for j in range (len(self.ledlist)):
            Pin(self.ledlist[-1-j],Pin.OUT).on()
            utime.sleep(delay)
        for k in range (len(self.ledlist)):
            Pin(self.ledlist[-1-k],Pin.OUT).off()
            utime.sleep(delay)


def test():
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).value([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    utime.sleep(2)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).off()
    utime.sleep(1)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).on()
    utime.sleep(1)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).blink(0.1,25)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).blink()
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).blink(0.5) # or LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).blink(delay=0.5).
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).blink(n=5) 
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).left(0.2,5)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).right(0.2,5)
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).left()
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).right()
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).left(0.5) # or LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).left(delay=0).
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).right(0.5) # or LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).right(delay=0).
    LEDSboard([0,1,2,3,4,5,6,7,16,17,26,27,28]).right(n=5)
    utime.sleep(1)
while True:
    # test
    test()