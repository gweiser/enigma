from machine import Pin, SoftI2C
from pico_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(16), scl=Pin(17), freq=40000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Initialize buttons
rotor_1_button = Pin(15, Pin.IN, Pin.PULL_UP)
rotor_2_button = Pin(14, Pin.IN, Pin.PULL_UP)
rotor_3_button = Pin(13, Pin.IN, Pin.PULL_UP)
reset_button = Pin(12, Pin.IN, Pin.PULL_UP)

def rotor_selection():
    rotor_nums = [1, 2, 3, 4, 5]
    rotor_allocation = [1, 3, 5]
    lcd.clear()
    lcd.putstr("ROTOREN")
    lcd.move_to(1, 0)
    lcd.putstr(f"   {rotor_allocation[0]:02}  {rotor_allocation[1]:02}  {rotor_allocation[2]:02}   ")

        
    

def main():
    rotors = [0, 0, 0]
    
    lcd.clear()
    while True:
        # Detect button press and adjust rotor position according to amount of button presses
        if rotor_1_button.value() == 0:
            rotors[0] += 1
            if rotors[0] == 27:
                rotors[0] = 0
        elif rotor_2_button.value() == 0:
            rotors[1] += 1
            if rotors[1] == 27:
                rotors[1] = 0
        elif rotor_3_button.value() == 0:
            rotors[2] += 1
            if rotors[2] == 27:
                rotors[2] = 0
                
        # Detect reset button press
#         elif reset_button.value() == 0:
#             for i in range(0, len(rotors)):
#                 rotors[i-1] = 0
                
        # While reset button pressed: rotor number selection for each slot
#         elif reset_button.value() == 0:
#             lcd.clear()
#             lcd.putstr("ROTOREN")
#             if rotor_1_button.value() == 0:
#                 print("Foo")
#             break
                    
        lcd.move_to(0, 0)
        lcd.putstr(f"   {rotors[0]:02}  {rotors[1]:02}  {rotors[2]:02}   ")
    
    
    
main()

