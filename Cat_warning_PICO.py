from machine import Pin
import utime
led_onboard = Pin(25, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)
led_3 = Pin(3, Pin.OUT)
buzz1 = Pin(10, Pin.OUT)
buzz2 = Pin(11, Pin.OUT)
PIR1 = Pin(16, Pin.IN, Pin.PULL_UP)
PIR2 = Pin(17, Pin.IN, Pin.PULL_UP)
while True:
    print(PIR1.value(), PIR2.value())
    if PIR1.value() == 1 and PIR2.value() == 0:
        led_1.value(1)
        led_2.value(0)
        buzz1.value(1)
        buzz2.value(0)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    elif PIR2.value() == 1 and PIR1.value() == 0:
        led_1.value(0)
        led_2.value(1)
        buzz1.value(0)
        buzz2.value(1)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    elif PIR2.value() == 1 and PIR1.value() == 1 :
        led_1.value(1)
        led_2.value(1)
        buzz1.value(1)
        buzz2.value(1)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    else:
        led_1.value(0)
        led_2.value(0)
        buzz1.value(0)
        buzz2.value(0)
        led_3.value(0)
        led_onboard.value(0)
        utime.sleep(2)
        
    
