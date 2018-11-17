
class Menu(object):
	"""docstring for Menu"""
	def __init__(self, name, price, calories):
		self.price = int(price)
		self.calories = int(calories)
		self.name = name
		# print ( "price =",self.price,"calories =", self.calories)
	
	def getInfo(self):
		print ( "name =",self.name, "price =",self.price, "calories =", self.calories)
	
		pass

	def p(self):
		return int(self.price)

	def c(self):
		return int(self.calories)

	def n(self):
		return self.name