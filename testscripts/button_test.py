from machine import Pin
from utime import sleep
button = Pin(10, Pin.IN, Pin.PULL_DOWN)
while True:
    if button.value() == 0:
        print("Pressed")
        sleep(1)
    else:
        print("Not pressed")
        sleep(1)
    