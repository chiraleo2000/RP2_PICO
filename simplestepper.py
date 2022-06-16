from machine import Pin
import utime

pins = [
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(4,Pin.OUT),
    Pin(5,Pin.OUT)
    ]
full_step_sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    ]

half_step_sequence = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
    ]

stop_step_sequence = [
    [0,0,0,0],
    ]

def forward_step(func,time):
    t = 0
    while t <= time:
        for step in func:
            for i in range(len(pins)):
                pins[i].value(step[i])
                utime.sleep(0.001)
                t +=0.001
    return

def backward_step(func,time):
    t = 0
    while t <= time:
        for step in func:
            for i in range(len(pins)):
                pins[i].value(step[-i])
                utime.sleep(0.001)
                t +=0.001
    return
def stop():
    for step in stop_step_sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
            break
                
while True:
    forward_step(full_step_sequence,2)
    print("full_step_sequence")
    forward_step(half_step_sequence,2)
    print("half_step_sequence")
    backward_step(full_step_sequence,2)
    print("full_step_sequence")
    backward_step(half_step_sequence,2)
    print("half_step_sequence")
    stop()
    print("stop")
    utime.sleep(1)