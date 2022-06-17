# This is my very first small project not for everyone to use it.
# Originate from Arduino, use 2 PIR Sensors, 2 RED LED, 1 Blue LED and 2 Buzzers.
# Use for warning and scare away any cat or wild animal that come across this device.
# 2 PIR use for covering 360 degree around the device and scary by using Active buzzers at high frequency.  
from machine import Pin 
import utime 
led_onboard = Pin(25, Pin.OUT) # for testing Raspberry pi PICO board
led_1 = Pin( _ , Pin.OUT) # Input mode (Configurate your Pins in integrate number)
led_2 = Pin( _ , Pin.OUT) #Input mode (Configurate your Pins in integrate number)
led_3 = Pin( _ , Pin.OUT) # Input mode (Configurate your Pins in integrate number)
buzz1 = Pin( _ , Pin.OUT) # Input mode (Configurate your Pins in integrate number)
buzz2 = Pin( _ , Pin.OUT) # Input mode (Configurate your Pins in integrate number)
PIR1 = Pin( _ , Pin.IN, Pin.PULL_UP) # Output mode (Configurate your Pins in integrate number)
PIR2 = Pin( _ , Pin.IN, Pin.PULL_UP) # Output mode (Configurate your Pins in integrate number)
# Equipvalent to viod loop()
while True:
    print(PIR1.value(), PIR2.value()) # For testing and setting PIRs 
		if PIR1.value() == 1 and PIR2.value() == 0:
        led_1.value(1)
        led_2.value(0)
        buzz1.value(1)
        buzz2.value(0)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    elif PIR2.value() == 1 and PIR1.value() == 0:
        led_1.value(0)
        led_2.value(1)
        buzz1.value(0)
        buzz2.value(1)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    elif PIR2.value() == 1 and PIR1.value() == 1 :
        led_1.value(1)
        led_2.value(1)
        buzz1.value(1)
        buzz2.value(1)
        led_3.value(1)
        led_onboard.value(1)
        utime.sleep(2)
    else:
        led_1.value(0)
        led_2.value(0)
        buzz1.value(0)
        buzz2.value(0)
        led_3.value(0)
        led_onboard.value(0)
        utime.sleep(2)
  
