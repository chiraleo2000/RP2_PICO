from machine import Pin
import utime 

leds = [
    Pin(0,Pin.OUT),
    Pin(1,Pin.OUT),
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(4,Pin.OUT),
    Pin(5,Pin.OUT),
    Pin(6,Pin.OUT),
    Pin(7,Pin.OUT),
    Pin(16,Pin.OUT),
    Pin(17,Pin.OUT),
    Pin(26,Pin.OUT),
    Pin(27,Pin.OUT),
    Pin(28, Pin.OUT)
    ]
class LED:
    def __init__(self,delay):
        self.delay = delay
    def case1(self):
            # Forward_from_low
        for i in range(len(leds)):
            leds[i].toggle()
            utime.sleep(self.delay)
        # backward_from_high
        for i in range(len(leds)):
            leds[-i-1].toggle()
            utime.sleep(self.delay)
    def case2(self):
            # Forward_from_low
        for i in range(len(leds)):
            leds[i].toggle()
            utime.sleep(self.delay)
        # backward_from_low
        for i in range(len(leds)):
            leds[i].toggle()
            utime.sleep(self.delay)
            
    def case3(self):
        # Forward_from_high
        for i in range(len(leds)):
            leds[-i-1].toggle()
            utime.sleep(self.delay)
        # backward_from_low
        for i in range(len(leds)):
            leds[i].toggle()
            utime.sleep(self.delay)
            
    def case4(self):
        # Forward_from_high
        for i in range(len(leds)):
            leds[-i-1].toggle()
            utime.sleep(self.delay)
        # backward_from_high
        for i in range(len(leds)):
            leds[-i-1].toggle()
            utime.sleep(self.delay)
            
    def case5(self):
        if len(leds) // 2 == 0:
            for i in range(len(leds)):
                leds[-i-1].toggle()
                leds[i].toggle()
                utime.sleep(self.delay)
        else: 
            for i in range(len(leds)//2):
                leds[-i-1].toggle()
                leds[i].toggle()
                utime.sleep(self.delay)
            leds[i+1].on()
            utime.sleep(self.delay)
            leds[i+1].off()
            for j in range(len(leds)//2):
                leds[-i+j-1].toggle()
                leds[i-j].toggle()
                utime.sleep(self.delay)
            
    def case6(self,n):
        if n < len(leds):
            #forward_limit_from_low
            for i in range (n):
                leds[i].toggle()
                utime.sleep(self.delay)
            for i in range(len(leds)-n):
                leds[i+n].toggle()
                leds[i].toggle()
                utime.sleep(self.delay)
            for i in range (n):
                leds[-n+i].toggle()
                utime.sleep(self.delay)
            #backward_limit_from_high
            for i in range (n):
                leds[-i-1].toggle()
                utime.sleep(self.delay)
            for i in range(len(leds)-n):
                leds[-i-n-1].toggle()
                leds[-i-1].toggle()
                utime.sleep(self.delay)
            for i in range (n):
                leds[n-i-1].toggle()
                utime.sleep(self.delay)
        else:
            print("Error")

def LEDx(x,y,n):
    i = 0
    if x ==6:
        k = int(input("Enter number of dot(s) (less than {}): ".format(len(leds))))
    while i < n:
        if x ==1:
            LED(y).case1()
        elif x ==2:
            LED(y).case2()
        elif x ==3:
            LED(y).casee()
        elif x ==4:
            LED(y).case4()
        elif x ==5:
            LED(y).case5()
        elif x ==6:
            LED(y).case6(k)
        else:
            print("Enter numbey only (1-6)")
            break
        i += 1
# For resetting        
for i in range(len(leds)):
    leds[i].off()
#
while True:
    try:
        X = int(input("Enter pattern (1-6): "))
        Y = float(input("Enter delay in seconds: "))
        N = int(input("Number of Cycle(s): "))
        LEDx(X,Y,N)
    except:
        print("input_incorrected")