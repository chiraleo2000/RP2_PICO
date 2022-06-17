# This is for testing ADC (Analog to Digital Convertor) in PICO.
# Using ADC library from machine to setting pin to accept ADC.
# Only specific pins can configurate to ADC pin and for Input only.
from machine import Pin, ADC
import utime
xAxis = ADC(Pin(27)) # ADC pins compatible only
yAxis = ADC(Pin(26)) # ADC pins conpatible only
button = Pin(16,Pin.IN, Pin.PULL_UP) # Normal Pins
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue= button.value()
    print(xValue, yValue, buttonValue)
    utime.sleep(0.1)
 
