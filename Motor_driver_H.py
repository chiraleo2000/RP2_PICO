from machine import Pin, ADC, PWM
import utime
potentiometer = ADC(26)
mtr_AI1 = Pin(2, Pin.OUT)
mtr_AI2 = Pin(3, Pin.OUT)
mtr_PWMa = PWM(Pin(10))
button_red = Pin(15, Pin.IN, Pin.PULL_DOWN)
button_black = Pin(16, Pin.IN, Pin.PULL_UP)
led_1 = Pin(5, Pin.OUT)
led_2 = Pin(6, Pin.OUT)
led_3 = Pin(7, Pin.OUT)
led_1.value(0)
led_2.value(0)
led_3.value(1)
mtr_PWMa.freq(50)
mtr_AI1.value(1)
mtr_AI2.value(0)
while True:
    mtr_PWMa.duty_u16(potentiometer.read_u16())
    if button_red.value() == 1:
        mtr_AI1.value(0)
        mtr_AI2.value(1)
        led_1.value(1)
        led_2.value(0)
        led_3.value(0)
    elif button_red.value() == 1:
        mtr_AI1.value(1)
        mtr_AI2.value(0)
        led_1.value(0)
        led_2.value(1)
        led_3.value(0)
        
    else:
        mtr_AI1.value(0)
        mtr_AI2.value(0)
        led_1.value(0)
        led_2.value(0)
        led_3.value(1)
    utime.sleep(1)        

