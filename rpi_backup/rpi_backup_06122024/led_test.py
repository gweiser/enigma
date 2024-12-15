"""SX1509 demo (Blink).
This example demonstrates the SX1509's set-it-and-forget-it
blink function. We'll set the pin up as an OUTPUT, and call
io.blink() all in setup(), then watch the LED blink by itself
in loop().

Hardware Hookup:
SX1509 Breakout ---- Pico --------- Breadboard
    GND ------------ GND
    3V3 ------------ 3V3(Out)
    SDA ------------ SDA (GPIO2)
    SCL ------------ SCL (GPIO3)
    15 -----------------------------LED+
                                    LED- --////-- GND
                                           330Ω
Derived from SparkFun_SX1509_Arduino_Library
Original source: https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library
"""
from time import sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes

i2c = I2C(0, freq=400000, scl=Pin(17), sda=Pin(16))  # Pico I2C bus 1
expander = Expander(i2c, address=0x3E3)

SX1509_LED_PIN = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # LED connected to SX1509's pin 15


def test():
    """Test code."""
    while True:
        number = int(input("Num: "))
    # Set LED pin to OUTPUT
        expander.pin_mode(SX1509_LED_PIN[number], PinModes.OUTPUT)
        # Start blinking: ~1000 ms LOW, ~500 ms HIGH
        expander.blink(SX1509_LED_PIN[number], 1000, 500)
        sleep(3)  # Reduce CPU load
        expander.reset()


test()
