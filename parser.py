from menu import Menu
from promo import Promo, Promo_Menu
# import pdb

def menuParser (path):
	file = open(path, 'r')
	menu = {}
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
	promo = []
	for l in file:
		products = []
		kind = int(l.split()[0])
		products_ = l.split()[1]
		discount = int(l.split()[2])
		for p in products_.split(','):
			products.append(int(p))
		promo.append(Promo(kind, products, discount))
	return promo


def make_additional_menu(menu, promo):

	N = len(menu)

	for v in promo:
		N+=1
		if (v.kind==1):
			names = []
			price = 0
			calories = 0 	
			print('products', v.products)
			for i in v.products:
				names.append(i)
				price = v.discount
				calories+=menu[i].calories
			print("names -",names,"price -",price,"calories -",calories)
			menu[N]=Promo_Menu(names, price, calories)
		else:
			names = []
			price = 0
			calories = 0 	
			print('products', v.products)
			for i in v.products:
				names.append(i)
				price+=menu[i].price
				calories+=menu[i].calories
			names.append(v.discount)
			calories+=menu[v.discount].calories

			print("names -",names,"price -",price,"calories -",calories)
			menu[N]=Promo_Menu(names, price, calories)

 


		