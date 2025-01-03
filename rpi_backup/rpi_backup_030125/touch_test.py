from machine import Pin
from time import

sensor = Pin(15, Pin.IN)
led = Pin(25, Pin.OUT)

while True:
    if sensor.value() == 1:
        led.toggle()
        sleep(1)