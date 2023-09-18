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
        template = (""
                    + "({bitrate}){ssid}\n"
                    + "CP: {cpu:>3} T: {temp:>3}\n"
                    + "MEM:  {mem_used:>4}/{mem_total:>4} MB\n"
                    + "DISK: {disk_used:>3}/{disk_total:>3} GB\n"
                    )
        msg = template.format(
            bitrate=int(informer.WiFiInfo.bit_rate),
            ssid=informer.WiFiInfo.ssid,
            cpu=int(informer.CPUInfo.percent),
            temp=int(informer.TempInfo.cpu_temp),
            mem_used=int(informer.MemInfo.used / 1024 / 1024),
            mem_total=int(informer.MemInfo.total / 1024 / 1024),
            disk_used=int(informer.DiskInfo.used / 1024 / 1024 / 1024),
            disk_total=int(informer.DiskInfo.total / 1024 / 1024 / 1024),
        )

        # TODO: Move it to PCB8544 class
        display.fill(0)
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
