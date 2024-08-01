import psutil


class ResourcesInformer:
    class CPUInfo:
        def __init__(self, percent: float, load_avr: tuple[float]):
            self.percent = percent
            self.load_avr = load_avr

    class MemInfo:
        def __init__(self, available: int, used: int, total: int, percent: float):
            self.available = available
            self.used = used
            self.total = total
            self.percent = percent

    class DiskInfo:
        def __init__(self, available: int, used: int, total: int, percent: float):
            self.available = available
            self.used = used
            self.total = total
            self.percent = percent

    def CPUPercent(self) -> float:
        return psutil.cpu_percent()

    def LoadAvr(self) -> tuple[float]:
        data = None
        with open("/proc/loadavg", "r") as f:
            data = f.readline().split()[:3]
        return tuple(data)

    def GetCPUInfo(self) -> CPUInfo:
        return self.CPUInfo(self.CPUPercent(), self.LoadAvr())

    def GetMemInfo(self) -> MemInfo:
        mem = psutil.virtual_memory()

        return self.MemInfo(mem.available, mem.used, mem.total, mem.percent)

    def GetDiskInfo(self):
        disk = psutil.disk_usage('/')

        return self.DiskInfo(disk.free, disk.used, disk.total, disk.percent)

    def MemoryAvailable(self) -> int:
        return psutil.virtual_memory().available

    def MemoryUsed(self) -> int:
        return psutil.virtual_memory().used

    def MemoryTotal(self) -> int:
        return psutil.virtual_memory().total

    def MemoryPercent(self) -> float:
        return psutil.virtual_memory().percent

    def DiskAvailable(self) -> int:
        return psutil.disk_usage('/').free

    def DiskUsed(self) -> int:
        return psutil.disk_usage('/').used

    def DiskTotal(self) -> int:
        return psutil.disk_usage('/').total

    def DiskPercent(self) -> float:
        return psutil.disk_usage('/').percent
