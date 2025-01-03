from sdcard import SDCard
from machine import SPI, Pin 
import uos

cs = Pin(15, Pin.OUT)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, sck=Pin(10), mosi=Pin(11), miso=Pin(8))

sd = SDCard(spi, cs)
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

data = "Foo"

for i in range(5):
    with open(f"/sd/foo_{i}.txt", "w") as file:
        file.write("Hello, world\n")
        file.write("Foo\n")
        file.write("Bar")
        print("Written!")
        

    

