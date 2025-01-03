# sx127x.py
from machine import Pin, SPI
import time

class SX127x:
    def __init__(self, spi, nss, rst, dio0, freq=433E6, bandwidth=125E3, spreading_factor=7, coding_rate=5):
        self.spi = spi
        self.nss = Pin(nss, Pin.OUT)
        self.rst = Pin(rst, Pin.OUT)
        self.dio0 = Pin(dio0, Pin.IN)
        self.freq = freq
        self.bandwidth = bandwidth
        self.spreading_factor = spreading_factor
        self.coding_rate = coding_rate

        self.reset()

    def reset(self):
        # Reset the LoRa module
        self.rst.value(0)
        time.sleep(0.1)
        self.rst.value(1)
        time.sleep(0.1)

    def write_reg(self, addr, value):
        self.nss.value(0)
        self.spi.write(bytes([addr | 0x80, value]))  # 0x80 to indicate write mode
        self.nss.value(1)

    def read_reg(self, addr):
        self.nss.value(0)
        self.spi.write(bytes([addr & 0x7F]))  # 0x7F for read mode
        result = self.spi.read(1)
        self.nss.value(1)
        return result[0]

    def set_frequency(self):
        freq_int = int(self.freq / 61.03515625)
        self.write_reg(0x06, (freq_int >> 16) & 0xFF)
        self.write_reg(0x07, (freq_int >> 8) & 0xFF)
        self.write_reg(0x08, freq_int & 0xFF)

    def set_mode(self, mode):
        self.write_reg(0x01, mode)

    def set_packet(self, packet):
        # Assumes the packet is a byte string
        self.write_reg(0x00, len(packet))  # Set the length of the packet
        for i in range(len(packet)):
            self.write_reg(0x80, packet[i])  # Writing data to FIFO buffer

    def send_packet(self, packet):
        self.set_packet(packet)
        self.set_mode(0x01)  # Transmit mode

    def wait_for_dio0(self):
        while self.dio0.value() == 0:
            time.sleep(0.01)

    def init(self):
        # Set frequency to 433MHz (can be changed)
        self.set_frequency()
        # Set LoRa mode
        self.set_mode(0x80)  # Sleep mode, which allows configuration changes
        # Set other configurations like bandwidth, spreading factor, etc. (customize as needed)
        self.write_reg(0x1D, 0x72)  # Bandwidth 125kHz, Spreading Factor 7, Coding Rate 5
        self.write_reg(0x1E, 0x74)  # Set other registers if necessary
        self.write_reg(0x06, 0x40)  # Set Preamble Length
