from machine import Pin, ADC, PWM
import utime
xAxis= ADC(26)
button = Pin(21,Pin.IN, Pin.PULL_DOWN)
mtr_AI1 = PWM(Pin(2))
mtr_AI2 = Pin(3, Pin.OUT)
mtr_BI1 = PWM(Pin(4))
mtr_BI2 = Pin(5, Pin.OUT)
mtr_AI1.freq(100)
mtr_BI1.freq(100)

while True:
    Value = xAxis.read_u16()
    buttonValue= button.value()
    print(Value, buttonValue)
    if 30000<= Value <=35000 or buttonValue == 0:
        mtr_AI1.duty_u16(0)
        mtr_AI2.value(0)
        mtr_BI1.duty_u16(0)
        mtr_BI2.value(0)
        print("stop")
        utime.sleep(0.2)
    elif Value >=35000 and buttonValue == 1:
        mtr_AI1.duty_u16(Value*2)
        mtr_AI2.value(0)
        mtr_BI1.duty_u16(Value*2)
        mtr_BI2.value(0)
        print("forward")
        utime.sleep(0.2)
    elif Value <=30000 and buttonValue == 1:
        mtr_AI1.duty_u16(Value*2)
        mtr_AI2.value(1)
        mtr_BI1.duty_u16(Value*2)
        mtr_BI2.value(1)
        print("backward")
        utime.sleep(0.2)
    else:
        mtr_AI1.duty_u16(0)
        mtr_AI2.value(0)
        mtr_BI1.duty_u16(0)
        mtr_BI2.value(0)
        print("stop")