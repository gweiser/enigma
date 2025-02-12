from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

lcd_i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
lcd = I2cLcd(lcd_i2c, 0x27, 2, 16)

while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(" R O T O R E N ")
    lcd.move_to(0, 1)
    lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")




