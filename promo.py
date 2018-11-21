from menu import Menu

class Promo():
	def __init__(self, kind, products, discount):
		self.kind = kind
		self.products = products
		self.discount = discount
		print("kind =",self.kind," products =",self.products, "discount =",self.discount)

	def getInfo(self):
		print ( "kind =",self.kind, "products =",self.products, "discount =", self.discount)

	def kind(self):
		return self.kind

	def products(self):
		return self.products			
	
	def discount(self):
		return self.discount

# class Promo_Menu(Menu):
# 	"""docstring for Promo_Menu"""
# 	def __init__(self, name, price, calories):
# 		super().__init__(name, price, calories)


		
		


