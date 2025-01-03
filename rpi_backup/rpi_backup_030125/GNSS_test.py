from NMEA import NMEAParser
import utime

# Initialize UART
uart = machine.UART(0, baudrate=115200, tx=machine.Pin(0), rx=machine.Pin(1))
parser = NMEAParser()

print("Starting GNSS data reading...")

while True:
    if uart.any():
        sentence = uart.readline()
        if sentence:
            try:
                sentence = sentence.decode('utf-8').strip()
                print(f"Raw Data: {sentence}")  # Debug: Log raw data
                parser.parse(sentence)

                if parser.latitude and parser.longitude:
                    print(f"Time: {parser.time_utc}")
                    print(f"Latitude: {parser.latitude}°")
                    print(f"Longitude: {parser.longitude}°")
                    print("-----------------------------")

            except UnicodeError:
                 pass #Ignore decoding errors

    utime.sleep(0.1)