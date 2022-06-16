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

forward_and_backward = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

while True:
    # Forward
    for step in forward_and_backward :
        for i in range(len(leds)):
            leds[i].value(step[i])
        utime.sleep(0.1)
    # backward
    for step in reversed(forward_and_backward):
        for i in range(len(leds)):
            leds[i].value(step[i])
        utime.sleep(0.1)