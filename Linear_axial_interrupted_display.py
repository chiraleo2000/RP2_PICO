from machine import Pin, ADC, PWM, UART, I2C
from ssd1306 import SSD1306_I2C
import utime, _thread

Motor = PWM(Pin(26))
Dir = Pin(27,Pin.OUT, Pin.PULL_DOWN)
button = Pin(20,Pin.IN, Pin.PULL_DOWN)
right = Pin(22,Pin.IN, Pin.PULL_DOWN)
left = Pin(21,Pin.IN, Pin.PULL_DOWN)
RGB = [
    Pin(7,Pin.OUT, Pin.PULL_DOWN),  
    Pin(6,Pin.OUT, Pin.PULL_DOWN),
    ] # [Red, Green]

sensor = Pin(9,Pin.IN, Pin.PULL_DOWN)
Motor.freq(1000)

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

Color = {"red":[1,0], "blue":[0,1], "pink":[0,0]}

def lid(color):
    word = str(color)
    ledpins = Color[word]
    for k in range(len(RGB)):
        RGB[k].value(ledpins[k])
            
def blink_RGB(color,delay):
    word = str(color)
    ledpin = Color[word]
    white = [1,1]
    for j in range(len(RGB)):
        RGB[j].value(ledpin[j])
    utime.sleep(delay)
    for j in range(len(RGB)):
        RGB[j].value(white[j])
    utime.sleep(delay)
    
def trigger():
    status = "come home"
    _thread.start_new_thread(display,(status, 0.1))
    while sensor.value() == 1:
        backward()
        blink_RGB("red", 0.5)
        s = sensor.value()

def stop():
    Motor.duty_u16(0)

def hit(pin):
    s = sensor.value()
    signal(s)
    oled.fill(0)
    status = "At home"
    _thread.start_new_thread(display,(status, 0.1))
    stop()
    utime.sleep(2)

sensor.irq(handler=hit, trigger=Pin.IRQ_FALLING)
    
def signal(n):
    if n == 0:
        lid("blue")
    elif n == 1:
        lid("pink")
        
def backward():
    Motor.duty_u16(20000)
    Dir.high()
    s = sensor.value()
    signal(s)
    
def forward():
    Motor.duty_u16(20000)
    Dir.low()
    s = sensor.value()
    signal(s)
    status = "move left"
    _thread.start_new_thread(display,(status, 0.1))
    
lid("pink")

def display(word,time):
    oled.text(word, 24, 24)
    oled.show()
    
uart0 = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
read = ""
status = ""

while True:
    try:
        if right.value() == 0:
            backward()
            status = "move right"
            _thread.start_new_thread(display,(status, 0.1))
        elif left.value() == 0:
            forward()
        elif button.value() == 0:
            trigger()
        else:
            stop()
            status = "stop"
            _thread.start_new_thread(display,(status, 0.1))
    except:
        stop()
        status = "stop"
        _thread.start_new_thread(display,(status, 0.1))
    utime.sleep(0.1)
    oled.fill(0)