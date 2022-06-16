from machine import Pin
import utime
trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)
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
def average():
    measure_1 = ultra()
    utime.sleep_us(10)
    measure_2 = ultra()
    utime.sleep_us(10)
    measure_3 = ultra()
    utime.sleep_us(10)
    avg = (measure_1 + measure_2 + measure_3) / 3
    return avg
while True:
    avg = average()
    print("The distance from object is ",avg,"cm")
    utime.sleep(1)