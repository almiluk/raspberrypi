from adafruit_pcd8544 import PCD8544
import busio
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin


class PCB8544(PCD8544):
    def __init__(self, dc_pin: Pin, cs_pin: Pin, reset_pin: Pin, backlight_pin: Pin, contrast: int = 80, bias: int = 4):
        # Initialize SPI bus and control pins
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        dc = digitalio.DigitalInOut(dc_pin)                 # data/command
        cs = digitalio.DigitalInOut(cs_pin)                 # Chip select
        reset = digitalio.DigitalInOut(reset_pin)           # reset
        #self.__backlight = digitalio.DigitalInOut(backlight_pin)   # backlight
        #self.__backlight.switch_to_output()

        super().__init__(spi, dc, cs, reset, contrast=contrast, bias=bias)

        self.fill(0)
        self.show()

    def SetBacklight(self, on: bool) -> None:
        self.__backlight.value = on
