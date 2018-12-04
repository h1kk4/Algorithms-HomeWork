from menu import Menu
from promo import Promo, Promo_Menu


# import pdb

def menuParser(path, grocery_list={}):
    file = open(path, 'r')
    menu = {}
    i = 1
    for l in file:
        name, price, calories = tuple(map(lambda x: int(x.strip('#()')), l.split()))
        if (len(grocery_list) == 0):
            count = 1
        elif (name in grocery_list):
            count = grocery_list[name]
        else:
            count = 0

        menu[i] = Menu(name, price, calories, count)
        i += 1
    return menu


def promoParser(path):
    file = open(path, 'r')
    promo = []
    for l in file:
        products = []
        data = l.split()
        kind = int(data[0])
        products_ = data[1]
        discount = int(data[2])
        for p in products_.split(','):
            products.append(int(p))
        promo.append(Promo(kind, products, discount))
    return promo


def make_additional_menu(menu, promo):
    N = len(menu)

    for v in promo:
        N += 1
        if (v.kind == 1):
            names = []
            price = 0
            calories = 0
            names.append("promo->")
            for i in v.products:
                names.append(i)
                price = v.discount
                calories += menu[i].calories
            menu[N] = Promo_Menu(names, price, calories)
        else:
            names = []
            price = 0
            calories = 0
            for i in v.products:
                names.append(i)
                price += menu[i].price
                calories += menu[i].calories
            names.append("the free one->")
            names.append(v.discount)
            calories += menu[v.discount].calories
            menu[N] = Promo_Menu(names, price, calories)
