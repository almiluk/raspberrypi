from .temp_informer import TempInformer
from .resources_informer import ResourcesInformer
from .wifi_informer import WiFiInformer

from datetime import datetime
from zoneinfo import ZoneInfo


from typing import Callable, Dict


class RPIInformer:
    class Rule:
        def __init__(self, premise: Callable[["RPIInformer"], bool], conclusion: Callable[["RPIInformer"], None]):
            self.__prem = premise
            self.__conc = conclusion

        def Check(self, informer: "RPIInformer") -> bool:
            if self.__prem(informer):
                self.__conc(informer)
                return True
            return False

    def __init__(self):
        self.__temp_informer = TempInformer()
        self.__resource_informer = ResourcesInformer()
        self.__wifi_informer = WiFiInformer()
        self.TempInfo = None
        self.CPUInfo = None
        self.MemInfo = None
        self.DiskInfo = None

        self.__rules = []

        self.Tick()

    def Tick(self):
        self.TempInfo = self.__temp_informer.GetTempInfo()
        self.CPUInfo = self.__resource_informer.GetCPUInfo()
        self.MemInfo = self.__resource_informer.GetMemInfo()
        self.DiskInfo = self.__resource_informer.GetDiskInfo()
        self.WiFiInfo = self.__wifi_informer.GetWiFiInfo()

        self.Datetime = datetime.now()

        print(vars(self.TempInfo), vars(self.CPUInfo), vars(self.MemInfo), vars(
            self.DiskInfo), self.Datetime.isoformat(), vars(self.WiFiInfo))

        for rule in self.__rules:
            rule.Check(self)

    def AddRule(self, premise: Callable[["RPIInformer"], bool], conclusion: Callable[["RPIInformer"], None]):
        self.__rules.append(self.Rule(premise, conclusion))
