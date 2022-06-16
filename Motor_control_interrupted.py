from machine import Pin, ADC, PWM
import utime
xAxis= ADC(26)
yAxis= ADC(27)
button = Pin(21,Pin.IN, Pin.PULL_DOWN)
mtr_AI1 = PWM(Pin(2))
mtr_AI2 = PWM(Pin(3))
mtr_BI1 = PWM(Pin(4))
mtr_BI2 = PWM(Pin(5))
mtr_AI1.freq(500)
mtr_BI1.freq(500)

def Move( x, y):
    mtr_AI1.duty_u16(x)
    mtr_AI2.duty_u16(((2**16)-1) - x)
    mtr_BI1.duty_u16(y)
    mtr_BI2.duty_u16(((2**16)-1) - y)
    
    
def Stop(pin):
    mtr_AI1.duty_u16(0)
    mtr_AI2.duty_u16(0)
    mtr_BI1.duty_u16(0)
    mtr_BI2.duty_u16(0)
    utime.sleep(1)
    

button.irq(handler=Stop, trigger=Pin.IRQ_FALLING)

while True:
    Move(xAxis.read_u16(), yAxis.read_u16())
