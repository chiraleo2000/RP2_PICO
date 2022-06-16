import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
x = 0
while True:
    led_onboard.value(1)
    utime.sleep(1)
    led_onboard.value(0)
    utime.sleep(1)
    x += 1
    print("loop times " + str(x))
    if x == 10 :
        led_onboard.value(0)
        utime.sleep(1)
        x = 0
        break
        