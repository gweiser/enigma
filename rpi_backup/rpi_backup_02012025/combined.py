from time import sleep_ms, sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes, HIGH, LOW
from pico_i2c_lcd import I2cLcd

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

def rotor_selection():
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
    """Test code."""
    rotor_selection()
    try:
        while True:
            sleep(1)
            key_data = keyboard_expander.read_keypad()                           
             
            if key_data != 0:
                
                # A key was pressed
              
                # Find the active row and columns
                row = keyboard_expander.get_row(key_data)
                col = keyboard_expander.get_col(key_data)
                
                # Get key pressed from key map
                key = int(KEY_MAP[row][col]) - 1
                #print(f"Row: {row}, Column: {col}, Key: {key}")
                print(f"Key: {key}")
                sleep_ms(100)
                if key < 16:
                    led_1_expander.pin_mode(LED_1_PINS[key], PinModes.OUTPUT)
                    led_1_expander.write_pin(LED_1_PINS[key], HIGH)
                    print("High")
                    sleep(1)
                    led_1_expander.write_pin(LED_1_PINS[key], LOW)
                    print("Low")
                elif key > 15:
                    key -= 16
                    led_2_expander.pin_mode(LED_2_PINS[key], PinModes.OUTPUT)
                    led_2_expander.write_pin(LED_2_PINS[key], HIGH)
                    print("High")
                    sleep(1)
                    led_2_expander.write_pin(LED_2_PINS[key], LOW)
                    print("Low")               
            elif key_26.value() == 0:
                print("Key: 26")
                led_2_expander.pin_mode(LED_2_PINS[9], PinModes.OUTPUT)
                led_2_expander.write_pin(LED_2_PINS[9], HIGH)
                print("High")
                sleep(1)
                led_2_expander.write_pin(LED_2_PINS[9], LOW)
                print("LOW")
                
                    
                sleep_ms(500)
            """if key_26.value() == 0:
                led_2_expander.pin_mode(9, PinModes.OUTPUT)
                led_2_expander.write_pin(9, HIGH)
                print("High")
                sleep(1)
                led_2_expander.write_pin(9, LOW)
                print("Low")
                """
            
    
        

    except KeyboardInterrupt:
        print("\nCtrl-C pressed to exit.")
    finally:
        keyboard_expander.reset()
        led_1_expander.reset()


main()