from machine import Pin
from machine import Timer
import utime, _thread

trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
water_low = Pin(16,Pin.IN, Pin.PULL_DOWN)
water_high = Pin(17,Pin.IN, Pin.PULL_DOWN)
solenoid_in = Pin(2,Pin.OUT, Pin.PULL_UP)
solenoid_out = Pin(3,Pin.OUT, Pin.PULL_UP)

status = ""

def ultra():
    trigger.low()
    utime.sleep_us(10)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance
def height():
    measure_1 = ultra()
    utime.sleep_us(10)
    measure_2 = ultra()
    utime.sleep_us(10)
    measure_3 = ultra()
    utime.sleep_us(10)
    avg = (measure_1 + measure_2 + measure_3) / 3
    return avg

def lowest(pin):
    while water_low.value() == 0:
        solenoid_in.value(0) # open input valve
        solenoid_out.value(1) # close output valve
    print("Lower valve has been closed\n")
    normal()
    
def highest(pin):
    while water_high.value() == 0:
        solenoid_in.value(1) # close input valve
        solenoid_out.value(0) # open output valve
    print("upper valve has been closed\n")
    normal()

def normal():
    status = monitor()
    solenoid_in.value(0) # close input valve
    solenoid_out.value(0) # open output valve
    print(status)
    utime.sleep(0.5)
    
def monitor():
    dis = height()
    max_high = 400 # in cm
    word = "The level of water is at " + str(max_high - dis) + " cm.\n"
    return word
    
water_low.irq(trigger=Pin.IRQ_FALLING, handler=lowest)
water_high.irq(trigger=Pin.IRQ_FALLING, handler=highest)
normal()
while True:
    normal()