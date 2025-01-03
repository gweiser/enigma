import time
from lc76g import LC76G

# Initialize the LC76G GNSS module on UART0 (default pins: TX=GPIO0, RX=GPIO1)
gnss = LC76G(tx_pin=0, rx_pin=1)

# Send command to set the GNSS module to NMEA output mode
gnss.uart.write(b"$PMTK185,0*00\r\n")  # Switch to NMEA output

# Give the module some time to process the command
time.sleep(1)

def print_gps_data():
    """Read and print raw GPS data"""
    data = gnss.read_data()
    
    if data:
        print("Raw data (bytes):", data)  # Print the raw data (bytes)

        # Check if data contains valid NMEA sentence markers ($ at start and * at end)
        if data.startswith(b'$') and b'*' in data:
            try:
                # Decode to UTF-8
                data_str = data.decode('utf-8')
                print("FOUND NMEA")
                print("Decoded NMEA:", data_str)  # Print the decoded NMEA sentence
            except Exception as e:
                print("Error decoding NMEA sentence:", e)
        else:
            print("No valid NMEA sentence found.")
    else:
        print("No data available from GNSS module.")

# Continuously read and print GPS data every 1 second
while True:
    print_gps_data()
    time.sleep(1)
