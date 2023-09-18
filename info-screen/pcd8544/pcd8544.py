from adafruit_pcd8544 import PCD8544
import busio
import board
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

from PIL import Image, ImageDraw, ImageFont


class PCB8544(PCD8544):
    def __init__(self, dc_pin: Pin, cs_pin: Pin, reset_pin: Pin, backlight_pin: Pin, contrast: int = 80, bias: int = 4, font: str = "DejaVuSansMono.ttf", font_size: int = 8):
        # Initialize SPI bus and control pins
        spi = busio.SPI(board.SCK, MOSI=board.MOSI)
        dc = digitalio.DigitalInOut(dc_pin)                 # data/command
        cs = digitalio.DigitalInOut(cs_pin)                 # Chip select
        reset = digitalio.DigitalInOut(reset_pin)           # reset
        # self.__backlight = digitalio.DigitalInOut(backlight_pin)   # backlight
        # self.__backlight.switch_to_output()

        super().__init__(spi, dc, cs, reset, contrast=contrast, bias=bias)

        self.__font = None
        self.SetTrueTypeFont(font, font_size)

        self.fill(0)
        self.show()

    def SetBacklight(self, on: bool) -> None:
        self.__backlight.value = on

    def SetTrueTypeFont(self, font: str, size: int) -> None:
        self.__font = ImageFont.truetype(font, size)

    def ShowMultilineText(self, text: str, spacing: int = -1) -> None:
        if spacing < 0:
            spacing = self.__font.size // 2

        self.fill(0)
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        draw.multiline_text(
            (0, 0),
            text,
            font=self.__font,
            fill=255,
            spacing=spacing,
        )

        self.image(image)

        # self.text(msg, 0, 0, 1)
        self.show()
