from machine import Pin, ADC
import utime
MH = ADC(Pin(26))
while True:
   x = MH.read_u16()
   print(x)
   utime.sleep(1)
