from machine import Pin
Pins = [
    Pin(0,Pin.OUT,Pin.PULL_DOWN),
    Pin(1,Pin.OUT,Pin.PULL_DOWN),
    Pin(2,Pin.OUT,Pin.PULL_DOWN),
    Pin(3,Pin.OUT,Pin.PULL_DOWN),
    Pin(4,Pin.OUT,Pin.PULL_DOWN),
    Pin(5,Pin.OUT,Pin.PULL_DOWN),
    Pin(6,Pin.OUT,Pin.PULL_DOWN),
    Pin(7,Pin.OUT,Pin.PULL_DOWN),
    Pin(8,Pin.OUT,Pin.PULL_DOWN),
    Pin(9,Pin.OUT,Pin.PULL_DOWN),
    Pin(10,Pin.OUT,Pin.PULL_DOWN),
    Pin(11,Pin.OUT,Pin.PULL_DOWN),
    Pin(12,Pin.OUT,Pin.PULL_DOWN),
    Pin(13,Pin.OUT,Pin.PULL_DOWN),
    Pin(14,Pin.OUT,Pin.PULL_DOWN),
    Pin(15,Pin.OUT,Pin.PULL_DOWN),
    Pin(16,Pin.OUT,Pin.PULL_DOWN),
    Pin(17,Pin.OUT,Pin.PULL_DOWN),
    Pin(18,Pin.OUT,Pin.PULL_DOWN),
    Pin(19,Pin.OUT,Pin.PULL_DOWN),
    Pin(20,Pin.OUT,Pin.PULL_DOWN),
    Pin(21,Pin.OUT,Pin.PULL_DOWN),
    Pin(22,Pin.OUT,Pin.PULL_DOWN),
    Pin(23,Pin.OUT,Pin.PULL_DOWN),
    Pin(24,Pin.OUT,Pin.PULL_DOWN),
    Pin(25,Pin.OUT,Pin.PULL_DOWN),
    Pin(26,Pin.OUT,Pin.PULL_DOWN),
    Pin(27,Pin.OUT,Pin.PULL_DOWN),
    Pin(28,Pin.OUT,Pin.PULL_DOWN)
    ]

values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

for i in range(len(Pins)):
    Pins[i].value(values[i])