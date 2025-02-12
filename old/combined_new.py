from time import sleep_ms, sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes, HIGH, LOW
from pico_i2c_lcd import I2cLcd





"""Hardware Initialisations"""
# Initialise I2C
i2c = I2C(0, freq=400000, scl=Pin(17), sda=Pin(16))

# Keyboard initialisations
keyboard_expander = Expander(i2c, address=0x70)
led_1_expander = Expander(i2c, address=0x3E)
led_2_expander = Expander(i2c, address=0x71)
key_26 = Pin(11, Pin.IN, Pin.PULL_UP)
KEY_ROWS = 5
KEY_COLS = 5

KEY_MAP = [
    ['1', '2', '3', '4', '5'],
    ['6', '7', '8', '9', '10'],
    ['11', '12', '13', '14', '15'],
    ['16', '17', '18', '19', '20'],
    ['21', '22', '23', '24', '25']
]
SLEEP_TIME = 500
SCAN_TIME = 2
DEBOUNCE_TIME = 5
keyboard_expander.keypad(KEY_ROWS, KEY_COLS, SLEEP_TIME, SCAN_TIME, DEBOUNCE_TIME)



# LED initialisations
LED_1_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
LED_2_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# LCD initialisations#
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Initialize buttons
rotor_1_button = Pin(15, Pin.IN, Pin.PULL_UP)
rotor_2_button = Pin(14, Pin.IN, Pin.PULL_UP)
rotor_3_button = Pin(13, Pin.IN, Pin.PULL_UP)
select_button = Pin(12, Pin.IN, Pin.PULL_UP)
buttons = [rotor_1_button, rotor_2_button, rotor_3_button]






"""Software Initialisations"""
# Initialise lists for base rotor and alphabet
rotor_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]







def rotor_selection():
    """Select which rotor to use"""
    rotor_allocation = [0, 0, 0]
 
    # Clear LCD and display values
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(" R O T O R E N ")
    lcd.move_to(0, 1)
    lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")
    
    while True:
        # Change rotor allocation on keypress, only change to rotor not already in use
        for button in buttons:
            if button.value() == 0:
                
             if (rotor_allocation[buttons.index(button)] + 1) not in rotor_allocation:
                rotor_allocation[buttons.index(button)] += 1
                
                if rotor_allocation[buttons.index(button)] > 5:
                 rotor_allocation[buttons.index(button)] = 0
                 
                while rotor_allocation.count(rotor_allocation[buttons.index(button)]) > 1:
                 rotor_allocation[buttons.index(button)] += 1
                 
                 if rotor_allocation[buttons.index(button)] > 5:
                     rotor_allocation[buttons.index(button)] = 0
                     
                 if rotor_allocation.count(rotor_allocation[buttons.index(button)]) == 1:
                     break
                      
             else:
                rotor_allocation[buttons.index(button)] += 1
                while rotor_allocation.count(rotor_allocation[buttons.index(button)]) > 1:             
                     rotor_allocation[buttons.index(button)] += 1
                     
                     if rotor_allocation[buttons.index(button)] > 5:
                         rotor_allocation[buttons.index(button)] = 0
                         break
                        
                     if rotor_allocation.count(rotor_allocation[buttons.index(button)]) == 1:
                         break
    
                                             
        lcd.move_to(0, 1)
        lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")
        
        if select_button.value() == 0:
            lcd.clear()
            return rotor_allocation
            break


def main():
   """Main script"""
   # Return a list with selected rotors
   rotors = rotor_selection()
   
