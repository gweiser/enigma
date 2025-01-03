import uos, gc9a01
from machine import Pin, SPI, ADC, I2C
from utime import sleep

from fonts import vga1_16x16 as font
from sdcard import SDCard
from bmp280 import BMP280I2C

# INITIALIZE ALL MODULES

white=65535
dark_blue=287
turquoise=1823
red = 63488
green=2016
yellow=63456
purple=61471
black=0

# LCD
# Initialize SPI
spi_lcd = SPI(0, baudrate=1000000, sck=Pin(18), mosi=Pin(19))


# From: github.com/todbot/HackadayVectorscopeHacks/blob/main/micropython/gc9a01_test.py
lcd = gc9a01.GC9A01(
    spi_lcd,
    240,
    240,
    reset=Pin(22, Pin.OUT),
    cs=Pin(20, Pin.OUT),
    dc=Pin(21, Pin.OUT),
    rotation=0)


# Initialize lcd
lcd.init()

# SD_READER
# Initialize SPI
spi_sd = SPI(1, baudrate=1000000, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
# Initialize CS
cs_sd = Pin(15, Pin.OUT)

sd = SDCard(spi_sd, cs_sd)
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

def write_sd(data):
    with open(f"/sd/data.txt", "a") as file:
        file.write(f"{data}\n")
        file.close()

def clear_lcd(colour=white):
    # Fill lcd with colour
    lcd.fill(colour)
    
def write_lcd(text, x=70, y=110, font=font, text_colour=turquoise, background_colour=white):
    # Write text to lcd
    #width = lcd.write_width(font, text)
    #x_pixel = x-width
    lcd.text(font, text, x-len(str(text)), y, text_colour, background_colour)
    
def get_bmp(data):
    i2c0 = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
    bmp280_i2c = BMP280I2C(0x76, i2c0)
    
    readout = bmp280_i2c.measurements
    
    if data == "pressure":
        return round(readout["p"], 1)
    elif data == "temp":
        return round(readout["t"], 2)
    
    
def main():
    print("Initialize...")
    #sleep(3)
    clear_lcd()
    while True:
        temp = f"{get_bmp('temp'):.2f} C"
        pressure = f"{get_bmp('pressure'):.1f} hPa"
#         clear_lcd()
        write_lcd(temp)
        write_lcd(pressure, y=130)
        write_sd([temp, pressure])
        print("Written!")
        sleep(.5)
    
    
    
main()
    
    
    
    
    
    

    