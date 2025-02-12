from time import sleep_ms, sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes, HIGH, LOW
from pico_i2c_lcd import I2cLcd
from enigma_encryption import initialise_rotor_position, initialise_ring_setting, encrypt, all_rotors, alphabet, result

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

# LCD initialisations
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Initialize buttons
rotor_1_button = Pin(15, Pin.IN, Pin.PULL_UP)
rotor_2_button = Pin(14, Pin.IN, Pin.PULL_UP)
rotor_3_button = Pin(13, Pin.IN, Pin.PULL_UP)
select_button = Pin(12, Pin.IN, Pin.PULL_UP)
buttons = [rotor_1_button, rotor_2_button, rotor_3_button]

def rotor_selection():
    """Select which rotors to use through Rotor Config Interface"""
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
        sleep(.1)
            

def ring_setting_selection():
    """Select ring settings through Rotor Config Interface"""
    ring_allocation = [0, 0, 0]
 
    # Clear LCD and display values
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("RINGEINSTELLUNG")
    lcd.move_to(0, 1)
    lcd.putstr(f"   {ring_allocation[0]:02}  {ring_allocation[1]:02}  {ring_allocation[2]:02}   ")
    
    while True:
        # Change rotor allocation on keypress, only change to rotor not already in use
        for button in buttons:
            if button.value() == 0:
                
             if (ring_allocation[buttons.index(button)] + 1) not in ring_allocation:
                ring_allocation[buttons.index(button)] += 1
                
                if ring_allocation[buttons.index(button)] > 5:
                 ring_allocation[buttons.index(button)] = 0
                 
                while ring_allocation.count(ring_allocation[buttons.index(button)]) > 1:
                 ring_allocation[buttons.index(button)] += 1
                 
                 if ring_allocation[buttons.index(button)] > 5:
                     ring_allocation[buttons.index(button)] = 0
                     
                 if ring_allocation.count(ring_allocation[buttons.index(button)]) == 1:
                     break
                      
             else:
                ring_allocation[buttons.index(button)] += 1
                while ring_allocation.count(ring_allocation[buttons.index(button)]) > 1:             
                     ring_allocation[buttons.index(button)] += 1
                     
                     if ring_allocation[buttons.index(button)] > 5:
                         ring_allocation[buttons.index(button)] = 0
                         break
                        
                     if ring_allocation.count(ring_allocation[buttons.index(button)]) == 1:
                         break
    
                                             
        lcd.move_to(0, 1)
        lcd.putstr(f"   {ring_allocation[0]:02}  {ring_allocation[1]:02}  {ring_allocation[2]:02}   ")
        
        if select_button.value() == 0:
            lcd.clear()
            return ring_allocation
        sleep(.1)
        

def starter_positions_selection():
    """Select rotor starter positions through Rotor Config Interface"""
    starter_positions = [0, 0, 0]
 
    # Clear LCD and display values
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("STARTERPOSITION") # <<<<<<<<<
    lcd.move_to(0, 1)
    lcd.putstr(f"   {starter_positions[0]:02}  {starter_positions[1]:02}  {starter_positions[2]:02}   ")
    
    while True:
        # Change rotor allocation on keypress, only change to rotor not already in use
        for button in buttons:
            if button.value() == 0:
                starter_positions[buttons.index(button)] += 1
                if starter_positions[buttons.index(button)] > 5:
                    starter_positions[buttons.index(button)] = 0
    
                                             
        lcd.move_to(0, 1)
        lcd.putstr(f"   {starter_positions[0]:02}  {starter_positions[1]:02}  {starter_positions[2]:02}   ")
        
        if select_button.value() == 0:
            lcd.clear()
            return starter_positions
        
        sleep(.1)
        


def detect_keypress():
    """Detect which key was pressed on keyboard"""
    sleep(1)
    key_data = keyboard_expander.read_keypad()                           
        
    if key_data != 0:
        
        # A key was pressed
        
        # Find the active row and columns
        row = keyboard_expander.get_row(key_data)
        col = keyboard_expander.get_col(key_data)
        
        # Get key pressed from key map
        key = int(KEY_MAP[row][col]) - 1
        return key
         
    elif key_26.value() == 0:
        key = 25
        return key
    
    sleep_ms(500)
    return "Empty"


def illuminate_lampboard(letter):
    """Illuminate a letter on the lampboard"""
    sleep_ms(100)
    # If SX1509 number 1 needs to be addressed 
    if letter < 16:
        led_1_expander.pin_mode(LED_1_PINS[letter], PinModes.OUTPUT)
        led_1_expander.write_pin(LED_1_PINS[letter], HIGH)
        sleep(1)
        led_1_expander.write_pin(LED_1_PINS[letter], LOW)
    # If SX1509 number 2 needs to be addressed
    elif letter > 15:
        letter -= 16
        led_2_expander.pin_mode(LED_2_PINS[letter], PinModes.OUTPUT)
        led_2_expander.write_pin(LED_2_PINS[letter], HIGH)
        sleep(1)
        led_2_expander.write_pin(LED_2_PINS[letter], LOW)

    # Reset LEDS
    led_1_expander.reset()


def main():
    """Main loop"""
    # Get input for rotor, ring settings and starter positions selection
    rotors_selected = rotor_selection()
    setting_selected = ring_setting_selection()
    positions_selected = starter_positions_selection()
    
    rotor1_pos = positions_selected[0]
    rotor2_pos = positions_selected[1]
    rotor3_pos = positions_selected[2]

    # Define rotors from dictionary
    rotor_1 = all_rotors[rotors_selected[0]]
    rotor_2 = all_rotors[rotors_selected[1]]
    rotor_3 = all_rotors[rotors_selected[2]]

    # Initialise rotors
    initialise_rotor_position(rotor_1, rotor1_pos)
    initialise_rotor_position(rotor_2, rotor2_pos)
    initialise_rotor_position(rotor_3, rotor3_pos)

    # Initialise ring settings
    initialise_ring_setting(rotor_1, setting_selected[0])
    initialise_ring_setting(rotor_2, setting_selected[1])
    initialise_ring_setting(rotor_3, setting_selected[2])

    lcd.clear()
    lcd.move_to(0, 1)
    lcd.putstr(f"   {rotor1_pos:02}  {rotor2_pos:02}  {rotor3_pos:02}   ")
    while True:
        sleep(1)
        # Detect keypress
        letter = detect_keypress()
        # If the letter is real
        if letter != "Empty":
            letter = alphabet[letter]
            # Encypt the letter, then turn it into index
            encrypted_letter = encrypt(letter, rotor_1, rotor_2, rotor_3)
            encrypted_letter = alphabet.index(encrypted_letter)
            # Illuminate corresponding index on Lampboard
            illuminate_lampboard(encrypted_letter)

            # Move rotor display on RCI after every keypress
            if result == 1:
                rotor2_pos += 1
            elif result == 2:
                rotor2_pos += 1
                rotor1_pos += 1
            else:
                rotor3_pos += 1
                if rotor3_pos > 26:
                    rotor3_pos = 0
            lcd.clear()
            lcd.move_to(0, 1)
            lcd.putstr(f"   {rotor1_pos:02}  {rotor2_pos:02}  {rotor3_pos:02}   ")            

main()