from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
import utime, _thread, random

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) # OLED
oled = SSD1306_I2C(128, 64, i2c) # OLED
switch1=Pin(2,Pin.OUT, Pin.PULL_DOWN)
switch2=Pin(3,Pin.OUT, Pin.PULL_DOWN)
RGB = [
    Pin(4,Pin.OUT, Pin.PULL_DOWN),  
    Pin(5,Pin.OUT, Pin.PULL_DOWN),
    Pin(6,Pin.OUT, Pin.PULL_DOWN),
    ] # [Red, Green, Blue]

Color = {"red":[1,0,1], "blue":[0,1,1], "yellow":[1,1,0], "white":[0,0,0]}

status = ""

def lid(color):
    word = str(color)
    ledpins = Color[word]
    for k in range(len(RGB)):
        RGB[k].value(ledpins[k])

def display(word,delay):
    oled.fill(0)
    if len(word) > 16:
        oled.text(word[0:15], 10, 12)
        oled.text(word[16:], 10, 24)
        oled.show()
    elif len(word) > 32:
        oled.text(word[0:15], 10, 12)
        oled.text(word[16:31], 10, 24)
        led.text(word[32:], 10, 36)
        oled.show()
    else:
        oled.text(word, 10, 12)
        oled.show()
        
class game:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
    def play(self):
        t = random.rand(3,15)
        utime.sleep(t)
        lid("red")
        _thread.start_new_thread(display,("Press!!.".format(n),0.1))
        switch1.irq(trigger=Pin.IRQ_RISING, handler=score(1,0))
        switch2.irq(trigger=Pin.IRQ_FALLING, handler=score(0,1))
        
    def score(self,x,y):
        lid("white")
        self.s1 +=x
        self.s2 +=y
        if x == 1 and y == 0:
            word = "player1"
        elif x == 0 and y == 1:
            word = "player2"
        else:
            word = "No one"
        _thread.start_new_thread(display,("{} wins!.".format(word),0.1))
        utime.sleep(5)
        return self.s1, self.s2 = s1, s2
    
def start():
    s1 = 0
    s2 = 0
    begin = "Let's the reaction game begin"
    _thread.start_new_thread(display,(begin,0.1))
        
while True:
    start()
    lid("green")
    n = int(input("number of round(s): "))
    _thread.start_new_thread(display,("Number of rounds to play: {}".format(n),0.1))
    for i in range(n):
        lid("blue")
        _thread.start_new_thread(display,("Round {}\n Get ready!! ".format(i+1),0.1))
        utime.sleep(3)
        game(s1,s2).play()
        _thread.start_new_thread(display,("Next round".format(word),0.1))
        utime.sleep(2)
    while True:
        if s1 > s2:
            print("Player1 wins the game")
            _thread.start_new_thread(display,("Player1 wins the game".format(word),0.1))
        elif s1 == s2:
            print("Draw !!")
            _thread.start_new_thread(display,("Draw !!".format(word),0.1))
        elif s1 < s2:
            print("Player2 wins the game")
            _thread.start_new_thread(display,("Player2 wins the game".format(word),0.1))
    except KeyboardInterrupt:
        _thread.start_new_thread(display,("Restart the game".format(word),0.1))
        print("Restart the game")
        utime.sleep(5)