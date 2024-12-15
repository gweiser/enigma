"""MicroPython SX1509 Expander I2C driver.

Derived from SparkFun_SX1509_Arduino_Library
Original source: https://github.com/sparkfun/SparkFun_SX1509_Arduino_Library
"""
from micropython import const  # type: ignore
from machine import Pin  # type: ignore
from time import sleep_ms

HIGH = const(1)  # Represents logical high or ON state
LOW = const(0)  # Represents logical low or OFF state
CHANGE = const(0b11)  # Interrupt change
FALLING = const(0b10)  # Interrupt falling
RISING = const(0b01)  # Interrupt rising


class PinModes:
    INPUT = 0  # Input mode
    INPUT_PULLUP = 1  # Input mode with pull-up resistor enabled
    OUTPUT = 2  # Output mode
    ANALOG_OUTPUT = 3  # Analog output mode


class Expander(object):
    """I2C interace for SX1509 Expander."""

    # Device & I/O Banks
    REG_INPUT_DISABLE_B = const(0x00)  # Input buffer disable (Bank B)
    REG_INPUT_DISABLE_A = const(0x01)  # Input buffer disable (Bank A)
    REG_LONG_SLEW_B = const(0x02)  # Output buffer long slew (Bank B)
    REG_LONG_SLEW_A = const(0x03)  # Output buffer long slew (Bank A)
    REG_LOW_DRIVE_B = const(0x04)  # Output buffer low drive (Bank B)
    REG_LOW_DRIVE_A = const(0x05)  # Output buffer low drive (Bank A)
    REG_PULL_UP_B = const(0x06)  # Pull-up (Bank B)
    REG_PULL_UP_A = const(0x07)  # Pull-up (Bank A)
    REG_PULL_DOWN_B = const(0x08)  # Pull-down (Bank B)
    REG_PULL_DOWN_A = const(0x09)  # Pull-down (Bank A)
    REG_OPEN_DRAIN_B = const(0x0A)  # Open drain (Bank B)
    REG_OPEN_DRAIN_A = const(0x0B)  # Open drain (Bank A)
    REG_POLARITY_B = const(0x0C)  # Polarity (Bank B)
    REG_POLARITY_A = const(0x0D)  # Polarity (Bank A)
    REG_DIR_B = const(0x0E)  # Direction (Bank B)
    REG_DIR_A = const(0x0F)  # Direction (Bank A)
    REG_DATA_B = const(0x10)  # Data (Bank B)
    REG_DATA_A = const(0x11)  # Data (Bank A)
    REG_INTERRUPT_MASK_B = const(0x12)  # Interrupt mask (Bank B)
    REG_INTERRUPT_MASK_A = const(0x13)  # Interrupt mask (Bank A)
    REG_SENSE_HIGH_B = const(0x14)  # Sense I/O[15:12]
    REG_SENSE_LOW_B = const(0x15)  # Sense I/O[11:8]
    REG_SENSE_HIGH_A = const(0x16)  # Sense I/O[7:4]
    REG_SENSE_LOW_A = const(0x17)  # Sense I/O[3:0]
    REG_INTERRUPT_SOURCE_B = const(0x18)  # Interrupt source (Bank B)
    REG_INTERRUPT_SOURCE_A = const(0x19)  # Interrupt source (Bank A)
    REG_EVENT_STATUS_B = const(0x1A)  # Event status (Bank B)
    REG_EVENT_STATUS_A = const(0x1B)  # Event status (Bank A)
    REG_LEVEL_SHIFTER_1 = const(0x1C)  # Level shifter 1
    REG_LEVEL_SHIFTER_2 = const(0x1D)  # Level shifter 2
    REG_CLOCK = const(0x1E)  # Clock management
    REG_MISC = const(0x1F)  # Miscellaneous device settings
    REG_LED_DRIVER_ENABLE_B = const(0x20)  # LED driver enable (Bank B)
    REG_LED_DRIVER_ENABLE_A = const(0x21)  # LED driver enable (Bank A)
    # Debounce and Keypad Engine
    REG_DEBOUNCE_CONFIG = const(0x22)  # Debounce configuration
    REG_DEBOUNCE_ENABLE_B = const(0x23)  # Debounce enable (Bank B)
    REG_DEBOUNCE_ENABLE_A = const(0x24)  # Debounce enable (Bank A)
    REG_KEY_CONFIG1 = const(0x25)  # Key scan configuration
    REG_KEY_CONFIG2 = const(0x26)  # Key scan configuration
    REG_KEY_DATA1 = const(0x27)  # Key value (column)
    REG_KEY_DATA2 = const(0x28)  # Key value (row)
    # LED Driver (PWM, Blinking, Breathing)
    REG_T_ON = {  # Time On
        0: 0x29, 1: 0x2C, 2: 0x2F, 3: 0x32, 4: 0x35, 5: 0x3A, 6: 0x3F, 7: 0x44,
        8: 0x49, 9: 0x4C, 10: 0x4F, 11: 0x52, 12: 0x55, 13: 0x5A, 14: 0x5F,
        15: 0x64
    }
    REG_I_ON = {  # Intensity On
        0: 0x2A, 1: 0x2D, 2: 0x30, 3: 0x33, 4: 0x36, 5: 0x3B, 6: 0x40, 7: 0x45,
        8: 0x4A, 9: 0x4D, 10: 0x50, 11: 0x53, 12: 0x56, 13: 0x5B, 14: 0x60,
        15: 0x65
    }
    REG_OFF = {  # Time / Intensity Off
        0: 0x2B, 1: 0x2E, 2: 0x31, 3: 0x34, 4: 0x37, 5: 0x3C, 6: 0x41, 7: 0x46,
        8: 0x4B, 9: 0x4E, 10: 0x51, 11: 0x54, 12: 0x57, 13: 0x5C, 14: 0x61,
        15: 0x66
    }
    REG_T_RISE = {  # Fade In
        4: 0x38, 5: 0x3D, 6: 0x42, 7: 0x47, 12: 0x58, 13: 0x5D, 14: 0x62,
        15: 0x67
    }
    REG_T_FALL = {  # Fade Out
        4: 0x39, 5: 0x3E, 6: 0x43, 7: 0x48, 12: 0x59, 13: 0x5E, 14: 0x63,
        15: 0x68
    }
    # Miscellaneous
    REG_HIGH_INPUT_B = const(0x69)  # High input enable (Bank B)
    REG_HIGH_INPUT_A = const(0x6A)  # High input enable (Bank A)
    REG_RESET = const(0x7D)  # Software reset
    REG_TEST1 = const(0x7E)  # Test register
    REG_TEST2 = const(0x7F)  # Test register

    def __init__(self, i2c, address=0x3E, reset_pin=None):
        """Constructor for expander.

        Args:
            i2c (class): I2C bus
            address (int): Expander I2C address (0x3E, 0x3F, 0x70 or 0x71)
                           Set using ADDR0 & ADDR1 pins. Default 0x3E
            reset_pin(int): Reset pin. Library attempts software reset if None
        """
        self.i2c = i2c
        self.address = address
        if reset_pin is None:
            self.reset_pin = None
        else:
            self.reset_pin = Pin(reset_pin, Pin.OUT)
            self.reset_pin.value(1)
        self.reset()
        # Test I2C connection
        test = self.read_word(self.REG_INTERRUPT_MASK_A)
        # Should equal default values 1111 1111 & 0000 0000
        if test != 0xFF00:
            print(test)
            raise OSError("I2C communication test failed!")
        # Set clock frequency using defaults (internal 2 Mhz)
        self.config_clock()

    def blink(self, pin, t_on, t_off, on_intensity=255, off_intensity=0):
        """Configures blinking behavior for a pin.

        Args:
            pin (int): The pin to configure for blinking
            t_on (int): The ON duration in milliseconds
            t_off (int): The OFF duration in milliseconds
            on_intensity (int): The intensity of the LED when ON, default 255
            off_intensity (int): The intensity of the LED when OFF, default 0
        """
        on_reg = self.calculate_led_t_register(t_on)
        off_reg = self.calculate_led_t_register(t_off)

        self.setup_blink(pin, on_reg, off_reg, on_intensity, off_intensity,
                         0, 0)

    def breathe(self, pin, t_on, t_off, rise, fall, on_intensity=255,
                off_intensity=0, log=False):
        """Configure a pin for breathing effect with specified parameters.

        Args:
            pin (int): Pin number to configure for the breathing effect
            t_on (int): ON duration in milliseconds
            t_off (int): OFF duration in milliseconds
            rise (int): Rise time duration in milliseconds
            fall (int): Fall time duration in milliseconds
            on_intensity (int): Intensity of the LED when on
            off_intensity (int): Minimum intensity of the LED
            log (bool): Use logarithmic scaling if True, else linear
        """
        # Constrain off_intensity to be between 0 and 7
        off_intensity = max(0, min(off_intensity, 7))

        on_reg = self.calculate_led_t_register(t_on)
        off_reg = self.calculate_led_t_register(t_off)

        rise_time = self.calculate_slope_register(rise, on_intensity,
                                                  off_intensity)
        fall_time = self.calculate_slope_register(fall, on_intensity,
                                                  off_intensity)

        self.setup_blink(pin, on_reg, off_reg, on_intensity, off_intensity,
                         rise_time, fall_time, log)

    def calculate_led_t_register(self, ms):
        """Calculates the optimal register value for LED ON time duration.

        This method determines the best register setting for configuring the
        LED driver's ON time based on the desired duration in milliseconds. It
        aims to find a register value that closely matches the specified ON
        time within the constraints of the SX1509's timing resolution and the
        current clock frequency.

        Args:
            ms (int or float): Desired LED ON time duration in milliseconds

        Returns:
            int: The register value (1 to 31) that best matches the desired
                ON time duration. Returns 0 if _clkX is not set
        """
        # Confirm valid clock
        if self._clkX == 0:
            raise ValueError("Clock cannot equal zero!")

        reg_on1 = (ms / 1000.0) / (64.0 * 255.0 / self._clkX)
        reg_on2 = reg_on1 / 8
        reg_on1 = max(1, min(reg_on1, 15))
        reg_on2 = max(16, min(reg_on2, 31))

        time_on1 = 64.0 * reg_on1 * 255.0 / self._clkX * 1000.0
        time_on2 = 512.0 * reg_on2 * 255.0 / self._clkX * 1000.0

        if abs(time_on1 - ms) < abs(time_on2 - ms):
            return int(reg_on1)
        else:
            return int(reg_on2)

    def calculate_slope_register(self, ms, on_intensity, off_intensity):
        """Calculates the register value for controlling LED intensity slope.

        Determines the best register setting for configuring the rate of change
        in LED intensity based on desired duration, on intensity, and off
        intensity.  It calculates two potential register values and selects the
        one whose corresponding time duration closely matches the specified
        duration in milliseconds.

        Args:
            ms (int or float): Desired duration for the intensity change in ms
            on_intensity (int): LED on intensity value (range 0 to 255)
            off_intensity (int): LED off intensity value (range 0 to 255)

        Returns:
            int: The register value (between 1 to 31) that best fits the
                desired duration and intensity change. Returns 0 if the clock
                frequency (_clkX) is not set.
        """
        # Confirm valid clock
        if self._clkX == 0:
            raise ValueError("Clock cannot equal zero!")

        # Calculate time factor based on intensities and clock frequency
        t_factor = (on_intensity - (4.0 * off_intensity)) * 255.0 / self._clkX
        time_s = ms / 1000.0

        # Calculate preliminary slope register values
        reg_slope1 = time_s / t_factor
        reg_slope2 = reg_slope1 / 16

        # Constrain the slope register values to valid ranges
        reg_slope1 = max(1, min(reg_slope1, 15))
        reg_slope2 = max(16, min(reg_slope2, 31))

        # Calculate the actual time durations for the slope register values
        reg_time1 = reg_slope1 * t_factor * 1000.0
        reg_time2 = 16 * reg_time1

        # Select slope register value that best matches the desired duration
        if abs(reg_time1 - ms) < abs(reg_time2 - ms):
            return int(reg_slope1)
        else:
            return int(reg_slope2)

    def check_interrupt(self, pin):
        """
        Checks if an interrupt has occurred on the specified pin.

        Args:
            pin (int): The pin number to check for an interrupt.

        Returns:
            bool: True if an interrupt has occurred on specified pin else False
        """
        if self.interrupt_source(False) & (1 << pin):
            return True
        return False

    def config_clock(self, osc_source=2, osc_pin_function=0, osc_freq_out=0,
                     osc_divider=1):
        """Configures clock settings.

        Args:
            osc_source (int): Oscillator frequency source selection. Default 2
                (0: Off, 1: External Input, 2: Internal 2 MHz, 3: Reserved)
            osc_pin_function (int): Function of the OSCIO pin. Default is 0
                (0: Input, 1: Output)
            osc_freq_out (int): Frequency of the OSCOUT pin. Default is 0
                (0: LOW, 1-14: Frequency = FoSC/(2^(value-1)), 15: HIGH)
            osc_divider (int): Clock divider for adjusting clock frequency.
                Default 1. Valid range is 1 to 7, where 1 results in no
                division and values > 1 result in divided frequencies
        """
        # Construct RegClock
        osc_source = (osc_source & 0b11) << 5
        osc_pin_function = (osc_pin_function & 1) << 4
        osc_freq_out = (osc_freq_out & 0b1111)
        reg_clock = osc_source | osc_pin_function | osc_freq_out
        self.write_byte(self.REG_CLOCK, reg_clock)

        # Config RegMisc[6:4] with osc_divider
        osc_divider = min(max(osc_divider, 1), 7)  # Constrain osc_divider 1-7
        self._clkX = 2000000.0 / (1 << (osc_divider - 1))
        osc_divider = (osc_divider & 0b111) << 4
        reg_misc = self.read_byte(self.REG_MISC)
        reg_misc &= ~(0b111 << 4)
        reg_misc |= osc_divider
        self.write_byte(self.REG_MISC, reg_misc)

    def debounce_config(self, config_value):
        """Configures the debounce settings.

        Args:
            config_value (int): The debounce configuration value (3-bit value)
        """
        # Apply the debounce configuration
        config_value &= 0b111  # Constrain to 3-bit value
        self.write_byte(self.REG_DEBOUNCE_CONFIG, config_value)

    def debounce_enable(self, pin):
        """
        Enables the debounce feature for a specific pin.

        Args:
            pin (int): The pin number for which to enable debounce.
        """
        debounce_enable = self.read_word(self.REG_DEBOUNCE_ENABLE_B)
        debounce_enable |= (1 << pin)  # Set the bit corresponding to the pin
        self.write_word(self.REG_DEBOUNCE_ENABLE_B, debounce_enable)

    def debounce_keypad(self, time, num_rows, num_cols):
        """
        Sets up debounce timing and enables debounce for the specified number
        of rows and columns in a keypad matrix configuration.

        Args:
            time (int): The debounce time to set
            num_rows (int): The number of rows in the keypad matrix
            num_cols (int): The number of columns in the keypad matrix
        """
        # Set up debounce time
        self.debounce_time(time)

        # Enable debounce for row pins
        for i in range(num_rows):
            self.debounce_enable(i)

        # Enable debounce for column pins, adjusting for column pin start index
        for i in range(8, 8 + num_cols):
            self.debounce_enable(i)

    def debounce_time(self, time):
        """
        Sets the debounce time.

        Args:
            time (int): The desired debounce time in milliseconds
        """
        # Confirm valid clock
        if self._clkX == 0:
            raise ValueError("Clock cannot equal zero!")

        # Mapping time to debounce configuration value
        config_value = 0
        for i in range(7, -1, -1):
            if time & (1 << i):
                config_value = i + 1
                break
        # Constrain config_value to be within 0-7
        config_value = max(0, min(config_value, 7))
        self.debounce_config(config_value)

    def enable_interrupt(self, pin, rise_fall):
        """
        Enables interrupts for a specified pin with the specified sensitivity.

        Args:
            pin (int): The pin number for which to enable interrupts.
            rise_fall (int): The interrupt sensitivity. Use global constants:
                             CHANGE, RISING, FALLING.
        """
        # Set REG_INTERRUPT_MASK
        temp_word = self.read_word(self.REG_INTERRUPT_MASK_B)
        temp_word &= ~(1 << pin)  # 0 = event on IO will trigger interrupt
        self.write_word(self.REG_INTERRUPT_MASK_B, temp_word)

        # Calculate bit position for the sensitivity setting
        pin_mask = (pin & 0x07) * 2
        sense_register = self.REG_SENSE_HIGH_B if pin >= 8 else (
            self.REG_SENSE_HIGH_A)
        temp_word = self.read_word(sense_register)
        temp_word &= ~(0b11 << pin_mask)  # Clear existing sensitivity bits
        temp_word |= (rise_fall << pin_mask)  # Set new sensitivity bits
        self.write_word(sense_register, temp_word)

    def get_col(self, key_data):
        """Extracts the column index from the key data.

        Args:
            key_data (int): The key data from which to extract the column index

        Returns:
            int: The index of the first active column or 0 if none
        """
        col_data = (key_data & 0xFF00) >> 8

        for i in range(8):
            if col_data & (1 << i):
                return i
        return 0

    def get_row(self, key_data):
        """Extracts the row index from the key data.

        Args:
            key_data (int): The key data from which to extract the row index

        Returns:
            int: The index of the first active row found or 0 if none
        """
        row_data = key_data & 0x00FF

        for i in range(8):
            if row_data & (1 << i):
                return i
        return 0

    def interrupt_source(self, clear=True):
        """
        Reads source of interrupt and optionally clears interrupt flags.

        Args:
            clear (bool, optional): If True, clears the interrupt flags after
            reading. Defaults to True.

        Returns:
            int: The source of the interrupt as a 16-bit value.
        """
        int_source = self.read_word(self.REG_INTERRUPT_SOURCE_B)
        if clear:  # Clear interrupts
            self.write_word(self.REG_INTERRUPT_SOURCE_B, 0xFFFF)
        return int_source

    def keypad(self, rows, columns, sleep_time, scan_time, debounce_time):
        """
        Configures keypad operation, setting up rows as outputs,
        columns as inputs, and configuring various parameters like sleep time,
        scan time, and debounce time to optimize performance and power.

        This method configures direction of the GPIO pins for rows & columns
        appropriately, sets open drain for row pins, enables pull-up resistors
        for column pins, and configures debounce settings to prevent false
        keypresses. Additionally, it calculates and sets timing parameters for
        efficient keypad scanning and power management.

        Args:
            rows (int): Number of rows in the keypad matrix.
            columns (int): Number of columns in the keypad matrix
            sleep_time (int): Sleep time in milliseconds, configuring the
                auto-sleep feature of the keypad scanning to save power. The
                device will enter sleep mode after this time if no keypresses
            scan_time (int): Time in milliseconds for each row scan, defining
                how long each row is powered during the scanning process
            debounce_time (int): Time in milliseconds to debounce the keypad,
                helping to eliminate false keypresses caused by switch bounce
        """

        # Confirm valid clock
        if self._clkX == 0:
            raise ValueError("Clock cannot equal zero!")

        # Configure row and column directions
        temp_word = self.read_word(self.REG_DIR_B)
        for i in range(rows):
            temp_word &= ~(1 << i)
        for i in range(8, columns * 2):
            temp_word |= (1 << i)
        self.write_word(self.REG_DIR_B, temp_word)

        # Configure open drain for rows
        temp_byte = self.read_byte(self.REG_OPEN_DRAIN_A)
        for i in range(rows):
            temp_byte |= (1 << i)
        self.write_byte(self.REG_OPEN_DRAIN_A, temp_byte)

        # Configure pull-up for columns
        temp_byte = self.read_byte(self.REG_PULL_UP_B)
        for i in range(columns):
            temp_byte |= (1 << i)
        self.write_byte(self.REG_PULL_UP_B, temp_byte)

        # Ensure debounce and scan times are within limits
        debounce_time = max(1, min(debounce_time, 64))
        scan_time = max(1, min(scan_time, 128))
        if debounce_time >= scan_time:
            debounce_time = scan_time >> 1

        self.debounce_keypad(debounce_time, rows, columns)

        # Calculate scan and sleep time bits
        scan_time_bits, sleep_time_bits = 0, 0
        for i in range(7, 0, -1):
            if scan_time & (1 << i):
                scan_time_bits = i
                break
        for i in range(7, 0, -1):
            if sleep_time & (1 << (i + 6)):
                sleep_time_bits = i
                break
        if sleep_time_bits == 0 and sleep_time > 0:
            sleep_time_bits = 1

        # Configure keypad timing and layout
        sleep_time_bits = (sleep_time_bits & 0x07) << 4
        scan_time_bits &= 0x07
        temp_byte = sleep_time_bits | scan_time_bits
        self.write_byte(self.REG_KEY_CONFIG1, temp_byte)

        rows, columns = (rows - 1) & 0x07, (columns - 1) & 0x07
        self.write_byte(self.REG_KEY_CONFIG2, (rows << 3) | columns)

    def led_driver_init(self, pin, freq=1, log=False):
        """Initializes a pin for LED driving with optional frequency and mode.

        Args:
            pin (int): The pin number to initialize for LED driving
            freq (int, optional): Frequency setting for the LED driver
            log (bool, optional): If True, sets logarithmic mode, else linear
        """
        # Confirm valid clock
        if self._clkX == 0:
            raise ValueError("Clock cannot equal zero!")

        # Disable input buffer
        temp_word = self.read_word(self.REG_INPUT_DISABLE_B)
        temp_word |= (1 << pin)
        self.write_word(self.REG_INPUT_DISABLE_B, temp_word)

        # Disable pull-up
        temp_word = self.read_word(self.REG_PULL_UP_B)
        temp_word &= ~(1 << pin)
        self.write_word(self.REG_PULL_UP_B, temp_word)

        # Set direction to output
        temp_word = self.read_word(self.REG_DIR_B)
        temp_word &= ~(1 << pin)  # 0=output
        self.write_word(self.REG_DIR_B, temp_word)

        # Configure LED driver clock and mode
        temp_byte = self.read_byte(self.REG_MISC)
        if log:
            temp_byte |= (1 << 7) | (1 << 3)  # Logarithmic mode
        else:
            temp_byte &= ~(1 << 7) & ~(1 << 3)  # Linear mode
        freq = (freq & 0x7) << 4  # mask only 3 bits & shift to bit 6:4
        temp_byte |= freq
        self.write_byte(self.REG_MISC, temp_byte)

        # Enable LED driver operation
        temp_word = self.read_word(self.REG_LED_DRIVER_ENABLE_B)
        temp_word |= (1 << pin)
        self.write_word(self.REG_LED_DRIVER_ENABLE_B, temp_word)

        # Set REG_DATA bit low ~ LED driver started
        temp_word = self.read_word(self.REG_DATA_B)
        temp_word &= ~(1 << pin)
        self.write_word(self.REG_DATA_B, temp_word)

    def pin_mode(self, pin, in_out, initial_level=0):
        """Configures direction of a pin and its initial level if applicable.

        Args:
            pin (int): The pin number to configure
            in_out (int): Pin mode (ANALOG_OUTPUT, OUTPUT, INPUT, INPUT_PULLUP)
            initial_level (int): The initial level HIGH or LOW (default)
        """
        if (in_out == PinModes.OUTPUT
                or in_out == PinModes.ANALOG_OUTPUT):
            # Output
            temp_reg_data = self.read_word(self.REG_DATA_B)
            # Initial output level
            if initial_level == LOW:
                temp_reg_data &= ~(1 << pin)
                self.write_word(self.REG_DATA_B, temp_reg_data)
            mode_bit = 0
        else:
            # Input
            mode_bit = 1

        temp_reg_dir = self.read_word(self.REG_DIR_B)
        if mode_bit:
            temp_reg_dir |= (1 << pin)
        else:
            temp_reg_dir &= ~(1 << pin)
        self.write_word(self.REG_DIR_B, temp_reg_dir)

        # Set up pull-up resistor if necessary
        if in_out == PinModes.INPUT_PULLUP:
            self.write_pin(pin, HIGH)

        # Initialize LED driver if analog output is selected
        if in_out == PinModes.ANALOG_OUTPUT:
            self.led_driver_init(pin)

    def pwm(self, pin, intensity):
        """Sets the PWM intensity for a specified pin.

        Args:
            pin (int): The pin number to set the PWM intensity
            intensity (int): The intensity value to set for the pin
        """
        if pin not in self.REG_I_ON:
            raise ValueError(f"Invalid pin: {pin}")
        self.write_byte(self.REG_I_ON[pin], intensity)

    def read_keypad(self):
        """
        Reads the keypad data register and returns the inverted key data.

        This method reads the 16-bit keypad data, inverts the bits
        (since a logical '0' indicates a button press), and returns the result.
        Each bit in the return value corresponds to a key in the keypad matrix,
        with '1' indicating a pressed key and '0' indicating no press.

        Returns:
            int: The inverted keypad data.
        """
        return 0xFFFF ^ self.read_word(self.REG_KEY_DATA1)

    def read_pin(self, pin):
        """Reads the state of a given input pin.

        Args:
            pin (int): The pin number to read.

        Returns:
            bool: True if the pin is high, False if low.

        Raises:
            ValueError: If the pin is not configured as an input.
        """
        temp_reg_dir = self.read_word(self.REG_DIR_B)
        # Check if the pin is configured as an input
        if not (temp_reg_dir & (1 << pin)):
            raise ValueError(f"Pin {pin} is not configured as an input.")

        temp_reg_data = self.read_word(self.REG_DATA_B)
        return bool(temp_reg_data & (1 << pin))

    def reset(self):
        """Reset expander."""
        if self.reset_pin is None:
            # Software reset
            self.write_byte(self.REG_RESET, 0x12)
            self.write_byte(self.REG_RESET, 0x34)
        else:
            # Hardware reset
            misc = self.read_byte(self.REG_MISC)
            if misc & (1 << 2):
                misc &= ~(1 << 2)
                self.write_byte(self.REG_MISC, misc)

            self.reset_pin.value(0)
            sleep_ms(1)
            self.reset_pin.value(1)

    def setup_blink(self, pin, t_on, t_off, on_intensity, off_intensity,
                    t_rise, t_fall, log=False):
        """Configures an LED for blinking or breathing effects.

        Args:
            pin (int): The pin to configure.
            t_on (int): Time ON duration as a 5-bit value
            t_off (int): Time OFF duration as a 5-bit value
            on_intensity (int): Intensity of the LED when on
            off_intensity (int): Intensity of the LED when off (3 bits)
            t_rise (int): Rise time duration as a 5-bit value
            t_fall (int): Fall time duration as a 5-bit value
            log (bool): If True, use logarithmic mode for intensity
        """
        self.led_driver_init(pin, log)

        # Keep parameters within their limits
        t_on &= 0x1F
        t_off &= 0x1F
        off_intensity &= 0x07

        # Write the time on, time/intensity off, and on intensity
        self.write_byte(self.REG_T_ON[pin], t_on)
        self.write_byte(self.REG_OFF[pin], (t_off << 3) | off_intensity)
        self.write_byte(self.REG_I_ON[pin], on_intensity)

        # Prepare tRise and tFall
        t_rise &= 0x1F
        t_fall &= 0x1F

        # Write tRise and tFall if the pin supports fading
        if pin in self.REG_T_RISE:
            self.write_byte(self.REG_T_RISE[pin], t_rise)
        if pin in self.REG_T_FALL:
            self.write_byte(self.REG_T_FALL[pin], t_fall)

    def sync(self):
        """Synchronizes the LED timers.

           Resets the PWM/Blink/Fade counters, syncing any blinking
           LEDs. Bit 2 of REG_MISC is set, which alters the functionality
           of the nReset pin. The nReset pin is toggled low->high, which should
           reset all LED counters. Bit 2 of REG_MISC is again cleared,
           returning nReset pin to POR functionality
        """
        # Verify hardware reset pin specified
        if self.reset_pin is None:
            raise ValueError("Hardware reset pin required for sync.")
        # Switch from POR to Reset PWM/Blink/Fade counters
        reg_misc = self.read_byte(self.REG_MISC)
        if not (reg_misc & 0x04):
            reg_misc |= (1 << 2)
            self.write_byte(self.REG_MISC, reg_misc)
        # Toggle nReset pin to sync LED timers
        self.reset_pin.value(0)
        sleep_ms(1)
        self.reset_pin.value(1)
        # Reset nReset to its default functionality
        self.write_byte(self.REG_MISC, (reg_misc & ~(1 << 2)))

    def write_pin(self, pin, high_low):
        """Writes high or low value to a pin or adjusts pull-up/down if input.

        This method sets pin to either high or low if configured as an output,
        or configures pull-up/down resistors if the pin is set as an input.

        Args:
            pin (int): The pin number to modify
            high_low (int): Desired state (high=1 or low=0) for the pin

        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        temp_reg_dir = self.read_word(self.REG_DIR_B)

        # Check if the pin is configured as an output
        if (0xFFFF ^ temp_reg_dir) & (1 << pin):
            temp_reg_data = self.read_word(self.REG_DATA_B)
            if high_low:
                temp_reg_data |= (1 << pin)
            else:
                temp_reg_data &= ~(1 << pin)
            return self.write_word(self.REG_DATA_B, temp_reg_data)
        else:
            # The pin is configured as an input, manage pull-up/down
            temp_pull_up = self.read_word(self.REG_PULL_UP_B)
            temp_pull_down = self.read_word(self.REG_PULL_DOWN_B)

            if high_low:  # Configure pull-up for high, disable pull-down
                temp_pull_up |= (1 << pin)
                temp_pull_down &= ~(1 << pin)
            else:  # Configure pull-down for low, disable pull-up
                temp_pull_down |= (1 << pin)
                temp_pull_up &= ~(1 << pin)
            success_up = self.write_word(self.REG_PULL_UP_B, temp_pull_up)
            success_down = self.write_word(self.REG_PULL_DOWN_B,
                                           temp_pull_down)
            return success_up and success_down

    def read_byte(self, cmd):
        """Read byte from expander.

        Args:
            cmd (byte): Command address to read
        """
        buf = self.i2c.readfrom_mem(self.address, cmd, 1)
        return int.from_bytes(buf, 'big')

    def read_word(self, cmd):
        """Read double byte from expander.

        Args:
            cmd (byte): Command address to read
        Returns:
            int: value
        """
        buf = self.i2c.readfrom_mem(self.address, cmd, 2)
        return int.from_bytes(buf, 'big')

    def write_byte(self, cmd, data):
        """Write byte to expander.

        Args:
            cmd (byte): Command address to write
            data (byte): Byte to write
        """
        self.i2c.writeto_mem(self.address, cmd, bytearray([data]))

    def write_bytes(self, cmd, data):
        """Write bytes to expander.

        Args:
            cmd (byte): Command address to write
            data (bytes): Bytes to write
        """
        self.i2c.writeto_mem(self.address, cmd, data)

    def write_word(self, cmd, data):
        """Write double byte to expander.

        Args:
            cmd (byte): Command address to write
            data (int): Int to write
        """
        self.i2c.writeto_mem(self.address,
                             cmd,
                             data.to_bytes(2, 'big'))

    def write_list(self, cmd, data):
        """Write list of bytes to expander.

        Args:
            cmd (byte): Command address to write
            data (list): List to write
        """
        self.i2c.writeto_mem(self.address, cmd, bytearray(data))
