from rpi_informer import RPIInformer
from pcd8544 import PCB8544

import board
import signal
from time import sleep


def main():
    informer = RPIInformer()
    display = PCB8544(
        board.D6,
        board.D5,
        board.D9,
        50
    )

    def print_rpi_info(informer: RPIInformer):
        display.fill(0)
        display.text("test", 0, 0, 1)
        display.show()

    informer.AddRule(
        lambda x: True,
        print_rpi_info,
    )

    def interrupt_handler(signum, frame):
        pass

    signal.signal(signal.SIGINT, interrupt_handler)

    while True():
        RPIInformer.Tick()
        sleep(1)


if __name__ == "__main__":
    main()
