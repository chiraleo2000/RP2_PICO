import machine
from machine import Timer
import utime
led1 = machine.Pin(0, machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(3, machine.Pin.OUT)
led5 = machine.Pin(4, machine.Pin.OUT)
led6 = machine.Pin(5, machine.Pin.OUT)
led7 = machine.Pin(6, machine.Pin.OUT)
led8 = machine.Pin(7, machine.Pin.OUT)
led9 = machine.Pin(16, machine.Pin.OUT)
led10 = machine.Pin(17, machine.Pin.OUT)
led11 = machine.Pin(26, machine.Pin.OUT)
led12 = machine.Pin(27, machine.Pin.OUT)
led13 = machine.Pin(28, machine.Pin.OUT)
timer = Timer()

def one_by_one(n):
    for i in range (0,n):
        led1.toggle()
        utime.sleep(0.1)
        led2.toggle()
        utime.sleep(0.1)
        led3.toggle()
        utime.sleep(0.1)
        led4.toggle()
        utime.sleep(0.1)
        led5.toggle()
        utime.sleep(0.1)
        led6.toggle()
        utime.sleep(0.1)
        led7.toggle()
        utime.sleep(0.1)
        led8.toggle()
        utime.sleep(0.1)
        led9.toggle()
        utime.sleep(0.1)
        led10.toggle()
        utime.sleep(0.1)
        led11.toggle()
        utime.sleep(0.1)
        led12.toggle()
        utime.sleep(0.1)
        led13.toggle()
        utime.sleep(0.1)
    return True

def blink(led,timer):
    led.toggle()
    
while True:
    one_by_one(2)
    timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
        