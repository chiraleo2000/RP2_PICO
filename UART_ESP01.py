from machine import UART, Pin
from time import sleep

uart0 = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
read = ""
while True:
    rxData = bytes()
    while uart0.any() > 0:
        rxData += uart0.read(1)
        
    if len(rxData):
        read = rxData.decode('utf-8')
        print(read.split()[-1])