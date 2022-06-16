from machine import Pin, PWM, Timer
import utime
EN = Pin(21,Pin.OUT, Pin.PULL_DOWN)
Dir = Pin(20,Pin.OUT, Pin.PULL_DOWN)
Step = Pin(19,Pin.OUT, Pin.PULL_DOWN)
timer = Timer()

def forward_times(times):
    EN.value(0)
    Dir.value(1)
    for i in range (times * 500):
        Step.value(1)
        utime.sleep(0.001)
        Step.value(0)
        utime.sleep(0.001)
    stop(0.1)
    return print("forward")

def backward_times(times):
    EN.value(0)
    Dir.value(0)
    for i in range (times * 500):
        Step.value(1)
        utime.sleep(0.001)
        Step.value(0)
        utime.sleep(0.001)
    stop(0.1)
    return print("backward")

def stop(times):
    EN.value(1)
    utime.sleep(times)
    return print("stop")

def forward_steps(steps):
    EN.value(0)
    Dir.value(1)
    for i in range (steps):
        Step.value(1)
        utime.sleep(0.001)
        Step.value(0)
        utime.sleep(0.001)
    stop(0.1)
    return print("forward")

def backward_steps(steps):
    EN.value(0)
    Dir.value(0)
    for i in range (steps):
        Step.value(1)
        utime.sleep(0.001)
        Step.value(0)
        utime.sleep(0.001)
    stop(0.1)
    return print("backward")

while True:
    forward_times(5)
    backward_times(5)
    stop(1)
    forward_steps(200)
    backward_steps(200)
    stop(1)
    