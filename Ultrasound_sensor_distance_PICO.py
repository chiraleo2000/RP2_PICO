from machine import Pin
import utime
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
def ultra():
    trigger.low()
    utime.sleep_us(10)
    trigger.high()
    utime.sleep_us(30)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.034278) / 2
    return distance
def average():
    lists = []
    for i in range (5):
        x = ultra()
        utime.sleep_us(10)
        lists.append(x)
    print(lists)
    print(sum(lists[:]))
    avg = sum(lists[:])/(len(lists))
    return avg
while True:
    avg = average()
    print("The distance from object is {:.2f} cm".format(avg))
    utime.sleep(1)