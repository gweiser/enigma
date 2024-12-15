from machine import Pin
from utime import sleep
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
while True:
    if button.value() == 1:
        print("Pressed")
        sleep(1)
    else:
        print("Not pressed")
        sleep(1)
    