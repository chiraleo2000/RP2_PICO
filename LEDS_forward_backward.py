from machine import Pin
import utime , _thread
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
def play(n, delay):
    for k in range(n):
        for step in forward_and_backward :
            for i in range(len(leds)):
                leds[i].value(step[i])
            utime.sleep(delay)
            # backward
        for step in reversed(forward_and_backward):
            for i in range(len(leds)):
                leds[i].value(step[i])
            utime.sleep(delay)
    utime.sleep(0.5)
    return print('LEDS Complete')
            
def task(pin,n, delay):
    led = machine.Pin(pin, Pin.OUT)
    for j in range(n):
        led.high()
        utime.sleep(delay)
        led.low()
        utime.sleep(delay)
    print('Task ' + str(pin) + ' complete')   
    
_thread.start_new_thread(task, (22 ,500, 0.01))
while True:
    play(5,0.1)
    _thread.start_new_thread(task, (22 ,500, 0.01))
    utime.sleep(1)
