
class Menu(object):
	"""docstring for Menu"""
	def __init__(self, name, price, calories):
		self._name = name
		self._price = price
		self._calories = calories
		# print ( "price =",self.price,"calories =", self.calories)
	
	def getInfo(self):
		print ( "name =",self._name, "price =",self._price, "calories =", self._calories)

	@property
	def name(self):
		return self._name

	@property
	def price(self):
		return self._price

	@property
	def calories(self):
		return self._calories

	