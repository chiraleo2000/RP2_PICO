from machine import Pin, ADC
import utime
sensor_temp = ADC(ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)
file = open("temps.txt", "w")
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    file.write(str(temperature))
    file.flush()
    utime.sleep(2)
