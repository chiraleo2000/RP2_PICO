from machine import Pin, ADC, PWM, UART, I2C
from ssd1306 import SSD1306_I2C
import utime, _thread, re

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

uart0 = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1)
read = ""
mytopic = "CPS/test"
status = ""

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
    
def physical_control():
    try:
        if right.value() == 0:
            backward()
            status = "move right"
            _thread.start_new_thread(display,(status, 0.1))
        elif left.value() == 0:
            forward()
        elif button.value() == 0:
            status = "come home"
            _thread.start_new_thread(display,(status, 0.1))
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
    
def decoding(code):
    read = rxData.decode().split('\n')
    x = read[0].split("[{}]".format(mytopic))
    return x[-1].strip()

def MQTT_Call(word):
    word = word.lower().strip()
    if word == "home":
        uart0.write("Go home")
        print("Go home")
        status = "come home"
        _thread.start_new_thread(display,(status, 0.1))
        trigger()
        if sensor.value() == 0:
            print("At home")
            uart0.write("At home")
    elif word == "help":
        uart0.write("There are three call function available\r\n")
        uart0.write("[('home') ('right, number_of_step')  ('left, number_of_step')]\r\n")
        print("There are three call function available\r\n ")
        print("[('home') ('right, number_of_step')  ('left, number_of_step')]\r\n")
        stop()
    else:
        try:
            x = word.split(',')
            if x[0].strip() == "right":
                step = int(x[1].strip())
                time = int((step*1000)/20000)
                i = 0
                uart0.write("Moving right\r\n")
                print("Moving right")
                while i < time:
                    backward()
                    status = "move right"
                    _thread.start_new_thread(display,(status, 0.1))
                    i+= 1
                    utime.sleep(0.1)
                uart0.write("Move right " + str(step) + " step\r\n")
                print("Move right " + str(step) + " step\r\n")
            elif x[0].strip() == "left":
                step = int(x[1].strip())
                time = int((step*1000)/20000)
                i = 0
                uart0.write("Moving left\r\n")
                print("Moving left")
                while i < time:
                    forward()
                    i += 1
                    utime.sleep(0.1)
                uart0.write("Move left " + str(step) + " step\r\n")
                print("Move left " + str(step) + " step\r\n")
        except:
            uart0.write("try 'help' for searching available functions!!")
            print("try 'help' for searching available functions!!")
            stop()

while True:
    rxData = bytes()
    while uart0.any() > 0:
        rxData += uart0.read()
    if len(rxData):
        call = decoding(rxData)
        MQTT_Call(call)
    else:
        physical_control()