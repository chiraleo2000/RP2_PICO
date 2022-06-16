from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime, random, _thread, framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

while True:
    display.rect(10, 10, 20, 20, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
    display.fill_rect(50, 50, 60, 55, 1)   # draw a solid rectangle 10,10 to 117,53, colour=1
    fbuf = framebuf.FrameBuffer(bytearray(8 * 8 * 1), 8, 8, framebuf.MONO_VLSB)
    fbuf.line(40, 30, 45, 30, 1)
    display.blit(fbuf, 60, 60, 0)           # draw on top at x=10, y=10, key=0
    display.show()
    utime.sleep(1)
    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    display.text('MicroPython', 40, 0, 1)
    display.text('SSD1306', 40, 12, 1)
    display.text('OLED 128x64', 40, 24, 1)
    display.show()
    utime.sleep(1)
    display.fill(0)
