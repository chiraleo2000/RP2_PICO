import machine
import neopixel

# 32 LED strip connected to X8.
p = machine.Pin(28)
n = neopixel.NeoPixel(p, 32)

# Draw a red gradient.
for i in range(32):
    n[i] = (i * 8, 0, 0)

# Update the strip.
n.write()