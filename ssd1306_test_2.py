from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime, random, _thread
import uselect
import sys
import select

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
t = 0
voltage = 10
Amp = 4
Status = ""

def display(volt,amp,time):
    oled.text("Voltage_Setting:", 0, 0)
    oled.text(str(voltage) + " V ", 10, 15)
    oled.text(str(t) + " sec ", 70, 15) 
    oled.text("Current_Setting:", 0, 30)
    oled.line(0,25, 127, 25, 1)
    oled.text( str(Amp) + " A ", 10, 45)
    oled.text(Status, 0, 55)
    oled.show()

while True:
    input = select.select([sys.stdin], [], [], 0.05)[0]
    if input:
        value = sys.stdin.readline().rstrip()
        if (value == "q"):
            print ("Exiting")
            sys.exit(0)
        elif value == "":
            Status = Status
        else:
            Status = value
            print ("You entered: %s" % value)
            
    voltage = random.uniform(0.1, 12.0)
    voltage = round(voltage, 2)
    Amp = random.uniform(0.01, 4.00)
    Amp = round(Amp, 2)
    _thread.start_new_thread(display,(voltage,Amp,t))
    utime.sleep(0.05)
    oled.fill(0)
    t += 0.1
    t = round(t,1)