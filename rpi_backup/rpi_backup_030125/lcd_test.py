import math, time
from machine import Pin, SPI, ADC
import gc9a01
from fonts import vga1_16x16 as font



def main():
    spi = SPI(0, baudrate=1000000, sck=Pin(18), mosi=Pin(19))
    white=65535
    dark_blue=287
    turquiose=1823
    red = 63488
    green=2016
    yellow=63456
    purple=61471
    black=0
    
    
    
    # From: github.com/todbot/HackadayVectorscopeHacks/blob/main/micropython/gc9a01_test.py
    lcd = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(22, Pin.OUT),
        cs=Pin(20, Pin.OUT),
        dc=Pin(21, Pin.OUT),
        rotation=0)
    

    #initialize lcd
    lcd.init()
    
    lcd.fill(white)
    #print(lcd.write_width(font, "foo")
    # Write to lcd
    lcd.text(font, "foo", 100, 110, turquiose, white)
        
    
    
    
main()
