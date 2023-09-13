from os import popen
from re import match

class WiFiInformer:
    class WiFiInfo:
        def __init__(self, ssid, bit_rate, quality):
            self.ssid = ssid
            self.bit_rate = bit_rate
            self.quality = quality


    def GetWiFiInfo(self):
        lines = popen("iwconfig wlan0").read().split("\n")

        ssid = match("^.*ESSID:\"(.*)\"", lines[0]).group(1)

        bit_rate = float(match("^.*Bit Rate=([0-9.]*) Mb/s.*", lines[2]).group(1))

        quality_strs = match("^.*Link Quality=(\d*)/(\d*)", lines[5]).groups()
        quality = int(quality_strs[0]) / int(quality_strs[1])

        return self.WiFiInfo(ssid, bit_rate, quality)



