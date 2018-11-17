from menu import Menu


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




		