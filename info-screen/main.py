from rpi_informer import RPIInformer
from pcd8544 import PCB8544

from PIL import Image, ImageDraw, ImageFont

import board
import signal
from time import sleep
from sys import exit


def main():
    informer = RPIInformer()
    display = PCB8544(
        board.D6,
        board.CE0,
        board.D5,
        board.D13,
        50,
    )

    def print_rpi_info(informer: RPIInformer):

        # TODO: Move it to PCB8544 class
        display.fill(0)
        msg = (""
        + "({bitrate}){ssid}\n"
        + "{cpu}"
        ).format(ssid=informer.WiFiInfo.ssid, bitrate=int(informer.WiFiInfo.bit_rate), cpu=informer.CPUInfo.percent)

        image = Image.new("1", (display.width, display.height))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("cg-pixel-4x5-mono.ttf", 5)
        draw.multiline_text(
            (0, 0),
            msg,
            font=font,
            fill=255,
            spacing=2,
        )

        display.image(image)

        # display.text(msg, 0, 0, 1)
        display.show()

    informer.AddRule(
        lambda x: True,
        print_rpi_info,
    )

    def interrupt_handler(signum, frame):
        display.fill(0)
        display.show()
        exit(0)

    signal.signal(signal.SIGINT, interrupt_handler)

    while True:
        informer.Tick()
        sleep(1)


if __name__ == "__main__":
    main()
