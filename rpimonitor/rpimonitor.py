#!/usr/bin/python3


from configparser import ConfigParser

from rpi_informer import RPIInformer
from pcd8544 import PCB8544

import board
import signal
from time import sleep
from sys import exit


def main():
    conf = get_config()
    pins = conf["pins"]

    informer = RPIInformer()
    display = PCB8544(
        pins["dc"],
        pins["cs"],
        pins["reset"],
        pins["backlight"],
        conf["screen"]["contrast"],
        conf["screen"]["bias"],
        conf["screen"]["font"],
        conf["screen"]["font_size"],
        conf["screen"]["reverse_backlight"],
        conf["screen"]["rotate"],
    )

    display.SetBacklight(True)

    def print_rpi_info(informer: RPIInformer):
        template = (""
                    + "({bitrate:>3}){ssid}\n"
                    + "CP:{cpu:>3}% T:{temp:>3}C\n"
                    + "MEM:{mem_used:>4} /{mem_total:>4} MB\n"
                    + "DISK:{disk_used:>3} /{disk_total:>4}  GB\n"
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

        display.ShowMultilineText(msg)

    informer.AddRule(
        lambda x: True,
        print_rpi_info,
    )

    def interrupt_handler(signum, frame):
        display.fill(0)
        display.show()
        display.SetBacklight(False)
        exit(0)

    signal.signal(signal.SIGINT, interrupt_handler)

    while True:
        informer.Tick()
        sleep(1)


def get_config():
    setting = ConfigParser()
    setting.read("/usr/local/etc/rpimonitor.conf")

    config = {}

    for section in setting.sections():
        items = setting.items(section)
        section_dict = dict(items)

        for key, value in section_dict.items():
            if value.isdigit():
                section_dict[key] = int(value) # type: ignore

        config[section] = section_dict

    for pin_name, pin_value in config["pins"].items():
        try:
            config["pins"][pin_name] = eval("board." + pin_value)
        except AttributeError as ex:
            print(f"Incorrect pin name: {pin_value}")
            exit(1)

    return config


if __name__ == "__main__":
    main()
