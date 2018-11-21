
class Menu(object):
	"""docstring for Menu"""
	def __init__(self, name, price, calories):
		self.price = price
		self.calories = calories
		self.name = name
		# print ( "price =",self.price,"calories =", self.calories)
	
	def getInfo(self):
		print ( "name =",self.name, "price =",self.price, "calories =", self.calories)

	def p(self):
		return self.price

	def c(self):
		return self.calories

	def n(self):
		return self.name