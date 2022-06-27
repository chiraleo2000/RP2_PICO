from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime, _thread

trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
solenoid_in = Pin(8,Pin.OUT)
solenoid_out = Pin(9,Pin.OUT)
water_low = Pin(2,Pin.IN)
water_high = Pin(3,Pin.IN)
# i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # OLED
# oled = SSD1306_I2C(128, 64, i2c) # OLED
i = 0
water_release = Pin(6,Pin.IN)

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
# for display on OLED need _thread
#def report(h,delay, i):
#    dis = h
#    max_high = 400 # in cm
#    if i == 0:
#        oled.text("The level of water is at ", 0 , 12)
#        oled.text(str(max_high - dis), 20 , 24)
#       oled.text(" cm.\n", 40 , 24)
#    elif i == 1:
#        oled.text("Lower valve has been closed", 0 , 12)
#    elif i == 2:
#        oled.text("upper valve has been closed", 0 , 12)
#    utime.sleep(delay)

#def lowest(pin):
#    solenoid_in.on() # open input valve
#    solenoid_out.off() # close output valve
#    #_thread.start_new_thread(report,(h, 0.1), 1)
#    print("Lower valve close")
#    utime.sleep(0.5)
    
#def highest(pin):
#    solenoid_in.off() # close input valve
    #_thread.start_new_thread(report,(h, 0.1), 2)
#    print("upper valve close")
#    utime.sleep(0.5)
    
def case(x,y,z):
    # [water_high, water_low, water_release]
    if z == 1:
        if (x, y) == (0, 0):
            #solenoid_in.off() # close input solenoid valve
            #solenoid_out.on() # open output solenoid valve 
            solenoid_in.value(0) # close input solenoid valve
            solenoid_out.value(1) # open output solenoid valve
            print("high release")
            utime.sleep(0.5)
        elif (x, y) == (1, 0):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.on()# open output solenoid valve       
            solenoid_in.value(0) # close input solenoid valve
            solenoid_out.value(1) # open output solenoid valve
            print("normal release")
            utime.sleep(0.5)
        elif (x, y) == (1, 1):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off() # close output solenoid valve
            solenoid_in.value(0) # close input solenoid valve
            solenoid_out.value(1) # open output solenoid valve
            print("low")
            utime.sleep(0.5)
    elif z == 0:
        if (x, y) == (0, 0):
            #solenoid_in.off() # close input solenoid valve
            #solenoid_out.off() # close output solenoid valve 
            solenoid_in.value(0) # close input solenoid valve
            solenoid_out.value(0) # open output solenoid valve
            print("high stock")
            utime.sleep(0.5)
        elif (x, y) == (1, 0):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off()# close output solenoid valve       
            solenoid_in.value(1) # close input solenoid valve
            solenoid_out.value(0) # open output solenoid valve
            print("normal stock")
            utime.sleep(0.5)
        elif (x, y) == (1, 1):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off() # close output solenoid valve
            solenoid_in.value(1) # close input solenoid valve
            solenoid_out.value(0) # open output solenoid valve
            print("low")
            utime.sleep(0.5)
    else:
        #solenoid_in.off()
        #solenoid_out.off()
        solenoid_in.value(0) # close input solenoid valve
        solenoid_out.value(0) # open output solenoid valve
        print("error")
        utime.sleep(0.5)
    
#water_low.irq(trigger=Pin.IRQ_RISING, handler=lowest)
#water_high.irq(trigger=Pin.IRQ_FALLING, handler=highest)
while True:
    h = height()
    try:
        case(water_high.value(), water_low.value(), water_release())
        print("water level: "+ str(400 - h) + " cm ")
#        _thread.start_new_thread(report,(h, 0.1), 0)
    except:
        case(0,0,0)
