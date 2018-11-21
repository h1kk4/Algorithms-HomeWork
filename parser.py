from menu import Menu
from promo import Promo, Promo_Menu

def menuParser (path):
	file = open(path, 'r')
	menu =  {}
	i = 1
	for l in file:
		name = int(l.split()[0][1:])
		price = int(l.split()[1][1:])
		calories = int(l.split()[2][:1])
		menu[i] = Menu(name, price, calories)
		i+=1 
	return menu



def promoParser (path):
	file = open(path, 'r')
	promo = {}
	i = 1
	for l in file:
		products = []
		kind = int(l.split()[0])
		products_ = l.split()[1]
		discount = int(l.split()[2])
		for p in products_.split(','):
			products.append(int(p))
		promo[i]= Promo(kind, products, discount)
		i+=1
	return promo



def make_additional_menu(menu, promo):

	N = len(menu)

	for k, v in promo.items():
		N+=1
		if (v.kind==1):
			names = []
			price = 0
			calories = 0 	
			print('products', v.products)
			for i in v.products:
				names.append(i)
				price = v.discount
				calories+=menu[i].c()
			print("names -",names,"price -",price,"calories -",calories)
			menu[N]=Promo_Menu(names, price, calories)
		else:
			names = []
			price = 0
			calories = 0 	
			print('products', v.products)
			for i in v.products:
				names.append(i)
				price+=menu[i].p()
				calories+=menu[i].c()
			names.append(v.discount)
			calories+=menu[v.discount].c()

			print("names -",names,"price -",price,"calories -",calories)
			menu[N]=Promo_Menu(names, price, calories)

 


		