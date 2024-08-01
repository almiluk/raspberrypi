class TempInformer:
	class TempInfo:
		def __init__(self, cpu_temp):
			self.cpu_temp = cpu_temp

	def __init__(self, src_file: str = "/sys/class/thermal/thermal_zone0/temp"):
		self.__src = src_file

	def GetTempInfo(self) -> TempInfo:
		return self.TempInfo(self.CPUTemp())

	def CPUTemp(self) -> float:
		with open(self.__src, 'r') as f:
			return float(f.readline()) / 1000
