from menu import Menu
from promo import Promo

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
	i = 0
	for l in file:
		products = []
		kind = (l.split()[0])
		products_ = l.split()[1]
		discount = int(l.split()[2])
		for p in products_.split(','):
			products.append(p)
		promo[i]= Promo(kind, products, discount)
		i+=1
	print("is it?", type(promo[0]) == Promo)
	print(promo[0])
	print(promo[1])
	return promo



def make_additional_menu(menu, promo):

	N = len(menu)
	for k, v in promo.items():
		print(k,v)
		# print(type(v) == Promo)
		# print (promo[0].getInfo())
		# print('MENU', menu [1].c())
		# N+=1
		# if (v.kind()):
		# 	#TODO случай когда цена фиксирована
		# 	return None
		# else:
		# 	name = []
		# 	price = 0
		# 	calories = 0 
		# 	for i in v.products():
		# 		name.append(i)
		# 		price+=menu[i].p()
		# 		calories+=menu[i].c()
		# 	menu[N]=Promo_Menu(name, price, calories)






	return 


		