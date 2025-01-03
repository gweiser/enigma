from machine import Pin, I2C
from utime import sleep

from bmp280 import BMP280I2C

i2c0_sda = Pin(8)
i2c0_scl = Pin(9)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl, freq=400000)
bmp280_i2c = BMP280I2C(0x76, i2c0)  # address may be different

#while True:
readout = bmp280_i2c.measurements
print(readout)
    #print(f"Temperature: {readout['t']} °C, pressure: {readout['p']} hPa.")
    #sleep(1)