class cars:
	def __init__(self):
		pass

	def setbrand(self, car_brand):
		self.brand = car_brand

	def getbrand(self):
		return self.brand 

	def printbrand(self):
		print(self.getbrand())

start=cars()
start.setbrand('Toyota')
start.printbrand()