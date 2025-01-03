# lc76g.py

import machine
import time

class LC76G:
    def __init__(self, tx_pin=0, rx_pin=1, baudrate=115200):
        # Initialize UART0 for communication with LC76G
        self.uart = machine.UART(0, baudrate=baudrate, tx=tx_pin, rx=rx_pin)
        self.uart.init(bits=8, parity=None, stop=2)

    def read_data(self):
        """Reads data from the GNSS module"""
        if self.uart.any():
            return self.uart.read()
        return None

    def parse_gps_data(self, data):
        """Parses the NMEA data and extracts useful information"""
        if not data:
            return None
        
        # Attempt to decode the data into a string
        try:
            data_str = data.decode('utf-8').strip()  # Decode to UTF-8
        except Exception:
            # If decoding fails (e.g., non-UTF-8 data), treat it as invalid data
            return None
        
        # Look for NMEA sentences like $GPGGA or $GPRMC (commonly used for GPS)
        if data_str.startswith('$GPGGA'):
            return self.parse_gpgga(data_str)
        elif data_str.startswith('$GPRMC'):
            return self.parse_gprmc(data_str)

        return None

    def parse_gpgga(self, nmea_data):
        """Parse GPGGA NMEA sentence (Global Positioning System Fix Data)"""
        parts = nmea_data.split(',')
        if len(parts) > 6:
            lat = parts[2]
            lon = parts[4]
            fix_quality = parts[6]
            return {
                'latitude': lat,
                'longitude': lon,
                'fix_quality': fix_quality
            }
        return None

    def parse_gprmc(self, nmea_data):
        """Parse GPRMC NMEA sentence (Recommended Minimum Specific GPS/Transit Data)"""
        parts = nmea_data.split(',')
        if len(parts) > 9:
            time_utc = parts[1]
            status = parts[2]
            lat = parts[3]
            lon = parts[5]
            speed = parts[7]
            return {
                'time_utc': time_utc,
                'status': status,
                'latitude': lat,
                'longitude': lon,
                'speed': speed
            }
        return None
