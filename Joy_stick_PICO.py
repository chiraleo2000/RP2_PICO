from machine import Pin, ADC
import utime
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(16,Pin.IN, Pin.PULL_UP)
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue= button.value()
    print(xValue, yValue, buttonValue)
    utime.sleep(0.1)
 