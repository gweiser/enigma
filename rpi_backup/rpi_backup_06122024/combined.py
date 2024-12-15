from time import sleep_ms, sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes, HIGH, LOW



i2c = I2C(0, freq=400000, scl=Pin(17), sda=Pin(16))  # Pico I2C bus 1
keyboard_expander = Expander(i2c, address=0x3F)
led_1_expander = Expander(i2c, address=0x3E)
led_2_expander = Expander(i2c, address=0x71)
#key_26 = Pin(15, Pin.IN)

# Keyboard initialisations
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

def main():
    """Test code."""
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