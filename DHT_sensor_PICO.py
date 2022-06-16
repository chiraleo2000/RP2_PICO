from machine import Pin, ADC
import dht
import utime
d = dht.DHT11(machine.Pin(8))
while True:
    try:
        d.measure()
        print(str(d.temperature()) + " *C")
        print(str(d.humidity()) + " %\n")
        utime.sleep(1)
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
    utime.sleep(1)