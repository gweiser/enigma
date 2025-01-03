import machine
import utime

class NMEAParser:
    """A simple NMEA parser for GNSS data."""

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.time_utc = None

    def parse(self, nmea_sentence):
        if nmea_sentence.startswith("$GNRMC") or nmea_sentence.startswith("$GPRMC"):
            self._parse_rmc(nmea_sentence)

    def _parse_rmc(self, rmc_sentence):
        try:
            parts = rmc_sentence.split(',')

            if parts[2] == 'A':  # Data valid
                self.time_utc = self._format_time(parts[1])
                self.latitude = self._parse_coordinate(parts[3], parts[4])
                self.longitude = self._parse_coordinate(parts[5], parts[6])
            else:
                self.latitude = None
                self.longitude = None
                self.time_utc = None
        except (IndexError, ValueError):
            pass  # Handle parsing errors silently

    def _parse_coordinate(self, value, direction):
        if not value or not direction:
            return None

        # Degrees and minutes format (ddmm.mmmm)
        degrees = int(value[:2])
        minutes = float(value[2:])

        coordinate = degrees + (minutes / 60)
        if direction in ['S', 'W']:
            coordinate = -coordinate

        return coordinate

    def _format_time(self, time_str):
        if not time_str or len(time_str) < 6:
            return None

        hours = time_str[0:2]
        minutes = time_str[2:4]
        seconds = time_str[4:6]

        return f"{hours}:{minutes}:{seconds} UTC"