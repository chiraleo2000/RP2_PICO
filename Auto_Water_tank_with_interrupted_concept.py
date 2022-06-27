from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
import utime, _thread

trigger = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
solenoid_in = Pin(8,Pin.OUT)
solenoid_out = Pin(9,Pin.OUT)
water_low = Pin(2,Pin.IN)
water_high = Pin(3,Pin.IN)
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # OLED
oled = SSD1306_I2C(128, 64, i2c) # OLED
i = 0
uart0 = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1)
water_release = Pin(6,Pin.IN)

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
# for display on OLED need _thread
def report(h,status,delay):
    dis = h
    max_high = 400 # in cm
    oled.fill(0)
    oled.text("The water level:", 0 , 12)
    oled.text(str(max_high - dis), 20 , 24)
    oled.text(" cm.", 90 , 24)
    oled.text(status, 0 , 36)
    oled.show()
    utime.sleep(delay)

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
            status = "high release"
            uart0.write("high release")
            utime.sleep(0.7)
        elif (x, y) == (1, 0):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.on()# open output solenoid valve       
            solenoid_in.value(1) # open input solenoid valve
            solenoid_out.value(1) # open output solenoid valve
            status = "normal release"
            uart0.write("normal release")
            utime.sleep(0.7)
        elif (x, y) == (1, 1):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off() # close output solenoid valve
            solenoid_in.value(1) # open input solenoid valve
            solenoid_out.value(0) # close output solenoid valve
            status = "low"
            uart0.write("low")
            utime.sleep(0.7)
    elif z == 0:
        if (x, y) == (0, 0):
            #solenoid_in.off() # close input solenoid valve
            #solenoid_out.off() # close output solenoid valve 
            solenoid_in.value(0) # close input solenoid valve
            solenoid_out.value(0) # close output solenoid valve
            status = "high stock"
            uart0.write("high stock")
            utime.sleep(0.7)
        elif (x, y) == (1, 0):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off()# close output solenoid valve       
            solenoid_in.value(1) # open input solenoid valve
            solenoid_out.value(0) # close output solenoid valve
            status = "normal stock"
            uart0.write("normal stock")
            utime.sleep(0.7)
        elif (x, y) == (1, 1):
            #solenoid_in.on()# open input solenoid valve
            #solenoid_out.off() # close output solenoid valve
            solenoid_in.value(1) # open input solenoid valve
            solenoid_out.value(0) # close output solenoid valve
            status = "low"
            uart0.write("low")
            utime.sleep(0.7)
    else:
        #solenoid_in.off()
        #solenoid_out.off()
        solenoid_in.value(0) # close input solenoid valve
        solenoid_out.value(0) # open output solenoid valve
        status = "error"
        uart0.write("error")
        utime.sleep(0.7)
    _thread.start_new_thread(report,(height(), status,0.1))
    
#water_low.irq(trigger=Pin.IRQ_RISING, handler=lowest)
#water_high.irq(trigger=Pin.IRQ_FALLING, handler=highest)
while True:
    case(water_high.value(), water_low.value(), water_release())
    uart0.write("water level: "+ str(400 - height()) + " cm ")
