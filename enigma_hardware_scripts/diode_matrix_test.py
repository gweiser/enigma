"""
Hardware Hookup:
SX1509 Breakout ---- Pico --------- Breadboard
    GND ------------ GND
    3V3 ------------ 3V3(Out)
    SDA ------------ SDA (GPIO2)
    SCL ------------ SCL (GPIO3)
      0 ------------ Keypad Row 1   
      1 ------------ Keypad Row 2 
      2 ------------ Keypad Row 3 
      3 ------------ Keypad Row 4 
      4 ------------ Keypad Row 5
      8 ------------ Keypad Col 1 
      9 ------------ Keypad Col 2 
     10 ------------ Keypad Col 3
     11 ------------ Keypad Col 4
     12 ------------ Keypad Col 5


"""

from time import sleep_ms, sleep
from machine import I2C, Pin  # type: ignore
from sx1509 import Expander, PinModes, HIGH, LOW

i2c = I2C(0, freq=400000, scl=Pin(17), sda=Pin(16))  # Pico I2C bus 1
expander = Expander(i2c, address=0x70)

KEY_ROWS = 5
KEY_COLS = 5

KEY_MAP = [
    ['1', '2', '3', '4', '5'],
    ['6', '7', '8', '9', '10'],
    ['11', '12', '13', '14', '15'],
    ['16', '17', '18', '19', '20'],
    ['21', '22', '23', '24', '25']
]

SLEEP_TIME = 256

SCAN_TIME = 2

DEBOUNCE_TIME = 1

expander.keypad(KEY_ROWS, KEY_COLS, SLEEP_TIME, SCAN_TIME, DEBOUNCE_TIME)
# expander.pin_mode(5, PinModes.INPUT)
# expander.write_pin(5, 1)
# 
# 
def test():
    """Test code."""
    try:
        while True:
            key_data = expander.read_keypad()
            if key_data != 0:
                # A key was pressed
                # Format the key_data into readable binary
                key_parts = [(key_data >> (4 * i)) & 0xF
                             for i in range(4)][::-1]
                formatted_key_data = " ".join(f"{part:04b}"
                                              for part in key_parts)
                #yprint(f"Key data: {formatted_key_data}")
                # Find the active row and columns
                row = expander.get_row(key_data)
                col = expander.get_col(key_data)
                # Get key pressed from key map
                key = KEY_MAP[row][col]
                #print(f"Row: {row}, Column: {col}, Key: {key}")
                print(f"Key: {key}")
            sleep_ms(100)
    except KeyboardInterrupt:
        print("\nCtrl-C pressed to exit.")
    finally:
        expander.reset()

#     while True:
#         if expander.read_pin(5) == False:
#             print("Pressed")
#             sleep(1)

test()
